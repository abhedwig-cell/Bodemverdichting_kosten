# Projecthandover en vervolgroute — kosten van bodemverdichting

Status: **WORKING CANONICAL HANDOVER v0.1**  
Doelgroep: projectcollega's die de ontwikkeling niet dagelijks hebben gevolgd  
Canonieke start voor deze versie: `main @ 621b6d487f721e0bbb83616540d51542d7f1b53e`  
Doel: uitleggen **wat we proberen te bereiken, hoe we willen werken, wat al is opgebouwd en hoe het project verantwoord kan worden voortgezet**.

> Dit document is nadrukkelijk geen samenvatting van alleen de Tollebeek- of SWAP-lijn. Het beschrijft de bredere projectlogica. Tollebeek en procesmodellering zijn mogelijke verdiepingsroutes binnen dat raamwerk.

---

## 1. De kernvraag

Het project probeert een wetenschappelijk verdedigbaar beeld te geven van de **gevolgen en kosten van bodemverdichting voor landbouw en maatschappij**.

De ambitie is daarbij niet om voor elk denkbaar effect een maximaal gedetailleerd model te bouwen. De oorspronkelijke en nog steeds leidende gedachte is juist:

> **gebruik zo veel mogelijk bestaande kennis en data, reken zo weinig als nodig, maar maak de causale redenering, toepasselijkheid en onzekerheid volledig zichtbaar.**

Het einddoel is dus niet één zo precies mogelijk ogend eurobedrag. Het doel is een transparante keten waarin zichtbaar blijft:

- welke fysieke toestand of blootstelling we bedoelen;
- welk effect daar volgens metingen, literatuur of berekening bij hoort;
- welk deel daarvan aan bodemverdichting kan worden toegeschreven;
- wie of welk systeem het effect ondervindt;
- hoe het effect eventueel naar een andere schaal of receptor wordt overgedragen;
- hoe en onder welke economische definitie het wordt gemonetariseerd;
- welke onzekerheid en overdraagbaarheidsbeperkingen in elke schakel zitten.

Een bruikbare uitkomst kan daarom ook een **bandbreedte**, een **ensemble van bronnen** of een **partieel gemonetariseerde keten** zijn. Niet ieder kennisgat hoeft met extra rekenwerk te worden dichtgemaakt.

---

## 2. Leidende werkwijze: minimum necessary computation

De projectmethode kan worden samengevat als een escalatieladder.

### Niveau 1 — Conceptueel begrijpen

Eerst wordt vastgesteld welke causale route plausibel en relevant is.

Vragen zijn bijvoorbeeld:

- wat verandert bodemverdichting fysiek in de bodem?
- welke on-site gevolgen kunnen daaruit volgen?
- welke off-site gevolgen kunnen buiten het perceel ontstaan?
- waar zit een daadwerkelijke receptor of kostendrager?
- welke stap is nodig om van een fysiek effect naar geld te gaan?

Op dit niveau is een helder conceptueel model belangrijker dan rekenen.

### Niveau 2 — Bestaande evidence benutten

Vervolgens wordt gezocht naar bestaande informatie die een of meer schakels direct kan invullen:

- peer-reviewed literatuur;
- Nederlandse en internationale technische rapporten;
- bestaande veldproeven;
- administratieve en ruimtelijke data;
- bestaande modelstudies;
- landbouw-economische bronnen;
- beheer- en operationele gegevens.

Wanneer een goede studie reeds een relevante relatie kwantificeert, hoeft die relatie niet opnieuw te worden gesimuleerd.

### Niveau 3 — Eenvoudig rekenen

Waar nodig gebruiken we eenvoudige, controleerbare relaties:

- oppervlakte × effect;
- frequentie × gevolg;
- prijs × productieverlies;
- waterdiepte × areaal;
- energie- of kostenidentiteiten;
- low/base/high-scenario's;
- transparante aggregatie.

### Niveau 4 — Onzekerheid en gevoeligheid

Voordat zwaarder wordt gemodelleerd, wordt gekeken of de beslisrelevante onzekerheid al voldoende kan worden beschreven met:

