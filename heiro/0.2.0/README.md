# Health Economics Institutions and Rules Ontology (HEIRO), version 0.2.0

The Health Economics Institutions and Rules Ontology (HEIRO) describes the institutions of health economics and health technology assessment (HTA), meaning the rules that shape the options open to decision makers, and keeps them apart from the organisations that issue and apply them. Each rule names its provision, the dated version of the guidance that states it, the body that issued it and the period when it is in force. Guidance versions are never edited, and dated check records show what a source page said on the day it was read. This lets any page, formula or rule that cites an older guidance version be flagged when a newer one appears. This is an alpha release for review.

## Who made it

Darrin Baines (ORCID https://orcid.org/0000-0001-9502-4678) and Michelle Ashley (ORCID https://orcid.org/0009-0006-0231-3731), for HealthEconomics.wiki (https://healtheconomics.wiki). Publisher Intelligent Parameters Ltd.

## Files in this package

- `heiro-0.2.0-merged.owl`. The merged OWL file that was loaded to BioPortal. It holds the core and the register with the outside terms used.
- `heiro.ttl`. The core ontology in Turtle.
- `heiro-register.ttl`. The register of bodies, guidance documents, versions, provisions, rules and check records, in Turtle.
- `heiro-wiki.ttl`. The records generated from HealthEconomics.wiki, in Turtle. These are not in the merged file.
- `heiro-shapes.ttl`. The SHACL record rules.
- `heiro-mappings.sssom.tsv`. The SSSOM file with the relationships to the other ontologies and the mappings to HEO, RHEO and standard vocabularies.
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

The same release is on BioPortal at https://bioportal.bioontology.org/ontologies/HEIRO and is documented on HealthEconomics.wiki at https://healtheconomics.wiki.

## How to cite

Please cite the Zenodo record of this version. Its DOI is shown on the record page, and CITATION.cff holds the other citation details.

## Licence

The files are published under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). Anyone may share and adapt them for any purpose, as long as they give credit. The full text is in LICENSE.txt.
