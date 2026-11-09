# HEAO 0.2.0 (8 November 2026)

Address release. No class, property, definition or axiom has changed since 0.1.0.

| Item | HEAO 0.1.0 | HEAO 0.2.0 |
|---|---|---|
| Ontology identifier | https://healtheconomics.wiki/ontology/heao | https://healtheconomics.wiki/ontologies/heao |
| Version identifier | https://healtheconomics.wiki/ontology/heao/0.1.0/heao.owl | https://healtheconomics.wiki/ontologies/heao/0.2.0/heao.owl |
| Term addresses | https://healtheconomics.wiki/ontology/heao/... | https://healtheconomics.wiki/ontologies/heao/... |
| Imports | earlier family releases at /ontology/ | the family releases of 8 November 2026 at /ontologies/ |

## Why

The ontology pages on the site moved to https://healtheconomics.wiki/ontologies/<name>. The identifiers now match the pages. The old /ontology/ addresses are retired and are not redirected. The prior version identifier, https://healtheconomics.wiki/ontology/heao/0.1.0/heao.owl, is kept as published.

## Checks

Every file was compared with the previous release triple by triple after mapping the old addresses and versions to the new ones. Only the ontology header differs. The merged file was checked for consistency with the ELK reasoner.

# HEAO changelog

## 0.1.0 (alpha), 18 October 2026

### Fix pass after three independent reviews, 18 October 2026

Reviews A (standards), B (content) and C (mappings) all found the release ready with fixes. Every MUST and SHOULD item was acted on, and NICE TO HAVE items where cheap. Each is logged in `../heao-v0.1.0-review/fix-log.csv`. The version stays 0.1.0, because nothing had been published.

- **Namespace.** Term IRIs changed from `https://healtheconomics.wiki/ontology/heao#HEAO_0000001` to `https://healtheconomics.wiki/ontology/heao/HEAO_0000001`, the pattern of RHEO, OHEO and HETO, so each term can have its own page. One prefix map in every file. This is a decision for Darrin Baines to confirm.
- **Health state scoring split.** Health outcome valuation (HEAO_0000002) is now health-adjusted time valuation, time into QALYs or DALYs. The new health state scoring holds preference-based index scoring and the new capability index scoring. The bridge of OHEO utility mapping was removed, as mapping is not yet valuation.
- **Disjointness.** The seven kinds of valuation are no longer disjoint, so one process can be a QALY calculation and a time valuation or a severity weighting, as RHEO's QC1 is. Every disjointness group has at most one member with bridged subclasses, and the bridge now entails no disjointness between OHEO or RHEO classes (640 pairs before).
- **Record rules.** The HEAO shapes apply only to records that use HEAO, so the RHEO and OHEO valid examples pass with HEAO loaded (164 violations before). New rule that a weight is not also a specification.
- **Bridge.** 19 subclass axioms and 1 disjointness axiom. Removed utility estimate (not every one is applied), utility mapping and monetary valuation estimate (a whole benefit is a result, not a rate). Cost estimation now sits under valuation only. OHEO preference weight moved from utility decrement to directly under valuation weight (OHEO already names it value set coefficient). Value of a statistical life and of a statistical life year added. Copied labels removed.
- **Thresholds.** Cost-effectiveness threshold value is now estimated supply-side threshold value. The new adopted threshold value holds NICE's £25,000 and £35,000 per QALY, which PMG36 section 6.3.1 intends to reflect opportunity cost. Health opportunity cost valuation applies any money value of a QALY.
- **New classes (33).** Health state scoring, capability index scoring, wellbeing-adjusted time valuation, monetary value of wellbeing, informal care valuation, proxy good method, well-being valuation method, accounting cost method, monetary benefit valuation, decision modifier weighting, size of benefit weighting, decision modifier rule, size of benefit weighting rule, decision modifier QALY weight, size of benefit weight (NICE PMG36 table 6.2), adopted threshold value, MCDA criterion weight, partial value function, MCDA weighted sum valuation, MCDA criterion weighting method, population EVSI estimate, ENBS estimate, non-constant rate discounting method, stepped declining rate discounting method, differential discounting specification, relative and absolute inequality aversion parameters, cross-ontology relationship kind, and the classes of named values price basis, cost increment basis, valuation component, appropriateness verdict and discounted stream.
- **Changed classes.** Productivity cost valuation covers unpaid work and premature death. Monetary revaluation covers a change of price basis. Equity weighting and equity weight sit under the new decision modifier classes. Hyperbolic discounting sits under non-constant rate discounting. Valuation provenance record is a data entity. The DALY scale states which DALY is meant. The capability index scale follows OHEO's anchors.
- **Properties.** The four free-text enumerations became object properties with named values (has price basis, has cost increment basis, has changed component, has appropriateness verdict), and applies to stream was added. Expresses time preference became is justified in part by. Linking kinds were reviewed. Follows valuation specification, uses valuation method, from valuation perspective and revaluation of are representational, and has health opportunity cost is computational. Linking kind individuals are typed and given as CURIEs in the SSSOM file.
- **Individuals.** Additive form and WELLBY scale, and 17 named values.
- **Sources.** HEMO-HOOK-02 and hyperbolic discounting cite Frederick et al. 2002 (footnote 13, to be confirmed by the curator). The EVPPI estimate cites Brennan et al. 2007, not Ades et al. 2004. Net benefit pairs Stinnett and Mullahy 1998 with Drummond et al. 2015. New citations were checked in Crossref and Europe PMC, and Frijters et al. 2020 was dropped for HM Treasury 2021, which defines the WELLBY.
- **SSSOM.** Row directions fixed (utility broad match, QALY and DALY calculation methods narrow match, acquisition cost, equity-weighted analysis and hyperbolic discounting related match). Resource valuation, exponential discounting, VOI analysis and preference weight added, with about 50 further HEO concepts. The revaluation row to RHEO adjusts cost record was replaced. Mapping justification is unspecified matching until a curator signs rows off.
- **Examples.** Value of information at £25,000 and £35,000 per QALY (the decision changes). Health opportunity cost at both values. Population EVPI rounded correctly (£11,620,376.79). A seventeenth planted error.
- **Files.** heao-base.owl added. The RHEO uncertainty module is imported. Import identity is checked against SHA-256 values recorded at build. The valid examples of RHEO 0.3.0 and OHEO 0.2.0 are copied for the compatibility checks. Identifiers are kept stable in `src/ids.json`.

