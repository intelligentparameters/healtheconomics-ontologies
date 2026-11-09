# Real Health Economics Ontology (RHEO), version 0.4.0

The Real Health Economics Ontology (RHEO) describes the real things that health economics works with, such as patients, households, care settings, resources, payments and costs, and the records made about them. It also describes the evidence built from these records, from estimates and assumptions to model parameters and results, so that a model result can be traced back to its sources. RHEO is written in the Web Ontology Language (OWL) and is aligned to the Basic Formal Ontology (BFO) 2020. Its relationships to the concepts of the Health Economics Ontology (HEO) are published as a separate mapping file. This is an alpha release for review, and terms may still change before version 1.0.

## Who made it

Darrin Baines (ORCID https://orcid.org/0000-0001-9502-4678) and Michelle Ashley (ORCID https://orcid.org/0009-0006-0231-3731), for HealthEconomics.wiki (https://healtheconomics.wiki). Publisher Intelligent Parameters Ltd.

## Files in this package

- `rheo-0.4.0-merged.owl`. The merged OWL file that was loaded to BioPortal. It holds the core, both modules and the Basic Formal Ontology terms used.
- `rheo.ttl`. The core ontology in Turtle.
- `rheo-rni.ttl`. The module for replacement, novation and innovation (RNI) changes of state, in Turtle.
- `rheo-uncertainty.ttl`. The optional module for uncertain quantities and the dependence between them, in Turtle.
- `rheo-shapes.ttl`. The SHACL record rules of the core.
- `rheo-rni-shapes.ttl`. The SHACL record rules of the RNI module.
- `rheo-uncertainty-shapes.ttl`. The SHACL record rules of the uncertainty module.
- `rheo-heo.sssom.tsv`. The SSSOM mappings from RHEO terms to HEO concepts.
- `rheo-obo.sssom.tsv`. The SSSOM mappings from obsolete RHEO terms to the terms of other ontologies that replace them.
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

The same release is on BioPortal at https://bioportal.bioontology.org/ontologies/RHEO and is documented on HealthEconomics.wiki at https://healtheconomics.wiki.

## How to cite

Please cite the Zenodo record of this version. Its DOI is shown on the record page, and CITATION.cff holds the other citation details.

## Licence

The files are published under the Creative Commons Attribution 4.0 International licence (CC BY 4.0). Anyone may share and adapt them for any purpose, as long as they give credit. The full text is in LICENSE.txt.
