# Collega-reviewpakket — kosten van bodemverdichting

**Werkdocument voor inhoudelijke review — 18 september 2026**  
**Doelgroep:** collega die bij het initiële overleg betrokken was, maar de ontwikkeling daarna niet van dichtbij heeft gevolgd  
**Doel:** in korte tijd begrijpen wat we proberen te bouwen, waarom we het zo aanpakken, wat er al staat en waarop inhoudelijke tegenspraak of bijsturing gewenst is.

> Dit is geen eindrapport en geen verzoek om de bestaande uitwerking als gegeven te accepteren. Het is een uitnodiging om de kernlogica, de effectketens, de evidence-keuzes, de onzekerheidsbehandeling en de beoogde presentatie kritisch te beoordelen.

---

## 1. Waarom dit project anders is dan “maak een model en bereken de schade”

De centrale vraag is eenvoudig te formuleren:

> **Wat kost bodemverdichting de landbouw en de maatschappij?**

Maar die vraag wordt snel misleidend als we meteen naar één landelijk eurobedrag springen. Tussen “bodem is verdicht” en “dit kost €X” zitten meerdere inhoudelijk verschillende vragen:

1. Welke bodemtoestand bedoelen we precies?
2. Met welke relevante referentietoestand vergelijken we die?
3. Welke fysieke of biologische respons volgt uit dat verschil?
4. Welk deel daarvan is werkelijk aan bodemverdichting toe te schrijven?
5. Blijft het effect op het perceel of bereikt het een ander systeem of actor?
6. Welke economische betekenis heeft het effect?
7. Hoe zeker zijn al die schakels?

De oorspronkelijke projectgedachte — en nog steeds de leidende gedachte — is daarom niet om zo veel mogelijk te modelleren.

De ambitie is:

> **Gebruik bestaande kennis en data waar die goed genoeg zijn. Reken alleen wat nodig is. Houd de volledige causale keten zichtbaar. Laat onzekerheid en ontbrekende schakels expliciet staan.**

Een uitkomst mag dus zijn:

- een getal;
- een bandbreedte;
- een set scenario's;
- een evidence-ensemble;
- een fysieke uitkomst die nog niet gemonetariseerd kan worden;
- of expliciet: **nog niet verantwoord berekenbaar**.

Dat laatste is geen mislukking. Het voorkomt dat een ontbrekende schakel ongemerkt wordt vervangen door een convenience default.

---

## 2. De wetenschappelijke basis in één verhaal

### 2.1 Bodemverdichting is een toestand in een systeem

De gevolgen van bodemverdichting hangen niet alleen af van “hoe verdicht” een bodem is.

Ze hangen onder andere af van:

- bodemtype en profielopbouw;
- diepte en dikte van de restrictieve laag;
- vochttoestand;
- gewas en beworteling;
- weer en antecedente omstandigheden;
- grondwater en drainage;
- waterbeheer en ruimtelijke connectiviteit;
- economische receptor en gekozen waarderingsconcept.

Daarom behandelen we bodemverdichting niet als één universeel schadepercentage.

### 2.2 Current versus reference

Voor attributie is een vergelijking nodig tussen een huidige of onderzochte toestand en een relevante referentie.

Conceptueel:

```text
respons_current   = M(bodem_current, forcing, gewas, systeemcontext)
respons_reference = M(bodem_reference, forcing, gewas, systeemcontext)

toerekenbaar effect = respons_current - respons_reference
```

De kern zit in het woord **matched**: als tegelijk weer, gewas, drainage en waterbeheer veranderen, meten we niet meer alleen het effect van de bodemtoestand.

De referentie is bovendien contextafhankelijk. Dat kan een gemeten controle zijn, een minder verdichte toestand, een agronomisch verdedigbare referentie of een evidence-based counterfactual. Het is niet automatisch “onbereden”, “natuurlijk” of “nul verdichting”.

### 2.3 Eén bodemtoestand, twee hoofdroutes

Vanaf dezelfde bodemtoestand lopen twee gelijkwaardige effectketens.