### For 0.2.0

- Added therapeutic value (an ordinal appraisal rating, which needs an ordinal value scale) and real option value with the other augmented elements of value (Lakdawalla et al. 2018).
- Value of implementation, a causal relationship in RHEO between spending and displaced care, and a property for the intended basis of an adopted threshold.

### First build

First release, built from the stage 1 design and inventory of 17 October 2026 (`../stage-1`) and the locked decisions of Michelle Ashley of 18 October 2026, following the pattern of OHEO 0.2.0 and HETO 0.2.0.

#### Added

- 78 classes, 30 object properties, 13 datatype properties, 20 named individuals and 2 annotation properties in the first build, before the fix pass.
- The act (valuation and 14 kinds), the judgement (valuation specification, equity weighting rule, severity weighting rule), the method (valuation method and 15 kinds), the numbers (valuation weight and its kinds, valuation parameters), weight functions, valuation functions, eight functional forms, value scales and seven named scales, the two perspectives, the valuation context, provenance, appropriateness and change records, three defined classes, and value of information estimates.
- Discounting as the valuation of time (time valuation, discount factor, discount rate, time preference), citing Drummond et al. 2015 and Attema et al. 2018.
- Value of information from the start (value of information analysis, EVPI, EVPPI, EVSI and population EVPI estimates, nested Monte Carlo and regression-based EVPPI methods), citing Claxton 1999, Ades et al. 2004, Brennan et al. 2007 and Strong et al. 2014.
- The bridge module `heao-bridge.ttl`, with 20 subclass axioms placing OHEO and RHEO classes under HEAO parents and one disjointness axiom between RHEO's perspective specification (the analytic perspective) and the HEAO valuation perspective. OHEO 0.2.0 and RHEO 0.3.0 are imported unchanged.
- The annotation property has linking kind (`HEAO_9000001`) and five linking kind individuals. Every HEAO object property and every bridge axiom carries one.
- The annotation property has HEMO hook (`HEAO_9000002`) and `hemo-hooks.md`, with twenty formula hooks.
- `heao-shapes.ttl`, the record rules, and `heao-mappings.sssom.tsv`, with mappings to HEO 1.3.0 concepts, the bridge axioms and property correspondences.
- Worked examples (QALY valuation from an EQ-5D-5L profile, unit-cost costing, coexisting valuations of the same bed days, a change of valuation, a price year adjustment, discounting at 3.5% a year, severity and equity weighting, health-money exchange, health opportunity cost and EVPI), 16 planted errors and 3 planted contradictions.
- `run_demo.py` with 12 competency questions.

#### Proposed for other ontologies (not changed here)

- OHEO 0.2.1. Make `OHEO_2000025` has QALY weight obsolete, with consider `HEAO_0000050` severity weight. This is the one move decided on 18 October 2026. Remove the HEO mappings of cost to economic outcome domain and of resource use to resource use outcome area, and relate costs to outcomes only through has health opportunity cost (`HEAO_1000024`). Review the placement of indirect health state valuation and the inputs allowed by the QALY calculation rule. See `oheo-0.2.1-proposal.md`.
- RHEO. A time-in-state record, an incremental health effect record and the others in `rheo-backlog-additions.md`.
- HEO. New concepts and a merge-review item in `heo-new-concepts-from-heao.md`. Five of the six gaps found in stage 1 are already live in HEO 1.3.0.

#### Sources checked

- NICE PMG36 (published 31 January 2022, last updated 13 October 2026), read on 18 October 2026, sections 4.5.1, 6.2.13 to 6.2.18 with table 6.1, and 6.3.4 to 6.3.8, and the update information page. See `src/checked-sources.md`.
