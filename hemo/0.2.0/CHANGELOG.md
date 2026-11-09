# HEMO 0.2.0 (8 November 2026)

Address release. No class, property, definition or axiom has changed since 0.1.0.

| Item | HEMO 0.1.0 | HEMO 0.2.0 |
|---|---|---|
| Ontology identifier | https://healtheconomics.wiki/ontology/hemo | https://healtheconomics.wiki/ontologies/hemo |
| Version identifier | https://healtheconomics.wiki/ontology/hemo/0.1.0/hemo.owl | https://healtheconomics.wiki/ontologies/hemo/0.2.0/hemo.owl |
| Term addresses | https://healtheconomics.wiki/ontology/hemo/... | https://healtheconomics.wiki/ontologies/hemo/... |
| Imports | earlier family releases at /ontology/ | the family releases of 8 November 2026 at /ontologies/ |

## Why

The ontology pages on the site moved to https://healtheconomics.wiki/ontologies/<name>. The identifiers now match the pages. The old /ontology/ addresses are retired and are not redirected. The prior version identifier, https://healtheconomics.wiki/ontology/hemo/0.1.0/hemo.owl, is kept as published.

The BioPortal file, hemo-0.2.0-merged.owl, now carries the main ontology identifier https://healtheconomics.wiki/ontologies/hemo instead of a file-specific one.

## Checks

Every file was compared with the previous release triple by triple after mapping the old addresses and versions to the new ones. Only the ontology header differs. The merged file was checked for consistency with the ELK reasoner.

# Changelog

## 0.1.0 (alpha), 18 October 2026, fixed after review on 19 October 2026

First release of the Health Economics Mathematics Ontology (HEMO), built from the stage 1 design (design.md, inventory.csv) with the recommended option of each of the 15 open decisions of its section 12. Three independent reviews (standards, content, and mappings and sources) were all ready with fixes on 19 October 2026. The fixes are made in place, still as version 0.1.0 and unpublished, and are listed below and, finding by finding, in `../hemo-v0.1.0-review/fix-log.csv`. Nothing has been uploaded.

### Added

- The core, hemo.ttl, with 39 classes for expressions, equations, formulas, mathematical functions, computational functions, implementations, test cases, test values, assumptions, variables, quantity kinds, units of measure, domains of validity, model structures, model components, model types, analysis wrappers and parameter bindings, and eleven kinds of named value.
- 64 object properties, among them Darrin Baines's eight relationships (realises, uses formula, uses computational function, implements, requires input, returns output, assumes, has test), the mathematical relationships between formulas (special case of, is limit of, implies condition of, algebraically equivalent to, inverse of, approximates, derived from, feeds), the four relationships of a parameter binding, and the property chain has implemented model type.
- 40 operators with their OpenMath symbols, and the content dictionary cd/hemo1.ocd for the seven operations OpenMath does not hold, each with a CMP and an example.
- 32 units of measure with UCUM codes and their variants, aligned with QUDT, and 51 quantity kinds with their dimensions, bounds and OHEO measurement scale types.
- 11 model types defined by their level, treatment of time, memory, interaction and stochasticity, a feature taking more than one value where the type allows it.
- The formula catalogue, hemo-formulae.ttl, generated from ff_master.csv with identifiers stable on the module Record ID, holding every Function, Applied Formula and Computational Function of the module with their variables, assumptions, tests, implementations, common errors and sources.
- 65 fully formalised records. 46 module formulas enriched by src/key_formulas.py, 18 HEMO-native formulas (HEAO hooks the module lacked, the arithmetic of eight RHEO competency queries, the dominance family, the general EVPPI estimator and the weighted net health benefit) and the flagship three-state Markov model structure.
- The HEMO grammar, writer of Content MathML and LaTeX, reader of Content MathML, evaluator and dimension checker (src/grammar.py), and the test runner (src/runner.py) with its tests, round trip, signature, tree, dimension, kind, money and computed-by rules.
- 21 SHACL shapes in plain SHACL, 26 planted errors and 3 planted contradictions.
- SSSOM mappings with the cross-ontology relationships as primary rows.
- heao-hooks-resolved.md, heo-calculated-from-coverage.csv, module-backlog.md, heo-new-concepts-from-hemo.md, rheo-0.4-proposals-from-hemo.md and heto-proposals-from-hemo.md.

