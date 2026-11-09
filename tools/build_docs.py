# -*- coding: utf-8 -*-
"""Build the documentation pages in docs/ from the release files in this repository.

Every page is generated from the Turtle files, so it cannot disagree with them. Run from the repository root:
    python tools/build_docs.py
Needs Python 3.10+ and rdflib. Writes docs/index.html, one main page per ontology (docs/<ontology>/index.html), extra
pages for large groups of concepts or records, and docs/manifest.json (what each page lists, used by tools/check_docs.py).

What a page lists: the ontology's own terms, meaning every typed term whose IRI sits in the ontology's own namespace
(https://healtheconomics.wiki/ontologies/<acronym>/ or .../<acronym>#), and for HEO also its concepts, which keep the wiki
concept addresses (https://healtheconomics.wiki/concept/<slug>). Imported terms (BFO, IAO, RO, PROV and so on) are linked
where they are used and marked as external, but are not listed."""
import collections, glob, html, json, os, re, sys
from rdflib import Graph, RDF, RDFS, OWL, XSD, URIRef, Literal, BNode, Namespace
from rdflib.collection import Collection

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "https://github.com/intelligentparameters/healtheconomics-ontologies"
RAW = "https://raw.githubusercontent.com/intelligentparameters/healtheconomics-ontologies/main"
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
DCT = Namespace("http://purl.org/dc/terms/")
SH = Namespace("http://www.w3.org/ns/shacl#")
OBO = Namespace("http://purl.obolibrary.org/obo/")
OIO = Namespace("http://www.geneontology.org/formats/oboInOwl#")
VANN = Namespace("http://purl.org/vocab/vann/")
BASE = "https://healtheconomics.wiki/ontologies/"
CONCEPT = "https://healtheconomics.wiki/concept/"
FAM = [("heo", "2.0.0", "24057055", "The concepts of health economics, with definitions and typed links between them, taken from the wiki"),
       ("rheo", "0.4.0", "24057151", "The real things health economics works with, such as patients, resources, care processes and payments, and the records made about them"),
       ("oheo", "0.3.0", "24057194", "Health outcomes as they are specified, measured, valued and summarised"),
       ("heto", "0.3.0", "24057218", "Units of health economics work, such as adding discounting to a model, and the inputs and outputs of each"),
       ("heao", "0.2.0", "24057282", "How quantities are turned into values, such as health into QALYs or resources into costs"),
       ("hemo", "0.2.0", "24057299", "The formulas, variables, assumptions and tests the other ontologies rely on"),
       ("helo", "0.2.0", "24057315", "Learning pathways through the HEO concepts, ordered by level"),
       ("heiro", "0.2.0", "24057331", "The institutions and rules of health economics and HTA, the bodies that issue them and when they apply")]
SING = {"Class": "Class", "Object property": "Object property", "Data property": "Data property", "Annotation property": "Annotation property",
        "Datatype": "Datatype", "Concept": "Concept", "Individual": "Record (individual)"}
VOCAB = ["Class", "Object property", "Data property", "Annotation property", "Datatype"]
PLURAL = {"Class": "Classes", "Object property": "Object properties", "Data property": "Data properties",
          "Annotation property": "Annotation properties", "Datatype": "Datatypes", "Concept": "Concepts", "Individual": "Records (individuals)"}
CHARS = [(OWL.FunctionalProperty, "functional"), (OWL.InverseFunctionalProperty, "inverse functional"), (OWL.TransitiveProperty, "transitive"),
         (OWL.SymmetricProperty, "symmetric"), (OWL.AsymmetricProperty, "asymmetric"), (OWL.ReflexiveProperty, "reflexive"),
         (OWL.IrreflexiveProperty, "irreflexive")]
DEFS = [OBO.IAO_0000115, SKOS.definition]
LABELS = [RDFS.label, SKOS.prefLabel]
REPLACED = [DCT.isReplacedBy, OBO.IAO_0100001]
CONSIDER = [OIO.consider]
STATUS = [OBO.IAO_0000114]
PAGE_SIZE = 1200

