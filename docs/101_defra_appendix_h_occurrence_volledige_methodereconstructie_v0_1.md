# Defra SP1606: reconstructie Appendix H en occurrence-bijlage

**28 oktober 2026 | SOURCE-LEVEL METHOD AUDIT | niet toegelaten voor Nederlandse schadeparameters**

**Primair gelezen bestanden uit de Teams-ZIP:** `10138_APPENDIX_H_COST_OF_COMPACTION_2.docx` (titel: *Appendix H: Cost of compaction*) en `10148_APPENDIX_C_OCCURANCE_OR_PROBABILITY_OF_SOIL_DEGRADATION_IN_ENGLAND_AND_WALES_1.docx` (**interne documenttitel: Appendix B**; bestandsnaam noemt C). Dit zijn de bronbestanden, geen gereconstrueerde algemene beschrijving. Aanvulling op [document 100](100_graves_defra_nederlandse_eindpunten_omgekeerde_schadebenadering_v0_1.md).

## 1. Grote methodologische scheiding

Appendix H kent twee verschillende routes:
- **On-site + stof-/emissieposten:** top-down nationale areaaltoerekening door bodem × landgebruik × type berijding, met empirische achtergrondgegevens, geometrische veldveronderstellingen en expliciet **personal communication/expert assumptions** voor opbrengst- en verliesfactoren.
- **Flooding:** een beoogde stroomgebiedsroute die verandering van bodemconditie via runoff, piekafvoer, kans, blootstelling en schade naar geld zou vertalen. **Deze keten was niet volledig doorberekend** wegens gegevensverwerkingsproblemen (Appendix H, paragraaf *Estimating changes in flood damage costs attributable to soil condition*). De **gepubliceerde flooding-uitkomst** is gebaseerd op een veel eenvoudiger aanname van proportionele schadeverandering.

Dat onderscheid moet in toekomstige Nederlandse methoden consequent worden beschreven: een modelontwerp is niet noodzakelijk de feitelijke gebruikte berekeningsmethode.

## 2. Stap-voor-stap: voorkomen van verdichting en opbrengstverlies

1. **Soilscape:** landgebruik × bodemtype (klei, silt, zand, veen), gekoppeld aan landschapsoppervlakte.
2. **Veldgeometrie:** GIS steekproef van veldgroottes uit Rural Payments Agency, vervolgens aannamen over rechthoekigheid, kopakkerbreedte, rijspoorbreedte en bewerkingsbreedte. Appendix H tabel 1 gebruikt bijvoorbeeld 15 m kopakker voor akkerbouw, 12 m voor grasland; tramline-compaction width 0,4 m en tillage-compaction width 0,4 m. Deze zijn geen directe metingen van actuele permanente ondergrondverdichting.
3. **Risico-oppervlakte:** afzonderlijke aandelen voor *headlands*, *tramlines* en *general field* (tabellen 2–5). Kopakker- en rijspoor-/algemene verdichtingsrisico's worden op representatieve velden geprojecteerd.
4. **Opbrengstreductie op getroffen oppervlak:** gebruikte opbrengstverliezen per bodem en landgebruik zijn ontleend aan literatuur én **persoonlijke communicatie** (Professor D. Godwin en Dr T. Chamen; Appendix H tekst voorafgaand aan tabellen 2–4). Voor tramlines is lokaal 100% gewasuitval aangenomen, waarvan **33%** aan het omgaan met verdichtingsrisico werd toegerekend (ibid.). Bij sommige aannamen is klei het meest en silt het minst gevoelig.
5. **Economisch productieverlies:** de resulterende areaal- en gewascombinaties × opbrengstdervings-/economische aannamen. Tabel 27 vermeldt **£161.670 miljoen**; in de voorafgaande tekst staat circa £162.7 miljoen. Deze interne afwijking verdient bronreconciliatie, niet stilzwijgend gelijkstellen.

**Resultaat voor areaal:** tabel 27: 13.928.575 ha categorieareaal, 3.858.670 ha 'at risk', **28%**. Dat is een modelmatig samengesteld *risicoareaal*, geen op 3,86 miljoen hectare direct gemeten toestand van de ondergrond.

### Occurrence/probability-bijlage

De in de ZIP als ‘Appendix C’ benoemde bijlage draagt intern de titel **Appendix B: What is the actual occurrence or probability of soil degradation in England and Wales?** De tekst zegt dat directe veldmetingen van verdichting schaars zijn en kaarten meestal gevoeligheid/risico aangeven. In de soilscape-tabellen zijn categorieën H/M/L/? **relatieve risico's** en nadrukkelijk **geen werkelijke degradatiepercentages** (paragraaf 'Estimates of the probability of soil degradation'). De relatie tussen de risicoklassen in deze bijlage en de geometrisch opgebouwde 28%-schatting in H moet vóór vergelijking formeel worden uitgewerkt.

