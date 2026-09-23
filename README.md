# Bodemverdichting kosten

Wetenschappelijk raamwerk en software-/data-infrastructuur voor het project **De kosten van bodemverdichting voor landbouw en maatschappij**.

## Start hier

Ben je nieuw in het project, begin dan met [`docs/57_colleague_review_package_v0_2.md`](docs/57_colleague_review_package_v0_2.md). Dat document legt in gewone taal uit wat het project wil weten, waarom we zo weinig mogelijk onnodig rekenen, hoe on-site en off-site effecten naast elkaar staan en waar onzekerheid of ontbrekende informatie de berekening begrenst.

Gebruik daarna [`docs/58_project_architecture_status_v0_1.md`](docs/58_project_architecture_status_v0_1.md) als actuele architectuur- en readinesspagina. Die pagina verwijst naar de canonieke theorie, modellen, schema's, evidence, code, tests en artifactcontracten zonder die inhoud te dupliceren.

De volledige documentatiekaart staat in [`docs/README.md`](docs/README.md). [`docs/00_colleague_reader_guide.md`](docs/00_colleague_reader_guide.md) blijft de verdiepende uitleg van current/reference, evidence en de Tollebeek-pilot.

Wil je bijdragen aan het project, lees dan [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Doel

Deze repository is de canonieke plek voor de relatie tussen:

**theorie → conceptueel model → formeel model → datamodel → implementatie → evidence/kwalificatie → artifact/applicatie**.

De Excel-workbooks, dashboards en latere applicatie zijn gebruikersgerichte artifacts. Zij horen het canonieke model te volgen, niet andersom.

## Huidige status

De repository bevindt zich in een **Status-A-light opbouwfase**. Het doel is nog niet om een volledig Status A-dossier te claimen, maar om dezelfde discipline vroeg toe te passen:

- expliciete scope en begrippen;
- traceerbare theorie- en modelkeuzes;
- gescheiden bron, evidence, claim en kwalificatie;
- een expliciet datamodel met dataset-grain en veldbetekenis;
- reproduceerbare implementatie en tests;
- duidelijke status van wat gemeten, afgeleid, scenario, benchmark, gekwalificeerd of nog geblokkeerd is.

De repository bevat inmiddels zowel projectbrede on-site effect- en evidence-oppervlakken als de Tollebeek off-site vertical slice. Tollebeek blijft een pilot voor source → transfer → dispatch en is niet de projectruggengraat. Landelijke schadeberekeningen blijven bewust data-gated waar actuele exposure, transfer of economische waardering ontbreekt.

## Documentatiestructuur

De hoofdstructuur is:

1. Project overview en colleague reader guide
2. Theoretisch raamwerk
3. Conceptueel model
4. Formeel model
5. Datamodel
6. Implementatie
7. Evidence en qualification
8. Workbook/application artifacts
9. Traceability en documentatiestatus
10. Status-A-light review/checkpoint

Zie [`docs/`](docs/) voor de inhoudelijke documentatie en [`schema/`](schema/) voor het canonieke datamodel.

## Belangrijk ontwerpprincipe

Een waarde zonder context is geen modelparameter. Voor ieder relevant gegeven willen we waar mogelijk vastleggen:

- betekenis;
- eenheid;
- entiteit en granulariteit;
- bron/provenance;
- evidence-status;
- qualification/admission-status;
- toegestane modeltoepassing;
- bekende beperkingen.

## Integriteitscontrole

Voor een inhoudelijke wijziging is de minimale lokale gate:

```bash
python tools/validate_project.py
python -m unittest discover -s tests -v
```

De validator controleert evidence-integriteit, formele traceability en de vereiste reviewstructuur. Een PASS betekent niet dat data-gated fysieke capabilities daarmee wetenschappelijk zijn gekwalificeerd.

## Artifacts

Binaire artifacts zoals Excel-workbooks worden niet automatisch de bron van waarheid. Zie [`artifacts/README.md`](artifacts/README.md) en [`docs/08_workbook_architecture.md`](docs/08_workbook_architecture.md) voor de rol van workbooks en dashboards in de projectarchitectuur.
