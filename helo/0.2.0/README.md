# Health Economics Learning Ontology (HELO), version 0.2.0

The Health Economics Learning Ontology (HELO) describes the learning pathways of HealthEconomics.wiki, which are ordered steps that build understanding of health economics concepts from foundational to advanced. It records pathway frameworks, intended learners, learning goals and proposed prerequisite relationships between concepts, and gives courses a shared structure of curricula and modules. Learning pathways build understanding and prepare learners for the work described in the Health Economics Task Ontology (HETO). This HELO is the Health Economics Learning Ontology of HealthEconomics.wiki. It is not the HypothEsis and Law Ontology, also called HELO, and is unrelated to it.

## Who made it

Darrin Baines (ORCID https://orcid.org/0000-0001-9502-4678) and Michelle Ashley (ORCID https://orcid.org/0009-0006-0231-3731), for HealthEconomics.wiki (https://healtheconomics.wiki). Publisher Intelligent Parameters Ltd.

## Files in this package

- `helo-0.2.0-merged.owl`. The merged OWL file that was loaded to BioPortal. It holds the core, the pathway and course records, the Basic Formal Ontology and the IAO terms used.
- `helo.ttl`. The core ontology in Turtle.
- `helo-pathways.ttl`. The learning pathways, their steps and frameworks and the semantic layer course, in Turtle.
- `helo-shapes.ttl`. The SHACL record rules.
- `helo-mappings.sssom.tsv`. The SSSOM file with the relationships to the other ontologies and the mappings to the Curriculum KG Ontology and schema.org.
- `CHANGELOG.md`. What changed in this version, copied from the release folder.
- `CITATION.cff`. How to cite this record.
- `LICENSE.txt`. The full text of the Creative Commons Attribution 4.0 International licence.
- `README.md`. This file.

## How to open the files

The merged OWL file holds the ontology together with the parts of the other ontologies it uses, so it opens on its own in Protege or any other OWL tool. It is the file that was loaded to BioPortal. The Turtle files hold the same content as separate modules that are easier to read and edit. They import their companion ontologies by web address, and those addresses are not all served yet, so open the merged OWL file if your tool cannot fetch them.

The SHACL (Shapes Constraint Language) files hold the record rules. They check that data written with the ontology is complete and consistent, and can be run with a SHACL tool such as pySHACL.

The SSSOM (Simple Standard for Sharing Ontological Mappings) file lists the mappings to other ontologies, one row per mapping, with the type of relationship, the reason for it and its review status. It is a tab-separated table that opens in a spreadsheet.

## Status

This is an alpha release for review by its creators and invited reviewers. Terms, definitions and mappings may still change before version 1.0.

## Where else to find it

The same release is on BioPortal at https://bioportal.bioontology.org/ontologies/HELO and is documented on HealthEconomics.wiki at https://healtheconomics.wiki.

## How to cite

Please cite the Zenodo record of this version. Its DOI is shown on the record page, and CITATION.cff holds the other citation details.

## Licence

The files are published under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). Anyone may share and adapt them for any purpose, as long as they give credit. The full text is in LICENSE.txt.
