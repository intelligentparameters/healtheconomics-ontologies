# -*- coding: utf-8 -*-
"""Check the generated docs against the release files, independently of the generator's own-term rule.

Own terms are found here a different way: every typed IRI under the ontology's vann:preferredNamespaceUri, its
/<acronym>/ path, or with rdfs:isDefinedBy the ontology, plus for HEO every skos:Concept in the file.
Checks: each own term is listed exactly once across the ontology's pages; ids are unique per page; every internal link
resolves to a page and an id; every definition appears verbatim; DOIs agree with README.md; the deprecated counts in the
manifest agree with the files; each page has a language, one title and a description.
Run from the repository root: python tools/check_docs.py"""
import glob, html as H, json, os, re, sys
from html.parser import HTMLParser
from rdflib import Graph, RDF, URIRef, Literal, Namespace, OWL
from rdflib.namespace import RDFS
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#"); VANN = Namespace("http://purl.org/vocab/vann/")
DEFS = [URIRef("http://purl.obolibrary.org/obo/IAO_0000115"), SKOS.definition]
BASE = "https://healtheconomics.wiki/ontologies/"
M = json.load(open(os.path.join(ROOT, "docs", "manifest.json"), encoding="utf-8"))


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.ids = []; s.hrefs = []; s.lang = None; s.titles = 0; s.desc = False; s.terms = []
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == "html": s.lang = a.get("lang")
        if t == "title": s.titles += 1
        if t == "meta" and a.get("name") == "description" and a.get("content"): s.desc = True
        if "id" in a: s.ids.append(a["id"])
        if t == "div" and a.get("class") == "term": s.terms.append(a["id"])
        if t == "a" and "href" in a: s.hrefs.append(a["href"])


fails = []
parsed = {}
for f in glob.glob(os.path.join(ROOT, "docs", "**", "*.html"), recursive=True):
    rel = os.path.relpath(f, os.path.join(ROOT, "docs")).replace("\\", "/")
    src = open(f, encoding="utf-8").read(); p = P(); p.feed(src); parsed[rel] = (p, src)
    if p.lang != "en-GB" or p.titles != 1 or not p.desc: fails.append(f"{rel}: language, title or description missing")
    dup = {i for i in p.ids if p.ids.count(i) > 1}
    if dup: fails.append(f"{rel}: duplicate ids {sorted(dup)[:4]}")
for rel, (p, src) in parsed.items():
    here = rel.rsplit("/", 1)[0] if "/" in rel else ""
    for h in p.hrefs:
        if h.startswith(("http", "mailto")): continue
        m = re.match(r"^([^#]*)(?:#(.*))?$", h); path, frag = m.group(1), m.group(2)
        tgt = os.path.normpath(os.path.join(here, path or rel.rsplit("/", 1)[-1])).replace("\\", "/")
        if tgt.endswith("/") or tgt in (".", "..") or not tgt.endswith(".html"): tgt = (tgt.rstrip("/") + "/index.html").lstrip("./")
        tgt = tgt.replace("./", "")
        if tgt not in parsed: fails.append(f"{rel}: link to missing page {h}"); continue
        if frag and H.unescape(frag) not in parsed[tgt][0].ids: fails.append(f"{rel}: broken anchor {h}")
readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
for k, o in M["ontologies"].items():
    v = o["version"]
    if f"zenodo.{o['doi']}" not in readme or f"[{k.upper()}]({k}/{v})" not in readme: fails.append(f"{k}: DOI or folder link disagrees with README")
    g = Graph()
    for f in glob.glob(os.path.join(ROOT, k, v, "*.ttl")):
        if "shapes" not in os.path.basename(f): g.parse(f, format="turtle")
    ont = URIRef(BASE + k)
    nss = {str(x) for x in g.objects(None, VANN.preferredNamespaceUri)} | {BASE + k + "/", BASE + k + "#"}
    onts = {str(x) for x in g.subjects(RDF.type, OWL.Ontology)} | {str(x) for x in g.objects(None, OWL.versionIRI)}
    want = set()
    for s in set(g.subjects(RDF.type, None)):
        if not isinstance(s, URIRef) or str(s) in onts: continue
        if any(str(s).startswith(n) for n in nss) or ((s, RDFS.isDefinedBy, ont) in g and str(s).startswith("https://healtheconomics.wiki/")) or (k == "heo" and (s, RDF.type, SKOS.Concept) in g):
            want.add(re.split(r"[/#]", str(s).rstrip("/"))[-1])
    odd = sorted(str(s) for s in g.subjects(RDFS.isDefinedBy, ont) if not str(s).startswith("https://healtheconomics.wiki/"))
    if odd: print(f"  note {k}: file says these imported terms are defined by {k.upper()}, left out as external: {odd}")
    listed = []
    for pg in M["pages"][k]:
        listed += parsed[f"{k}/{pg}"][0].terms
    dupl = {x for x in listed if listed.count(x) > 1}
    miss = want - set(listed); extra = set(listed) - want
    if dupl: fails.append(f"{k}: listed more than once {sorted(dupl)[:5]}")
    if miss: fails.append(f"{k}: {len(miss)} terms missing, e.g. {sorted(miss)[:5]}")
    if extra: fails.append(f"{k}: {len(extra)} listed ids are not terms, e.g. {sorted(extra)[:5]}")
    alltext = "".join(parsed[f"{k}/{pg}"][1] for pg in M["pages"][k])
    bad = 0
    for s in set(g.subjects()):
        if not isinstance(s, URIRef) or re.split(r"[/#]", str(s).rstrip("/"))[-1] not in want: continue
        d = sorted(str(x) for p in DEFS for x in g.objects(s, p) if isinstance(x, Literal))
        if d and not any(H.escape(x, quote=True) in alltext for x in d): bad += 1
    if bad: fails.append(f"{k}: {bad} definitions not found verbatim")
    ndep = sum(1 for s in g.subjects(OWL.deprecated, Literal(True)) if re.split(r"[/#]", str(s).rstrip("/"))[-1] in want)
    if ndep != o["deprecated"]: fails.append(f"{k}: deprecated count {o['deprecated']} on the page but {ndep} in the files")
    print(f"{k}: own terms in files {len(want):,}, listed {len(set(listed) & want):,}, deprecated {ndep:,}, pages {len(M['pages'][k])}")
print("FAILS" if fails else "ALL CHECKS PASS")
for f in fails[:40]: print(" ", f)
