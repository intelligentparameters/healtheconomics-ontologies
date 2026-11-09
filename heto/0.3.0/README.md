# Health Economics Task Ontology (HETO), version 0.3.0

The Health Economics Task Ontology (HETO) describes recognisable units of health economics work, such as adding discounting to an economic model or running a probabilistic sensitivity analysis. Each task states its intended result, its main actions, the role of the person who does it and the real things it uses and produces, as the Real Health Economics Ontology (RHEO) and the Outcomes Health Economics Ontology (OHEO) define them. Larger tasks are broken into smaller ones, and the usual order of work is recorded apart from that breakdown. Task specifications follow the Information Artifact Ontology (IAO). This pilot release is an alpha version for review before the task list grows.

## Who made it

Darrin Baines (ORCID https://orcid.org/0000-0001-9502-4678) and Michelle Ashley (ORCID https://orcid.org/0009-0006-0231-3731), for HealthEconomics.wiki (https://healtheconomics.wiki). Publisher Intelligent Parameters Ltd.

## Files in this package

- `heto-0.3.0-merged.owl`. The merged OWL file that was loaded to BioPortal. It holds HETO with RHEO 0.4.0, OHEO 0.3.0 and the Basic Formal Ontology.
- `heto.ttl`. The ontology and the pilot task catalogue in Turtle.
- `heto-shapes.ttl`. The SHACL record rules for the catalogue and for records of tasks carried out.
- `heto-mappings.sssom.tsv`. The SSSOM file with the task relationships to RHEO, OHEO and IAO types, and the related HEO concepts for learning and navigation.
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

The same release is on BioPortal at https://bioportal.bioontology.org/ontologies/HETO and is documented on HealthEconomics.wiki at https://healtheconomics.wiki.

## How to cite

Please cite the Zenodo record of this version. Its DOI is shown on the record page, and CITATION.cff holds the other citation details.

## Licence

The files are published under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). Anyone may share and adapt them for any purpose, as long as they give credit. The full text is in LICENSE.txt.
