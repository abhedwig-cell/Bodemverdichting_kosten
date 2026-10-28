# SWAP-profielen voor ondergrondverdichting: brongetoetst onderzoeksprotocol v0.1

**28 oktober 2026 | METHOD_DESIGN_ONLY | geen parameter-admission of uitgevoerde SWAP-run**

Vervolg op [broncontrole 93](93_primaire_broncontrole_hydrologie_gewas_N2O_20261028.md) en de literatuurregisters 90–92. Deze notitie legt vast hoe de Nederlandse WENR-handreiking over modellering van bodemverbeterende maatregelen bruikbaar is voor de gezamenlijke on-site/off-site verkenning. **Geen nieuwe V-pijlen:** V01–V42 blijven het conceptuele referentiekader.

## 1. Wat de primaire bron daadwerkelijk zegt

**Bron:** WENR rapport 2811, *Effecten van verbetering bodemkwaliteit op waterhuishouding en waterkwaliteit*, hoofdstuk 5 ‘Handreiking modellering bodemverbeterende maatregelen’. Pagina's hieronder zijn **gedrukte rapportpagina's**, niet noodzakelijk de PDF-paginateller.

| Rapportpagina | Brongegeven | Wat daaruit volgt voor dit project |
|---|---|---|
| 71–72 | 1D-SWAP geschikt wanneer verticale transportbenadering verantwoord is; lokale vaste rijpaden vragen mogelijk 2D; neerslag op uurbasis, laagdikte en discretisatie zijn belangrijk | Niet zonder meer een 1D-kolom gebruiken voor ruimtelijk heterogene rijsporen; caseafhankelijke tijdstap en laagresolutie |
| 72–73 | Verdichte laag afzonderlijk karakteriseren met waterretentiecurve en K(h) (Mualem–Van Genuchten). SWAP-variabelen `ORES, OSAT, ALFAD, NPAR, LEXP, KSAT` | Verander een **consistent pakket** bodemfysische parameters, niet alleen bulkdichtheid of KSAT |
| 72 | `BDENS` relevant voor zuurstofstress-optie en stof-/N-processen | Geen hydraulisch effect uitsluitend uit een BDENS-aanpassing afleiden |
| 73–74 | Invoer kan rekening houden met macroporiën en hun geometrie; directe observatie van scheuren/wormgangen is nodig | Water dat via matrix niet doordringt, kan langs macroporiën toch passeren; macroporie-instellingen niet automatisch kopiëren |
| 74–75 | Wortelgroeiparameters `RDS, RDTB, RDCTB` relevant; een indringingsweerstand op basis van `PENETR` kan als begrenzing dienen | Hydraulische en wortelmechanische scenario's **apart en gecombineerd** verkennen |
| 75–77 | Wortels kunnen langs bestaande wormgangen door verdichte lagen groeien; macroporiën zijn contextafhankelijk | Mechanistische steun voor V42, maar geen algemeen herstelpercentage |
| 75 | Veel invoerparameters zijn statisch: verandering door maatregelen wordt doorgaans via gepaarde runs vergeleken | Jaarlijkse huidige schade onderscheiden van een dynamische meerjarige herstelhypothese |
| 76–77 | Pedotransferfuncties zijn empirisch en geldig binnen het kalibratiebereik; macropore-flow kent bypass en internal catchment | Buiten kalibratiebereik of bij onbekende macroporiën geen schijnprecisie toelaten |

## 2. Belangrijker dan één verdichtingsparameter: een gepaarde profielvergelijking

Per representatieve bodem–gewas–watersysteemcontext moeten de profielen **dezelfde** meteorologie, gewas, drainage/peilinstelling en beschikbare uitgangsinformatie delen. Alleen de voor verdichting gekozen toestand verandert.

**A. Referentie:** fysisch aannemelijke, minder antropogeen verdichte ondergrond voor dit bodemtype, met intern consistente waterretentie, geleidbaarheid, dichtheid en worteltoegankelijkheid. Dit is niet automatisch een ‘natuurlijke’ bodem.

**B. Huidige verdichte toestand:** ondergrond met passende laagdiepte en -dikte, bodemtype, gemeten/onderbouwde hydrologie en eventuele wortelbeperking.

**C. Variantanalyse:** (H) alleen hydrauliek gewijzigd, (R) alleen wortelparameterisatie gewijzigd, (HR) beide, en indien data dat toelaten (M) effecten van macroporiën. **De H/R/HR-varianten zijn sensitiviteitsproeven, geen onafhankelijk op te tellen schadeposten.** De alleen-wortelvariant is een diagnostische ingreep en hoeft geen fysisch realiseerbare bodemtoestand voor te stellen.