## 3. Overige on-site posten

### Extra diesel, Appendix H tabellen 6–7

De Britse berekening gaat uit van een representatieve trekker en veronderstelde uren/bewerkingsintensiteit, waarbij een **extra vermogensvraag door verdichting** bovenop gewone bewerking wordt aangenomen. Bronresultaat tabel 27: **£17,477 miljoen** extra dieselkosten en **41,611 miljoen liter per jaar** additioneel dieselvolume. Het rapport geeft als voorbeeld 200 HP, met aannamen bij specifieke bedrijfsgegevens.

**Risico voor Nederland:** mechanische weerstand van de bewerkte bovengrond en extra trekvermogen door subsoil compaction kunnen niet zonder meer worden gelijkgesteld. Scheid echte extra arbeid/brandstof van al in landbouwprijzen en opbrengstverlies vervatte kosten.

### Extra N/P/K-verliezen, Appendix H tabellen 8–9

De auteurs gebruiken een **voor tarwe afgeleid N-verliesmodel als representatief voor andere landbouwsystemen**. Van toegediende N wordt 62% als door gewas gebruikt/vastgelegd beschouwd, 38% als verlies. Van dat verlies: 34% uitspoeling en 66% denitrificatie, waarvan 5% als N₂O, 7% als NH₃ en 55% als N₂. De getallen zijn een veronderstelde N-verdeling, geen Nederlands experimenteel bewijs van een verdichtingsrespons. Voor P en K wordt een verliesfractie van 4% aangenomen. De extra door verdichting veroorzaakte verliezen worden **uitsluitend toegepast op de reeds verloren fracties**, en alleen op verondersteld risicoareaal (tekst bij tabel 9).

Tabel 27 meldt extra **37.044 ton N/jaar, 979 ton P/jaar en 1.751 ton K/jaar**. Kosten volgens dezelfde tabel: N **£22,968 miljoen**, P **£0,666 miljoen** en K **£0,911 miljoen**.

**Bijzonder risico:** een proportionaliteitsaanname voor alle landbouwsystemen kan het verschil tussen nitraatuitspoeling, oppervlakkige P-afvoer en N₂O-emissie missen. Neem deze fracties niet als Nederlandse effectfactor.

## 4. Off-site: stofvrachten, broeikasgassen en kosten

De Britse route voor extra verlies aan N/P rekent met milieurisico-/schadekosten voor N in water, P in water en N₂O/NH₃ in lucht, en emissie-effecten van extra diesel-/kunstmestgebruik. Tabel 27 geeft afgerond:

| Eindpunt | Kosten volgens tabel 27 (£ miljoen/jaar) | Oordeel voor Nederlandse toepassing |
|---|---:|---|
| N in rivieren en meren | 2,028 | Historische waarderingsbenchmark, geen verdichtingsfactor |
| N in overgangswater | 0,112 | Idem |
| N in drinkwater | 2,166 | Behandel receptor en drinkwaterzuivering separaat |
| P in zoetwatermeren | 1,377 | Idem, stofspecifieke respons vereist |
| N₂O gerelateerd aan extra N-verlies | 73,627 | Sterk afhankelijk van aannamen over N-verlies en omzetting |
| NH₃ | 3,458 | Geen broeikasgas; afzonderlijke milieu-impact |
| Flooding | 168,000 | Vereenvoudigde, niet fysisch volledig doorgetrokken route |

De bron bevat ook posten voor broeikasgaslast van extra diesel en vervangende N/P/K-kunstmest. **Tabel 27 is intern administratief niet volledig eenduidig:** diesel-GHG wordt zichtbaar tweemaal vermeld, N₂O-rij is als 'NO2' getiteld, en enkele P/K-gerelateerde tabelbenamingen wijken af van de beschreven grootheid. Ongecontroleerd optellen van alle regels zou daarom **dubbeltelling kunnen veroorzaken**. Uit de slottekst: totale on-site **£203,691 miljoen**, totale off-site **£273,468 miljoen**; samen ca. **£477,158 miljoen**. Dit is niet dezelfde grootheid als de gehele bodem-degradatiekosten van Graves, en de classificatie van sociale versus financiële kosten vergt aparte controle.

### Waterbedrijven

Appendix H opent met OFWAT-data en concludeert expliciet dat de beschikbare waterbedrijfscijfers **niet betrouwbaar naar bodemdegradatie en specifiek verdichting zijn toe te rekenen**. Daarom zijn deze nationale uitgaven niet simpelweg als een proportionele schadepost opgenomen. Ook KRW-gerelateerde investeringen zijn niet zonder causaliteitsketen toe te rekenen.

## 5. Flooding: beoogde methode versus berekende uitkomst

