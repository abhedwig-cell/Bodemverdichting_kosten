# PROJECT_ARCHITECTURE_STATUS

Status: **CURRENT STATUS-A-LIGHT PROJECT AUTHORITY**
Reconciled: **23 september 2026**
Reconciliation basis: `main @ 7ccc2cab8c05fc21611226d88c7224842ad4cbbc`

## Doel van deze pagina

Deze pagina is de centrale wegwijzer voor de actuele projectarchitectuur en readiness. Zij vervangt de inhoud van de onderliggende documenten niet. Zij zegt welke onderdelen nu authority zijn, hoe ze samenhangen, waar de projectbrede lijn volwassen is en waar nog echte gaten of blockers zitten.

De repository blijft de bron van betekenis. Excel, dashboards en een toekomstige applicatie zijn afgeleide interfaces.

De leidende keten is:

```text
THEORY
  → CONCEPTUAL MODEL
  → FORMAL MODEL
  → DATA MODEL
  → EVIDENCE / QUALIFICATION
  → IMPLEMENTATION
  → ARTIFACTS
  → USER / REVIEW VIEWS
```

De volgorde betekent niet dat ieder effect door een procesmodel moet. De projectregel blijft: **gebruik direct gekwalificeerd bewijs als dat de vraag voldoende beantwoordt, en reken alleen wat aanvullend nodig is.**

## 1. Waar staat de actuele authority?

| Laag | Actuele authority | Huidige toestand |
|---|---|---|
| Projectvraag en methode | `docs/00_project_handover_and_continuation.md`, `docs/02_theoretical_framework.md`, `docs/49_project_effect_pathway_matrix_v0_1.md` | projectbreed werkbaar |
| Conceptueel model | `docs/03_conceptual_model.md`, `schema/entities.yml`, `schema/relationships.yml` | generieke kern aanwezig |
| Formeel model | `docs/04_formal_model.md`, `model/equations.csv`, `model/traceability.csv` | kern aanwezig, dekking nog ongelijk over pathways |
| Datamodel | `docs/05_data_model.md`, `schema/` | composite Status-A-light baseline |
| Evidence en kwalificatie | `docs/07_evidence_and_qualification.md`, `evidence/` | partieel canoniek, intended use blijft leidend |
| Implementatie | `src/`, `tools/`, `tests/` | bounded implementaties, geen volledige nationale rekenmotor |
| Workbookcontract | `schema/workbook_contract.yml`, `tools/workbook_generator/` | generiek contract met Tollebeek-pilotadapter |
| Collega-review | `docs/57_colleague_review_package_v0_2.md`, `review/` | reviewbaar in gewone taal |

`docs/18_status_a_light_checkpoint_v0_1.md` blijft een historische momentopname van 16 september. Het is niet langer de actuele projectbrede statusauthority.

## 2. Projectbrede inhoudelijke positie

De gemeenschappelijke stam blijft:

```text
bodemverdichting
  → bodemfysische toestand
  → landbouwkundige of hydrologische respons
  → attributie aan bodemverdichting
```

Daarna lopen ten minste twee gelijkwaardige routes.

**On-site** omvat onder meer gewasopbrengst, beworteling, droogtestress, beregeningsbehoefte, extra bewerkingen en private economische gevolgen.

**Off-site** omvat onder meer extra afvoer, overdracht naar het watersysteem, regionale watervraag, bemaling, systeemdruk en later eventueel stoffenstromen en bredere maatschappelijke gevolgen.

Geen van beide routes is verplicht gekoppeld aan SWAP. Een directe empirische of literatuurrelatie heeft de voorkeur wanneer context, referentie en intended use voldoende gekwalificeerd zijn.

## 3. Huidige maturity per laag

