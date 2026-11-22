# Health Economics Ontology (HEO), version 2.0.1

The Health Economics Ontology (HEO) is a vocabulary of health economics concepts taken from HealthEconomics.wiki, each with a permanent web address, a name and a definition. It is written in the Simple Knowledge Organization System (SKOS) and the Web Ontology Language (OWL), with typed relationships between concepts such as part of, measures and used to calculate. Concepts sit under one top concept, Health Economics, and the subdomains of the wiki. HEO describes meanings, not real things, and its companion the Real Health Economics Ontology (RHEO) describes the real world.

## About version 2.0.1

Version 2.0.1 is a small patch on top of 2.0.0. It adds 22 concepts that were published on the wiki between 14 and 21 November 2026, after 2.0.0, and that the RHEO 0.5.1 mappings to HEO point to, such as Care Home, Estimand, Informal Care and Model Run. It also adds the live wiki links that join these concepts to each other and to concepts already in HEO, and places the new concepts that have no is-type-of parent in the wiki's subject structure. Nothing that was in 2.0.0 is changed or removed. The CHANGELOG lists the concepts and the checks.

Other pages published on the wiki since 2.0.0 are not in this patch. They will come with the next full rebuild of HEO from the wiki.

## Who made it

Darrin Baines (ORCID https://orcid.org/0000-0001-9502-4678) and Michelle Ashley (ORCID https://orcid.org/0009-0006-0231-3731), for HealthEconomics.wiki (https://healtheconomics.wiki). Publisher Intelligent Parameters Ltd.

## Files in this package

- `heo-2.0.1.owl`. The OWL file to load to BioPortal.
- `heo-2.0.1.ttl`. The same content in Turtle.
- `heo-shapes-2.0.ttl`. The SHACL record rules that the release was checked against, the same file as in 2.0.0.
- `CHANGELOG.md`. What changed in this version, with the earlier entries below it.
- `CITATION.cff`. How to cite this record.
- `LICENSE.txt`. The full text of the Creative Commons Attribution 4.0 International licence.
- `README.md`. This file.

## How to open the files

The OWL file and the Turtle file hold the same content, and both open on their own in Protege or any other OWL or SKOS tool. HEO does not import other ontologies.

The SHACL (Shapes Constraint Language) file holds the record rules. It checks that data written with the ontology is complete and consistent, and can be run with a SHACL tool such as pySHACL.

HEO has no mapping file of its own. The mappings from the other ontologies of HealthEconomics.wiki to HEO concepts are published with those ontologies, for example in the RHEO package.

## Status

This is a stable release. Each concept records its own review status, and inclusion in HEO does not mean that a concept has been expert verified. The 22 new concepts are expert verified on the wiki. Their new links have not yet been reviewed on their own, and each link record says so.

## Where else to find it

HEO is on BioPortal at https://bioportal.bioontology.org/ontologies/HEO and is documented on HealthEconomics.wiki at https://healtheconomics.wiki.

## How to cite

Please cite the Zenodo record of this version. Its DOI is shown on the record page, and CITATION.cff holds the other citation details.

## Licence

The files are published under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). Anyone may share and adapt them for any purpose, as long as they give credit. The full text is in LICENSE.txt.
