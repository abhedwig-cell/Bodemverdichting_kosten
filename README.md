# Bodemverdichting kosten

Wetenschappelijk raamwerk en software-/data-infrastructuur voor het project **De kosten van bodemverdichting voor landbouw en maatschappij**.

## Doel

Deze repository wordt de canonieke plek voor de relatie tussen:

**theorie → conceptueel model → formeel model → datamodel → implementatie → evidence/kwalificatie**.

De Excel-workbooks, dashboards en latere applicatie zijn gebruikersgerichte artifacts. Zij horen het canonieke model te volgen, niet andersom.

## Huidige status

De repository bevindt zich in een **Status-A-light opbouwfase**. Het doel is nog niet om een volledig Status A-dossier te claimen, maar om dezelfde discipline vroeg toe te passen:

- expliciete scope en begrippen;
- traceerbare theorie- en modelkeuzes;
- gescheiden bron/evidence/kwalificatie;
- een expliciet datamodel;
- reproduceerbare implementatie;
- duidelijke status van wat gemeten, afgeleid, scenario, benchmark, gekwalificeerd of nog geblokkeerd is.

## Documentatiestructuur

Zie [`docs/`](docs/) voor de inhoudelijke documentatie en [`schema/`](schema/) voor het canonieke datamodel.

De beoogde hoofdstructuur is:

1. Project overview en reader's guide
2. Theoretisch raamwerk
3. Conceptueel model
4. Formeel model
5. Datamodel
6. Implementatie
7. Evidence en qualification

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

Binaire artifacts zoals Excel-workbooks worden niet automatisch de bron van waarheid. Zie [`artifacts/README.md`](artifacts/README.md) voor de rol van workbooks en dashboards in de projectarchitectuur.
