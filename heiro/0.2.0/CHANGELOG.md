# HEIRO 0.2.0 (8 November 2026)

Address release. No class, property, definition or axiom has changed since 0.1.0.

| Item | HEIRO 0.1.0 | HEIRO 0.2.0 |
|---|---|---|
| Ontology identifier | https://healtheconomics.wiki/ontology/heiro | https://healtheconomics.wiki/ontologies/heiro |
| Version identifier | https://healtheconomics.wiki/ontology/heiro/0.1.0/heiro.owl | https://healtheconomics.wiki/ontologies/heiro/0.2.0/heiro.owl |
| Term addresses | https://healtheconomics.wiki/ontology/heiro/... | https://healtheconomics.wiki/ontologies/heiro/... |
| Imports | earlier family releases at /ontology/ | the family releases of 8 November 2026 at /ontologies/ |

## Why

The ontology pages on the site moved to https://healtheconomics.wiki/ontologies/<name>. The identifiers now match the pages. The old /ontology/ addresses are retired and are not redirected. The prior version identifier, https://healtheconomics.wiki/ontology/heiro/0.1.0/heiro.owl, is kept as published.

The BioPortal file, heiro-0.2.0-merged.owl, now carries the main ontology identifier https://healtheconomics.wiki/ontologies/heiro instead of a file-specific one.

## Checks

Every file was compared with the previous release triple by triple after mapping the old addresses and versions to the new ones. Only the ontology header differs. The merged file was checked for consistency with the ELK reasoner.

# HEIRO changelog

## 0.1.0 (alpha), 19 October 2026

First release of the Health Economics Institutions and Rules Ontology. Reviewed by three independent reviewers on 19 October 2026 and fixed in place, still unpublished. Not uploaded.

### Renamed from HEIO to HEIRO, 20 October 2026

- The ontology was built and reviewed as HEIO, the Health Economics Institutional Ontology. The acronym HEIO is already taken on BioPortal by the Regional Healthcare System Interoperability and Information Exchange Measurement Ontology (2015), so the curators renamed it HEIRO, the Health Economics Institutions and Rules Ontology. Michelle checked that HEIRO is free on BioPortal.
- The namespace is now https://healtheconomics.wiki/ontology/heiro/ and terms are HEIRO_ followed by the same seven digits as before, so every number is unchanged. Files, prefixes (heiro), titles and labels follow the new name.
- Nothing had been published under HEIO, so no deprecation records are made. The HEIO build is kept unchanged in Downloads/heio as the record of the reviews.

### Added

- The core, `heiro.ttl` and `heiro.owl`. 24 classes, among them institutional role and its two kinds, two defined classes of body, jurisdiction, guidance document and version, guidance provision, stated decision rule as a defined class, comparator rule, price benchmark rule, listed amendment, check record and the value classes for status, binding force, check method, staleness verdict, deontic modality, comparator selection basis and amendment kind. 24 object properties, 36 datatype properties, 7 annotation properties and 24 vocabulary individuals.
- The institutional register, `heiro-register.ttl`. 109 bodies (107 named on the Institutional Perspectives tab, and the European Parliament and the Council of the European Union, which issued Regulation (EU) 2021/2282), 4 jurisdictions, 9 sourced roles, 7 guidance documents with their binding force, 18 versions (8 of NICE PMG36, from 31 January 2022 to 13 October 2026), 25 dated check records, 5 listed amendments, 59 provisions with their quoted text and 29 stated decision rules.
- The wiki records, `heiro-wiki.ttl`. 926 institutional perspective records on 408 concepts, read from the live concept pages, and 653 guidance citation records of NICE PMG36 from the concept export of 17 October 2026 and the Functions and Formulae module.
- `heiro-guidance-version-report.csv`, one row per PMG36 citation with the version cited, the version it resolves to, the verdict and whether the cited text changed since.
- The record rules `heiro-shapes.ttl`, the mappings `heiro-mappings.sssom.tsv`, the BioPortal file `heiro-0.1.0-merged.owl`, the base file `heiro-base.owl`, fictional worked examples with 29 planted errors and 3 planted contradictions, `run_demo.py` with 14 competency questions, proposals for RHEO 0.4, HEAO and HEO, and the build scripts with every source page saved in `src/sources/`.

### Fixed after the three reviews (details in ../heiro-v0.1.0-review/fix-log.csv)

- HEIRO's own is issued by replaces RHEO's issued by, whose definition does not cover guidance. A widening proposal for RHEO 0.4 is in `rheo-0.4-proposals-from-heiro.md`.
- The linking kinds now come from HEAO 0.1.0's own published heao.owl, pinned to that release, and the import check passes on a fresh build.
- Versions are never edited. Their status is reported by dated check records, and SHACL ties status, supersedes and in-force dates together. The validity period class is retired, in favour of publication date, in force from and until, and first-read version date.
- Every functional property has a maximum count rule, and every date a pattern and a calendar check. Shapes now reach records that do not assert a HEIRO class.
- Each guidance document states its binding force, binding or advisory. ICER's framework is advisory with no jurisdiction, and its range is a price benchmark rule per evLY and per QALY.
- Rules may apply only to topics started after or before a date, as with PMG51 paragraphs 1.17 and 1.18 and the HealthTech transition of July 2025. PMG51's amendments now carry their kind, including the new section 4.3.10, the renumbering after it, figure 4.1 and PMG20. NICE's undated minor changes are listed amendments, such as the budget impact test of June 2025. The 20,000 to 30,000 pounds rules start on 31 January 2022.
- The citation scan counts one citation per reference with its mentions, treats the earlier title as stale, gives "updated 2026" an imprecise verdict and resolves it from other citations in the record where it can, and adds whether the cited text changed.
- Joint bodies are split into their member bodies. Regulation (EU) 2021/2282 is a guidance document, not a body. WHO Europe, HHS OIG and the NICE Decision Support Unit have their parent or commissioning body.
- The mappings follow review C, with OHEO profiles as individuals, HEO and DCMI rows added, ELI 1.5 read and mapped, no linking kind on standard vocabulary rows, and HEMO labels read from its release.

### Design choices taken from the HEAO 0.1.0 and HEMO 0.1.0 reviews

- No bridge axioms, and no disjointness, domain or range on another ontology's term. HEO is mapped only.
- Shapes with core targets only, run with plain pyshacl, targeting HEIRO terms only.
- One prefix map, slash IRIs, one ontology IRI per file, byte-stable Turtle, imports checked by SHA-256.
- Every mapping proposed with unspecified matching until a curator signs it.
- The causal kind is not used between records.

### Not in this release

- Saudi, Thai and Canadian guidance, and the other facts listed in build-report.md, which could not be read on 19 October 2026.
- Option spaces, rights and actor networks, which belong to a separate layer above HEIRO.
