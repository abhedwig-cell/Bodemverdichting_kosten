# Project architecture status v0.1

**Status:** CURRENT STATUS-A-LIGHT PROJECT AUTHORITY  
**Datum:** 23 september 2026  
**Gereconcilieerde main:** 7ccc2cab8c05fc21611226d88c7224842ad4cbbc  
**Doel:** één actuele wegwijzer voor architectuur, traceability, overdraagbaarheid, blockers en de eerstvolgende ontwikkelstap. Deze pagina dupliceert de onderliggende theorie, evidence of schema's niet.

## 1. Projectpositie

De repository ondersteunt één projectvraag: wat zijn de gevolgen en kosten van bodemverdichting voor landbouw en maatschappij, en hoe ver kunnen we die gevolgen verantwoord kwantificeren?

De leidende rekenstrategie is minimum necessary computation. Bestaande metingen, literatuur en directe empirische relaties krijgen voorrang wanneer zij de bedoelde schakel voldoende afdekken. Een procesmodel wordt pas ingezet als een materiële onzekerheid niet eenvoudiger kan worden begrensd en het model met gekwalificeerde invoer werkelijk informatiewinst kan leveren.

De gemeenschappelijke causale stam is:

bodemverdichting → bodemfysische toestand → fysieke/agronomische respons → attributie → effect op perceel of overdracht naar een extern systeem → waardering.

Daarbinnen zijn on-site en off-site gelijkwaardige paden. Tollebeek is een lokale managed-system pilot voor source → transfer → dispatch en een kwalificatieomgeving voor hydrologische off-site berekeningen. Het is niet het nationale projectmodel.

### Einddoel: conditionele kosten in plaats van één universele schadefactor

Een bodemtype × landgebruikcombinatie heeft niet één contextvrij schadebedrag. De uitkomst kan veranderen met de verdichtingstoestand, het gewas, droogte of neerslagbelasting, antecedente toestand, grondwater en drainage, watersysteemcapaciteit, tijdshorizon en de gekozen waardering.

De projectoutput moet daarom scenario's en bandbreedtes kunnen dragen. Een scenario is een expliciete combinatie van relevante condities, niet een ongedefinieerd label. Niet alle mogelijke combinaties worden vooraf gemodelleerd. Per pathway worden alleen de condities expliciet die de interpretatie of kostenuitkomst materieel veranderen.

De systematiek is bewust uitbreidbaar. Nieuwe evidence of gerichte rekenexperimenten kunnen later een belangrijke bandbreedte verkleinen zonder de bestaande semantiek te herschrijven.

De prioriteit van vervolgonderzoek wordt uiteindelijk bepaald door de vraag hoeveel onzekerheid het wegneemt in **schade en kosten**. Een grote fysische onzekerheid die nauwelijks doorwerkt in de eindraming heeft een lagere projectprioriteit dan een eenvoudiger onzekerheid die de kostenuitkomst domineert.

## 2. Waar hoort welke betekenis?

| Laag | Canonieke authority | Huidige functie |
|---|---|---|
| Theorie | docs/02_theoretical_framework.md en theory-evidence baseline | definieert state, response, attributie, transfer, aggregatie en waardering |
| Conceptueel model | docs/03_conceptual_model.md, schema/entities.yml, schema/relationships.yml | definieert objecten en causale relaties |
| Formeel model | docs/04_formal_model.md, model/equations.csv | definieert vergelijkingen, units, nullgedrag en toepassingsgrenzen |
| Datamodel | schema/ en docs/05_data_model.md | definieert datasetidentiteit, grain, keys, velden en relaties |
| Evidence/qualification | evidence/ en docs/07_evidence_and_qualification.md | houdt source, evidence, claim en intended-use qualification uit elkaar |
| Implementatie | src/, tools/ en docs/06_implementation.md | implementeert gedeelde relaties, acquisitie en validatie |
| Traceability | model/traceability.csv plus validators | koppelt capability aan theorie, datasets, code, tests en evidence |
| Artifact/workbook | schema/workbook_contract.yml en tools/workbook_generator/ | afgeleide reviewinterface, nooit bron van betekenis |
| Gebruikers-/reviewview | docs/57_colleague_review_package_v0_2.md en review/ | legt het project in gewone taal uit en verzamelt inhoudelijke feedback |

Oudere checkpoints en Tollebeek-workunits blijven traceerbare geschiedenis. Zij zijn niet automatisch de actuele projectbrede authority.

## 3. Huidige readiness per laag

### Theorie en projectframe: WORKING_BASELINE

De hoofdredenering is coherent genoeg om verder te werken. Current/reference, minimum necessary computation, de scheiding state/response/attribution/transfer/valuation en de economische categorieën zijn expliciet. De projectbrede effect-pathways O1–O5 en F1–F6 maken zichtbaar dat zowel landbouwkundige als maatschappelijke routes worden gevolgd.

### Conceptueel en formeel model: PARTIAL_PROJECT_WIDE_BASELINE

