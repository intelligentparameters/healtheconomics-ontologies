# HEO 2.0.1 (22 November 2026)

Patch release. It adds 22 concepts that were published on HealthEconomics.wiki between 14 and 21 November 2026, after HEO 2.0.0, and that the RHEO 0.5.1 mappings to HEO point to (28 mapping rows). Nothing that was in 2.0.0 has been changed or removed, apart from the ontology header.

| Item | HEO 2.0.0 | HEO 2.0.1 |
|---|---|---|
| Version identifier | https://healtheconomics.wiki/ontologies/heo/2.0.0 | https://healtheconomics.wiki/ontologies/heo/2.0.1 |
| Prior version | https://healtheconomics.wiki/ontology/heo/1.3.1 | https://healtheconomics.wiki/ontologies/heo/2.0.0 |
| Concepts in use | 4,009 | 4,031 |
| Obsolete concepts | 1,192 | 1,192 |
| Expert verified concepts | 1,280 | 1,302 |
| Concept-to-concept relationships | 17,671 | 17,780 |
| Annotated relationship records | 12,544 | 12,631 |

## Added

- 22 concepts, each with its live wiki name, short definition, term code, the source named on its page, page version, review status (all 22 are expert verified on the wiki) and verification date.
- 70 live wiki links that join the new concepts to each other or to concepts already in HEO. 55 start at a new concept (7 of them join two new concepts) and 15 start at a concept already in HEO, for example Screening precedes Diagnostic Testing and Carer performs Informal Care. Five of them are is-type-of links (heo:isTypeOf, also stated as skos:broader).
- 17 placement links (heo:classifiedUnder, also stated as skos:broader) for the new concepts that have no is-type-of parent in HEO. None of the 22 is listed on a wiki topic page yet, so each is placed by its catalogue Level 1, 2 and 3 through the mapping table used since 1.2.0, under the concept its Level 3 names where that concept sits in the same subdomain.
- 87 link records, one for each new link, with a permanent ID made from the two concepts and the link type, in the same way as before. All are marked unreviewed. The placement records give the basis of each placement.
- Insurance Enrolment carries its two wiki aliases, Insurance Enrollment and Plan Enrolment, as search terms (skos:hiddenLabel), the rule for aliases not yet typed.

| Concept | Source on the wiki page | Sits under |
|---|---|---|
| Carbon Footprint (`carbon-footprint`) | Wiedmann & Minx 2007; Tennison et al. 2021 | Costs (placed, classified under) |
| Care Home (`care-home`) | Care Standards Act 2000 | Health Systems (placed, classified under) |
| Care Home Stay (`care-home-stay`) | Ciminata et al. 2020 | Long Term Care (is type of) |
| Classification Revision (`classification-revision`) | Harrison et al. 2021 | Health Systems (placed, classified under) |
| Classification System (`classification-system`) | Harrison et al. 2021 | Data Standard (is type of) |
| Clinical Event (`clinical-event`) | Schlaich et al. 2026 | Clinical Outcome (is type of) |
| Correction Notice (`correction-notice`) | Wager et al. 2009; ICMJE 2026; Lefebvre et al. 2025 | Evidence Source (placed, classified under) |
| Cost Aggregation (`cost-aggregation`) | Faria et al. 2014 | Costs (placed, classified under) |
| Diagnostic Testing (`diagnostic-testing`) | Ferrante di Ruffano et al. 2012 | Health Technology Assessment (placed, classified under) |
| Emission Factor (`emission-factor`) | Misrai et al. 2021 | Parameter Input (is type of) |
| Episode of Care (`episode-of-care`) | Bozic et al. 2014 | Costs (placed, classified under) |
| Estimand (`estimand`) | ICH E9(R1) 2019 | Evidence Synthesis (placed, classified under) |
| GDP per Capita (`gdp-per-capita`) | World Bank 2026 | Cost-Effectiveness Analysis (placed, classified under) |
| Health State Transition (`health-state-transition`) | Siebert et al. 2012 | Markov Model (placed, classified under) |
| Household Consumption Expenditure (`household-consumption-expenditure`) | ILO 2023 | Health System Financing (placed, classified under) |
| Informal Care (`informal-care`) | van den Berg et al. 2004 | Costs (placed, classified under) |
| Innovation, Novation and Replacement (`innovation-novation-and-replacement`) | Baines 2008 | Classification System (is type of) |
| Insurance Enrolment (`insurance-enrolment`) | Jensen et al. 2015 | Health Insurance (placed, classified under) |
| Model Run (`model-run`) | Karnon et al. 2012 | Economic Modelling (placed, classified under) |
| Model Version (`model-version`) | Kent et al. 2019 | Model Validation (placed, classified under) |
| Patient Transport (`patient-transport`) | Hains et al. 2011 | Health Systems (placed, classified under) |
| Retraction Notice (`retraction-notice`) | Wager et al. 2009 | Evidence Assessment (placed, classified under) |

