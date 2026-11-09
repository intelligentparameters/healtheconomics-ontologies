# HETO 0.3.0 (8 November 2026)

Address release. No class, property, definition or axiom has changed since 0.2.0.

| Item | HETO 0.2.0 | HETO 0.3.0 |
|---|---|---|
| Ontology identifier | https://healtheconomics.wiki/ontology/heto | https://healtheconomics.wiki/ontologies/heto |
| Version identifier | https://healtheconomics.wiki/ontology/heto/0.2.0/heto.owl | https://healtheconomics.wiki/ontologies/heto/0.3.0/heto.owl |
| Term addresses | https://healtheconomics.wiki/ontology/heto/... | https://healtheconomics.wiki/ontologies/heto/... |
| Imports | earlier family releases at /ontology/ | the family releases of 8 November 2026 at /ontologies/ |

## Why

The ontology pages on the site moved to https://healtheconomics.wiki/ontologies/<name>. The identifiers now match the pages. The old /ontology/ addresses are retired and are not redirected. The prior version identifier, https://healtheconomics.wiki/ontology/heto/0.2.0/heto.owl, is kept as published.

The BioPortal file, heto-0.3.0-merged.owl, now carries the main ontology identifier https://healtheconomics.wiki/ontologies/heto instead of a file-specific one.

## Checks

Every file was compared with the previous release triple by triple after mapping the old addresses and versions to the new ones. Only the ontology header differs. The merged file was checked for consistency with the ELK reasoner.

# HETO changelog

## 0.2.0 (alpha, pilot), 17 October 2026, fix pass completed 20 October 2026

Decided by Darrin Baines on 17 October 2026 and approved by Michelle Ashley. HEO is concepts, which are not real, so HETO links to RHEO. Three independent reviews (standards, real-world links, mappings) were answered in a fix pass that was stopped on 17 October at Michelle's request and completed on 20 October, listed in `../heto-v0.2.0-review/fix-log.csv`. The version stays 0.2.0 because nothing has been uploaded. BioPortal holds 0.1.0.

### The policy
- Primary, logical links go to RHEO 0.3.0 (with its uncertainty module) and OHEO 0.2.0, and to the general IAO *document* where RHEO has no class yet. HEO concepts appear only as secondary `skos:relatedMatch` rows in the SSSOM file, for learning and navigation. No HEO IRI is in `heto.ttl`, and the build stops if one is.
- `HETO_3000001` *requires concept* is obsolete (out of scope, consider *involves type*).
- HETO imports the RHEO uncertainty module and OHEO 0.2.0 as well as RHEO 0.3.0, so draw set, value set and health state valuation process are declared classes.

### The catalogue (20 tasks, 5 composite, 20 objectives, 51 steps, 19 decomposition and 18 ordering links)
- New task *Value resource use* (`HETO_4000020`), part of *Develop an economic model*, after *Select unit costs* and before the incremental results. Resource use and unit cost estimates go in, a cost estimate comes out.
- The evidence chain joins up. *Develop an economic model* takes in the resource use, unit cost, cost, utility, probability and relative effect estimates. The PSA outputs its draw set. Links were moved, added or removed task by task as reviewer B asked (population and intervention specifications are outputs of defining the decision problem, the value set is an input of assigning utilities, the QALY record is no longer a link of that task, the undiscounted records are inputs of discounting, and so on).
- 124 catalogue links to RHEO, OHEO and IAO types. Every task names at least one RHEO or OHEO input or output.
- Every objective and step now has a short definition naming its task, so other ontologies (HEMO, HEIRO) can quote it. Every HETO term names its term editor as an ORCID (`dcterms:contributor`).
- The inputs text of *Report an economic evaluation* and *Estimate transition probabilities and treatment effects* now names what their links name.

### Rules (`heto-shapes.ttl`)
- New rules *RealTypeLinkShape* (every task names a RHEO or OHEO input or output type) and *NoHEOLinkShape* (no HEO link on a HETO task, objective, step or class). The concept rules of 0.1.0 are removed.
- Every rule targets HETO's own records only. The objective and step rules target the values of HETO's two part properties (`sh:targetObjectsOf` HETO_1000005 and HETO_1000006), not every IAO objective or action specification, so HELO's learning goals and other ontologies' records are not touched (HELO 0.1.0 proposal). The two orphan rules are dropped, because every target they could reach is part of a task, and the build stops an orphan objective or step instead. Planted error BAD15 now tests a step with no text.
- Plain SHACL only (core targets and SHACL-SPARQL constraints, run with `advanced=False`), checked by run_demo.py.

### Mappings (`heto-mappings.sssom.tsv`, 208 rows, 124 primary and 84 secondary)
- New column `mapping_tier`. Primary rows are exactly the catalogue links in `heto.ttl`; HEO rows and class-level rows are secondary.
- Every row is proposed and unreviewed, with `semapv:UnspecifiedMatching` until a named curator signs it off; the header says how.
- HEO concepts take the family prefix `hewc`. Entity types use the SSSOM 1.0 text values. New column `predicate_type`. Class-level rows have labels, not CURIEs. Three repeated reasons were rewritten.

### The BioPortal file
- `heto-0.2.0-merged.owl` is now HETO with a ROBOT BOT extract of the external terms it uses, not the whole of RHEO, OHEO and BFO. Each extracted RHEO and OHEO term says which ontology defines it.
- It has its own ontology IRI `https://healtheconomics.wiki/ontology/heto/heto-merged.owl`, with version IRI `.../heto/0.2.0/heto-0.2.0-merged.owl` and prior version `.../heto/0.1.0/heto-0.1.0-merged.owl`, following HEMO 0.1.0. `heto.owl` keeps `https://healtheconomics.wiki/ontology/heto`.

### Checks (`run_demo.py`)
- New section 11 runs `src/family_compat.py`. It checks that loading HETO leaves the valid records of RHEO, OHEO, HEAO, HEMO, HELO and HEIRO unchanged under their own rules and under OWL 2 RL, and that HETO's rules give no result on them.
- New checks on import SHA-256 against the release files, step definitions, the SSSOM justification and prefix, plain SHACL, rules that target only HETO records, the OWL 2 DL profile of the worked example and the BioPortal file's IRIs and contents.
- The build raises an error instead of using `assert`, so `python -O` cannot skip a gate.
- Created and issued stay 2026-10-17; modified is 2026-10-20.

### Notes
- `rheo-backlog-additions.md` lists real things HETO needs that RHEO 0.3.0 lacks. `heto-sankey-proposal.md` says how the Relationship Map should show HETO through RHEO classes.

### Left for 0.3.0
- A value of information task (HEMO 0.1.0 proposal 1), with the other planned tasks (evidence synthesis, budget impact, trial-based evaluation) and appraisal side and health system tasks (HELO 0.1.0 proposal).
- Splitting validation into three tasks with a reviewer role, and the CHEERS concept for HEO (from 0.1.0).
- A `linking_kind` column with the HEAO linking kinds, once HEAO_9000001 is widened beyond HEAO's own relationships.
- sssom-py in the toolchain, so the SSSOM validator gates the build.

## 0.1.0 (alpha, pilot), 16 October 2026

First release, with the fix pass from three reviews. See `../heto-v0.1.0/CHANGELOG.md`.