| Laag | Oordeel | Belangrijkste grens |
|---|---|---|
| Theorie | `WORKING_BASELINE` | brede causale en economische decompositie staat; niet iedere pathway heeft actuele Nederlandse kwantitatieve evidence |
| Conceptueel model | `WORKING_BASELINE` | generieke objecten zijn bruikbaar; verdere objectuitbreiding alleen bij aantoonbare behoefte |
| Formeel model | `PARTIAL_METHOD_READY` | off-site/Tollebeek is relatief sterk geformaliseerd; nieuwere on-site surfaces lopen nog achter in formele traceability |
| Datamodel | `WORKING_BASELINE` | datasets hebben grain/key; veldschema is nog een bewust samengestelde baseline met oudere kern en nieuwere extensions |
| Evidence/qualification | `PARTIAL_CANONICAL` | eerste on-site ensembles en meerdere pilotclaims zijn gekwalificeerd; actuele exposure, transfer en economische input blijven incompleet |
| Implementatie | `PARTIAL_METHOD_READY` | generieke identities, fail-closed crosswalk en validators bestaan; geen generieke nationale schade-engine |
| Workbook | `WORKING_BASELINE` | contract is generiek; huidige generator is bewust een Tollebeek reviewadapter, geen application backend |
| Applicatie | `SKELETON` | architectuurrichting bestaat, productimplementatie en gebruikersvalidatie nog niet |

## 4. On-site readiness

De on-site lijn is projectbreed hersteld en niet langer alleen een toekomstig hoofdstuk.

Wat er nu staat:

- gekwalificeerde grass/sand en maize/sand evidence-ensembles met expliciete rollen en overdraagbaarheidsgrenzen;
- een bounded calculation surface die geen schadegetal produceert zolang exposure, crop share of economische waarden ontbreken;
- een fail-closed BRP × BRO ontwerp voor silage-maïs, waarbij onbekende of niet-gekwalificeerde bodemcodes geen automatische restklasse krijgen;
- expliciete scheiding tussen historische areaalbasis, actuele verdichtingsexposure, gewasrespons en economische waardering.

Belangrijkste blockers:

- actuele verdichting naar relevante diepte en ernst;
- voor maïs een volledig gekwalificeerde crop × soil crosswalk op actuele brondata;
- crop-specifieke economische waarden met expliciet gekozen waarderingsperspectief;
- contextmatch tussen response-evidence en de uiteindelijke soil × crop × weather × reference combinatie.

Daarom is een actuele landelijke on-site totaalschade **niet toegelaten**.

## 5. Off-site readiness en Tollebeek

De generieke off-site keten is inhoudelijk duidelijk:

```text
bronrespons
  → field-edge delivery
  → sloot/netwerk
  → managed-system response
  → operationele of maatschappelijke consequentie
  → waardering
```

Tollebeek blijft een sterke pilot voor deze keten, vooral voor source → transfer → dispatch en voor het zichtbaar maken van de gegevens die nodig zijn. Tollebeek is geen nationaal projectmodel.

De belangrijkste externe blocker blijft issue #36: `Acquire WER3382 Tollebeek current-state records`.

Actuele readiness:

`DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE / HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`

De eerder onderzochte publieke BIS-4D/4TU/DOI-routes worden niet opnieuw geopend zonder nieuwe aanleiding. De legitieme vervolgroutes zijn bronhoudercontact via Aeres/RAAK-PRO, WUR/WENR of Actieplan Bodem & Water Flevoland.

Zolang de bronrecords ontbreken, volgt geen soil-state admission en geen daarop gebaseerde SWAP-runclaim.

## 6. Wat de huidige repository expliciet niet autoriseert

- geen actueel landelijk schadebedrag;
- geen 32% of 37% sample-location percentage als nationaal affected area;
- geen historische opbrengstcoëfficiënt als universele actuele schadefactor;
- geen generieke maize-coëfficiënt voor alle akkerbouw;
- geen Tollebeek-pompbenchmark als nationale kostenfactor;
- geen default voor delivery, assist, availability, head of pump efficiency;
- geen automatische overdracht van een bodemtoestand tussen 1998, 2020-2021 en 2026;
- geen workbook of dashboard als bron van canonieke betekenis.

## 7. Datamodel: oordeel en bekende schuld

De generieke kern is voldoende volwassen om verdere applicatieontwikkeling op te baseren. `schema/datasets.yml` heeft voor de huidige datasetobjecten expliciete grain en primary key. De entities en relationships zijn overwegend generiek en niet Tollebeek-specifiek.

De belangrijkste resterende datamodelschuld is niet een ontbrekende database. Het is vooral versie- en registratiediscipline:

- de schemafolder is een **composite baseline**: oudere kernbestanden en nieuwere domain extensions bestaan naast elkaar;
- `soil_state_id` is de actuele identifier in de v0.3 domain extension; legacy `state_id` mag geen tweede bodemtoestand-identiteit creëren;
- projectbrede effect-pathway, ensemble- en bounded-surface registers zijn belangrijke control surfaces, maar zijn nog niet allemaal als volwaardige domeindataset/object gepromoveerd. Promotie is pas zinvol als hun lifecycle en opslagbehoefte stabiel genoeg zijn.

Dat laatste is bewust geen reden om nu nieuwe framework-entiteiten te maken.

## 8. Workbook- en applicatiecontract

De workbookrichting blijft:

- `00_METADATA`;
- `01_GUIDE`;
- `DATA_DICTIONARY`;
- één datasetobject per tabel;
- datasetmetadata met minimaal dataset ID, entity, role, grain, primary key en canonical status;
- velddefinities en headerhelp uit hetzelfde canonieke schema;
- views en dashboards expliciet gescheiden van bron-/registertabellen;
- onbekende waarden als null/leeg;
- schema version en Git commit in artifactmetadata wanneer beschikbaar.

De huidige workbookgenerator is een **bounded Tollebeek reviewadapter** die dit contract demonstreert. Hij is niet het generieke datamodel en niet de toekomstige applicatie.

Een toekomstige applicatie hoort dezelfde canonieke dataset- en veldbetekenis te consumeren, maar mag eigen taakgerichte views hebben.

## 9. Collega-overdraagbaarheid

Beoordeling van `docs/57_colleague_review_package_v0_2.md`:

- **30-45 minuten voor de wetenschappelijke projectlogica:** ja;
- **theorie vóór techniek:** voldoende duidelijk;
- **balans on-site/off-site:** goed hersteld;
- **onzekerheidslogica:** begrijpelijk, inclusief het niet automatisch middelen van bronnen;
- **minimum necessary computation:** duidelijk;
- **architectuur/datamodel als enige bron:** nee, daarvoor is deze statuspagina plus de gekoppelde canonieke onderdelen nodig.

Het reviewdocument hoeft daarom niet opnieuw technisch te worden gemaakt. Deze pagina vult precies het overdrachtsgat tussen gewone projectuitleg en repositorydetails.

## 10. Actuele architectuurschuld die review vereist

1. De machine-readable traceability is historisch relatief Tollebeek/off-site-zwaar en moet de nieuwere on-site lijnen expliciet blijven volgen.
2. Oude statusdocumenten mogen niet opnieuw als actuele projectprioritering worden gelezen.
3. Schema-componentversies moeten als componentversies worden gelezen, niet als één fictieve globale v0.4-release.
4. Workbookdatasetmetadata moet uit het canonieke datasetcontract komen en niet via hard-coded migratiestatussen.
5. Validators moeten alle canonieke datasets op entity, role, grain, primary key en veldidentiteit bewaken, niet alleen een kleine subset.

## 11. Eerstvolgende ontwikkelstap

De logisch eerstvolgende stap is **geen nieuw hydrologisch detailmodel**.

Projectbreed heeft de hoogste informatiewaarde nu:

1. actuele compaction exposure naar diepte/ernst verwerven of kwalificeren voor de eerste on-site strata;
2. crop-specifieke economische input en de maize crop × soil route gecontroleerd sluiten;
3. voor off-site opschaling een kleine, evidence-based hydrologische systeemtypologie en transferroute ontwikkelen voordat een nationaal procesmodel wordt overwogen.

Tollebeek kan parallel verder zodra issue #36 of andere echte bronhouderdata beschikbaar komen, zonder dat die blocker de on-site of nationale projectlijn stilzet.

## 12. Closure-oordeel van deze reconciliation

De repository heeft een bruikbare Status-A-light kern. De grootste zwakte zat niet in ontbrekende theorie, maar in **authority drift** tussen oudere Tollebeek-zware statusstukken, nieuwere projectbrede documentatie en gedeeltelijk achtergebleven schema/workbookmetadata.

Na deze reconciliation is de bedoelde projectstructuur:

```text
projectbrede theorie en effectpaden
  → expliciete context/reference/attribution
  → canonical schema + evidence qualification
  → alleen benodigde berekeningen
  → bounded outputs
  → transparante workbook/app views
```

Nieuwe frameworklagen zijn alleen gerechtvaardigd als een concrete workflow anders niet eenduidig traceerbaar of testbaar kan worden gemaakt.