- bronspreiding;
- gerapporteerde onzekerheidsintervallen;
- low/base/high;
- scenario's;
- alternatieve toepasselijkheidskeuzes;
- gevoeligheidsanalyse.

### Niveau 5 — Alleen indien nodig: procesmodellering

Een gedetailleerd procesmodel wordt pas ingezet wanneer een belangrijke schakel niet voldoende door bestaande evidence of eenvoudige berekening kan worden begrensd en wanneer verdere detaillering de uiteindelijke effect- of kosteninschatting werkelijk kan verbeteren.

SWAP kan daarom later een waardevol instrument zijn, maar is **geen verplichte tussenstap** in de algemene projectmethode.

---

## 3. De causale keten als referentiekader

De volledige keten blijft zichtbaar, ook wanneer we met literatuurevidence één of meer tussenstappen kunnen overslaan.

De gemeenschappelijke stam is:

```text
bodemverdichting / bodemtoestand
        ↓
verandering in bodemfunctie
        ↓
fysieke of biologische respons
        ↓
attributie aan bodemverdichting
```

Vanaf daar lopen ten minste twee hoofdroutes.

### 3.1 On-site route

```text
bodemverdichting
  → bodemstructuur / beworteling / water / lucht
  → gewas- of bedrijfsrespons
  → opbrengst, kwaliteit, beregening, bewerking of andere bedrijfsgevolgen
  → private fysieke/economische schade
  → eventuele maatschappelijke waardering
```

Voorbeelden van potentiële on-site effecten:

- opbrengstverlies;
- kwaliteitsverlies;
- droogtestress;
- wateroverlast;
- extra beregeningsbehoefte;
- extra of moeilijkere veldbewerkingen;
- verandering van kosten of marge.

### 3.2 Off-site route

```text
bodemverdichting
  → verandering in infiltratie / opslag / drainage / afstroming / stofstromen
  → overdracht buiten het perceel
  → receptor of beheerd systeem
  → operationeel, fysiek of maatschappelijk gevolg
  → publieke kosten en/of maatschappelijke waardering
```

Voor water kan dat bijvoorbeeld zijn:

```text
extra of anders getimede perceelsrespons
  → veldrand / drainage / sloot
  → netwerk / peilgebied
  → gemaal of andere beheermaatregel
  → energie, capaciteit, beheerlast of risico
  → economische waardering
```

Andere off-site routes, bijvoorbeeld nutriënten of andere ecosysteemdiensten, kunnen later volgens dezelfde logica worden uitgewerkt maar hebben hun eigen evidence- en waarderingsketen nodig.

### 3.3 On-site en off-site zijn gekoppeld

Beide routes beginnen bij dezelfde bodemtoestand en kunnen dezelfde fysieke processen delen. Ze moeten daarom niet als twee onafhankelijke modellen worden behandeld.

Een verandering in infiltratie en wortelzone-opslag kan tegelijk effect hebben op:

- gewasstress en opbrengst;
- beregeningsvraag;
- drainage;
- oppervlakkige afstroming;
- timing van waterafvoer.

De routes mogen daarna wel verschillend worden gekwantificeerd en gemonetariseerd.

---

## 4. Empirische verkorting van de keten

Een belangrijk projectprincipe is dat de causale keten **conceptueel volledig** blijft, maar niet altijd volledig hoeft te worden doorgerekend.

Wanneer een voldoende relevante studie bijvoorbeeld rechtstreeks een opbrengsteffect van bodemverdichting rapporteert, kan de on-site route worden verkort tot:

```text
verdichting
  → [gekwalificeerde empirische effectrelatie]
  → opbrengstverlies
  → economische waardering
```

We hoeven dan niet eerst alle tussenliggende bodemfysische en hydrologische processen opnieuw te simuleren.

Dit noemen we hier een **empirische verkorting** of **evidence shortcut**.

Een evidence shortcut is alleen verantwoord wanneer expliciet wordt vastgelegd:

- welke tussenstappen conceptueel worden overgeslagen;
- welke bron de directe relatie ondersteunt;
- voor welke bodem, gewas, klimaat, belasting en schaal de bron geldt;
- welke referentietoestand in de studie is gebruikt;
- of het een directe meting, modelresultaat, benchmark of proxy is;
- welke onzekerheid de bron zelf rapporteert;
- hoe overdraagbaar de relatie naar de Nederlandse toepassing is;
- welk gebruik wel en niet is toegestaan.

