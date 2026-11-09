# OHEO 0.3.0 (8 November 2026)

Address release. No class, property, definition or axiom has changed since 0.2.0.

| Item | OHEO 0.2.0 | OHEO 0.3.0 |
|---|---|---|
| Ontology identifier | https://healtheconomics.wiki/ontology/oheo | https://healtheconomics.wiki/ontologies/oheo |
| Version identifier | https://healtheconomics.wiki/ontology/oheo/0.2.0/oheo.owl | https://healtheconomics.wiki/ontologies/oheo/0.3.0/oheo.owl |
| Term addresses | https://healtheconomics.wiki/ontology/oheo/... | https://healtheconomics.wiki/ontologies/oheo/... |
| Imports | earlier family releases at /ontology/ | the family releases of 8 November 2026 at /ontologies/ |

## Why

The ontology pages on the site moved to https://healtheconomics.wiki/ontologies/<name>. The identifiers now match the pages. The old /ontology/ addresses are retired and are not redirected. The prior version identifier, https://healtheconomics.wiki/ontology/oheo/0.2.0/oheo.owl, is kept as published.

## Checks

Every file was compared with the previous release triple by triple after mapping the old addresses and versions to the new ones. Only the ontology header differs. The merged file was checked for consistency with the ELK reasoner.

# OHEO changelog

## 0.2.0 (16 October 2026, alpha)

Built by `src/build_oheo.py` from the 0.1.0 draft (`oheo-from-bioportal.owl`, 433 classes, 38 object properties), which was not edited. Prior version `https://healtheconomics.wiki/ontology/oheo/0.1.0`. Version IRI `https://healtheconomics.wiki/ontology/oheo/0.2.0/oheo.owl`.

### Fix pass after four independent reviews (18 October 2026, still 0.2.0, never published)
Every finding and what was done with it is in `oheo-v0.2.0-review/fix-log.csv`.
- New class capability or care-related index value set (OHEO_0000400) beside value set. The ICECAP-A UK index values (0000184) move there, with the new property has published index value set (1000039). ICECAP-A, ICECAP-O and CarerQol-7D are no longer inferred to be preference-based measures, and a QALY record may not rest on index values.
- Reporter type moves to the version, with the new property has reporter type (1000040) and the values self-report (0000401), observer or proxy report (0000402) and clinician rating (0000403). Lawton IADL Scale, Barthel Index, Katz Index, PedsQL 4.0 and the EQ-5D family now sit under outcome measurement instrument.
- The instrument requirement moves from outcome measurement datum (0000189) to instrument score record (0000190), so survival records validate.
- OHEO_0000296 is now the DSU and EEPRU response mapping model (Hernández Alava et al. 2023), either direction, with the value set applied as a separate step. OHEO_0000186 is cited as PMG51 cites it.
- Rowen 2026 valued by composite time trade-off, fieldwork 2023. "In use since 2012" removed. Unchecked worst-state utilities flagged, and their rule is a Warning.
- NICE PMG51 profile rebuilt from the verified text, with the new property has topic start date (2000035). Rowen 2026 is required for adult reference-case utilities in topics started on or after 27 August 2026, not applied to EQ-5D-Y. Mapped data give a Warning (a departure from the reference case), and EQ-5D-3L value set utilities are a Violation in any analysis. The PMG36 profile is superseded for new topics only. Rules not checked against a body's own text are Warnings (10 profiles, 38 constraints, 18 at Violation level).
- Record rules recognise indirect utilities by structure, let a QALY record rest on one utility record, a model run or a source, reject utilities outside the QALY period and capability values in QALYs, and let text labels name the instrument, its family or the copy.
- Definitions changed for patient-reported outcome measure, crosswalk, EQ-5D, health state valuation process, health-adjusted life year estimate, utility function, complete response, biomarker endpoint (now under intermediate outcome) and choice experiment (now beside conjoint analysis). Health profile scoring removed from ten single-total instruments. ReQoL-10 and ReQoL-20 are condition-specific.
- Sources from reviewer B's sample added. Disease control rate, clinical benefit rate, the carer domain and the symptom domain flagged as OHEO working definitions or extensions.
- MID, MCID, EQ-5D youth, conditional logit, choice-based conjoint and CBC are related synonyms.
- Property labels that clashed with RHEO changed. OHEO_1000031 is "value set elicited by" and OHEO_2000031 "has instrument version label".
- IAO annotation properties declared in OHEO. Obsolescence reason and consider added on the 19 obsolete properties. Duplicate alternative labels removed. The disjointness between two RHEO classes dropped. Merged file `oheo-0.2.0-merged.owl` built for BioPortal.
- Mappings now 303 rows. Process and coefficient rows are related matches, four rows were dropped and fourteen added. Michelle Ashley is the author, and new columns give subject_type, object_type, confidence and review_status (proposed).
- In the type records heo_concepts is always a list, with heo_status.
- run_demo.py has an --out option, its contradiction checks name the expected pair, and it checks ROBOT report and the merged file. It runs 83 checks.
- Next release work is a worked example instance for each type page.