**Beoogde benadering (niet volledig gerealiseerd):**
1. Soilscapes, landgebruik, bodemconditie, stroomgebiedsdata.
2. JBA/Cranfield catchment flood management tool → gemiddelde afvoerdiepte per herhalingstijd.
3. Catchment descriptors, Flood Estimation Handbook en ReFH → relatieve verandering in piekafvoer.
4. NaFRA → aantal/type blootgestelde objecten.
5. Gebeurteniskans × gevolgschade → verandering van verwachte jaarlijkse overstromingsschade.

**Feitelijk gepubliceerde vereenvoudiging:**
- Scenario's *fair → good* en *fair → poor* voor bodemconditie; categorieën nemen naast ondergrondverdichting ook andere factoren zoals bovengrondstructuur, rijsporen, hellingslengte en beheer mee (Appendix H, tabel 25).
- Hydrologische analyse geeft onder gekozen aannamen een orde van **3–10% extra afvoerdiepte**, centrale **7%** voor representatieve Q75-gebeurtenis.
- Aanname: vergelijkbare relatieve verandering bij andere herhalingstijden, **en** een overeenkomstige proportionele verandering van kans op overstroming en schade.
- Nationale basis: circa **£1,4 miljard directe jaarlijkse schadelasten + £1 miljard risicobeheer = £2,4 miljard/jaar**.
- Resulterend **£72–240 miljoen/jaar** en centraal **£168 miljoen/jaar**; direct **0,07 × £2,4 miljard**.

**Belangrijk:** de gelijkstelling procentuele verandering runoff → procentuele verandering kans → procentuele verandering kosten is een sterke, niet onafhankelijk bevestigde vereenvoudiging. De £1 miljard aan risicobeheeruitgaven als onderdeel van de schadebasis is daarnaast economisch discutabel als deze uitgaven bij een veranderd risico niet werkelijk veranderen. Niet zonder afzonderlijke scenario-/kostentoets met fysieke schadelasten samenvoegen.

## 6. Reconstructie naar bestaande V-routes

| Britse stap | V01–V42 in ons raamwerk | Overnemen / vervangen |
|---|---|---|
| Soilscape en risk-of-compaction | toestand voorafgaand aan V01 | **Vervangen** door Nederlandse gemeten verdichting, met meetsteekproef-/areaalcorrectie |
| Geometrisch berijdingsareaal | toestand/context voorafgaand aan V01 | Hooguit historie/benchmark, geen rechtstreeks Nederlandse areaalfactor |
| Yield-factor per landgebruik × bodem | V03, V05–V07 | Gewas- en seizoensafhankelijke literatuurband, mogelijk SWAP voor diagnostiek |
| Extra diesel | bedrijfseconomisch eindpunt, eventueel V08 | Niet afleiden uit normale verdichtingsklasse zonder aangetoond extra brandstofgebruik |
| Extra nutriëntenverliezen | V30–V35 | Fysische water- en stofbalansen, routes en context, geen universeel percentage |
| N₂O/NH₃ | V23–V29 voor N₂O; NH₃ apart | Boven- en ondergrond, N-aanvoer en nettoflux scheiden |
| Runoff | V11 | Gemodelleerd/perceelsgebaseerd met huidige/referentieprofielen |
| Routing/piekafvoer | V12–V13 | Gebieds- en gebeurtenisafhankelijk bepalen |
| Kans, blootstelling en flooding | V15–V16 | Niet lineair veronderstellen; receptor-/schadefunctie |
| Waterbedrijven/KRW | receptor en waarderingslaag | Alleen echt toerekenbare extra kosten/verminderde effecten, vermijd dubbeltelling |

## 7. Conclusie voor onderzoeksstrategie

De Britse methode is waardevol als **procesinventarisatie en historisch rekenvoorbeeld**, maar veel effectgroottes zijn aannames, expert judgment of brede bodembeheercontrasten. Ons project heeft met Nederlandse verdichtingsmetingen potentieel betere **toestandsinformatie**, maar mist nog de lokale/regionale causale transfer- en receptorresponse om nationale monetaire bedragen te rechtvaardigen.

**Besluit:** gebruik de Britse fysieke en economische relaties als te toetsen hypothesen of benchmarks. **Niet:** de Britse 28% risicoareaal, 7% flooding-verhouding, vaste N/P-verliesfracties of opbrengstschadefactoren in een Nederlandse nationale raming invoeren.

**Status:** primaire H en occurrence-bijlage direct gelezen, belangrijke tekst, tabellen en rekenstappen gereconstrueerd. Een volledige audit van de onderliggende economische *unit values*, alle tabelrekenformules en de precieze samenstelling van de tabel-27-eindtotalen is nog niet afgerond. Geen nieuwe admitted coefficient, geen wijziging aan v0.7 of de WUR-notitie.
