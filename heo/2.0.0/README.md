# Health Economics Ontology (HEO), version 2.0.0

The Health Economics Ontology (HEO) is a vocabulary of health economics concepts taken from HealthEconomics.wiki, each with a permanent web address, a name and a definition. It is written in the Simple Knowledge Organization System (SKOS) and the Web Ontology Language (OWL), with typed relationships between concepts such as part of, measures and used to calculate. Concepts sit under one top concept, Health Economics, and the subdomains of the wiki. HEO describes meanings, not real things, and its companion the Real Health Economics Ontology (RHEO) describes the real world. Version 2.0.0 changes only the file layout of version 1.3.0.

## Who made it

Darrin Baines (ORCID https://orcid.org/0000-0001-9502-4678) and Michelle Ashley (ORCID https://orcid.org/0009-0006-0231-3731), for HealthEconomics.wiki (https://healtheconomics.wiki). Publisher Intelligent Parameters Ltd.

## Files in this package

- `heo-2.0.0.owl`. The OWL file that was loaded to BioPortal.
- `heo-2.0.0.ttl`. The same content in Turtle.
- `heo-shapes-2.0.ttl`. The SHACL record rules that the release was checked against.
- `CHANGELOG.md`. What changed in this version, copied from the release folder.
- `CITATION.cff`. How to cite this record.
- `LICENSE.txt`. The full text of the Creative Commons Attribution 4.0 International licence.
- `README.md`. This file.

## How to open the files

The OWL file and the Turtle file hold the same content, and both open on their own in Protege or any other OWL or SKOS tool. HEO does not import other ontologies.

The SHACL (Shapes Constraint Language) files hold the record rules. They check that data written with the ontology is complete and consistent, and can be run with a SHACL tool such as pySHACL.

HEO has no mapping file of its own. The mappings from the other ontologies of HealthEconomics.wiki to HEO concepts are published with those ontologies, for example in the RHEO package.

## Status

This is a stable release. Each concept records its own review status, and inclusion in HEO does not mean that a concept has been expert verified.

## Where else to find it

The same release is on BioPortal at https://bioportal.bioontology.org/ontologies/HEO and is documented on HealthEconomics.wiki at https://healtheconomics.wiki.

## How to cite

Please cite the Zenodo record of this version. Its DOI is shown on the record page, and CITATION.cff holds the other citation details.

## Licence

The files are published under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). Anyone may share and adapt them for any purpose, as long as they give credit. The full text is in LICENSE.txt.
