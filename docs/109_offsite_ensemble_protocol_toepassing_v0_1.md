# Toepassing bestaand evidence-ensembleprotocol op zes off-site categorieën

**28 oktober 2026 | ENSEMBLE_CANDIDATE_SCREEN | geen nieuwe effectcoëfficiënten toegelaten**

Dit is de gevraagde toepassing van [document 50](50_evidence_ensemble_protocol_v0_1.md), **niet** het ontwerp van een nieuw ensembleprotocol. De bronleden staan in [kandidaat-screening CSV](../evidence/offsite_ensemble_candidate_screen_v0_1.csv). De bestaande canonieke ensembles in `evidence/evidence_ensemble_register_v0_1.csv` blijven ongewijzigd; waar reeds een bestaande evidence ID bekend is, verwijst deze screening ernaar. Andere bronnamen zijn nog **geen canonieke source- of evidence-IDs**.

## 1. Terminologie

De oorspronkelijke `F1–F6` in [document 49](49_project_effect_pathway_matrix_v0_1.md) zijn *proces-/effectpadcodes*, terwijl `F1–F6` in de nieuwere zes-categorieën-CSV als *uitkomstcategorieën* werden gebruikt. In deze screening heten de zes uitkomstcategorieën daarom **EC1–EC6**. Dit zijn presentatie-aliases, geen stilzwijgende datamodelmigratie. De bestaande matrix heeft nog steeds haar historische F-labels en wordt niet zonder migratie hernoemd.

De toegestane **member roles** volgen letterlijk document 50: `DIRECT_CANDIDATE`, `PROXY`, `BOUND`, `SCENARIO`, `BENCHMARK`, `GUARDRAIL`. De ensembleverdicts volgen hetzelfde protocol: `COMPARABLE_ENSEMBLE`, `BOUND_ENSEMBLE`, `SCENARIO_ENSEMBLE`, `INCOMPATIBLE_SET`, `SINGLE_SOURCE_ONLY`.

## 2. Resultaat van classificatie

| Uitkomstcategorie | Beschikbaar ensemblebewijs | Te rechtvaardigen samenvoeging? | Beslissing |
|---|---|---|---|
| EC1 wateroverlast | WENR2811 hydrologie; bestaand legacy-ensemble runoff; UK Defra benchmark | **Nee**: runoff aan perceel is geen flooding-schade | Reeds geconditioneerde fysieke bronresponsen alleen als aparte scenario's |
| EC2 waterbeschikbaarheid | bestaand `H07_GRASS_IRRIGATION` 50–90 mm voor droge-jaar *potentiële vraag*; BoVer kasproef | **Nee**: andere bodem/route/eindpunt | Behoud bestaand bound voor potentiële vraag, geen regionale leveringsfactor |
| EC3 N₂O/CH₄ | Bessou veldcontrast; Pulido-Moncada subsoil-gastransport | **Nee**: netto flux tegenover gastransport en topsoil-/rijspoorbehandeling | Veldcontrast als proxy, mechanisme als guardrail |
| EC4 N/P | Britse rijspoor-P-vrachten; Nederlandse gecombineerde bodemverbeteringsstudie | **Nee**: topsoil P versus gemengde N/P-route | Stofroute aantoonbaar, geen subsoil-vrachtband |
| EC5 middelen | Nederlandse preferente transportmetingen; MONOVI-baseline | **Nee**: geen treatment contrast | Alleen route-/receptorcontext |
| EC6 bodemleven | regenwormherstel; BoVer bio-subsoiling synthese | **Nee**: verschillende mechanismen en tijdschalen | Biologische en hydraulische herstelmaten apart beschrijven |

**0 van 6** effectcategorieën hebben met deze bronnen een `COMPARABLE_ENSEMBLE` dat specifiek een Nederlandse ondergrondverdichtingsschadecoëfficiënt kan voeden. Dit betekent niet dat de effecten nul zijn.

## 3. Belangrijkste inhoudelijke vooruitgang

De oorspronkelijke methodiek *bevatte al* empirische fysische bound-kandidaten die in de recentere zes-categorieënmatrix enigszins uit beeld waren geraakt:

- `ENS_O3_IRRIGATION_DRY` met `H07_GRASS_IRRIGATION`: **50–90 mm potentiële extra beregeningsbehoefte** onder droge condities, expliciet geen feitelijk toegediend water; bestaand registerstatus `LEGACY_WORKBOOK_NOT_YET_CANONICAL`.
- `ENS_F1_RUNOFF_LOCAL` bevat een Nederlandse model/proxy `H04_VK_RUNOFF_MAIZE` met **10–12 mm/jaar** en Vlaamse proxy van **9 mm/jaar**, eveneens legacy of contextgebonden; geen nationale of receptor-gerichte schadefactor.

Dat is geen nieuw ontdekt bewijs en behoort niet met de actuele 6-categorieën-screening te worden vermengd als het een toegelaten effect betreft. Het wordt hier terug in beeld gebracht omdat het **waar het direct op zijn eigen fysische vraag past** een zinvolle *kandidaatgrens* kan bieden.

Verder blijkt dat Deasy, Bessou en Capowiez wel effectgrootten melden, maar hun verschillen in **behandeling, diepte, schaal, receptor en tijdsdefinitie** verhinderen het numeriek combineren tot Nederlandse subsoil-effectbanden. Het ensembleprotocol werkt dus zoals bedoeld: bewijs wordt niet weggegooid, maar ook niet geforceerd gemiddeld.

## 4. Uitwerking via de bestaande methodiek

Per toepassing volgt de bestaande procedure:
1. doelvraag met bodem, landgebruik, diepte, referentie en tijdvenster;
2. bronlid inclusief reeds bestaande evidence ID waar geverifieerd;
3. rol `PROXY/BOUND/SCENARIO/... ` en expliciete toegestane en verboden inzet;
4. verdict passend bij directe vergelijkbaarheid, *zonder te middelen bij `INCOMPATIBLE_SET`*;
5. pas na onafhankelijke admission van het toepassingsbereik gebruik als berekeningsinvoer.

**Eerstvolgende concrete beslissingen:** voor EC1 en EC2 de **reeds bestaande** Nederlandse fysische proxy-ensembles op bronmethodiek en toepassing toetsen; voor EC3 een doelvraag formuleren voor netto *subsoil-only* N₂O-flux; voor EC4/EC5 N/P- en middelenvracht per route afzonderlijk behandelen; voor EC6 een niet-monetaire ecologische effectkaart maken. SWAP en de landelijke meetdataset blijven geparkeerd.

## 5. Status

Geen wijziging aan documents 02/04/49/50/59, causaal netwerk v0.7, Word-notitie of `evidence/evidence_ensemble_register_v0_1.csv`. Dit is een kandidaat-screening **onder** bestaande governance, geen admission van een nationale effectfactor of monetarisering.