Een shortcut is dus niet hetzelfde als een ongedocumenteerde aanname.

---

## 5. Evidence kan meerdere routes tegelijk ondersteunen

Het project heeft al een expliciete evidence-architectuur:

```text
Source
  ↓
Evidence item
  ↓
Project claim
  ↓
Qualification for intended use
  ↓
Allowed use in calculation / reporting
```

De canonieke registers staan onder:

- `evidence/sources.csv`;
- `evidence/evidence_register.csv`;
- `evidence/claims.csv`;
- `evidence/qualification_register.csv`.

Belangrijk is dat een bron niet één universele kwaliteitsscore krijgt. Dezelfde bron kan:

- sterk zijn voor mechanistische kennis;
- bruikbaar zijn als orde-groottebenchmark;
- beperkt overdraagbaar zijn als Nederlandse parameter;
- ongeschikt zijn voor directe monetarisering.

Dat onderscheid is essentieel voor het gebruik van literatuur als directe rekenbron.

---

## 6. Onzekerheid is onderdeel van de architectuur

Onzekerheidsanalyse wordt niet pas aan het eind toegevoegd.

Voor iedere schakel wordt bijgehouden waar onzekerheid vandaan komt.

### 6.1 Onzekerheid binnen een bron

Een publicatie kan zelf een bandbreedte, standaardfout, confidence interval, scenario-range of gevoeligheidsrange geven.

Deze informatie moet worden behouden en niet vervangen door alleen een centraal getal.

### 6.2 Spreiding tussen bronnen

Meerdere relevante studies kunnen verschillende effecten geven.

Dat verschil kan ontstaan door:

- bodemtype;
- gewas;
- vochtregime;
- verdichtingsniveau;
- machinebelasting;
- referentietoestand;
- tijdschaal;
- geografische context;
- meet- of modelmethode.

Wanneer meerdere bronnen voldoende relevant zijn, kan een **evidence ensemble** worden gebruikt.

Het project hoeft dan niet automatisch één "beste" bron te kiezen of alle bronnen statistisch te middelen. Eerst wordt zichtbaar gemaakt:

- welke bronnen vergelijkbaar genoeg zijn;
- welke verschillen inhoudelijk verklaarbaar zijn;
- welke bandbreedte of set van uitkomsten zij samen ondersteunen.

### 6.3 Structurele onzekerheid

Soms bestaan er verschillende geldige routes door de causale keten.

Bijvoorbeeld:

```text
Route A: directe veldstudie → opbrengstverlies
Route B: bodemtoestand → waterstress → opbrengstverlies
Route C: historische economische benchmark
```

De uitkomsten kunnen naast elkaar worden gehouden zolang hun betekenis en toepasselijkheid duidelijk zijn.

### 6.4 Propagatie

De vroege workbookarchitectuur ondersteunt reeds:

- `value_low`;
- `value_base`;
- `value_high`;
- onzekerheid per parameter;
- scenario's;
- voorbereiding op kansverdelingen / Monte Carlo.

Een latere Monte-Carlo-analyse kan nuttig worden, maar is geen doel op zichzelf. Eerst moet de inhoudelijke onzekerheidsstructuur kloppen.

### 6.5 Resultaatvorm

Het gewenste eindproduct hoeft daarom niet altijd te zijn:

> kosten = €X

Een wetenschappelijk sterkere uitkomst kan zijn:

> Voor deze route ondersteunen toepasbare bronnen een effect van X–Y. Onder de gekozen Nederlandse exposure en waardering resulteert dat in €A–€B. De spreiding wordt vooral bepaald door schakel P en Q.

---

## 7. Wat er al is opgebouwd

### 7.1 Brede literatuur- en evidencebasis

In de eerdere projectfase is een uitgebreide workbooklijn opgebouwd waarin literatuur, effectrelaties, kosteninformatie, toepasselijkheid en metadata zijn vastgelegd.

De momenteel teruggevonden ontwikkellijn omvat onder meer:

- `Bodemverdichting_Cost_Framework_v0_3.xlsx`;
- `v0_4`, `v0_5`, `v0_8`;
- `v1_1_Dashboard`;
- `v1_2_Dashboard_Backend`;
- `v1_8_MeetingAligned`;
- `v2_6_AssoulineBridge`;
- `v2_7_PTFValidation`.

De workbooks vormen belangrijke **design- en evidencegeschiedenis**. Ze zijn niet automatisch canonieke einddatabases, maar bevatten veel inhoud die in de verdere projectontwikkeling moet worden behouden.

### 7.2 Wat in v2.7 expliciet aanwezig is

De v2.7-lijn bevat onder andere:

- variabelen en definities;
- regels en rule inputs/outputs;
- parameters met ranges en onzekerheid;
- evidence met schaal en overdraagbaarheid;
- applicability per bodem, landgebruik, watersysteem en regio;
- knowledge gaps;
- low/base/high;
- scenario's;
- on-site evidence;
- off-site scaling;
- crop-specific damage and valuation;
- cost accounting en dubbeltelchecks;
- result views per kostendrager;
- provenance en bronlocators;
- file manifests / hashes;
- source → claim → result lineage;
- Tollebeek als latere pilot;
- een expliciete engine die ontbrekende input niet automatisch als nul behandelt.

### 7.3 Voorbeelden van reeds vastgelegde evidence

De vroege evidencebasis bevat bijvoorbeeld:

- Nederlandse en internationale veldstudies naar opbrengstverandering;
- studies naar bodemfysische/hydrologische respons;
- historische Nederlandse economische benchmarks;
- Europese economische/scenariovergelijkingen;
- kengetallen voor waterbeschikbaarheid en waardering;
- metadata over directness, schaal, transferability en allowed use.

Voorbeelden moeten altijd met hun status worden gelezen. Een historisch of internationaal getal kan nuttig zijn als benchmark zonder dat het een Nederlandse actuele parameter wordt.

### 7.4 Canonieke theorie/evidence die al naar GitHub is gemigreerd

Een deel van die brede basis is al genormaliseerd in de huidige repository.

Belangrijke bronnen zijn bijvoorbeeld:

- Keller et al. 2019 — mechanistische en synthese-evidence;
- Graves et al. 2015 — on-site/off-site en economische/ecosysteemdienst-architectuur;
- Groenendijk et al. 2017 — Nederlandse hydrologische en profielgevoeligheid;
- Kuhlman et al. 2010 — historische Nederlandse economische context;
- Romero-Ruiz et al. 2026 — multi-service en Europees scenarioframe.

Zie `docs/16_theory_evidence_baseline_v0_1.md` voor de huidige gekwalificeerde theoretische baseline.

---

## 8. Wat de vroege workbooks ons methodisch al leren

De oude workbooklijn bevat een aantal ontwerpkeuzes die behouden moeten blijven.

### 8.1 Geen geforceerde euro-uitkomst

Als een belangrijke schakel ontbreekt, blijft die leeg of geblokkeerd.

Een onvolledige keten wordt niet met een convenience default gesloten.

### 8.2 Fysieke effecten en monetarisering zijn verschillende regels

Een opbrengstverlies, extra wateraanvoer of extra pompvolume is nog geen economische schade totdat een expliciete waarderingsrelatie wordt toegepast.

### 8.3 Geldigheid en broncontext horen bij het getal

Een effectcoëfficiënt zonder bodem-, gewas-, tijd-, regio- en referentiecontext is onvoldoende.

### 8.4 Crop refinement kan noodzakelijk zijn

Een brede klasse "akkerbouw" kan bruikbaar zijn voor exposure, maar is vaak te grof voor monetarisering.

Productiewaarde en gevoeligheid verschillen sterk tussen gewassen. De vroege lijn koos daarom voor rekenen op bodem × gewas en pas daarna aggregeren.

### 8.5 Private, publieke en maatschappelijke kosten blijven gescheiden

Minimaal onderscheiden we:

- private/farm cost;
- public-budget expenditure;
- societal-welfare effect.

Deze mogen niet zonder dubbeltelreview tot één totaal worden opgeteld.

---

## 9. Huidige balans tussen on-site en off-site