#### On-site

```text
bodemverdichting
 → bodemstructuur / wortels / water / lucht
 → gewas- of bedrijfsrespons
 → opbrengst, kwaliteit, beregening, bewerking
 → private fysieke/economische gevolgen
 → eventuele bredere maatschappelijke waardering
```

#### Off-site

```text
bodemverdichting
 → infiltratie / opslag / drainage / afstroming / stofstromen
 → overdracht buiten het perceel
 → ontvangend watersysteem of andere receptor
 → operationeel / fysiek / maatschappelijk gevolg
 → publieke kosten en/of maatschappelijke waardering
```

De twee routes mogen daarna andere data en waarderingsmethoden gebruiken, maar ze mogen niet impliciet met twee verschillende fysische werkelijkheden werken.

### 2.4 Geld komt pas aan het einde van een gedefinieerde fysieke keten

Een fysiek effect is nog geen economische schade.

We houden daarom minimaal uit elkaar:

- **private kosten voor het bedrijf**;
- **publieke uitgaven**, bijvoorbeeld waterbeheer;
- **maatschappelijke welvaartseffecten**.

Een verloren brutoproductiewaarde is bijvoorbeeld niet automatisch gelijk aan private netto schade. En een publieke uitgave is niet automatisch een additioneel maatschappelijk welvaartsverlies.

---

## 3. Onze rekenstrategie: zo licht als kan, zo zwaar als nodig

De werkwijze is een escalatieladder.

### Stap 1 — Begrijp de causale route

Eerst bepalen:

- wat verandert er?
- welke receptor ondervindt dat?
- welke tussenstappen zijn werkelijk nodig?

### Stap 2 — Gebruik bestaande evidence

Daarna zoeken we of één of meer schakels al voldoende worden ingevuld door:

- peer-reviewed studies;
- Nederlandse veldproeven;
- technische rapporten;
- monitoringdata;
- administratieve en ruimtelijke data;
- bestaande modelstudies;
- landbouw-economische bronnen;
- operationele data.

Als een geschikte studie rechtstreeks een opbrengsteffect rapporteert, hoeven we niet per se eerst bodemfysica → waterbalans → gewasgroei opnieuw te simuleren.

### Stap 3 — Gebruik eenvoudige controleerbare relaties

Bijvoorbeeld:

```text
affected area × response × economische waarde
```

of:

```text
extra waterdiepte × areaal = extra volume
```

mits iedere factor inhoudelijk is gedefinieerd.

### Stap 4 — Breng onzekerheid expliciet in beeld

Voor we zwaarder modelleren, kijken we of de beslisrelevante onzekerheid al kan worden beschreven met:

- bronranges;
- low/base/high;
- scenario's;
- alternatieve referenties;
- gevoeligheidsanalyse;
- meerdere evidencebronnen naast elkaar.

### Stap 5 — Pas procesmodellering alleen toe als die informatiewinst oplevert

Een model zoals SWAP, WOFOST of een ander procesmodel is waardevol als:

- een cruciale schakel onvoldoende door data/literatuur kan worden begrensd;
- die onzekerheid de einduitkomst echt domineert;
- het model met voldoende gekwalificeerde input die onzekerheid kan verkleinen.

Procesmodellering is daarmee een **escalatieroute**, niet de ruggengraat waar iedere kostenketen verplicht doorheen moet.

---

## 4. Evidence: een bron is nog geen parameter

Een belangrijke ontwerpkeuze is dat we verschillende kennisstappen niet op één hoop gooien.

De keten is:

```text
Bron
  ↓
Evidence-item
  ↓
Projectclaim / interpretatie
  ↓
Beoordeling voor een specifiek gebruik
  ↓
Toegestane toepassing in berekening of dashboard
```

### Waarom dit belangrijk is

Een goede bron kan een betrouwbaar getal bevatten dat toch ongeschikt is voor onze huidige toepassing.

Voorbeelden:

- een historische Nederlandse schatting kan een nuttige benchmark zijn, maar geen actuele parameter;
- een modelstudie kan sterke mechanistische evidence geven, maar niet direct een nationale schadefactor;
- een waterpeil kan administratief exact bekend zijn, maar geen dynamische pompopvoerhoogte voorstellen;
- een bodemkaart kan geschikt zijn voor regionale classificatie, maar geen nieuwe perceelsmeting zijn.

### Belangrijke regels

- onbekend blijft leeg en wordt niet nul;
- een benchmark blijft zichtbaar een benchmark;
- context hoort bij het getal;
- de toegestane toepassing hoort bij de evidence;
- softwaretests bewijzen dat een berekening technisch klopt, niet dat de fysieke input waar is;
- een dashboardresultaat moet terug te leiden zijn naar de gebruikte bron, interpretatie en ontbrekende schakels.

---

## 5. Onzekerheid: meerdere bronnen zijn informatie, geen probleem dat direct moet worden gladgestreken

Voor verschillende routes bestaan meerdere relevante studies.

Die kunnen verschillen door:

- bodem;
- gewas;
- verdichtingsbehandeling;
- diepte;
- referentie;
- weer;
- tijdschaal;
- meet- of modelmethode;
- land of regio.

Daarom gebruiken we waar zinvol een **evidence-ensemble**.

Een bron kan daarin bijvoorbeeld fungeren als:

- directe kandidaat;
- proxy;
- bovengrens/ondergrens;
- scenario;
- benchmark;
- guardrail.

### Geen standaardgemiddelde

We middelen bronnen niet automatisch tot één “beste” factor.

De eerste verdedigbare uitkomst is eerder:

- een range;
- meerdere scenario's;
- een bounded ensemble;
- of de conclusie dat bronnen te verschillend zijn om numeriek te combineren.

### Drie soorten onzekerheid blijven zichtbaar

1. **Binnen-bron:** de range of onzekerheid die de studie zelf rapporteert.
2. **Tussen-bron:** verschil tussen studies en contexten.
3. **Structureel:** verschillende plausibele routes door de causale keten.

Dit is uiteindelijk ook hoe het dashboard onzekerheid moet tonen: niet alleen als één foutbalk, maar waar mogelijk als uitleg **waarom** de range ontstaat.

---

## 6. Het dashboard: niet alleen een presentatie, maar de zichtbare vorm van de methode

Er is al een interactief dashboardprototype gemaakt. De exacte cijfers/statussen in dat prototype zijn deels ingehaald door de verdere ontwikkeling; de schermen zijn daarom vooral belangrijk als **interface- en denkkader**.

De hoofdgedachte is dat een gebruiker nooit alleen een eindgetal ziet. Het dashboard moet hem kunnen laten bewegen van:

```text
resultaat
 → bodem / gewas / gebied
 → causale route
 → gebruikte regel
 → parameter/evidence
 → bron
 → onzekerheid / blocker
```

De beoogde hoofdschermen zijn:

- **Overzicht**
- **On-site**
- **case-schermen**
- **Off-site**
- **Kaart**
- **Provenance**

### 6.1 Overzicht — laat ook zien wat nog niet berekenbaar is

Het overzicht moet tegelijk laten zien:

- welke structurele basisdata gereed zijn;
- welke kostenresultaten al of nog niet verantwoord berekenbaar zijn;
- welke inputlagen de bottleneck vormen;
- welke cases het meest kansrijk zijn.

Een rode of lege KPI is dus bewust onderdeel van de informatiearchitectuur. Het dashboard mag geen getal fabriceren om “compleet” te ogen.

**Gedachte achter het scherm:** voortgang en onzekerheid zijn zelf projectresultaten.

### 6.2 On-site — rekenen per betekenisvolle bodem × gewas-context

De eenvoudige rekenvorm is:

```text
kosten =
  relevant areaal
  × actuele verdichtingsexposure
  × gekwalificeerde gewasrespons
  × expliciete economische waarde
```

Maar ieder van die termen heeft context.