### Header and imports
- Imports RHEO 0.3.0 by its version IRI, and through it BFO 2020. The 32 RHEO terms that 0.1.0 copied with RHEO 0.2 wording are no longer declared here.
- Creators and term editors are ORCID IRIs. Version info is "0.2.0 (alpha)". Added `dcterms:issued`, `dcterms:modified`, `owl:priorVersion` and a citation.
- The preferred namespace prefix is `oheo` and the preferred namespace URI matches the term IRIs.
- The description states the concept and type policy of 15 October 2026 and the Caminao principle.

### Reused terms
- The 25 reused classes not declared by RHEO carry their source label and definition (EBI OLS, 16 October 2026), the source ontology as `IAO_0000412`, and one source-asserted parent. Parents that the sources do not assert were removed (odds ratio, relative risk, standardised mean difference, survival rate, median time-to-event, statistical model).
- Added the intermediate STATO and OGMS classes that the source chains need (absolute difference, average value, center value, pathological bodily process, bodily process).
- The survival rate definition is OBI's own text again.
- Thirteen DCMI, VANN, FOAF and oboInOwl terms lost the definitions 0.1.0 wrote for them.
- `dcterms:bibliographicCitation` on classes became `dcterms:source`, because DCMI defines the first as the citation of the resource itself.

### Hierarchy
- All 67 classes with more than one asserted parent now have one.
- Eight facet classes are defined classes (generic, condition-specific, health profile, preference-based, generic preference-based, condition-specific preference-based, wellbeing or capability, activities of daily living). Facts are stated with the new properties `has instrument classification` (OHEO_1000035) and `has published value set` (OHEO_1000034), and with `has outcome domain`.
- New class `instrument classification value` (OHEO_0000385) under OBI categorical value specification, with the values generic design (0000386), condition-specific design (0000387) and health profile scoring (0000388).
- Value set is under multi-attribute utility function only, no longer under scoring algorithm.
- Direct health state valuation, discrete choice experiment with duration, contingent valuation and standardised response mean keep the parent of their purpose and say the other in an editor note.
- 92 definitions reworded to open with their asserted parent.

### Disjointness
- Outcome domain, outcome measurement instrument, utility function, health-adjusted life year estimate, outcome specification and mapping function are pairwise disjoint.
- The 63 named instruments that do not contain one another are pairwise disjoint, and so are the named value sets and the named mapping functions.
- OHEO outcome measurement datum is disjoint from RHEO state observation, utility measurement record, QALY record and DALY record. Health-adjusted life year estimate is disjoint from RHEO utility estimate and disability weight estimate.

### Instruments, versions and value sets
- The definitions of outcome measurement instrument, value set and preference-based measure say how instrument, version and value set are identified separately.
- `obtained with instrument` (OHEO_1000013) is relabelled `obtained with instrument version`, with the old label kept as an alternative label.
- New properties `scored from observation` (1000032), `calculated from utility record` (1000033), `mapped with function` (1000038), `has valuation method` (1000031), `has health state profile code` (2000030), `has version label` (2000031), `has language tag` (2000032), `has dimension code` (2000033) and `has response level number` (2000034).
- The valuation method of each value set is an object restriction to the OHEO method class, replacing 22 text values of RHEO `has valuation method`.
- New annotation `names a published artefact` (OHEO_9000002) on 95 classes.
- `derived from instrument` is no longer a subproperty of RHEO `derived from`, which RHEO defines for estimates.

### Reference cases
- The ten reference case profile classes (0000375 to 0000384) are obsolete and replaced by named individuals (0000390 to 0000399).
- New profile for the NICE reference case as amended by PMG51 (27 August 2026), which supersedes the PMG36 profile and requires the UK EQ-5D-5L value set of Rowen et al. 2026.
- The 45 requirement classes (0000329 to 0000373) and the 19 properties they used are obsolete. Their rules are SHACL constraints in `oheo-reference-case-shapes.ttl` (10 shapes, 33 constraints).
- New properties `claims conformance to` (1000036) and `supersedes reference case profile` (1000037). `uses estimate` (1000030) and `has QALY weight` (2000025) are redefined for analyses.
- Bare "NICE 2022" and "NICE 2026" sources now name PMG36 and PMG51.

### Other obsolete classes
- `instrument family` (0000095), because a version of an instrument is not a family. Consider EQ-5D, Health Utilities Index and AQoL.
- `SF instrument family` (0000126), because its members are of different kinds.

### Synonyms
- Split into exact (220), related (79), broad (5) and narrow (8). 72 abbreviations carry the OMO abbreviation synonym type.
- The bare name of a summary measure is a related synonym of its estimate class.

### Mappings
- The 239 uses of the obsolete RHEO annotation "closest HEO concept" are removed from the ontology. Mappings are in `oheo-mappings.sssom.tsv` (295 rows in the first build, 303 after the fix pass), with no exact match.
- Two misleading links dropped (to adverse event reporting). 36 links on obsolete requirement classes dropped. Six archived HEO targets redirected to their replacements.
- All 54 NCIt codes checked in EBI OLS. 48 close matches stay in the ontology as `oboInOwl:hasDbXref`.

### New files
- `oheo-shapes.ttl`, `oheo-reference-case-shapes.ttl`, `oheo-mappings.sssom.tsv`, `types/`, `examples/`, `run_demo.py`, `catalog-v001.xml`, `imports/`, `src/`.

## 0.1.0 (8 October 2026, draft)

First draft for review by its creators. Not for operational use.