### Changed after the three reviews

- A formula's identity is its expression with its assumptions and domain of validity. Tests are evidence, not identity. Formula now sits beside mathematical expression and is disjoint from it (curator decision 2, reviewer A S1, reviewer B S1).
- The weak or Pareto rule of HE-FM-DOM-001 is the one dominance rule, now with tie tolerances, beside new records for strict dominance, the mirror for dominated and a four-way classification. CQ8 compares the full grid of nine sign cases with RHEO cq38 and finds its two errors (curator decision 1, reviewer B M1).
- Policy figures are inputs. HE-FM-ASF-003 takes its severity cut-offs and weights, and HE-FM-TPR-003 its band ends, as inputs, with the module's text kept verbatim (curator decision 3, reviewer B S2).
- The model type of a RHEO model version follows from the property chain has implemented model type. RHEO does not import HEMO (curator decision 4).
- Bindings are parameter binding records on the RHEO model version and option, not triples on a shared structure's variables (curator decision 7).
- Unreviewed unit proposals are annotations, not facts. QALYs and DALYs have their own dimension Q and WELLBYs W, so money per QALY is no longer money per year and QALYs cannot be added to life-years. The model cycle is no longer a unit of duration (curator decision 8, reviewer A S2 and S4).
- minmax1 min and max take one set, s_data1 mean replaces hemo1 mean, n-ary operators are marked apart from constants, and the runner checks every application's signature and that the MathML and RDF trees agree. Every shape uses core SHACL targets and every run uses plain pyshacl, with a sentinel planted error (curator decision 9, reviewer A M1, M2 and S6).
- The HermiT reuse key covers the core, the imports and ROBOT, a gate checks the split is sound, and all eight parts and the worked examples were rerun fresh (curator decision 10, reviewer A M3 and S12).
- The SSSOM file has correct object sources for QUDT, STATO and SBO, the prefix hewc for HEO concepts, 34 namesake rows to HEO, takes input of type for record types that only supply inputs, representational kinds for causal claims and weights, and the corrected rows reviewer C named. Every row stays proposed (curator decision 11, reviewer A M4, reviewer C).
- Sources. Wagstaff et al. 2018 for catastrophic spending, RHEO competency queries as the definition source of three native records, Drummond et al. 2015 no longer cited for vaccine wastage, every checked DOI in the reference list, STATO and the Frederick footnote recorded as checked (curator decision 12, reviewer C).
- The BioPortal file is built from the base file and a BOT extract, without expression nodes and steps, and each file has its own ontology IRI (curator decision 13, reviewer A S8 and S9).
- The discount timing and the within-cycle correction are two vocabularies, the model type features are corrected, health quantities are typed as QALYs or DALYs, the relation directions are corrected and checked by evaluation, and new records state the weighted net health benefit at NICE's two values, the general EVPPI estimator and the prevalence-based YLD (curator decision 14, reviewer B).
- The build is self-contained and byte-stable, with a logical SHA-256 of each file (reviewer A S10).

### Found while building

- The dimension check showed that the flagship structure's cost and QALY sums leave the one-year cycle length implicit. HEMO states it as the variable L, and the results are unchanged.
- The Build demonstrator's RHEO records give annual transition probabilities the unit code /a, a rate, and the horizon in cycles the code a. RHEO 0.4 proposal 5.
- RHEO cq38 differs from the one HEMO dominance rule in two of nine cases, equal QALYs at a lower cost and identical cost and QALYs. RHEO 0.4 proposal 1.
- HermiT on the whole catalogue, about 15,000 individuals, did not finish in 40 minutes with or without its data values. src/hermit_parts.py splits it along its connected components into 8 parts that HermiT checks one by one.
- HEAO's worked QALY records count each interval at its starting utility, so the trapezium formula HE-FM-QALY-002 does not reproduce them, while HE-FM-QALY-001 reproduces HEAO's total. CQ2 compares HE-FM-QALY-002 with RHEO's own records only.
- In the module's population EVPI (HE-FM-VOI-002) T is the last year index, so the sum has T plus 1 terms, while HEAO's hook 20 counts T years. Both are right with their own T, and HEMO says so in an editor note.
- The flagship's ICER of GBP 29,360 lies between NICE's two values, so its incremental net monetary benefit changes sign between GBP 25,000 and GBP 35,000 per QALY.
