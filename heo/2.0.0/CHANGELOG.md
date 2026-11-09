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
