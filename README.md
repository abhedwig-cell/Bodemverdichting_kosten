# Bodemverdichting kosten

Wetenschappelijk raamwerk en software-/data-infrastructuur voor het project **De kosten van bodemverdichting voor landbouw en maatschappij**.

## Start hier

Ben je nieuw in het project, begin dan met [`docs/00_colleague_reader_guide.md`](docs/00_colleague_reader_guide.md). Die geeft eerst het inhoudelijke verhaal: wat we proberen te berekenen, waarom current versus reference centraal staat, hoe de off-site waterketen is opgebouwd, waarom Tollebeek als pilot wordt gebruikt, hoe evidence wordt gekwalificeerd en welke rol GitHub, Excel en de toekomstige applicatie hebben.

De volledige documentatiekaart staat in [`docs/README.md`](docs/README.md). De Status-A-light documentatieregels staan in [`docs/14_documentation_status_a_light.md`](docs/14_documentation_status_a_light.md) en de huidige cross-layer traceability in [`docs/15_traceability_matrix_v0_1.md`](docs/15_traceability_matrix_v0_1.md).

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

De eerste volledige vertical slice is de Tollebeek-lijn van bronrespons via transfer naar pompdispatch. De architectuur, evidence-baseline en schema-driven workbookinterface bestaan; de daadwerkelijke hydrologische attributie blijft bewust data-gated zolang current soil/drainage state en operationele transferdata ontbreken.

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

## Artifacts

Binaire artifacts zoals Excel-workbooks worden niet automatisch de bron van waarheid. Zie [`artifacts/README.md`](artifacts/README.md) en [`docs/08_workbook_architecture.md`](docs/08_workbook_architecture.md) voor de rol van workbooks en dashboards in de projectarchitectuur.