**Noodzakelijke baselinecontrole:** bodemfysische invoer uit oudere monsters of databanken kan reeds door berijding beïnvloed zijn. Voordat een extra laag wordt toegevoegd moet worden nagegaan wat het oorspronkelijke monster representeert. Een ‘huidige’ bodem en een ‘niet-verdichte’ referentie mogen niet dezelfde reeds verdichte hydraulische eigenschappen gebruiken zonder motivering.

## 3. Minimaal uitvoercontract voor gekoppelde on-site/off-site toets

| Grootheid | Waarom | Gebruik |
|---|---|---|
| Neerslag, initiële opslag en bodemvocht | Forcing en initiële toestand gelijk houden | Herleidbaarheid vergelijking |
| Bergingsverandering en drukhoogten boven/onder laag | Schijngrondwaterstand en veranderingen in vochttoestand | V04, V05, V11, V25 |
| Matrixinfiltratie en eventuele macropoorstroming | Verschillende routes, onder meer bypass | V04, V11, V30–V35 |
| Maaiveldafvoer per gebeurtenis, drainafvoer en tijdsverloop | Alleen lokale hydrologische bronrespons | V11–V13, nog géén regionale schade |
| Werkelijke transpiratie, bodemverdamping, interceptie | Waterbalans en mogelijke gewaswaterstress | V05–V07, V17 |
| Opnameverdeling en worteldiepte | Mechanische beperking als aparte aanname | V03, V05, V06 |
| Ondergrondflux en diepe percolatie | Niet vereenzelvigen met netto regionale aanvulling | V21–V22 |
| Sluitfout waterbalans | Numerieke en fysische consistentie | Voorwaarde voor verdere interpretatie |

Voor gewasopbrengst blijft empirische effectliteratuur leidend totdat hydrologie én wortelrestrictie passend zijn gevalideerd. SWAP/WOFOST kan plausibiliteit en klimaat-/bodemgevoeligheid toetsen, niet vanzelf een nationale opbrengstdervingsfactor vaststellen.

## 4. Vier concrete kwalificatietests

1. **Identificeer eerst de representatieve laag:** 30–100 cm uit de huidige meetopzet betekent niet dat iedere locatie over die hele zone één verdichte laag heeft. Laaggrenzen, textuur, ernst en profielopbouw blijven afzonderlijk geregistreerd.
2. **Hydraulische consistentie:** voor ieder geval controle op porositeit versus `OSAT`, retentie, onverzadigde en verzadigde doorlatendheid; parameters moeten bij dezelfde bodemtoestand passen.
3. **Gekoppelde bodemrespons:** vergelijk onder identieke natte en droge jaren zowel afvoer en percolatie als wortelwateropname. Rapporteer verschillen met teken en onzekerheid, niet alleen relatieve percentages.
4. **Schaalgrens:** modelmatige verandering van runoff aan de perceelsrand is *niet* gelijk aan extra bemaling, overstromingsschade, pesticidenvracht of KRW-kosten. Deze eindpunten vereisen routing, bronconcentraties, receptorrespons of economische waardering.

## 5. Wat nog onvoldoende onderbouwd is

- De vertaling van 2024-bulkdichtheidsmetingen naar **volledige** Mualem–Van Genuchten-sets per Nederlandse bodemklasse.
- Welke referentieprofielen in BOVEC/Staringreeks-achtige bestanden reeds historische verdichting bevatten.
- Of de hydrologische representatie voor de geplande situaties met **1D** volstaat en waar rijsporen om 2D vragen.
- De empirische relatie tussen verdichtingslaag en gewasspecifieke wortelrestrictie, afzonderlijk van waterstress.
- De werkelijke invloed van macroporiën op afvoer- en stofroutes in de Nederlandse cases.
- Een passende classificatie voor veengronden.

**Beslisregel:** zonder betrouwbare toestand–referentie en fysisch consistente waterbalans geen landelijke verdichtingscoëfficiënt afleiden. Rapporteer zo nodig eerst lokale bronresponsbanden met herkenbare bodem-, gewas- en hydrologische context.

## 6. Brongebruik en versiegrenzen

De Nederlandse handreiking in WENR rapport 2811 is de **primaire methodologische basis** van dit protocol. Het bevat deels oudere SWAP-invoernamen en oudere modelaannames; verifieer actuele SWAP5/SWAP4.3.1-invoer voordat een technische uitvoering begint. Het rapport is geen rechtstreekse validatie voor SWAP5 of voor een Nederlands nationaal schadepercentage.

De andere broncontroles staan in documenten 90–93. Er zijn in deze sessie **geen SWAP-runs uitgevoerd**, geen bodemfysische parameters geaccepteerd en geen canonical `evidence/*.csv` bestanden aangepast. Het doel is eerst een toetsbare specificatie voor de eerste modelproef vast te leggen.