## Left out

Eight live links of the new concepts were left out because the concept at the other end is a published wiki page that is not in HEO yet. They are Care Home is type of Care Setting, Classification System is type of Knowledge Organisation System, Classification System contrasts with Ontology, Cost Aggregation part of Costing, Informal Care contrasts with Paid Work, Consultation part of Episode of Care, and Model State and Domain Event each contrast with Clinical Event. Care Home is therefore placed under Health Systems until Care Setting is in HEO.

Other concepts published on the wiki since 2.0.0, such as the ontology foundation pages and the OHDSI pages of 21 and 22 November 2026, are not in this patch. They wait for the next full rebuild.

## Changed

- The ontology header names version 2.0.1, prior version 2.0.0 and modification date 2026-11-22, and has two new comments, the 2.0.1 note and the release counts.
- The 2.0.0 note in the header now carries its English language tag in the Turtle file too. heo-2.0.0.owl, the file on BioPortal, already had it, and heo-2.0.0.ttl had lost it.

## How it was built

HEO 2.0.0 was made from 1.3.1 by moving the addresses, and 1.3.1 from 1.3.0, the last release built from the wiki data. That build depends on a signed-in admin export of 17 October 2026 and could not be rerun for a patch, so 2.0.1 starts from the published heo-2.0.0.ttl and adds the new concepts with the same rules the 1.3.0 build applies. The live records were read from the wiki's public concept data on 22 November 2026. The OWL file was written from the Turtle by ROBOT 1.9.11, the writer used for 1.3.1 and 2.0.0. The same step applied to heo-2.0.0.ttl gives the published heo-2.0.0.owl, apart from the language tag noted above.

## Checks

- OWL 2 DL profile (ROBOT 1.9.11 validate-profile) passes. ELK and HermiT (ROBOT reason) both finish with exit 0, so the ontology is consistent.
- OWL 2 RL closure (owlrl) has nothing in owl:Nothing and no rule violations. SHACL (heo-shapes-2.0.ttl, pySHACL) conforms with 0 violations.
- SKOS integrity passes. Health Economics is the only top concept, there are no broader cycles, each concept has one preferred label per language and no two concepts in use share one. All 4,031 concepts in use reach Health Economics and there are no orphans. Maximum depth is still 8.
- Every heo:isTypeOf and heo:classifiedUnder link is also skos:broader, no concept has both, and there are no precedes cycles.
- Never-drop check against 2.0.0. Every 2.0.0 triple and every one of its 12,544 link records is in 2.0.1 unchanged, apart from the version, prior version, version number and date in the header. The only triples added to concepts already in 2.0.0 are links to the new concepts (14 concepts).
- All 12,631 link IDs are unique. Every concept in use has a definition, and every new concept has the source named on its wiki page (none is wiki editorial text or Wikipedia).
- The Turtle and OWL files hold the same content. The OWL file adds the owl:NamedIndividual declarations the OWL API writes (5,829).
- No date after 2026-11-22 appears in the file.

## Files

- heo-2.0.1.owl, the file to upload to BioPortal
- heo-2.0.1.ttl, the same content in Turtle
- heo-shapes-2.0.ttl, the SHACL shapes, unchanged from 2.0.0

# HEO 2.0.0 (8 November 2026)

Address release. No concept, definition, label or relationship has changed since 1.3.1.

| Item | HEO 1.3.1 | HEO 2.0.0 |
|---|---|---|
| Ontology identifier | https://healtheconomics.wiki/ontology/heo | https://healtheconomics.wiki/ontologies/heo |
| Version identifier | https://healtheconomics.wiki/ontology/heo/1.3.1 | https://healtheconomics.wiki/ontologies/heo/2.0.0 |
| HEO's own terms (prefix heo:) | https://healtheconomics.wiki/ontology/heo# | https://healtheconomics.wiki/ontologies/heo# |
| Concept addresses | https://healtheconomics.wiki/concept/<slug> | unchanged |
| Concepts, relationships, annotated relationship records | 4,009 active, 1,192 obsolete, 17,671, 12,544 | the same |

## Why

The ontology pages on the site moved to https://healtheconomics.wiki/ontologies/<name>. The identifiers now match the pages, so following an identifier opens its page. The old /ontology/ addresses are retired and are not redirected. The prior version identifier, https://healtheconomics.wiki/ontology/heo/1.3.1, is kept as published.