De generieke keten is duidelijk. De meest uitgewerkte formele vergelijkingen liggen nog bij de hydrologische source/transfer/dispatch-lijn. Voor opbrengst, irrigatie, werkbaarheid en economische consolidatie bestaan inmiddels begrensde rekencontracten en evidence-oppervlakken, maar nog niet voor iedere pathway een production-grade formele functie. Dat is geen reden om nu extra modelcode te bouwen: eerst moet blijken welke relaties werkelijk nodig zijn.

### Datamodel: COMPOSITE_BASELINE_READY

De kernentiteiten voor bodem, modelruns, transfer, watersysteem, waardering en evidence zijn aanwezig. Projectbrede effect-pathways, evidence-ensembleleden en bounded calculation surfaces zijn nu eveneens expliciete datasetobjecten. Dataset grain en primary key zijn machineleesbaar.

De schemafiles hebben verschillende lokale versienummers. De projectauthority is daarom de samengestelde schema-inhoud plus de integriteitsvalidators, niet één los schema_version-label.

### Evidence en qualification: PARTIAL_CANONICAL

De source/evidence/claim/qualification-keten werkt en wordt gevalideerd. Voor grass/sand en maize/sand zijn de eerste response-ensembles gemigreerd. Sommige ensembleleden blijven expliciet legacy totdat de bron volledig canoniek is gemaakt. Verschil tussen studies wordt niet automatisch tot één gemiddeld schadepercentage gereduceerd.

### Implementatie: BOUNDED

De gedeelde code voor generated volume, dispatch en pump energy is klein en testbaar. De on-site bounded calculation surface en BRP × BRO crosswalk zijn fail-closed tools/contracten, geen nationale schadeberekening. Er bestaat nog geen algemene productie-applicatiebackend en dat hoeft in deze fase ook niet.

### Workbook/app-contract: WORKING_BASELINE

Het workbookcontract bewaakt 00_METADATA, 01_GUIDE, DATA_DICTIONARY, dataset-id, entity, role, grain, primary key en canonical status. Het huidige gegenereerde workbook is bewust een Tollebeek reviewartifact. Het is een voorbeeld van de adapterarchitectuur, niet de generieke projectdatabase of de toekomstige applicatiestructuur.

Een toekomstige applicatie moet rechtstreeks dezelfde canonieke datasets en velddefinities consumeren. Views mogen de presentatie aanpassen, maar geen tweede semantiek introduceren.

## 4. Projectbrede effectpaden

De huidige machineleesbare pathwaymatrix bevat:

On-site:
- O1 gewasopbrengst/productie;
- O2 gewaskwaliteit;
- O3 potentiële beregeningsbehoefte/droogtegevoeligheid;
- O4 extra veldbewerkingen/werkbaarheid;
- O5 private bedrijfsschadeconsolidatie.

Off-site:
- F1 extra runoff/veranderde drainage;
- F2 field-edge/ditch/network delivery;
- F3 bemaling, energie en capaciteitsdruk;
- F4 wateroverlast/flood/peak-risk;
- F5 regionale watervoorzieningsdruk;
- F6 waterkwaliteit/nutriënten/pesticiden als latere route.

Deze matrix is de projectbrede voortgangskaart. Een route mag direct van goede empirische evidence naar een effectschatting gaan als de contextmatch en intended use dat toelaten. Er is geen eis dat alle paden via SWAP of Tollebeek lopen.

## 5. Wat mag nu al wel en niet?

Wel:
- rapporteren welke effectroutes en bronnen beschikbaar zijn;
- grass/sand en maize/sand response-evidence als expliciete scenario/ensembleleden tonen;
- de eerste on-site calculation surfaces tonen als fail-closed rekenstructuur;
- historische/reporting area als context gebruiken wanneer de status en bronbeperking zichtbaar blijven;
- BRP × BRO mappingvoorstellen genereren en alleen expliciet gekwalificeerde mappings toelaten;
- Tollebeek gebruiken als lokale pilot en methode-/transferkwalificatie.

Niet:
- actuele landelijke verdichting invullen met historische prevalence of sample-location percentages;
- een ensemble tot één centrale schadefactor reduceren zonder afzonderlijke authority;
- akkerbouwareaal behandelen als maïsareaal;
- gegenereerde runoff direct als pompvolume of maatschappelijke schade behandelen;
- historische pompcapaciteit of kosten als actuele nationale factor gebruiken;
- een technisch mogelijke SWAP-run als wetenschappelijk toegelaten run presenteren;
- workbook- of dashboardwaarden tot canonieke projectstate promoveren.

## 6. Externe en inhoudelijke blockers

### Actuele nationale exposure

Voor de eerste landelijke on-site berekeningen ontbreekt nog een voldoende actuele en bruikbare verdichtingslaag met relevante diepte- en ernstsemantiek. Historische CC-NL-informatie blijft context/reference, geen 2026 exposure.

### Economische waardering

Crop-specifieke actuele waarden en de keuze tussen gross revenue, marginal private damage en societal production/welfare moeten per toepassing worden gekwalificeerd. Deze categorieën mogen niet stilzwijgend worden opgeteld.

### Maïs × bodem