Conceptueel zijn beide routes onderdeel van de projectbasis, maar ze zijn tot nu toe niet even ver uitgewerkt.

### On-site

De vroege workbooks bevatten relatief veel:

- opbrengstevidence;
- crop refinement;
- private-damage methoden;
- landbouw-economische databronnen;
- yield-loss × production-value routes;
- eerste cases voor gras, maïs en akkerbouw.

De canonieke GitHub-documentatie heeft deze lijn later minder ver gemigreerd dan de off-site waterlijn.

### Off-site

De latere Tollebeek-lijn heeft de waterroute veel verder technisch en evidence-matig uitgewerkt:

- transfer tussen perceel en watersysteem;
- routingsemantiek;
- gemaalcapaciteit;
- dispatch;
- energie;
- historische managed boundary;
- drainage;
- event forcing.

Daardoor kan de huidige repository de indruk geven dat deze off-site route de hoofdroute is. Dat is niet de bedoeling.

**Voor het vervolg moeten on-site en off-site weer als evenwaardige hoofdtakken worden behandeld.**

---

## 10. De rol van Tollebeek

Tollebeek OT.02 is een **pilot en reality check**, niet de definitie van het project.

De pilot is nuttig omdat een echte locatie dwingt om vragen over:

- ruimtelijke schaal;
- bodemtoestand;
- landgebruik;
- drainage;
- transfer;
- operationeel waterbeheer;
- bronkwaliteit

concreet te maken.

De Tollebeek-lijn heeft daardoor waardevolle governance, data-acquisitie en modelstructuur opgeleverd.

Maar de pilot moet niet de volgorde omdraaien. We hoeven niet eerst iedere ontbrekende Tollebeek-modelparameter te reconstrueren voordat bredere on-site of off-site kostenroutes kunnen worden beoordeeld.

---

## 11. De rol van SWAP en andere procesmodellen

SWAP kan later op meerdere manieren nuttig zijn:

- wanneer literatuurrelaties te grof zijn;
- wanneer bodemtype en hydrologische context sterk bepalend zijn;
- om alternatieve current/reference bodemtoestanden fysisch consistent te vergelijken;
- om een belangrijke onzekerheid rond waterbalans, stress of runoff te begrenzen;
- om eenvoudige relaties te testen of te ondersteunen.

Het reeds verrichte SWAP5-voorbereidingswerk is daarom **niet verloren**.

Wel geldt:

> een SWAP-run is een mogelijke evidence-/rekenroute, niet het standaardpad waar iedere kostenketen doorheen moet.

Hetzelfde geldt voor andere procesmodellen.

---

## 12. Voorgestelde vervolgstrategie

Voor de eerstvolgende projectfase is de meest productieve volgorde:

### Stap A — Maak de twee effectbomen compleet

Voor on-site en off-site afzonderlijk:

- eindpunten;
- tussenmechanismen;
- kostendragers;
- waarderingsconcepten;
- mogelijke empirische shortcuts.

### Stap B — Koppel bestaande evidence aan iedere schakel

Gebruik:

- huidige GitHub evidence registers;
- teruggevonden workbookliteratuur;
- aanvullende literatuur alleen waar echte gaten bestaan.

Per bron vastleggen:

- context;
- effect;
- low/base/high of eigen onzekerheid;
- directness;
- applicability;
- allowed use.

### Stap C — Vorm evidence ensembles waar zinvol

Voor iedere relevante effectroute bepalen:

- is er één sterke bron?
- zijn er meerdere vergelijkbare bronnen?
- is de bronspreiding een zinvolle onzekerheidsband?
- zijn de studies te verschillend en moeten zij als aparte scenario's blijven?

### Stap D — Identificeer de goedkoopste verdedigbare berekening

Per route:

1. directe empirische relatie;
2. simpele rekenregel;
3. gevoeligheids-/scenarioanalyse;
4. procesmodel alleen indien nodig.

### Stap E — Monetariseer pas na fysieke/economische scopecheck

Controleer:

- receptor/kostendrager;
- prijsjaar;
- vermeden kosten;
- dubbeltelling;
- transfer payments versus welfare loss;
- ruimtelijke en temporele schaal.

### Stap F — Rapporteer resultaat én kennisgat

