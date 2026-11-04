# BoVer SWAP-WOFOST kolomproef: reconstructie en reproduceerbaarheid

**28 oktober 2026 | SOURCE_RECONSTRUCTION, NOT_EXECUTED | Wetenschappelijk referentiedossier**

Bron: Bakema et al. (2024), WENR-rapport 3404, **appendix 5 (rapportpagina's 107–119)**; achtergrond appendix 1–3. Deze reconstructie is gebaseerd op de door de gebruiker aangeleverde volledige PDF. Zij beschrijft de **oorspronkelijke proef**, niet een nieuwe SWAP-run. Zie ook [parameterreview 97](97_bover_3404_primaire_parameterreview_20261028.md) en [curvediagnostiek 98](98_bover_hydraulische_functies_diagnostische_vergelijking.md).

## 1. Modeldoel en beperking

Appendix 5 (Marius Heinen, Martin Mulder) rekent de kasproef met SWAP-WOFOST na. **Gewasgroei is niet dynamisch gesimuleerd**; de wortelverdeling is voorgeschreven en **dagelijks** geactualiseerd via de herstartfunctie. De proef vergelijkt S0–S4 voor een 10 cm laag op 30–40 cm en onderscheidt empirische Feddes-opname (Fe_0), Feddes met compensatie (Fe_1) en de Willigen/Van Noordwijk (dW). De auteurs vergelijken dW bij twee waarden van de Mualemparameter λ. Dit is geen zelfstandige test van een werkende ondergrondverdichtingsmodule voor dynamische wortelgroei.

## 2. Uit de primaire tekst reconstrueerbare invoer

| Onderdeel | Gepubliceerde waarde/keuze | Bron, rapportpagina | Status |
|---|---|---|---|
| Kolom | 0–30 cm bovenlaag, 30–40 cm verdichte laag, 40–70 cm onderlaag, 70–85 cm grof zand | 108–109 | BEVESTIGD |
| Toprand | Dichte rand, afdekfolie: geen aanvoer of afvoer, bodemverdamping uit | 109–110 | BEVESTIGD |
| Onderrand | Opgelegde drukhoogte onder grof zand **h = -85 cm** (niet de oorspronkelijk beoogde -75 cm) | 108 | BEVESTIGD |
| S0 | Referentie dichtheid ca. 1350 kg/m³, **afwijkend voorbereid en n=1 voor hydrologische bepaling** | A2 p.50, A3 p.75 | BEVESTIGD MET BEPERKING |
| S1–S4 hydrologisch | 1416, 1507, 1535, 1573 kg/m³ voor verdampingsringen; bijbehorende *casus 0* MVG-set | A3 p.75 | BEVESTIGD |
| Initieel θ | Bovenlaag .16, middelste .10, onderste .10 m³/m³ | 109 | BEVESTIGD |
| Initieel h bovenlaag | -541.7 cm voor alle behandelingen | 109, tabel 1 | BEVESTIGD |
| Initieel h tussenlaag | S0 -1465.5, S1 -816.9, S2 -771.0, S3 -712.7, S4 -732.2 cm | 109, tabel 1 | BEVESTIGD |
| Initieel h onderlaag | -1465.5 cm voor alle behandelingen | 109, tabel 1 | BEVESTIGD |
| Watervraag tot 31 maart | 0.5 mm/d | 110 | BEVESTIGD |
| 31 maart–6 april | 0.7 mm/d | 110 | BEVESTIGD |
| 6 april–13 april | 1.4 mm/d | 110 | BEVESTIGD |
| Na 13 april tot einde proef | **2.0 mm/d aangenomen**, niet gemeten | 110 | MODEL_AANNAME |
| Wortelverdeling | Eindprofiel gemeten, tussenliggend profiel verondersteld; diepte +2 cm per dag tot 70 cm | 110 | GEDEELTELIJK GEMETEN / AANNAME |
| Dagelijkse koppeling | Dag-voor-dag run met doorstart voor aangepaste wortelprofielen | 108 | BEVESTIGD |
| Wateropname | Fe_0, Fe_1 en dW, met illustratieve λ-aanpassing 6 naar 3 voor niet-verdichte lagen | 110–111 | BEVESTIGD |

**Hydraulische invoer:** de bijbehorende theta_r/theta_s/alpha/n/lambda/Ks zijn in [document 97](97_bover_3404_primaire_parameterreview_20261028.md) getranscribeerd uit appendix 3, tabellen 4–5. Bij de oorspronkelijke SWAP-kolomproef zijn volgens appendix 5 casus-0-parameters gebruikt. Niet uit de context af te leiden is een volledig, exact SWAP-inputdeck inclusief numerieke discretisatie, alle materiaallaagconfiguraties, uitvoerformaten en solveropties. Daarom is de gepubliceerde configuratie **nog niet reproduceerbaar zonder aanvullende bronbestanden of bewuste reconstructie-aannames**.

## 3. Resultaatcontrole tegen oorspronkelijke publicatie

| Resultaat | Originele bevinding | Rapportpagina | Betekenis |
|---|---|---|---|
| Drukhoogte 25 cm | Redelijk vergelijkbaar verloop van meting en simulatie | 111–112 | Beperkte hydraulische plausibiliteit |
| Watergehalte 45 cm | Redelijk vergelijkbare trends, simulaties dalen soms sneller | 112 | Beperkte hydraulische plausibiliteit |
| Aanvoer via grof zand | Circa **0.45 mm/d**, vooral bepaald door grofzand/onderrand | 113 | Geen verdichtingsspecifieke veldflux |
| Opwaartse flux door verdichte laag | Verwaarloosbaar; in gevoeligheidsvariant minder dan **0.03 mm/d** bij 2 mm/d vraag | 114 | Proefspecifiek, geen universele capillaire factor |
| Wateropnamereductie | Bij behandelingen ongeveer gelijk; sterk modelconceptafhankelijk | 110–111, 118 | Niet gebruiken om gemeten scheutafname te voorspellen |
| Bovengrondse droge biomassa | Daalt van S0 naar S4, maar **totale biomassa** (boven + onder) niet significant gewijzigd | A2 p.53, 62; A5 p.111, 118 | Allocatie van assimilaten naar wortels belangrijk |
| dW met λ=6 versus 3 | Sterk verschil in opnamegedrag | 111, 117–118 | Kritische modelparameteronzekerheid |

**Belangrijke waarschuwing:** appendix 5 stelt expliciet dat er onvoldoende waarnemingen van **actuele transpiratie als tijdreeks** zijn om één wateropnameconcept te verkiezen. De wortelontwikkeling in de tijd is evenmin rechtstreeks gemeten. Er zijn bovendien imperfecte onderrandcondities, mogelijke wandwortelgroei, en hydraulische metingen uit afzonderlijke monsters. Dit verhindert strikte modelvalidatie.

## 4. Eerste reproduceerbare proef: wat kan zonder verzinnen?

**Wel mogelijk nu:** reconstructie van de bronparametertabellen en bijbehorende θ(h)/K(h)-curves, plus een testcontract voor vergelijkingen met de oorspronkelijke figuren.

**Niet wetenschappelijk verantwoord zonder aanvullend materiaal:** een modelrun als exacte reproductie labelen. Nodig zijn in elk geval:
- originele SWAP-WOFOST inputdeck of voldoende volledige numerieke instellingen;
- dagreeks opgelegde waterbehoefte, exacte start/einddata en tijdstap;
- dagelijkse opgelegde wortelverdelingen per behandeling, inclusief aannames voor dunne/dikke wortels en de dW-vertaling naar root mass;
- exacte grofzand- en overige laagparameters en numerieke onderrandconfiguratie;
- gebruikte SWAP-versie en restartbestanden, of nauwkeurig omschreven equivalentie;
- toegang tot de oorspronkelijk gemeten sensortijdreeksen voor onafhankelijke validatie.

**Tweedeling die moet blijven:** (A) reproduceer de gepubliceerde *kolomproef* met voorgeschreven wortels voor modelcontrole; (B) ontwikkel later een aparte *Nederlandse ondergrondprofielproef* met onderbouwde CURRENT/REFERENCE-staten. A is geen automatische toelating voor B.

## 5. Praktische acceptatiecontrole

Voor een eerste uitvoering moeten de volgende toetsen slagen:
1. Iedere S0–S4-profielparameter met bronpagina en eenheid vastgelegd, met casus 0 als originele modelbasis; casus 1 alleen als gevoeligheid.
2. Identieke boven-/ondergrens en modelperiode voor alle behandelingen; verschillen uitsluitend door de bedoelde parameters en voorgeschreven wortelverdelingen.
3. Waterbalanssluiting per behandeling en per dag; fluxen met correcte richting en eenheid.
4. Reproductie van **patroon en schaal** van gemeten drukhoogte 25 cm, vochtgehalte 45 cm en aanvulling via onderrand, met expliciete meetonzekerheden.
5. Vergelijk Fe_0, Fe_1 en dW, met λ-sensitiviteit; geef eerlijk aan waar originele observaties onvoldoende onderscheid maken.
6. Geen projectie van kolomuitvoer naar landelijk runoff-, opbrengst- of kostenpercentage zonder afzonderlijke transfer- en waarderingstoets.

## 6. Besluit voor de volgende werkstap

**Huidige status: RECONSTRUCTABLE_IN_PART, EXACT_REPRO_BLOCKED.** De literatuur biedt voldoende cijfers en referentiegedrag om een gericht reproductieonderzoek in te richten, maar niet voldoende om met zekerheid een exacte oorspronkelijke run uit te voeren. De kortste weg is het originele SWAP-inputdeck en de tijdsafhankelijke wortel- en sensordata achter appendix 5 op te sporen. Een zelfstandig alternatief is een expliciet als *nieuw diagnostisch scenario* gemarkeerde berekening met openbare curves en aannames.

Geen nieuwe V-relaties; geen wijziging van projectbrede evidence-admission; geen uitgevoerde SWAP-run in deze sessie.
