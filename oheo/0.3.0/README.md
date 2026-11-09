# Outcomes Health Economics Ontology (OHEO), version 0.3.0

The Outcomes Health Economics Ontology (OHEO) describes health outcomes as they are specified, measured, valued and summarised in health economics and health technology assessment (HTA). It keeps apart what is measured, the instruments used to measure it, the value sets that turn answers into utility values and summary measures such as the quality-adjusted life year (QALY). The reference cases of the National Institute for Health and Care Excellence (NICE) and other HTA bodies are included as rules that records can be checked against. OHEO builds on the Real Health Economics Ontology (RHEO) and the Basic Formal Ontology (BFO). This is an alpha release for review.

## Who made it

Darrin Baines (ORCID https://orcid.org/0000-0001-9502-4678) and Michelle Ashley (ORCID https://orcid.org/0009-0006-0231-3731), for HealthEconomics.wiki (https://healtheconomics.wiki). Publisher Intelligent Parameters Ltd.

## Files in this package

- `oheo-0.3.0-merged.owl`. The merged OWL file that was loaded to BioPortal. It holds OHEO with RHEO 0.4.0 and the Basic Formal Ontology.
- `oheo.ttl`. The ontology in Turtle.
- `oheo-shapes.ttl`. The SHACL record rules for instrument versions, value sets, responses, utilities and QALY records.
- `oheo-reference-case-shapes.ttl`. The SHACL reference case rules, one set for each reference case profile.
- `oheo-mappings.sssom.tsv`. The SSSOM mappings to HEO concepts, RHEO types and other vocabularies.
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

The same release is on BioPortal at https://bioportal.bioontology.org/ontologies/OHEO and is documented on HealthEconomics.wiki at https://healtheconomics.wiki.

## How to cite

Please cite the Zenodo record of this version. Its DOI is shown on the record page, and CITATION.cff holds the other citation details.

## Licence

The files are published under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). Anyone may share and adapt them for any purpose, as long as they give credit. The full text is in LICENSE.txt.
