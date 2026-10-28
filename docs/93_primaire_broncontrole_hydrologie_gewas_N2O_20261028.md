# Primaire broncontrole: hydrologie, suikerbieten, emissies en aardappelen

**28 oktober 2026 | DEEP_SOURCE_CHECK_01 | expliciet beperkt tot vijf primaire documenten.**

Voortbouwend op [intake 90](90_teams_literatuur_intake_20261028.md), [triage 91](91_teams_literatuur_bronreview_ronde1_20261028.md) en [triage 92](92_teams_literatuur_ronde2_en_defra_methodetoets_20261028.md). Dit document bevat opnieuw nagelezen concrete bronpassages met **PDF-paginanummers (1-gebaseerd in aangeleverde bestanden)**. Geen nieuwe canonieke evidence admission en geen automatische Nederlandse modelparameters.

## Bronnen en controleerbare bevindingen

### 1. Nederlandse hydrologie, WENR rapport 2811, `literatuur/water/effecten_van_verbetering_bodemkwaliteit_op_waterh-wageningen_university_and_research_418283.pdf`

- **PDF p. 11:** de samenvatting stelt dat bodemverbetering de waterretentie kan vergroten en droogtegevoeligheid en oppervlakkige afstroming kan verminderen. De *uit- en afspoeling van stikstof en fosfaat* wordt daar expliciet als onduidelijk en soms tegenstrijdig omschreven. Het is bovendien een gecombineerde ingreep (verdichting opheffen **én** organische stof verhogen), niet een geïsoleerde compaction effectmeting. **V04–V07, V11, V17, V30–V35**: relevant voor mechanisme, niet voor toerekening aan verdichting alleen.
- **PDF p. 23:** veldwerk 2014–2015 op 12 melkveebedrijven in Liemers-Achterhoek, profielkuilen en bodemfysische metingen, vooral podzol/dekzand onder grasland; midden versus kopakker en in een deel ook onbereden perceelsrand. Dit is een contextgebonden steekproef, geen nationaal representatieve prevalentiemeting.
- **PDF p. 31:** modelstudie: grotere infiltratie bij verbeterde bodem maar geen universele kritische bui; antecedente natheid is belangrijk, en ook een goed doorlatende bodem kan bij zware buien runoff genereren. **V11–V16**: gebeurtenis- en contextafhankelijk.
- **PDF p. 75:** drie voorgestelde routes om verdichte laag in SWAP te parametriseren; per laag afzonderlijke Mualem–Van Genuchten-retentie- en doorlatendheidsparameters. Genoemde SWAP-symbolen: `ORES, OSAT, ALFAD, NPAR, LEXP, KSAT`. **Concreet nut:** hulpmiddel voor de te ontwerpen matched profielen. **Niet:** een complete, reeds gevalideerde omzettingsfunctie bulkdichtheid → hydrauliek voor alle Nederlandse bodemtypen.
- **PDF p. 76:** oude literatuur-/expertopvatting dat verdichting in veen niet relevant zou zijn, wordt als persoonlijke mededeling weergegeven. Dit is **geen bewijs** dat moderne intensieve berijding van veen geen blijvende effecten heeft. Het vormt juist een onderzoeksmotief om veen apart te behandelen.

### 2. Nederlandse bieten, Hanse-dissertatie, `literatuur/opbrengstreductie/bieten/hanse.pdf`

- **PDF p. 76, hoofdstuk 4 abstract:** vergelijking van 26 ‘top’ en 26 ‘gemiddelde’ bietenbedrijven, per paar nabij gelegen met gelijk bodemtype, gegevens 2006–2007. ‘Top’ had 20% hogere suikeropbrengsten (P < 0,001); dit is **geen compaction-schadepercentage**, omdat meerdere factoren verschillen.
- In de ondergrond was de gemiddelde verzadigde hydraulische geleidbaarheid **0,49 versus 0,31 m/dag**, respectievelijk top- en gemiddelde groep. Bij 34% versus 27% van de velden lag Ks onder de in de studie genoemde drempel van 0,10 m/dag; deze cijfers zijn geen nationale prevalentie van ondergrondverdichting.
- De tekst meldt **24,9% verklaarde variantie van suikeropbrengst** via een regressiemodel met ondergrond-Ks en luchtgevulde porositeit van de bovengrond; **niet** 24,9% opbrengstverlies, en **niet** uitsluitend een ondergrondverdichtingsverband. Bodemtextuur, zaaitijd en bedrijfsverschillen zijn relevant.
- **Koppeling:** V02, V04–V07 en de on-site kalibratie/plausibiliteit. Geen direct bruikbare nationale schadecoëfficiënt. Nader te doen: methode/regressietabel, controlevragen en causale identificatie volledig uitwerken.

### 3. Franse N₂O-veldproef, Bessou et al. (2010), `literatuur/greenhouse gasses/European J Soil Science - 2010 - Bessou - Modelling soil compaction impacts on nitrous oxide emissions in arable fields.pdf`