## Checks

The 2.0.0 files were compared with 1.3.1 triple by triple after mapping the old addresses to the new ones. Only the ontology header differs (version, date, the address note and the prior version). The Turtle and OWL files both parse. The shapes file is heo-shapes-2.0.ttl, with the same shapes under the new prefixes.

## Files

- heo-2.0.0.owl, the file to upload to BioPortal
- heo-2.0.0.ttl, the same content in Turtle
- heo-shapes-2.0.ttl, the SHACL shapes

# HEO 1.3.1 (18 October 2026)

Layout-only release. No concept, definition, label or relationship has changed since 1.3.0.

| Item | HEO 1.3.0 | HEO 1.3.1 |
|---|---|---|
| Concepts (active) | 4,009 | 4,009 |
| Concepts (obsolete) | 1,192 | 1,192 |
| Concept-to-concept relationships | 17,671 | 17,671 |
| Annotated relationship records | 12,544 | 12,544 |
| Ontology header | present, written inside another record | at the top of the file |
| Property declarations | present, written inside other records | at the top level (21 object properties, 55 annotation properties) |
| File writer | rdflib (nested RDF/XML) | ROBOT 1.9.11 with the OWL API (standard flat RDF/XML) |

## What changed in the file

1. The OWL file is now written in the standard flat layout, so every checker finds the ontology header, the property declarations and each concept at the top level.
2. Each concept carries an explicit owl:NamedIndividual declaration, added by the OWL API (5,804 declarations). This adds no new meaning.
3. Six inverse property pairs are written from the other side (for example hasPart inverseOf partOf instead of partOf inverseOf hasPart). The meaning is the same.
4. The ontology record now says 1.3.1, points to 1.3.0 as its prior version and carries a short note that only the layout changed.

## Check against the BioPortal CSV export of 1.3.0

The BioPortal CSV export (HEO.csv.gz) was compared with the 1.3.0 OWL file. Every one of the CSV's 17,292 concept-to-concept relationships is in the OWL file, with identical counts for every relationship type. The OWL file also holds 379 rdfs:seeAlso links that the CSV export leaves out. The two files agree.

## Files

- heo-1.3.1.owl, the file to upload to BioPortal
- heo-1.3.1.ttl, the same content in Turtle


# HEO 1.3.0 changelog (17 Oct 2026)

Version IRI https://healtheconomics.wiki/ontology/heo/1.3.0, prior version 1.2.0, modified 2026-10-17. Built by articles/plans/build_heo13.py.

## Added
- 70 new concepts uploaded to the wiki on 17 Oct 2026 (outcome instruments, value sets and methods). 64 sit under their own is-type-of parent. The other 6 are placed by their live wiki topic with heo:classifiedUnder.
- 12 new site links, among them Discrete Choice Experiment uses Multinomial Logit Model, and Ordinal Scaling, Interval Scaling, Nominal Scale and Ratio Scale are each a type of Measurement Scale Type. These were read from the live site, because the 17 Oct export did not yet carry them.

## Changed
- The aliases Dimensional Validity and Internal Structure Validity moved from Structural Validity to Structural Validity (Measurement Instrument), as on the live site.
- Ordinal Scaling and Interval Scaling now sit under Measurement Scale Type by is-type-of links. Their 1.2.0 placement links are superseded, and the IDs are kept in the link records.
- The 6 fixed definitions (Construct Validity, Distress, Depression Symptoms, Anxiety Symptoms, Equal Value of Life Year Gained, Assistive Technology Coverage) were already in 1.2.0, so they are unchanged.

## Unchanged
- Health Economics is the single root, with nine subdomains directly under it.
- All other 1.2.0 placements are unchanged. No 1.2.0 concept IRI or link ID is dropped.

## Counts
- 4,009 concepts in use and 1,192 deprecated.
- 10,836 site links and 1,708 placement links (12,544 link records).
- Level 1 has 9 concepts and 0 are orphans. Maximum depth is 8 (level 2 has 1,007, level 3 has 1,616, level 4 has 846, level 5 has 413, level 6 has 94, level 7 has 19 and level 8 has 4).

## Checks
- OWL 2 DL profile, ELK and HermiT pass. owlrl has nothing in owl:Nothing and no rule violations. SHACL conforms with 0 violations.
- SKOS integrity passes and there are no broader cycles.
- The never-drop check against 1.2.0 passes.
- RDF/XML and Turtle round-trip to the same 190,860 triples.
- No date after 2026-10-17 appears in the file.


# HEO 1.2.0 changelog (16 Oct 2026)

