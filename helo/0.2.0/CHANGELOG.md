# HELO 0.2.0 (8 November 2026)

Address release. No class, property, definition or axiom has changed since 0.1.0.

| Item | HELO 0.1.0 | HELO 0.2.0 |
|---|---|---|
| Ontology identifier | https://healtheconomics.wiki/ontology/helo | https://healtheconomics.wiki/ontologies/helo |
| Version identifier | https://healtheconomics.wiki/ontology/helo/0.1.0/helo.owl | https://healtheconomics.wiki/ontologies/helo/0.2.0/helo.owl |
| Term addresses | https://healtheconomics.wiki/ontology/helo/... | https://healtheconomics.wiki/ontologies/helo/... |
| Imports | earlier family releases at /ontology/ | the family releases of 8 November 2026 at /ontologies/ |

## Why

The ontology pages on the site moved to https://healtheconomics.wiki/ontologies/<name>. The identifiers now match the pages. The old /ontology/ addresses are retired and are not redirected. The prior version identifier, https://healtheconomics.wiki/ontology/helo/0.1.0/helo.owl, is kept as published.

The BioPortal file, helo-0.2.0-merged.owl, now carries the main ontology identifier https://healtheconomics.wiki/ontologies/helo instead of a file-specific one.

## Checks

Every file was compared with the previous release triple by triple after mapping the old addresses and versions to the new ones. Only the ontology header differs. The merged file was checked for consistency with the ELK reasoner.

# Changelog

## 0.1.0 (alpha), 19 October 2026, fixed after review on 19 October 2026

First release of the Health Economics Learning Ontology (HELO), built to Darrin Baines's scope of 18 October 2026 and following the build pattern of HEAO 0.1.0 and HEMO 0.1.0. HELO here is the Health Economics Learning Ontology of HealthEconomics.wiki. It is not the HypothEsis and Law Ontology, also called HELO (Soldatova et al. 2013), and is unrelated to it. Three independent reviews (standards, learning design and content, and mappings and sources) were all ready with fixes on 19 October 2026. The fixes are made in place, still as version 0.1.0 and unpublished, and are listed below and, finding by finding, in `../helo-v0.1.0-review/fix-log.csv`. Nothing has been uploaded.

### Added

- The core, helo.ttl, with 14 classes for learning pathways, learning steps, learning topics, pathway frameworks, intended learner profiles, learning goals with their two disjoint kinds, prerequisite relationships and their derivation rules, curricula, course modules and two status vocabularies.
- 28 object properties, among them the ordered step relationships (has learning step, has next learning step, functional, inverse functional, asymmetric and irreflexive), the core and optional concepts of a step, the concepts a pathway builds on and leads to, leads into step for the Knowledge Map junctions, and prepares for task, which never trains.
- 5 datatype properties for positions, display order and HEO relationship identifiers, and 24 annotation properties for the site's own text, the course outline's text and the proposals with their basis and counts.
- 17 vocabulary individuals, six intended learner profiles, two publication statuses, four prerequisite statuses and five prerequisite derivation rules.
- Darrin Baines's disclaimer on the learning pathway class, "Learning pathways build understanding, not hands-on skills."
- helo-pathways.ttl, generated from a read-only snapshot of the live site, with the eight published pathways, their 42 steps and topics, 8 frameworks, 8 pathway goals and 41 step goals, 348 core and 664 optional concept relationships, the 7 Knowledge Map junctions, and the semantic layer course as one draft curriculum with ten modules, its outcomes as eleven goals and Darrin Baines's six building blocks as learning topics.
- 391 prerequisite relationships proposed from 393 HEO 1.3.1 relationships, each with its HEO-L- identifiers, its rule, HEO's review status and rationale, the pathways whose order agrees or conflicts with it, and for a conflict where each concept sits and review B's recommendation.
- 15 proposed task preparations from pathways to HETO 0.2.0 tasks, 31 proposed intended learners, 3 proposed module topics and 2 proposed topic orders, with their basis on each axiom.
- Extracts of IAO 2026-03-30, the HEAO 0.1.0 linking kinds, HEO 1.3.1 and HETO 0.2.0, each keeping the source identifiers and labels.
- 14 shapes in plain SHACL, 23 planted errors, 6 planted contradictions, a worked example and 12 competency questions.
- helo-mappings.sssom.tsv with 38 primary cross-ontology rows and 23 secondary rows to the Curriculum KG Ontology and schema.org.
- site-text-proposals.csv, heto-0.2.1-proposal.md, proposals-from-helo.md, run_demo.py, and the note for Darrin Baines.

### Changed after the three reviews

- The name HELO is kept (curator decision 1), and every header, the shapes, the BioPortal header and the README say it is not the HypothEsis and Law Ontology (reviewer A M1).
- Understanding and capability are split by the revised Bloom taxonomy (Krathwohl 2002). Understanding goals may name learning topics, so course outcome 1 and the first half of outcome 4 are understanding goals, and outcome 4 is split in two (curator decision 2, reviewer B M1 and M2).
- Steps have their own concept understanding goals, made by the build and marked requires discussion (reviewer B S6).
- Used to calculate gives a proposal only where the result's HEO definition names the input, assumes is read as taught no later than, proposals from unreviewed HEO relationships have their own status, and the factor loading cycle is broken. 371 proposals of the first build no longer qualify (curator decision 3, reviewer B S1 to S3).
- Conflicts cover a pathway that builds on the dependent concept, and record where each concept sits and review B's recommendation. Builds-on concepts taught by no pathway and cycles between pathways are found and reported (reviewer B M3 and M4).
- Learners are review B's mapping as proposals. Task preparation needs at least two covered concepts on tasks with three or more (curator decision 4, reviewer B S7 and S10).
- The site's task wording is answered with `site-text-proposals.csv`, with the snapshot unchanged (curator decision 5, reviewer B M5).
- Steps and modules are directive information entities and prerequisite records data entities. No property whose values are HEO concepts is functional, and HELO's vocabularies are declared different (reviewer A S1 and S2).
- dcterms contributor and date are declared, the shape messages each belong to one constraint, topic proposals have a rule, outcomes are keyed on their text, and the build stops rather than asserts (reviewer A M2, M3, S3 and S4).
- The BioPortal file leaves out the HEO and HETO copies and the unreviewed proposals, with version IRI .../helo/0.1.0/helo-merged.owl (reviewer A S6).
- The SSSOM file has the right subject sources and schema.org types, HEO's labels, reasons equal to the axioms, confidence 0.6 for rule outputs, the Curriculum KG readable copy and namespaces in its header, and the reworded rows reviewer C named (reviewer A S5, reviewer C).
- The building block definitions keep NISO's note and minimum rules, equivalence, the real world and the realist sense of ontology, and NISO's order of controlled vocabularies is a proposal (reviewer B S8).

### Found while building

- The acronym HELO is already the name of the HypothEsis and Law Ontology (Soldatova et al. 2013).
- HEMO 0.1.0's HEAO linking kinds extract, as rewritten on 19 October, takes hemo.owl out of OWL 2 DL, because its header uses three undeclared Dublin Core properties. HELO uses its own extract of the same terms.
- Two HETO 0.2.0 shapes target every IAO objective specification, so they flag HELO's learning goals when both are loaded (`heto-0.2.1-proposal.md`).
- The Curriculum KG Ontology uses two namespaces, one in its schema and one in its data, and its learning step axioms would contradict the first and last steps of a pathway in meaning, so HELO maps to it rather than subclassing it.
- The upload file of 12 October names 18 obsolete HEO concepts that the live site already drops.
- The one lines of the live pathways describe tasks, while the scope says pathways build understanding.