Voor akkerbouw betekent dit bijvoorbeeld dat “akkerbouw op zand” niet automatisch gelijk is aan “snijmaïs op zand”. Daarom wordt de gewasmix eerst verfijnd en pas daarna gemonetariseerd.

**Gedachte achter het scherm:** nationale aggregatie komt ná de inhoudelijk relevante segmentatie, niet ervoor.

### 6.3 Case-schermen — toon bewijs en blocker tegelijk

Voor bijvoorbeeld grasland op zand/eerd zijn al relevante Nederlandse studies beschikbaar.

Een goed case-scherm laat dan naast elkaar zien:

- structureel areaal;
- literatuur-/modeleffecten;
- bronstatus;
- hydrologische context;
- ontbrekende actuele exposure;
- ontbrekende waarderingsinput;
- wat wel en niet uit de evidence mag worden afgeleid.

**Gedachte achter het scherm:** een sterke deelketen mag zichtbaar worden zonder te suggereren dat de nationale eindraming al bestaat.

### 6.4 Off-site — de schaalovergang is een eigen wetenschappelijke stap

Voor water is de route niet:

```text
extra runoff op perceel = extra schade in watersysteem
```

maar bijvoorbeeld:

```text
perceelrespons
 → veldrand / drain
 → sloot / lokaal netwerk
 → buffering en timing
 → beheerobject / receptor
 → operationeel of risico-effect
 → waardering
```

**Gedachte achter het scherm:** transfer/connectiviteit mag niet verdwijnen in één factor zonder onderbouwing.

De Tollebeek-pilot heeft hier veel nuttig denk- en ontwikkelwerk opgeleverd. Dat maakt Tollebeek een waardevolle reality check, maar niet de definitie van het hele project.

### 6.5 Kaart — dezelfde inhoud ruimtelijk, geen aparte waarheid

Het kaartscherm moet dezelfde berekende/evidence-state ruimtelijk ontsluiten.

Een kaartlaag mag pas worden gebruikt als:

- een ruimtelijke sleutel reproduceerbaar is;
- classificatie en jaar duidelijk zijn;
- niet-gemapte gebieden zichtbaar blijven;
- kaartresolutie niet wordt verward met meetnauwkeurigheid.

**Gedachte achter het scherm:** ruimtelijke visualisatie verandert de bewijsstatus niet.

### 6.6 Provenance — van dashboard terug naar bron

Voor iedere belangrijke KPI of case moet de gebruiker uiteindelijk kunnen zien:

- welke regel;
- welke input;
- welke bron;
- welke evidence-status;
- welke toepasselijkheidsbeoordeling;
- welke blocker;
- welke waarschuwing.

**Gedachte achter het scherm:** transparantie is niet een appendix achteraf; zij zit in de gebruikersinterface zelf.

---

## 7. Wat er inmiddels concreet is opgebouwd

### 7.1 Een brede literatuur- en evidencebasis

De eerdere workbooklijn bevat veel verzamelde en geordende literatuur, effectrelaties, economische informatie, metadata, ranges, applicability en knowledge gaps.

Die oudere workbooks zijn niet de bron van waarheid geworden, maar hun inhoud is niet weggegooid. Relevante onderdelen worden gecontroleerd naar de huidige canonieke evidence-laag gemigreerd.

### 7.2 Canonieke evidence-registers

De repository bevat nu machine-readable registers voor:

- bronnen;
- evidence-items;
- projectclaims;
- beoordelingen voor bedoeld gebruik;
- evidence-ensembles.

Hierdoor kunnen broncontext en toegestane toepassing naast het getal blijven bestaan.

### 7.3 De eerste on-site ensembles

Voor gras op zand en snijmaïs op zand is inmiddels oorspronkelijke Nederlandse evidence opnieuw teruggevonden en gecontroleerd gemigreerd.

Belangrijk resultaat:

- voor gras ondersteunt de evidence **geen universele monotone relatie** “meer verdichting = altijd meer opbrengstverlies”;
- voor maïs zijn materiële effecten aangetoond, maar sterk afhankelijk van behandeling, profiel en weer;
- droge jaren en langjarige gemiddelden moeten gescheiden blijven;
- historische nationale schattingen blijven benchmark/context en worden geen actuele coefficient.

Dat is inhoudelijk waardevol: het voorkomt dat een simpel gemiddeld schadepercentage de verschillende mechanismen maskeert.

### 7.4 Eerste bounded on-site calculation surface

Voor enkele prioritaire zandcontexten is een rekenoppervlak gemaakt dat expliciet vastlegt:

- areaal/context;
- crop share;
- verdichtingsexposure;
- response-ensemble;
- economische input;
- blocker;
- volgende actie.

Cruciaal: zolang een noodzakelijke term ontbreekt, kan het oppervlak **geen schade-uitkomst** genereren.

### 7.5 Actuele verdichtingsexposure blijft een kernblocker

De gepubliceerde CC-NL 2018-basis is nuttig als historische/structurele reporting-basis.

Voor een actuele nationale schaderaming is echter actuele exposure nodig met voldoende semantiek, minimaal passend bij:

- landgebruik/bodem;
- diepte;
- ernst/state.

Een headline percentage “verdicht areaal” is onvoldoende om rechtstreeks met een crop-damage coefficient te vermenigvuldigen.

### 7.6 Snijmaïs × bodem wordt reproduceerbaar gemaakt

Voor maïs is de parentklasse “akkerland” te grof.

Daarom is een reproduceerbare route ontworpen:

```text
BRP 2025 definitieve gewaspercelen
 ×
versioned BRO Bodemkaart
 →
maïsareaal per relevante bodemklasse
```

Daarbij gelden fail-closed regels:

- onbekende bodemcodes worden niet stil als “overig zand” toegewezen;
- officiële bodemfamilies kunnen voorstellen genereren;
- voorstellen worden nooit automatisch gekwalificeerd;
- iedere gebruikte mapping moet expliciet worden beoordeeld;
- ruimtelijke areaalclosure wordt gecontroleerd;
- de huidige BRO-kaart wordt niet voorgesteld als historische LSK-reconstructie.

Een uitvoerbare bronmaterialisatieroute is daarnaast voorbereid: ruwe BRP-responses en BRO-download worden vóór transformatie bewaard en gehasht.

### 7.7 Economische routes zijn onderscheiden, nog niet ingevuld met convenience values

Voor crop-specific waardering zijn onder andere KWIN en BINternet als routes geïdentificeerd.

Maar vóór invullen moet worden gekozen welke economische vraag wordt beantwoord:

- bruto opbrengstwaarde;
- marginale private boerenschade;
- productiewaarde;
- maatschappelijke welvaart.

Voor gras is bovendien een eigen voeder-/bedrijfseconomische interpretatie nodig; gras kan niet simpelweg als marktgewas met één prijs worden behandeld.

### 7.8 Off-site waterroute: conceptueel sterk, transfer blijft de sleutel

De off-site lijn is relatief ver uitgewerkt in termen van:

- onderscheid tussen perceelrespons en systeemrespons;
- connectiviteit;
- routing;
- gemalen en capaciteit;
- operationele data;
- energie- en kostenlogica.

Maar landelijke opschaling is nog niet gerechtvaardigd.

De volgende vraag is niet “kunnen we Tollebeek nog gedetailleerder modelleren?”, maar eerder:

> welke hydrologische systeemtypen en bestaande data/literatuur zijn voldoende om de nationale off-site bijdrage eerst eenvoudig te begrenzen?

---

## 8. De discipline achter de schermen

Hoewel de gebruiker uiteindelijk een dashboard of rapport ziet, proberen we de onderliggende kennisstructuur zo te organiseren dat een collega de redenering later kan reconstrueren.

De gewenste keten is:

```text
theorie / betekenis
 ↓
conceptueel model
 ↓
formele relatie of beslisregel
 ↓
data en context
 ↓
implementatie
 ↓
evidence en beoordeling
 ↓
dashboard / rapport
```