CSS = """
:root{--bg:#fbf8f2;--card:#fffdf8;--fg:#24211c;--muted:#6b6458;--line:#e4dccd;--gold:#a87b1e;--accent:#1f4e79;--chip:#f1ead9;--warn:#b3261e;color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#171512;--card:#1f1c18;--fg:#ece6da;--muted:#b0a796;--line:#3a352d;--gold:#d6a94a;--accent:#8db8e0;--chip:#2b2721;--warn:#f28b82;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#171512;--card:#1f1c18;--fg:#ece6da;--muted:#b0a796;--line:#3a352d;--gold:#d6a94a;--accent:#8db8e0;--chip:#2b2721;--warn:#f28b82;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding-block:28px 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
a{color:var(--accent)} a:hover{text-decoration:none}
.kicker{color:var(--gold);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600}
h1,h2,h3{font-family:Georgia,"Times New Roman",serif;font-weight:600;line-height:1.2;text-wrap:balance}
h1{font-size:2.1rem;margin:.3rem 0 .8rem} h2{font-size:1.45rem;margin:2.2rem 0 .8rem} h3{font-size:1.08rem;margin:0 0 .3rem}
.lede{max-width:70ch} .muted{color:var(--muted)} .small{font-size:.9rem}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:8px;padding:14px 16px;min-width:0}
.card p{margin:.3rem 0 0;font-size:.93rem}
.meta{display:grid;grid-template-columns:max-content 1fr;gap:6px 16px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:14px 16px}
.meta dt{color:var(--muted)} .meta dd{margin:0;min-width:0;overflow-wrap:anywhere}
@media (max-width:560px){.meta{grid-template-columns:1fr}.meta dt{margin-top:6px}}
.stats{display:flex;flex-wrap:wrap;gap:8px;margin:.6rem 0}
.chip{background:var(--chip);border-radius:999px;padding:3px 11px;font-size:.85rem}
.search{width:100%;max-width:520px;padding:9px 12px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg);font-size:1rem}
.term{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 16px;margin:10px 0;min-width:0}
.term h3 a{color:inherit;text-decoration:none}
.iri{font-family:ui-monospace,Consolas,monospace;font-size:.8rem;color:var(--muted);overflow-wrap:anywhere}
.def{margin:.45rem 0}
.rel{font-size:.9rem;margin:.2rem 0;overflow-wrap:anywhere} .rel b{font-weight:600;color:var(--muted)}
.dep{color:var(--warn);font-weight:600;font-size:.88rem}
.st{font-size:.78rem;color:var(--muted)}
.ext{font-size:.72rem;color:var(--muted);margin-left:2px}
details>summary{cursor:pointer;font-weight:600;padding:6px 0}
.cite{background:var(--card);border-left:3px solid var(--gold);padding:10px 14px;border-radius:4px;overflow-wrap:anywhere}
.tablewrap{overflow-x:auto} table{border-collapse:collapse;width:100%;font-size:.92rem} th,td{border-bottom:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top} th{color:var(--muted);font-weight:600}
nav.pages{display:flex;flex-wrap:wrap;gap:6px;margin:.6rem 0} nav.pages a{background:var(--chip);border-radius:6px;padding:3px 9px;text-decoration:none;font-size:.9rem}
footer{margin-top:3rem;color:var(--muted);font-size:.88rem;border-top:1px solid var(--line);padding-top:1rem}
"""
JS = """<script>
(function(){var q=document.getElementById('q');if(!q)return;var items=[].slice.call(document.querySelectorAll('[data-s]'));
var n=document.getElementById('n');q.addEventListener('input',function(){var v=q.value.trim().toLowerCase(),c=0;
items.forEach(function(e){var hit=!v||e.getAttribute('data-s').indexOf(v)>-1;e.hidden=!hit;if(hit)c++;});
document.querySelectorAll('details.grp').forEach(function(d){if(v)d.open=true;});if(n)n.textContent=v?c+' matching on this page':'';});
if(location.hash){var t=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(t){var d=t.closest('details');if(d)d.open=true;t.scrollIntoView();}}})();
</script>"""


def esc(x):
    return html.escape(str(x), quote=True)


def lits(g, s, ps):
    vals = [o for p in ps for o in g.objects(s, p) if isinstance(o, Literal)]
    return sorted(vals, key=lambda v: (0 if (v.language or "en").startswith("en") else 1, str(v)))


def lit(g, s, ps):
    v = lits(g, s, ps)
    return str(v[0]) if v else ""


def page(title, desc, body, alts=(), jsonld=None):
    links = "".join(f"<link rel=\"alternate\" type=\"{t}\" href=\"{esc(h)}\">" for t, h in alts)
    ld = f"<script type=\"application/ld+json\">{json.dumps(jsonld, ensure_ascii=False)}</script>" if jsonld else ""
    return (f"<!doctype html><html lang=\"en-GB\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<title>{esc(title)}</title><meta name=\"description\" content=\"{esc(desc)}\">{links}{ld}<style>{CSS}</style></head>"
            f"<body><div class=\"wrap\">{body}<footer>Generated from the release files in <a href=\"{REPO}\">{REPO.split('github.com/')[1]}</a> "
            f"by tools/build_docs.py. Content CC BY 4.0, HealthEconomics.wiki.</footer></div>{JS}</body></html>")


