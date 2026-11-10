# Health Economics Ontologies

Eight linked ontologies for health economics, published by [HealthEconomics.wiki](https://healtheconomics.wiki). HEO holds the concepts of the field, and each of the other seven covers one part of it, as the table below shows.

Each ontology has its own folder, with one subfolder per release. The ontology files in each release are the same as those deposited on Zenodo and uploaded to BioPortal.

| Ontology | What it covers | Release | DOI | BioPortal |
|---|---|---|---|---|
| [HEO](heo/2.0.0), Health Economics Ontology | The concepts of health economics, with definitions and typed links between them, taken from the wiki | 2.0.0 | [10.5281/zenodo.24057055](https://doi.org/10.5281/zenodo.24057055) | [HEO](https://bioportal.bioontology.org/ontologies/HEO) |
| [RHEO](rheo/0.4.0), Real Health Economics Ontology | The real things health economics works with, such as patients, resources, care processes and payments, and the records made about them | 0.4.0 (alpha) | [10.5281/zenodo.24057151](https://doi.org/10.5281/zenodo.24057151) | [RHEO](https://bioportal.bioontology.org/ontologies/RHEO) |
| [OHEO](oheo/0.3.0), Outcomes Health Economics Ontology | Health outcomes as they are specified, measured, valued and summarised | 0.3.0 (alpha) | [10.5281/zenodo.24057194](https://doi.org/10.5281/zenodo.24057194) | [OHEO](https://bioportal.bioontology.org/ontologies/OHEO) |
| [HETO](heto/0.3.0), Health Economics Task Ontology | Units of health economics work, such as adding discounting to a model, and the inputs and outputs of each | 0.3.0 (alpha) | [10.5281/zenodo.24057218](https://doi.org/10.5281/zenodo.24057218) | [HETO](https://bioportal.bioontology.org/ontologies/HETO) |
| [HEAO](heao/0.2.0), Health Economics Axiology Ontology | How quantities are turned into values, such as health into QALYs or resources into costs | 0.2.0 (alpha) | [10.5281/zenodo.24057282](https://doi.org/10.5281/zenodo.24057282) | [HEAO](https://bioportal.bioontology.org/ontologies/HEAO) |
| [HEMO](hemo/0.2.0), Health Economics Mathematics Ontology | The formulas, variables, assumptions and tests the other ontologies rely on | 0.2.0 (alpha) | [10.5281/zenodo.24057299](https://doi.org/10.5281/zenodo.24057299) | [HEMO](https://bioportal.bioontology.org/ontologies/HEMO) |
| [HELO](helo/0.2.0), Health Economics Learning Ontology | Learning pathways through the HEO concepts, ordered by level | 0.2.0 | [10.5281/zenodo.24057315](https://doi.org/10.5281/zenodo.24057315) | [HELO](https://bioportal.bioontology.org/ontologies/HELO) |
| [HEIRO](heiro/0.2.0), Health Economics Institutions and Rules Ontology | The institutions and rules of health economics and HTA, the bodies that issue them and when they apply | 0.2.0 (alpha) | [10.5281/zenodo.24057331](https://doi.org/10.5281/zenodo.24057331) | [HEIRO](https://bioportal.bioontology.org/ontologies/HEIRO) |

Each ontology is identified by its address on the wiki, for example `https://healtheconomics.wiki/ontologies/heo`, and each release by its version address. HEO concepts keep the wiki concept addresses, such as `https://healtheconomics.wiki/concept/cost`. The ontology pages are at [healtheconomics.wiki/ontologies](https://healtheconomics.wiki/ontologies).

## Documentation

The documentation pages list every term in each ontology with its definition and links, at https://intelligentparameters.github.io/healtheconomics-ontologies/

## What is in each release folder

- The ontology in OWL and Turtle. For the seven formal ontologies, a merged OWL file holds the ontology with the parts of other ontologies it uses, so it opens on its own.
- SHACL shapes, the rules that data written with the ontology must meet.
- SSSOM mapping files, where the release has them.
- A README describing the files, a CHANGELOG, a CITATION file and the licence.

## Using the files

Open a merged OWL file in [Protégé](https://protege.stanford.edu) or any OWL tool. In Python the Turtle files load with rdflib.

```python
from rdflib import Graph
g = Graph().parse("rheo/0.4.0/rheo.ttl", format="turtle")
print(len(g))
```

Data can be checked against the SHACL files with a tool such as pySHACL.

## Authors and licence

Written by Darrin Baines ([ORCID](https://orcid.org/0000-0001-9502-4678)) and Michelle Ashley ([ORCID](https://orcid.org/0009-0006-0231-3731)) for HealthEconomics.wiki and published by Intelligent Parameters Ltd.

The ontologies are released under the [Creative Commons Attribution 4.0 International licence](LICENSE). Please cite the release you used, with its DOI. Each release folder has a CITATION file.

## Note on this copy

The ontology files are byte for byte the same as the Zenodo deposits. In the seven formal ontologies, the version named in the README heading and in the CITATION file has been corrected here to the release version. The Zenodo copies still show the previous version number in those two places, and will be corrected in the next release.