Daaruit volgen een paar praktische principes.

### Een getal zonder context is geen parameter

We willen waar relevant weten:

- betekenis;
- eenheid;
- schaal;
- tijd;
- bron;
- referentie;
- toegestane toepassing;
- onzekerheid;
- verboden interpretatie.

### Een wijziging kan doorwerken naar andere lagen

Als bijvoorbeeld de referentietoestand verandert, kan een eerder passende response-relatie opnieuw beoordeeld moeten worden.

Als alleen de dashboardlayout verandert, hoeft evidence niet opnieuw inhoudelijk te worden gekwalificeerd.

### Tests hebben een afgebakende betekenis

Softwaretests kunnen bewijzen dat:

```text
100 ha × 10 mm = 10.000 m³
```

correct is geïmplementeerd.

Ze bewijzen niet dat in werkelijkheid 10 mm extra runoff optreedt.

### De projectstate moet overdraagbaar zijn

Een nieuwe collega moet kunnen vaststellen:

- wat weten we?
- waarom denken we dat?
- wat gebruiken we waarvoor?
- wat weten we niet?
- wat is de kleinste logische volgende stap?

Dit is uiteindelijk belangrijker dan een “af” ogend spreadsheet.

---

## 9. Hoe ik de huidige projectstatus samenvat

### Wat volgens mij stevig staat

- de brede projectfilosofie;
- current/reference en causale attributie;
- het onderscheid state → response → transfer → valuation;
- on-site en off-site als gelijkwaardige hoofdtakken;
- evidence/provenance-architectuur;
- het principe van evidence shortcuts;
- evidence ensembles en expliciete onzekerheid;
- geen verborgen defaults;
- dashboard/provenance-concept;
- eerste concrete on-site cases en rekenoppervlak;
- reproduceerbare data-/GIS-route voor maïs;
- een sterke off-site pilotarchitectuur.

### Wat inhoudelijk nog openstaat

- actuele nationale verdichtingsexposure met voldoende diepte/ernst-semantiek;
- welke referentietoestanden per eerste on-site case het best verdedigbaar zijn;
- economische waardering per gewas/bedrijfsroute;
- bredere evidence voor crop quality en extra field operations;
- eenvoudige nationale off-site systeemtypologie;
- transfer/connectivity en timing/buffering voor off-site opschaling;
- omgang met dubbeltelling bij private, publieke en maatschappelijke kosten.

### Wat volgens mij nu níét de hoofdvraag is

- een groot nationaal procesmodel bouwen;
- alle Tollebeek-inputgaten sluiten voordat andere routes verder mogen;
- één universele schadefactor zoeken;
- een dashboard vullen met voorlopige eurobedragen omdat lege KPI's ongemakkelijk voelen.

---

## 10. Waar ik jouw review specifiek voor zou willen gebruiken

Ik zou jouw oordeel vooral willen op onderstaande punten.

### A. Klopt het fundamentele projectframe?

Is **minimum necessary computation** hier volgens jou de juiste strategie?

Of missen we daarmee een reden waarom een geïntegreerd procesmodel juist eerder nodig zou zijn?

### B. Zijn de effectketens compleet genoeg?

Vooral:

- on-site landbouw/bedrijf;
- off-site water;
- mogelijke overige maatschappelijke effecten.

Welke belangrijke receptor of kostenroute ontbreekt?

### C. Is de current/reference-benadering bruikbaar voor de onderzoeksvraag?

Waar moeten we volgens jou scherper zijn in de keuze van de referentie?

### D. Is de manier waarop we literatuur als shortcut gebruiken wetenschappelijk verdedigbaar?

Wanneer vind jij een directe empirische relatie sterk genoeg om een mechanistische tussenketen niet opnieuw door te rekenen?

### E. Is de uncertainty-/ensemble-aanpak goed?

Vind je het terecht dat we bronnen niet standaard middelen?

Welke soorten bronnen zouden volgens jou wél gezamenlijk tot één bandbreedte mogen leiden?