def cff(path):
    t = open(path, encoding="utf-8").read()
    g = lambda k: (re.search(rf'^{k}:\s*"?([^"\n]+)"?', t, re.M) or [None, ""])[1]
    authors = re.findall(r'family-names:\s*"([^"]+)"\s*\n\s*given-names:\s*"([^"]+)"', t)
    return {"title": g("title"), "version": g("version"), "date": g("date-released"), "authors": authors}


def load(k, v):
    d = os.path.join(ROOT, k, v)
    files = sorted(os.listdir(d))
    g, sg, mods = Graph(), Graph(), {}
    for f in files:
        if not f.endswith(".ttl"): continue
        one = Graph().parse(os.path.join(d, f), format="turtle")
        (sg if "shapes" in f else g).__iadd__(one)
        if "shapes" not in f:
            for o in one.subjects(RDF.type, OWL.Ontology):
                mods[f] = (str(o), lit(one, o, [DCT.title, RDFS.label]), sorted(str(x) for x in one.objects(o, OWL.imports)))
    return d, files, g, sg, mods


def build():
    graphs = {k: load(k, v) for k, v, *_ in FAM}
    own, kind_of, page_of = {}, {}, {}
    for k, v, *_ in FAM:
        g = graphs[k][2]
        ns = (BASE + k + "/", BASE + k + "#")
        onts = set(map(str, g.subjects(RDF.type, OWL.Ontology))) | {str(o) for o in g.objects(None, OWL.versionIRI)}
        for s in set(g.subjects(RDF.type, None)):
            if not isinstance(s, URIRef) or str(s) in onts: continue
            u = str(s)
            if not (u.startswith(ns) or (k == "heo" and u.startswith(CONCEPT))): continue
            ts = set(g.objects(s, RDF.type))
            if OWL.Class in ts: kd = "Class"
            elif OWL.ObjectProperty in ts: kd = "Object property"
            elif OWL.DatatypeProperty in ts: kd = "Data property"
            elif OWL.AnnotationProperty in ts: kd = "Annotation property"
            elif RDFS.Datatype in ts: kd = "Datatype"
            elif SKOS.Concept in ts: kd = "Concept"
            else: kd = "Individual"
            a = re.split(r"[/#]", u.rstrip("/"))[-1]
            own[u] = (k, a); kind_of[u] = kd

    def label_of(u):
        u = URIRef(u)
        for k, *_ in FAM:
            l = lit(graphs[k][2], u, LABELS)
            if l: return l
        return re.split(r"[/#]", str(u).rstrip("/"))[-1]

    # page assignment: vocabulary on the main page; HEO concepts by first letter; records by type, split when large
    groups = collections.defaultdict(list)
    for u, (k, a) in own.items():
        kd = kind_of[u]
        if kd in VOCAB: page_of[u] = (k, "index.html")
        elif kd == "Concept":
            first = (label_of(u)[:1] or "0").lower()
            key = first if first.isalpha() else "0-9"
            page_of[u] = (k, f"concepts-{key}.html")
        else:
            g = graphs[k][2]
            ty = sorted(str(o) for o in g.objects(URIRef(u), RDF.type) if o != OWL.NamedIndividual)
            groups[(k, ty[0] if ty else "untyped")].append(u)
    page_label = {}
    for (k, ty), us in groups.items():
        us.sort(key=lambda u: label_of(u).lower())
        slug = re.split(r"[/#]", ty.rstrip("/"))[-1].lower()
        n = max(1, -(-len(us) // PAGE_SIZE))
        for i, u in enumerate(us):
            pg = f"records-{slug}{'' if n == 1 else '-' + str(i // PAGE_SIZE + 1)}.html"
            page_of[u] = (k, pg); page_label[(k, pg)] = label_of(ty) + ("" if n == 1 else f" {i // PAGE_SIZE + 1}")

    def href(u, here):
        k, p = page_of[u]; a = own[u][1]
        if k == here[0] and p == here[1]: return f"#{a}"
        return (f"{p}#{a}" if k == here[0] else f"../{k}/{p}#{a}")

    def link(o, here):
        u = str(o)
        if u in own: return f"<a href=\"{esc(href(u, here))}\">{esc(label_of(u))}</a>"
        if isinstance(o, Literal): return esc(o)
        return f"<a href=\"{esc(u)}\">{esc(label_of(u))}</a><span class=\"ext\">external</span>"

    def expr(g, x, here, depth=0):
        if isinstance(x, URIRef): return link(x, here)
        if isinstance(x, Literal): return f"\"{esc(x)}\""
        if depth > 6: return "(nested expression)"
        for p, word in ((OWL.unionOf, " or "), (OWL.intersectionOf, " and ")):
            l = g.value(x, p)
            if l is not None:
                return "(" + word.join(expr(g, m, here, depth + 1) for m in Collection(g, l)) + ")"
        c = g.value(x, OWL.complementOf)
        if c is not None: return "not " + expr(g, c, here, depth + 1)
        l = g.value(x, OWL.oneOf)
        if l is not None: return "{" + ", ".join(expr(g, m, here, depth + 1) for m in Collection(g, l)) + "}"
        dt = g.value(x, OWL.onDatatype); wr = g.value(x, OWL.withRestrictions)
        if dt is not None and wr is not None:
            fac = []
            for f in Collection(g, wr):
                for p, o in g.predicate_objects(f): fac.append(f"{p.split('#')[-1]} \"{esc(o)}\"")
            return f"{link(dt, here)}[{', '.join(fac)}]"
        p = g.value(x, OWL.onProperty)
        if p is not None:
            pl = expr(g, p, here, depth + 1)
            for q, word in ((OWL.someValuesFrom, "some"), (OWL.allValuesFrom, "only"), (OWL.hasValue, "value"), (OWL.hasSelf, "Self")):
                o = g.value(x, q)
                if o is not None: return f"{pl} {word} {expr(g, o, here, depth + 1)}"
            for q, word in ((OWL.qualifiedCardinality, "exactly"), (OWL.minQualifiedCardinality, "min"), (OWL.maxQualifiedCardinality, "max"),
                            (OWL.cardinality, "exactly"), (OWL.minCardinality, "min"), (OWL.maxCardinality, "max")):
                o = g.value(x, q)
                if o is not None:
                    oc = g.value(x, OWL.onClass) or g.value(x, OWL.onDataRange)
                    return f"{pl} {word} {esc(o)}" + (f" {expr(g, oc, here, depth + 1)}" if oc is not None else "")
        inv = g.value(x, OWL.inverseOf)
        if inv is not None: return f"inverse ({expr(g, inv, here, depth + 1)})"
        return "(expression not shown)"

    # axiom annotations (HEO link review status)
    axst = {}
    g0 = graphs["heo"][2]
    for ax in g0.subjects(RDF.type, OWL.Axiom):
        s, p, o = g0.value(ax, OWL.annotatedSource), g0.value(ax, OWL.annotatedProperty), g0.value(ax, OWL.annotatedTarget)
        st = [str(v) for q, v in g0.predicate_objects(ax) if str(q).endswith("linkReviewStatus")]
        if st: axst[(str(s), str(p), str(o))] = st[0]

    # reverse indexes
    sub = collections.defaultdict(list); dom_of = collections.defaultdict(list); rng_of = collections.defaultdict(list)
    inv_of = collections.defaultdict(list); members = collections.Counter()
    for k, *_ in FAM:
        g = graphs[k][2]
        for s, o in g.subject_objects(RDFS.subClassOf):
            if str(s) in own and str(o) in own: sub[str(o)].append(str(s))
        for s, o in g.subject_objects(RDFS.domain):
            if str(s) in own and str(o) in own: dom_of[str(o)].append(str(s))
        for s, o in g.subject_objects(RDFS.range):
            if str(s) in own and str(o) in own: rng_of[str(o)].append(str(s))
        for s, o in g.subject_objects(OWL.inverseOf):
            if isinstance(s, URIRef) and isinstance(o, URIRef): inv_of[str(o)].append(str(s))
        for s, o in g.subject_objects(RDF.type):
            if str(s) in own and str(o) in own: members[str(o)] += 1

    CONSUMED = set(LABELS + DEFS + REPLACED + CONSIDER + STATUS) | {RDF.type, RDFS.subClassOf, RDFS.subPropertyOf, OWL.equivalentClass, OWL.disjointWith,
                                                                    RDFS.domain, RDFS.range, OWL.inverseOf, OWL.deprecated, SKOS.notation, SKOS.broader,
                                                                    OWL.propertyChainAxiom, OWL.equivalentProperty, OWL.withRestrictions, OWL.onDatatype}

    def render(u, here):
        k = here[0]; g = graphs[k][2]; s = URIRef(u); a = own[u][1]; kd = kind_of[u]
        lab = label_of(u); df = lit(g, s, DEFS); notation = lit(g, s, [SKOS.notation])
        syn = [str(x) for x in lits(g, s, [SKOS.altLabel, OIO.hasExactSynonym, OIO.hasRelatedSynonym, OIO.hasBroadSynonym, OIO.hasNarrowSynonym])]
        out = [f"<div class=\"term\" id=\"{esc(a)}\" data-s=\"{esc((lab + ' ' + a + ' ' + notation + ' ' + ' '.join(syn) + ' ' + df).lower())}\">",
               f"<h3><a href=\"#{esc(a)}\">{esc(lab)}</a></h3><div class=\"iri\"><a href=\"{esc(u)}\">{esc(u)}</a>{(' · ' + esc(notation)) if notation else ''}</div>"]
        if (s, OWL.deprecated, Literal(True)) in g or (s, OWL.deprecated, Literal("true", datatype=XSD.boolean)) in g:
            rep = [link(o, here) for p in REPLACED for o in g.objects(s, p)]
            con = [link(o, here) for p in CONSIDER for o in g.objects(s, p)]
            out.append("<div class=\"dep\">Deprecated" + (f" · replaced by {', '.join(rep)}" if rep else "") + (f" · see also {', '.join(con)}" if con else "") + "</div>")
        stt = [link(o, here) for o in g.objects(s, OBO.IAO_0000114)]
        if stt: out.append(f"<div class=\"st\">Curation status {', '.join(stt)}</div>")
        if df: out.append(f"<p class=\"def\">{esc(df)}</p>")
        rel = []
        if syn: rel.append(("Also known as", esc("; ".join(syn))))
        sup = list(g.objects(s, RDFS.subClassOf))
        named = [link(o, here) for o in sup if isinstance(o, URIRef)]
        if named: rel.append(("Subclass of", ", ".join(named)))
        rs = sorted(expr(g, o, here) for o in sup if isinstance(o, BNode))
        if rs: rel.append(("Restrictions", "<br>".join(rs)))
        eq = [expr(g, o, here) for o in g.objects(s, OWL.equivalentClass)]
        if eq: rel.append(("Equivalent to", "<br>".join(eq)))
        dj = [expr(g, o, here) for o in g.objects(s, OWL.disjointWith)]
        if dj: rel.append(("Disjoint with", ", ".join(dj)))
        if u in sub: rel.append(("Subclasses", ", ".join(link(URIRef(x), here) for x in sorted(sub[u], key=lambda x: label_of(x).lower()))))
        if members[u]: rel.append(("Records of this type", f"{members[u]:,}"))
        sp = [link(o, here) for o in g.objects(s, RDFS.subPropertyOf)]
        if sp: rel.append(("Subproperty of", ", ".join(sp)))
        eqp = [link(o, here) for o in g.objects(s, OWL.equivalentProperty)]
        if eqp: rel.append(("Equivalent property", ", ".join(eqp)))
        dom = [expr(g, o, here) for o in g.objects(s, RDFS.domain)]
        rng = [expr(g, o, here) for o in g.objects(s, RDFS.range)]
        if dom: rel.append(("Domain", "<br>".join(dom)))
        if rng: rel.append(("Range", "<br>".join(rng)))
        inv = [link(o, here) for o in g.objects(s, OWL.inverseOf)] + [link(URIRef(x), here) for x in inv_of.get(u, [])]
        if inv: rel.append(("Inverse of", ", ".join(dict.fromkeys(inv))))
        ch = [w for t, w in CHARS if (s, RDF.type, t) in g]
        if ch: rel.append(("Characteristics", ", ".join(ch)))
        for c in g.objects(s, OWL.propertyChainAxiom):
            rel.append(("Property chain", " then ".join(link(m, here) for m in Collection(g, c))))
        wr = g.value(s, OWL.equivalentClass)
        if kd == "Datatype":
            for o in g.objects(s, OWL.equivalentClass): pass
        if u in dom_of: rel.append(("In domain of", ", ".join(link(URIRef(x), here) for x in sorted(dom_of[u], key=lambda x: label_of(x).lower()))))
        if u in rng_of: rel.append(("In range of", ", ".join(link(URIRef(x), here) for x in sorted(rng_of[u], key=lambda x: label_of(x).lower()))))
        if kd == "Concept":
            isT = [o for o in g.objects(s, URIRef(BASE + "heo#isTypeOf"))]
            cu = [o for o in g.objects(s, URIRef(BASE + "heo#classifiedUnder"))]
            if isT: rel.append(("Is a type of", ", ".join(link(o, here) for o in isT)))
            if cu: rel.append(("Classified under", ", ".join(link(o, here) for o in cu)))
            other_br = [o for o in g.objects(s, SKOS.broader) if o not in isT and o not in cu]
            if other_br: rel.append(("Broader", ", ".join(link(o, here) for o in other_br)))
        if kd == "Individual":
            ty = [link(o, here) for o in g.objects(s, RDF.type) if isinstance(o, URIRef) and o != OWL.NamedIndividual]
            if ty: rel.append(("Type", ", ".join(ty)))
        # everything else the files say about this term
        rest = collections.defaultdict(list)
        for p, o in g.predicate_objects(s):
            if p in CONSUMED or (kd == "Concept" and str(p) in (BASE + "heo#isTypeOf", BASE + "heo#classifiedUnder")): continue
            if isinstance(o, BNode):
                v = expr(g, o, here)
            else:
                v = link(o, here)
                st = axst.get((u, str(p), str(o)))
                if st: v += f" <span class=\"st\">({esc(st)})</span>"
            rest[str(p)].append(v)
        for p in sorted(rest, key=lambda p: label_of(p).lower()):
            vals = sorted(rest[p])
            rel.append((label_of(p), ("<br>" if any(len(x) > 120 for x in vals) else ", ").join(vals)))
        out += [f"<div class=\"rel\"><b>{esc(x)}</b> {y}</div>" for x, y in rel]
        out.append("</div>")
        return "".join(out)

    manifest = {"pages": {}, "ontologies": {}}
    for k, v, doi, summary in FAM:
        d, files, g, sg, mods = graphs[k]
        ont = URIRef(BASE + k)
        title = lit(g, ont, [DCT.title, RDFS.label]) or k.upper()
        desc = lit(g, ont, [DCT.description, RDFS.comment])
        ver = lit(g, ont, [OWL.versionInfo])
        meta = [("Ontology IRI", f"<a href=\"{esc(ont)}\">{esc(ont)}</a>"), ("Version", esc(ver))]
        for p, l in ((OWL.versionIRI, "Version IRI"), (OWL.priorVersion, "Previous version")):
            x = g.value(ont, p)
            if x is not None: meta.append((l, f"<span class=\"iri\">{esc(x)}</span>"))
        for p, l in ((DCT.issued, "Issued"), (DCT.modified, "Modified")):
            x = lit(g, ont, [p])
            if x: meta.append((l, esc(x)))
        meta.append(("DOI", f"<a href=\"https://doi.org/10.5281/zenodo.{doi}\">10.5281/zenodo.{doi}</a>"))
        meta.append(("BioPortal", f"<a href=\"https://bioportal.bioontology.org/ontologies/{k.upper()}\">{k.upper()} on BioPortal</a>"))
        lic = g.value(ont, DCT.license)
        if lic is not None: meta.append(("Licence", f"<a href=\"{esc(lic)}\">{esc(lic)}</a>"))
        cr = sorted(str(o) for o in g.objects(ont, DCT.creator))
        if cr: meta.append(("Authors", ", ".join(f"<a href=\"{esc(c)}\">{esc(c.rsplit('/', 1)[-1])}</a>" for c in cr)))
        here_files = set(files)
        modrows = []
        for f, (iri, mt, imps) in sorted(mods.items()):
            ims = []
            for i in imps:
                fn = i.rstrip("/").rsplit("/", 1)[-1]
                missing = "/imports/" in i and fn not in here_files
                fam = next((kk for kk, *_ in FAM if i.startswith(BASE + kk + "/") or i.rstrip("/") == BASE + kk), None)
                note = (" <span class=\"st\">(extract file not included in this release folder)</span>" if missing
                        else (f" <a class=\"st\" href=\"../{fam}/\">{fam.upper()} documentation</a>" if fam and fam != k else ""))
                ims.append(f"<span class=\"iri\">{esc(i)}</span>" + note)
            modrows.append(f"<tr><td><a href=\"{REPO}/blob/main/{k}/{v}/{esc(f)}\">{esc(f)}</a></td><td>{esc(mt)}<div class=\"iri\">{esc(iri)}</div></td>"
                           f"<td>{'<br>'.join(ims) or 'None'}</td></tr>")
        meta.append(("Files", "<br>".join(f"<a href=\"{REPO}/blob/main/{k}/{v}/{esc(f)}\">{esc(f)}</a>" for f in files)))
        c = cff(os.path.join(d, "CITATION.cff"))
        names = ", ".join(f"{fam} {''.join(x[0] for x in giv.split())}" for fam, giv in c["authors"])
        cite = f"{esc(names)}. {esc(c['title'])}, version {esc(c['version'])}. HealthEconomics.wiki; {esc(c['date'][:4])}. https://doi.org/10.5281/zenodo.{doi}"
        terms = {kd: [] for kd in VOCAB + ["Concept", "Individual"]}
        for u, (kk, a) in own.items():
            if kk == k: terms[kind_of[u]].append(u)
        dep = lambda u: (URIRef(u), OWL.deprecated, Literal(True)) in g
        chips = []
        for kd, us in terms.items():
            if not us: continue
            nd = sum(1 for u in us if dep(u))
            live = len(us) - nd
            word = lambda x: (SING[kd] if x == 1 else PLURAL[kd]).lower()
            chips.append(f"<span class=\"chip\">" + (f"{live:,} {esc(word(live))}" + (f" (plus {nd:,} deprecated)" if nd else "") if live
                         else f"{nd:,} deprecated {esc(word(nd))}") + "</span>")
        nshapes = len(set(sg.subjects(RDF.type, SH.NodeShape)))
        if nshapes: chips.append(f"<span class=\"chip\">{nshapes:,} SHACL node shapes</span>")
        head = [f"<p class=\"kicker\"><a href=\"../\">Health Economics Ontologies</a></p><h1>{esc(title)}</h1>",
                f"<p class=\"lede\">{esc(desc)}</p>" if desc else "",
                "<dl class=\"meta\">" + "".join(f"<dt>{x}</dt><dd>{y}</dd>" for x, y in meta) + "</dl>",
                "<div class=\"stats\">" + "".join(chips) + "</div>",
                f"<h2>Cite this release</h2><p class=\"cite\">{cite}</p>",
                "<h2>What these pages list</h2><p class=\"lede small\">These pages list every term the ontology defines in its own namespace, "
                f"<span class=\"iri\">{esc(BASE + k)}/</span>"
                + (", and every HEO concept at its wiki address <span class=\"iri\">https://healtheconomics.wiki/concept/</span>" if k == "heo" else "")
                + ". Terms from other ontologies, such as BFO, IAO and PROV, are linked where they are used and marked external. "
                "Deprecated terms are counted separately in the figures above.</p>",
                "<h2>Modules</h2><div class=\"tablewrap\"><table><tr><th>File</th><th>Module</th><th>Imports</th></tr>" + "".join(modrows) + "</table></div>"]
        # SHACL and SSSOM summaries
        if nshapes:
            rows = []
            for sh in sorted(set(sg.subjects(RDF.type, SH.NodeShape)), key=str):
                tg = [link(o, (k, "index.html")) for p in (SH.targetClass, SH.targetNode, SH.targetSubjectsOf, SH.targetObjectsOf) for o in sg.objects(sh, p)]
                msg = lit(sg, sh, [SH.message, RDFS.comment, SH.description, RDFS.label])
                rows.append(f"<tr><td class=\"iri\">{esc(re.split(r'[/#]', str(sh).rstrip('/'))[-1])}</td><td>{', '.join(tg) or 'see file'}</td>"
                            f"<td>{len(list(sg.objects(sh, SH.property)))}</td><td>{esc(msg)}</td></tr>")
            head.append("<h2>SHACL shapes</h2><details class=\"grp\"><summary>" + f"{nshapes:,} node shapes</summary><div class=\"tablewrap\"><table>"
                        "<tr><th>Shape</th><th>Target</th><th>Property shapes</th><th>Message or description</th></tr>" + "".join(rows) + "</table></div></details>")
        ss = [f for f in files if f.endswith(".sssom.tsv")]
        if ss:
            lines = []
            for f in ss:
                cnt = collections.Counter()
                hdr = None
                for line in open(os.path.join(d, f), encoding="utf-8"):
                    if line.startswith("#") or not line.strip(): continue
                    cols = line.rstrip("\n").split("\t")
                    if hdr is None: hdr = cols; continue
                    row = dict(zip(hdr, cols)); cnt[row.get("predicate_id", "?")] += 1
                lines.append(f"<li><a href=\"{REPO}/blob/main/{k}/{v}/{esc(f)}\">{esc(f)}</a>, {sum(cnt.values()):,} mappings ("
                             + ", ".join(f"{esc(p)} {n:,}" for p, n in cnt.most_common()) + ")</li>")
            head.append("<h2>Mappings</h2><ul>" + "".join(lines) + "</ul>")
        # page index and the main page body
        sub_pages = collections.defaultdict(list)
        for u, (kk, p) in page_of.items():
            if kk == k and p != "index.html": sub_pages[p].append(u)
        main = list(head)
        main.append("<h2>Terms</h2><label for=\"q\" class=\"muted\">Filter this page by label, identifier, synonym or definition</label><br>"
                    "<input id=\"q\" class=\"search\" type=\"search\" autocomplete=\"off\"> <span id=\"n\" class=\"muted\"></span>")
        if sub_pages:
            main.append("<p class=\"small muted\">" + ("Concepts are listed by first letter on separate pages, and records by type." if k == "heo" else "Records are listed by type on separate pages.") + "</p><nav class=\"pages\">"
                        + "".join(f"<a href=\"{esc(p)}\">{esc(('Concepts ' + p[9:-5].upper()) if p.startswith('concepts') else page_label[(k, p)])} ({len(us):,})</a>"
                                  for p, us in sorted(sub_pages.items())) + "</nav>")
        for kd in VOCAB:
            us = [u for u in terms[kd] if page_of[u] == (k, "index.html")]
            if not us: continue
            us.sort(key=lambda u: label_of(u).lower())
            main.append(f"<details class=\"grp\" open><summary>{esc(PLURAL[kd])} ({len(us):,})</summary>" + "".join(render(u, (k, "index.html")) for u in us) + "</details>")
        alts = [("text/turtle", f"{RAW}/{k}/{v}/{f}") for f in files if f.endswith(".ttl") and "shapes" not in f] + \
               [("application/rdf+xml", f"{RAW}/{k}/{v}/{f}") for f in files if f.endswith(".owl")]
        ld = {"@context": "https://schema.org", "@type": "Dataset", "name": title, "version": ver, "description": desc,
              "identifier": f"https://doi.org/10.5281/zenodo.{doi}", "url": str(ont), "license": str(lic) if lic is not None else None,
              "creator": [{"@type": "Person", "@id": c2} for c2 in cr],
              "distribution": [{"@type": "DataDownload", "contentUrl": h, "encodingFormat": t} for t, h in alts]}
        os.makedirs(os.path.join(ROOT, "docs", k), exist_ok=True)
        ps = {"index.html": sorted(u for u in own if page_of[u] == (k, "index.html"))}
        open(os.path.join(ROOT, "docs", k, "index.html"), "w", encoding="utf-8", newline="\n").write(
            page(f"{k.upper()} {v} documentation", f"Terms, definitions and links in the {title}, version {ver}.", "".join(main), alts, ld))
        for p, us in sorted(sub_pages.items()):
            us.sort(key=lambda u: label_of(u).lower())
            ps[p] = us
            body = [f"<p class=\"kicker\"><a href=\"../\">Health Economics Ontologies</a> · <a href=\"index.html\">{esc(k.upper())} {esc(v)}</a></p>",
                    f"<h1>{esc(title)}</h1><p class=\"muted\">{len(us):,} {'concepts' if p.startswith('concepts') else 'records'} on this page.</p>",
                    "<label for=\"q\" class=\"muted\">Filter this page</label><br><input id=\"q\" class=\"search\" type=\"search\" autocomplete=\"off\"> <span id=\"n\" class=\"muted\"></span>",
                    "".join(render(u, (k, p)) for u in us)]
            open(os.path.join(ROOT, "docs", k, p), "w", encoding="utf-8", newline="\n").write(
                page(f"{k.upper()} {v}, " + (f"concepts {p[9:-5].upper()}" if p.startswith("concepts") else page_label[(k, p)]), f"Part of the documentation for the {title}, version {ver}.", "".join(body)))
        manifest["pages"][k] = ps
        manifest["ontologies"][k] = {"version": v, "title": title, "doi": doi,
                                     "counts": {kd: len(us) for kd, us in terms.items() if us},
                                     "deprecated": sum(1 for kd, us in terms.items() for u in us if dep(u)), "shapes": nshapes}
    cards = "".join(f"<div class=\"card\"><h3><a href=\"{k}/\">{esc(manifest['ontologies'][k]['title'])}</a></h3><p class=\"muted\">Release {esc(v)}</p><p>{esc(s)}.</p></div>"
                    for k, v, _, s in FAM)
    body = ("<p class=\"kicker\">HealthEconomics.wiki</p><h1>Health Economics Ontologies</h1>"
            "<p class=\"lede\">HealthEconomics.wiki publishes eight linked ontologies for health economics. HEO holds the concepts of the field, "
            "and each of the other seven covers one part of it. "
            "Each ontology has a page that lists every term in the current release with its definition and links.</p>"
            f"<div class=\"cards\">{cards}</div>"
            f"<p class=\"muted\" style=\"margin-top:1.6rem\">Files, licence and citation details are in the <a href=\"{REPO}\">GitHub repository</a>. "
            "The ontology pages on the wiki are at <a href=\"https://healtheconomics.wiki/ontologies\">healtheconomics.wiki/ontologies</a>.</p>")
    ld = {"@context": "https://schema.org", "@type": "DataCatalog", "name": "Health Economics Ontologies", "url": REPO,
          "dataset": [{"@type": "Dataset", "name": manifest["ontologies"][k]["title"], "identifier": f"https://doi.org/10.5281/zenodo.{doi}"} for k, v, doi, _ in FAM]}
    open(os.path.join(ROOT, "docs", "index.html"), "w", encoding="utf-8", newline="\n").write(
        page("Health Economics Ontologies", "Documentation for the eight HealthEconomics.wiki ontologies.", body, (), ld))
    open(os.path.join(ROOT, "docs", ".nojekyll"), "w").write("")
    json.dump(manifest, open(os.path.join(ROOT, "docs", "manifest.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return manifest


if __name__ == "__main__":
    m = build()
    for k, x in m["ontologies"].items(): print(k, x, len(m["pages"][k]), "pages")
