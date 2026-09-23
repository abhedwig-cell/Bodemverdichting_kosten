# Bodemverdichting kosten

Wetenschappelijk raamwerk en software-/data-infrastructuur voor het project **De kosten van bodemverdichting voor landbouw en maatschappij**.

## Start hier

Ben je nieuw in het project, begin dan met [`docs/00_colleague_reader_guide.md`](docs/00_colleague_reader_guide.md). Die geeft eerst het inhoudelijke verhaal: wat we proberen te berekenen, waarom current versus reference centraal staat, hoe de off-site waterketen is opgebouwd, waarom Tollebeek als pilot wordt gebruikt, hoe evidence wordt gekwalificeerd en welke rol GitHub, Excel en de toekomstige applicatie hebben.

De actuele projectbrede architectuur en readiness staan in [`PROJECT_ARCHITECTURE_STATUS.md`](PROJECT_ARCHITECTURE_STATUS.md). Gebruik die pagina als authority voor de huidige stand en als wegwijzer naar de onderliggende canonieke onderdelen. De volledige documentatiekaart staat in [`docs/README.md`](docs/README.md). De Status-A-light documentatieregels staan in [`docs/14_documentation_status_a_light.md`](docs/14_documentation_status_a_light.md), met formele traceability in [`model/traceability.csv`](model/traceability.csv) en [`docs/17_formal_traceability_register_v0_1.md`](docs/17_formal_traceability_register_v0_1.md). `docs/18_status_a_light_checkpoint_v0_1.md` blijft een historische checkpoint van 16 september 2026.

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

De repository bevat zowel projectbrede on-site/off-site control surfaces als een ver uitgewerkte Tollebeek vertical slice voor source → transfer → dispatch. Tollebeek is een pilot en kwalificatielijn, niet het nationale projectmodel. Actuele landelijke schadeberekeningen blijven bewust data-gated zolang onder meer current compaction exposure, contextmatch, transfer en economische input niet voldoende zijn gekwalificeerd.

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