### F. Is de balans on-site / off-site goed hersteld?

De technische uitwerking is enige tijd sterk richting Tollebeek/off-site gegaan. Vind je dat het huidige raamwerk beide hoofdtakken weer voldoende gelijkwaardig behandelt?

### G. Werkt het dashboardconcept?

Kan een gebruiker hiermee zien:

- wat we weten;
- wat we niet weten;
- waarom een uitkomst een bepaalde range heeft;
- waar het getal vandaan komt;
- welke vervolgstap de meeste informatiewinst geeft?

Welke informatie zou jij op het eerste scherm anders organiseren?

### H. Waar zou jij als eerste verder investeren?

Als je maar enkele vervolgstappen mocht kiezen, waar zit volgens jou de meeste informatiewinst?

---

## 11. Voorstel voor een reviewgesprek

Ik zou niet beginnen met GitHub, code of een lange lijst bestanden.

Een effectieve volgorde lijkt mij:

1. **10 min — projectdoel en filosofie**  
   Wat proberen we eigenlijk te weten en waarom kiezen we voor zo min mogelijk noodzakelijke berekening?

2. **15 min — theorie en twee effectketens**  
   Current/reference, on-site en off-site, transfer en waardering.

3. **15 min — evidence en onzekerheid**  
   Hoe gebruiken we literatuur, hoe voorkomen we verkeerde overdracht, waarom ensembles?

4. **15 min — dashboardschermen**  
   Niet “vind je de kleur mooi?”, maar: laat de interface de wetenschappelijke structuur goed zien?

5. **15–30 min — kritiek en prioritering**  
   Welke aannames zijn zwak, welke routes ontbreken en waar levert extra werk de meeste kenniswinst?

Het gewenste resultaat van het gesprek is dus geen akkoordstempel, maar een lijst van:

- bevestigd;
- aanpassen;
- nader uitzoeken;
- voorlopig buiten scope.

---

## 12. Korte leesroute als je weinig tijd hebt

Als je maar ongeveer 20–30 minuten hebt:

1. lees hoofdstuk 1–5 van dit document;
2. bekijk de dashboardbeelden bij het reviewdocument;
3. kijk naar hoofdstuk 7 en 9;
4. noteer je antwoorden op de vragen in hoofdstuk 10.

De technische details zijn daarna beschikbaar als je op een specifieke schakel wilt inzoomen.

---

## 13. Verdieping in de repository

Voor wie daarna verder wil:

- `docs/00_project_handover_and_continuation.md` — brede projectfilosofie;
- `docs/02_theoretical_framework.md` — theoretische basis;
- `docs/03_conceptual_model.md` — objecten en relaties;
- `docs/07_evidence_and_qualification.md` — bron/evidence/claim/toepassing;
- `docs/49_project_effect_pathway_matrix_v0_1.md` — on-site/off-site routes en lichtste verdedigbare rekenweg;
- `docs/50_evidence_ensemble_protocol_v0_1.md` — omgaan met meerdere bronnen;
- `docs/51_onsite_ensemble_source_migration_v0_1.md` — eerste grass/maize evidence-migratie;
- `docs/52_onsite_bounded_calculation_surface_v0_1.md` — eerste fail-closed on-site rekenoppervlak;
- `docs/53_onsite_crop_and_valuation_input_routes_v0_1.md` — crop- en economische routes;
- `docs/54_onsite_maize_soil_crosswalk_v0_1.md` — BRP × BRO crop/soil crosswalk;
- `docs/55_bro_ccnl6_rule_proposals_v0_1.md` — reviewbare bodemclassificatievoorstellen;
- `docs/56_onsite_maize_soil_source_materialization_v0_1.md` — reproduceerbare bronacquisitie zodra deze workunit canoniek is.

De oudere workbook- en dashboardlijn blijft design- en evidencegeschiedenis. De huidige repository is de plaats waar betekenis, evidence en beslisregels gecontroleerd worden samengebracht.