- **PDF p. 1 (abstract):** twee suikerbietengroeiseizoenen; geobserveerde cumulatieve emissies in niet-verdichte behandeling **944 en 977 g N/ha**, tegenover **1448 en 1382 g N/ha** in verdichte behandeling (2007, 2008). Het gaat om *N₂O-N* en een specifiek Frans proefontwerp, geen nationale jaaremissiefactor. De verschilwaarden zijn respectievelijk **504 en 405 g N/ha per gewascyclus**, niet per kalenderjaar.
- **PDF p. 2–3:** automatische kamers en quasi-continue metingen; bodemvocht en temperatuur gemonitord op 10 en 20 cm. Dit ondersteunt de noodzaak van gebeurtenis-/tijdresolutie en contextvariabelen, maar kwalificeert nog niet specifiek verdichting op 30–100 cm.
- **PDF p. 6:** NOE/NOE2-modelparameters, met gekalibreerde empirische responsfuncties. Modelovereenkomst met proeven is niet automatisch validatie voor andere bodems.
- **Koppeling:** V23–V27. **Voorwaardelijke kwantitatieve benchmark**, niet direct als Nederlands ondergrond-effect toelaten.

### 4. Review over N₂O, Pulido-Moncada, Petersen & Munkholm (2022), `literatuur/greenhouse gasses/pulido-moncada 2022.pdf`

- **PDF p. 1 (abstract):** meldt voor **bovengrondverdichting** een reeks relatieve N₂O-factoren 1,3–42 tussen onderzochte situaties en stelt expliciet dat weinig bekend is over de bijdrage van **ondergrondverdichting**.
- **Koppeling:** V23–V27 als mechanistische achtergrond. **Hard uitsluiten** als rechtstreeks te gebruiken emissiemultiplicator voor Nederlandse ondergrondverdichting.

### 5. Wisconsin aardappelproeven, Copas et al. (2009), `literatuur/opbrengstreductie/aardappelen/Agronomy Journal - 2009 - Copas - Potato Yield and Quality Response to Subsoil Tillage and Compaction.pdf`

- **PDF p. 1:** historische beschrijving van compactielaag op circa 22–23 cm onder het oppervlak, 5–20 cm dik. Geen directe representatieve Nederlandse ‘30–100 cm’-behandeling.
- **PDF p. 7–8:** in de onderzochte irrigatiecontext leidde ondergrondbewerking niet tot hogere **verhandelbare totaalopbrengst**, maar soms wel tot grotere knollen en daarmee mogelijk hogere opbrengstprijs. Een agronomisch kwaliteitseffect is niet hetzelfde als een productiemassa-effect.
- **Koppeling:** V03–V07; nuttige tegenproef tegen universeel opbrengstverlies. Niet gebruiken als bewijs dat verdichting geen opbrengstderving veroorzaakt in andere bodems/jaren.

## Wetenschappelijke implicaties

1. **Koppeling bulkdichtheid → SWAP-parameter:** WENR 2811 beschrijft alternatieve parametrisatiepaden, maar valideert geen universele functie. Toets of bestaande bodemprofielen reeds compactie bevatten, en houd bodemlaagdiepte/onderrand expliciet.
2. **Opbrengst:** Hanse toont bodemfysische associatie mét sterk concurrerende verklaringen; Copas toont in een bepaalde irrigatiecontext geen algemene opbrengstreactie. Beide voorkomen dat een extreme proefwaarde als gemiddeld gewasverlies wordt aangenomen.
3. **N₂O:** Deense review en Franse proef ondersteunen mechanistische relevantie en mogelijke grote lokale respons, maar leveren geen uitwisselbare ondergrondcoëfficiënt.
4. **Waterkwaliteit:** watertransport is gemeenschappelijke drijver, maar veranderingen in N/P-uitspoeling kunnen tegengesteld zijn en zijn niet alleen uit een runoffverschil af te leiden.
5. **Veen:** een oudere deskundigenopmerking is geen empirische uitsluiting. Organische bodems vragen afzonderlijke meet- en classificatiesystematiek.

## Kwalificatieniveau

**SOURCE_CHECKED_CONTEXT_AND_SELECTED_RESULTS** voor deze vijf primaire werken, met bovenstaande paginaprecisie. Dit is niet gelijk aan **ADMITTED_FOR_NL_MONETARY_CALCULATION**. Voor kwantitatieve toelating ontbreken per bron nog onder meer alle methodedetails, statistische onzekerheidsgrenzen, expliciete referentieprotocollen en validatie van de overdraagbaarheid naar de Nederlandse huidige verdichtingsklassen.

**Registratiebeleid:** bestaande `evidence/sources.csv`, `evidence/evidence_register.csv`, `evidence/claims.csv` en `evidence/qualification_register.csv` blijven intact; gebruik deze notitie als ondersteunende controle totdat formele bron-evidence-claim-review-records volledig zijn gecontroleerd.