De fail-closed BRP × BRO route bestaat. Een productieresultaat vereist nog volledig gekwalificeerde bronmaterialisatie en expliciete mapping van de werkelijk aangetroffen BRO-codes. Onbekende/ambigue codes blijven REVIEW_REQUIRED.

### Off-site transfer

De conceptuele source → field edge → network → managed system keten staat. Generieke nationale transferfactoren zijn niet toegelaten. De volgende schaalstap is eerder een kleine watersysteemtypologie met gekwalificeerde evidence dan een nieuw nationaal procesmodel.

### Tollebeek current state

Issue #36 blijft de harde externe bronhouderroute voor de WER3382 2020–2021 records. Publieke BIS/DOI-routes zijn al inhoudelijk gesloten. Geen current soil-state admission of SWAP-resultaatclaim zonder ontvangst en afzonderlijke qualification.

## 7. Collega-overdraagbaarheid

Oordeel voor een WENR-collega met ongeveer 30–45 minuten:

**voldoende voor inhoudelijke projectreview, mits de leesroute bij docs/57 begint en niet bij de historische Tollebeek-documenten.**

Waarom:
- theorie en projectvraag komen vóór techniek;
- on-site en off-site zijn in docs/57 en de pathwaymatrix weer in balans;
- minimum necessary computation is duidelijk;
- verschillen tussen studies worden als onzekerheidsinformatie uitgelegd;
- current/reference en economische categorieën zijn begrijpelijk;
- het document maakt expliciet wat nog niet berekend mag worden.

Resterende beperking:
- de oudere uitgebreide reader guide en veel historische workunits zijn nog Engelstalig/technisch en Tollebeek-zwaar;
- zonder deze authoritypagina kon een nieuwe lezer daardoor ten onrechte denken dat de hydrologische pilot de projectarchitectuur definieert.

Voor de eerste review is daarom de aanbevolen volgorde:
1. docs/57_colleague_review_package_v0_2.md;
2. deze pagina;
3. docs/49_project_effect_pathway_matrix_v0_1.md of docs/50_evidence_ensemble_protocol_v0_1.md alleen waar verdieping nodig is;
4. technische documenten pas bij een concrete reviewvraag.

## 8. Structurele correcties van deze reconciliation

Deze workunit maakt geen nieuwe hydrologische of economische claim. De structurele correcties zijn:

- één actuele projectbrede authoritypagina;
- oude Tollebeek-first checkpoints expliciet als historische/partiële oppervlakken gemarkeerd;
- schema-documentatie bijgewerkt naar de samengestelde v0.3.x-baseline;
- projectbrede pathways, ensembles en bounded surfaces geregistreerd als canonieke datasetobjecten;
- validators voor dataset grain/key/storage-field-integriteit en pathwayreferenties;
- workbookcontract en generator weer in lijn gebracht voor role, grain, primary key en datasetstatus;
- Tollebeek workbookdatasetstatussen niet langer allemaal generiek als MIGRATION_BASELINE gelabeld;
- src-documentatie gecorrigeerd zodat toekomstige packages niet als reeds geïmplementeerd worden gepresenteerd;
- resterende Engelse reviewdispositions gehumaniseerd.

## 9. Eerstvolgende ontwikkelstap

De logisch volgende stap is niet nog een frameworkversie en ook niet automatisch een nieuwe SWAP-campagne.

Werk in twee gecontroleerde sporen:

**Wetenschappelijke inhoud:** bind de eerste nationale on-site surfaces verder met actuele exposure, maïs × bodem en economische data zodra die daadwerkelijk gekwalificeerd beschikbaar zijn. Leg per prioritaire pathway vast welke scenario/contextdimensies de kostenuitkomst materieel sturen en kies vervolgens de lichtste route die de dominante eindonzekerheid reduceert.

**Applicatie/overdracht:** bouw eerst een generieke read-only application/workbook view over pathway → evidence/ensemble → calculation readiness → blocker → allowed output. Die view moet rechtstreeks uit de geregistreerde canonieke datasets komen. Pas daarna is invoer/editing of een productiebackend zinvol.

Voor off-site is de eerstvolgende projectbrede stap een kleine, expliciete watersysteemtypologie en evidencebehoefte per type. Tollebeek blijft één kwalificatiecase binnen die typologie.

## 10. Closure-oordeel

- repositoryarchitectuur: **coherent na beperkte authority-/contractreparatie**;
- Status-A-light traceability: **voldoende voor huidige ontwikkelfase, nu projectbreder bewaakt**;
- collega-overdraagbaarheid: **review-ready via docs/57 + deze pagina**;
- datamodel: **voldoende volwassen voor verdere bounded applicatieontwikkeling, nog geen v1**;
- workbook/app-contract: **geschikt als afgeleide interface, bestaande generator blijft pilot-specifiek**;
- blockers: **expliciet en fail-closed**;
- volgende stap: **populateer en ontsluit projectbrede bounded surfaces; model alleen waar directe evidence niet genoeg informatiewinst geeft**.

Deze workunit sluit architectuurconsolidatie, niet de inhoudelijke schadeberekening.