Version IRI https://healtheconomics.wiki/ontology/heo/1.2.0, prior version 1.1.0, modified 2026-10-16. Built by articles/plans/build_heo12.py from the export catalog-2026-10-16-night, taken after the two 16 Oct uploads. Responds to Darrin Baines's structural check of HEO 1.1.0, and to two independent reviews (fix pass, same day).

## Hierarchy
- One top concept. Health Economics is the only skos:hasTopConcept / skos:topConceptOf (1.1.0 had 1,677 top concepts).
- Nine concepts sit directly under Health Economics. These are the wiki's eight subdomains (Costs, Outcomes, Economic Evaluation, Health Technology Assessment, Economic Modelling, Evidence Synthesis, Health Systems, Health Policy) plus Economic Foundations, the ninth subdomain Darrin agreed on 16 Oct 2026.
- Five new wiki concepts were uploaded on 16 Oct 2026 and are live: Costs, Outcomes, Economic Modelling, Health Systems and Economic Foundations, each partOf Health Economics. Cost, Health Outcome, Health Economic Model and Health System are now filed under their subdomain concept.
- The 23 disease-area economics concepts (Cardiovascular Economics and others) are part of Health Economics, not a type of it. The site link changed from isTypeOf to partOf (upload 2, live). In HEO they are classified under Economic Evaluation (wiki topic Disease-area economics), except Global Health Economics (Health Systems), and One Health Economics and Prevention Economics (Health Policy).
- New object property heo:classifiedUnder, a sub-property of skos:broader. It places a concept with no is-type-of parent in the wiki's subject structure and is not a type-of claim. There are 1,704 placement links. Each is also stated as skos:broader, so SKOS tools that do not reason show one tree.
- New object property heo:isTypeOf, a sub-property of skos:broader, on the 2,551 wiki "is type of" links (each also stated as skos:broader). Type-of links can now be queried directly.
- Placement sources, in order. 143 curated placements from the two reviews, then the live wiki topic pages, then the catalogue Level 1/2/3 fields through the mapping table in subdomain-mapping.csv. 723 concepts sit below a concept inside their subdomain.
- Result. 1 root, 0 orphans, all 3,939 live concepts reach Health Economics, maximum depth 8. No skos:broader cycles.
- Wiki topics are not a separate level. Three topic misfilings found by the reviews are listed in wiki-topic-fixes.md for the site.

## Deprecated concepts
- Every deprecated concept now has a successor (dcterms:isReplacedBy) or a skos:editorialNote giving the reason for retirement.
- 13 successors were added from merge notes. 4 of them are the nearest broader concept, and their notes say so. 828 retirement notes were taken from the archive Review notes, with internal jargon removed. The 3 concepts with no archive note point to the published concept that covers the idea.
- Grid terms whose note names a redirect carry rdfs:seeAlso to that concept.

## Removed
- heo:evidenceLevel and its 1,201 values. It was "high" on every concept that had it. The grade stays on the wiki.

## Link records
- heo:linkReviewDate is corrected on every link record. Records stamped 2026-10-16 now carry 2026-10-14 or 2026-10-15, and those stamped 2026-10-17 carry 2026-10-15, the dates of the review files the decisions came from. 57 records use 2026-10-15, the 1.1.0 build date. Full list in date-fixes.csv.
- 70 link reasons that said "graph connectivity review (17 Oct 2026)" now say 15 Oct 2026.
- The 23 replaced type-of links keep their IDs, with status superseded. Each new part-of link names the ID it replaces (dcterms:replaces).
- New link records for the placement links (status unreviewed, with the placement basis and a creation date).
- No 1.1.0 concept IRI or link ID was dropped.

## Description and labelling
- The description now says concepts sit under one top concept and the wiki's subdomains, with heo:classifiedUnder for placement.
- The scheme note now says skos:broader is the navigation tree. It holds is-type-of links (heo:isTypeOf) and placement links (heo:classifiedUnder).
- A new comment gives the release counts. 1,280 concepts with a full article are expert verified and 2,659 dictionary entries are not yet expert verified. Inclusion in HEO does not mean a concept has been verified.

## Checks
- OWL 2 DL profile (ROBOT), ELK and HermiT pass. The owlrl closure has nothing in owl:Nothing and no rule violations. SHACL (heo-shapes-1.0.ttl) conforms with 0 violations. RDF/XML and Turtle round-trip to the same 187,539 triples.
- SKOS integrity passes. No top concept has a broader concept, there are no broader cycles, and each concept has one prefLabel per language.
- No date after 2026-10-16 appears anywhere in the file.
