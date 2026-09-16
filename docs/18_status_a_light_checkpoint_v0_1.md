# Status-A-light checkpoint v0.1

**Datum:** 2026-09-16  
**Doel:** een collega-reviewbare momentopname van wat inhoudelijk, formeel en technisch bestaat, wat daarvan gekwalificeerd is en welke data-gates de volgende wetenschappelijke stap blokkeren.

Dit document is geen claim dat het project Status A heeft bereikt. Het gebruikt Status-A-achtige discipline om de huidige staat reconstructeerbaar en overdraagbaar te maken.

## 1. Waar staan we nu?

De repository heeft inmiddels een doorlopende architectuur van theorie naar artifact:

`theorie → conceptueel model → formeel model → datamodel → implementatie → evidence/qualification → workbook/app-view`

De belangrijkste winst is dat deze lagen niet meer alleen in één groot Excel-bestand impliciet naast elkaar staan. De betekenis van velden, formele relaties, projectclaims, bron-evidence, qualification en softwaretests hebben nu afzonderlijke canonieke plekken.

## 2. Maturity per laag

| Laag | Huidige staat | Wat al bruikbaar is | Belangrijkste grens |
|---|---|---|---|
| Theoretisch raamwerk | BASELINE_READY | state → response → attribution → transfer → valuation is expliciet; algemene literatuurbaseline bestaat | niet iedere pathway heeft al Nederlandse/current kwantitatieve evidence |
| Conceptueel model | BASELINE_READY | objecten en causale ketens zijn expliciet | spatial/event operationalisering wordt nog uitgebreid |
| Formeel model | BASELINE_READY | equations-register met IDs, units, null semantics en toepassingsgrenzen | data-gated relaties mogen nog geen operationele default krijgen |
| Datamodel | MIGRATION_BASELINE | entiteiten, datasets, relaties, velden, grain en workbook-contract zijn machineleesbaar | nog niet alle legacy workbook-datasets zijn gemigreerd naar canonieke v1-objecten |
| Implementatie | VERTICAL_SLICE_READY | generated-volume, dispatch- en energy-semantiek zijn geïmplementeerd en getest | fysieke Tollebeek-kwalificatie ontbreekt nog |
| Evidence/qualification | PARTIAL_CANONICAL | Tollebeek- en algemene theory-baselines bestaan met source → evidence → claim → qualification | belangrijke current soil/drainage/operations data ontbreken |
| Traceability | BASELINE_READY | equation- en capability-register koppelen theorie, dataset, code, tests en evidence | matrix moet meegroeien met nieuwe capabilities |
| Workbookinterface | REVIEW_READY | schema-driven workbook met metadata, guide, data dictionary en evidence-populatie | wetenschappelijke resultaatsheets blijven terecht leeg zolang data-gates niet zijn opgelost |
| Applicatie | NOT_STARTED_AS_PRODUCT | architectuur en datamodel bereiden de applicatie voor | nog geen productimplementatie of gebruikersvalidatie |

## 3. Tollebeek vertical slice

Tollebeek is de eerste end-to-end reviewlijn, niet de definitie van het algemene raamwerk.

### Reeds expliciet

- current/reference attributie moet matched zijn;
- generated runoff is niet hetzelfde als field-edge delivery, network volume of pumped volume;
- IJsvogel installed capacity heeft een afzonderlijke betekenis van event-specifieke availability;
- Kievit nominal hardware, historische calculated capacity en current operating capacity zijn verschillende grootheden;
- Kievit-zone → IJsvogel assist bestaat als routingsemantiek, maar heeft geen default assist-fractie;
- pump energy vereist expliciete routed volume, total dynamic head en efficiency;
- historische FutureWater-drainage-instellingen zijn method priors, geen current OT.02 calibration.

### Nog geblokkeerd

De fysieke Tollebeek-attributie blijft **NO-GO** totdat minimaal voldoende evidence bestaat voor:

1. current OT.02 geometry / relevante spatial units;
2. current drainage configuration;
3. current depth-resolved soil/compaction state;
4. matched reference state;
5. event forcing en initial hydrological state;
6. managed groundwater/surface-water boundary representation;
7. event-scale transfer/routing evidence;
8. current pump operation where capacity/cost claims are intended.

## 4. Wat bewijzen de huidige tests?

De huidige tests en validators bewijzen onder andere:

- IDs en foreign-key-achtige referenties zijn intern consistent;
- controlled vocabularies worden gerespecteerd;
- formele equation IDs en capability-traceability verwijzen naar bestaande datasets/code/tests/evidence;
- generated-volume, dispatch en energy software identities gedragen zich volgens de vastgelegde semantiek;
- workbook specs gebruiken bestaande canonieke velden en evidencekolommen.

Zij bewijzen **niet** dat een data-gated fysiek effect voor Tollebeek empirisch juist is. Software-QA en referentiële integriteit zijn voorwaarden voor wetenschappelijke kwaliteit, geen vervanging ervan.

## 5. Canonieke reviewoppervlakken

Voor collega-review zijn de belangrijkste oppervlakken nu:

- inhoudelijk verhaal: `docs/00_colleague_reader_guide.md` en `docs/01`–`07`;
- documentatieregels: `docs/14_documentation_status_a_light.md`;
- collega-traceability: `docs/15_traceability_matrix_v0_1.md`;
- machine-readable formeel model: `model/equations.csv`;
- machine-readable capability-chain: `model/traceability.csv`;
- evidence: `evidence/`;
- datamodel: `schema/`;
- workbookinterface: `tools/workbook_generator/` + artifact spec;
- integriteitsgate: `python tools/validate_project.py`.

## 6. Eerstvolgende inhoudelijke mijlpaal

De volgende wetenschappelijke mijlpaal is niet een grotere architectuurversie, maar een **eerste spatial source model** met echte current/reference invoer.

Doeloutput op recordniveau:

| spatial/profile | drainage | current state | reference state | event | runoff current | runoff reference | delta runoff | delta drainage | delta ET |
|---|---|---|---|---|---:|---:|---:|---:|---:|

Pas nadat deze bronrespons inhoudelijk gekwalificeerd is, hoort opschaling naar transfer, pump dispatch en kosten plaats te vinden.

## 7. Eerstvolgende overdrachtsmijlpaal

Voor collega's is de volgende review niet: "begrijp alle oude Excel-tabs". De reviewvraag is:

1. klopt de theoretische decompositie?
2. zijn de current/reference en attribution-regels wetenschappelijk verdedigbaar?
3. zijn objecten, dataset-grain en veldbetekenissen begrijpelijk?
4. zijn claims en hun evidence/qualification correct gescheiden?
5. zijn de huidige data-gates terecht en volledig?
6. kan een collega via de traceability van claim naar formeel model, data, code en test navigeren?

Feedback op deze vragen heeft nu hogere waarde dan uitbreiding van de applicatie-interface.

## 8. Status van dit checkpoint

`CHECKPOINT_V0_1 = REVIEW_READY`

Dat betekent: geschikt als overdrachts- en reviewmoment voor de huidige architectuur. Het betekent niet dat data-gated capabilities zijn gekwalificeerd of dat het project een volledig Status A-dossier heeft.