Een route die niet volledig kan worden gemonetariseerd kan nog steeds een belangrijk projectresultaat opleveren:

- fysieke bandbreedte;
- benchmark;
- scenario;
- dominant kennisgat;
- waarde van aanvullende data of modellering.

---


## 12A. Praktisch werkinstrument: effect-pathway matrix

De brede filosofie uit dit document is uitgewerkt in:

- `docs/49_project_effect_pathway_matrix_v0_1.md`;
- `evidence/effect_pathway_matrix_v0_1.csv`.

Die matrix is het aanbevolen werkoppervlak voor de volgende inhoudelijke fase. Per on-site en off-site route legt zij vast:

- de volledige causale keten;
- reeds beschikbare evidence;
- bron- en transferonzekerheid;
- mogelijke empirische verkorting;
- monetariseringsroute;
- huidig verdict;
- de lichtste volgende actie;
- expliciete verboden shortcuts.

De matrix is geen verzameling centrale schadecoëfficiënten. Zij is juist bedoeld om zichtbaar te maken wanneer meerdere bronnen als ensemble of scenario naast elkaar moeten blijven staan.

## 13. Praktische overname voor een nieuwe collega

Een collega die vanaf hier instapt hoeft niet de volledige commitgeschiedenis te reconstrueren.

### Eerst lezen

1. dit document;
2. `docs/01_overview.md`;
3. `docs/02_theoretical_framework.md`;
4. `docs/16_theory_evidence_baseline_v0_1.md`;
5. `docs/07_evidence_and_qualification.md`.

### Daarna bekijken

- `evidence/sources.csv`;
- `evidence/evidence_register.csv`;
- `evidence/claims.csv`;
- `evidence/qualification_register.csv`;
- de oude v2.7-workbook als brede design/evidencebron;
- Tollebeek-documenten alleen wanneer aan de off-site/pilotlijn wordt gewerkt.

### Bij nieuw werk

Gebruik steeds dezelfde vragen:

1. Welke schakel in de keten proberen we in te vullen?
2. Is die schakel on-site, off-site of gemeenschappelijk?
3. Bestaat er al relevante evidence?
4. Kunnen we een empirische shortcut verantwoord gebruiken?
5. Welke onzekerheid zit in bron en transfer?
6. Hebben we echt extra rekenwerk nodig?
7. Wat is de lichtste verdedigbare methode?
8. Welke economische categorie wordt uiteindelijk geraakt?
9. Welke aannames mogen niet stilzwijgend worden gemaakt?
10. Wat moet in repository/evidence-register worden bijgewerkt?

---

## 14. Governance voor dit levende document

Dit document is bedoeld als **levend canoniek onboarding- en continuatiedocument**.

Het moet worden aangepast wanneer een wijziging materially verandert:

- de projectfilosofie;
- de on-site/off-site effectarchitectuur;
- de onzekerheidsmethode;
- de rol van literatuur/evidence shortcuts;
- de nationale schaalstrategie;
- de rol van pilots of procesmodellen;
- de aanbevolen vervolgroute.

Detailwijzigingen binnen één pilot horen primair in hun eigen werkdocumenten en hoeven dit document niet telkens te veranderen.

---

## 15. Kernboodschap in één alinea

Het project probeert de gevolgen en kosten van bodemverdichting te ramen door de volledige causale keten zichtbaar te houden, maar niet iedere schakel onnodig opnieuw te modelleren. Bestaande literatuur, metingen en administratieve data zijn primaire rekenbronnen wanneer hun toepasselijkheid voldoende kan worden onderbouwd. On-site en off-site effecten worden als twee gekoppelde maar afzonderlijk te waarderen routes behandeld. Meerdere bruikbare bronnen kunnen als evidence ensemble worden behouden; onzekerheid binnen bronnen, tussen bronnen en tussen alternatieve causaliteitsroutes blijft expliciet. Eenvoudige berekeningen hebben de voorkeur boven complexe modellen zolang zij de relevante orde van grootte en onzekerheid verantwoord kunnen beschrijven. Tollebeek en SWAP zijn waardevolle verdiepingsroutes, maar niet de kern of verplichte volgorde van het project.
