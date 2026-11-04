# Hydrologische off-site routes: evidence-toets en onderzoekskeuze v0.1

**Datum:** 12 oktober 2026, inhoudelijk werkpakket aangevuld 4 november 2026. **Status:** RESEARCH_REVIEW_ONLY, niet gekwalificeerd voor nationale schadeberekeningen. Aansluiting op F1 tot F5, O3 en de bestaande evidence-governance. Geen nieuwe empirische parameters.

**Actuele leesroute voor Ab:** de oorspronkelijke ketentoets hieronder blijft achtergrond. De [uitgewerkte hydrologische bijdrage](#uitwerking-hydrologische-bijdrage-ab-4-november-2026) bevat een inhoudelijke concepttekst, een beperkte overdracht van bestaande modelgegevens en een concrete aanpak voor de eerste gebiedsberekening van 2026. De [werkplancheck 113](113_lvvn_rapportagegereedheid_bronclaimtoets_20261103.md) en [rapportblauwdruk 114](114_rapportblauwdruk_en_expertopdracht_20261104.md) bepalen de huidige prioriteit; de oudere aanbeveling om meerdere systeemtypen te verkennen is geen opdracht om in 2026 meerdere pilots te starten.

## Getoetste bestaande repositorybronnen

- `docs/02_theoretical_framework.md`: matched current/reference, respons onder dezelfde forcing, afzonderlijke transfer- en waarderingsstappen; occurrence en magnitude van runoff scheiden.
- `docs/49_project_effect_pathway_matrix_v0_1.md`: F1 heeft lokale/modelmatige bronrespons, F2 mist generieke delivery, F3 is vooral Tollebeek-pilot, F4 heeft uitsluitend benchmark voor schade, F5 mist overgang van potentiële behoefte naar feitelijke levering.
- `docs/50_evidence_ensemble_protocol_v0_1.md`: bronleden met verschillende context niet middelen; DIRECT_CANDIDATE/PROXY/BOUND/SCENARIO/BENCHMARK/GUARDRAIL en intended-use onderscheiden.
- `docs/07_evidence_and_qualification.md`: bron, evidence-item, claim en intended-use-qualification gescheiden.
- `docs/58_project_architecture_status_v0_1.md`: kleine watersysteemtypologie als eerstvolgende off-site-stap; Tollebeek is geen nationaal model.

**Reikwijdte van deze toets:** documentatie- en bewijsarchitectuur plus de in bovenstaande documenten vastgelegde samenvattingen. Geen heranalyse van oorspronkelijke meetreeksen of numerieke herberekening; daarmee kunnen we nog geen onafhankelijke kwantitatieve validatie claimen.

## Beoordeling per hydrologische schakel

| Schakel | Huidige onderbouwing in Git | Wat is verantwoord | Blokkade voor geldbedrag |
|---|---|---|---|
| S0: toestand/referentie | Diepte- en ernstafhankelijkheid expliciet; actuele landelijke exposure ontbreekt | Gedefinieerde matched scenario's | Representativiteit en actuele verdichtingsomvang |
| F1: bodem → runoff/drainage | Lokale empirische/modelvoorbeelden, contextafhankelijk | Conditionele bronrespons en gevoeligheidsgrenzen, mits bronmatch | Niet elke lokale respons is nationaal overdraagbaar |
| F2: bron → perceelsrand/netwerk | Causale route bekend, generieke delivery ontbreekt | Transfer als afzonderlijke te toetsen relatie | Connectiviteit, opslag, timing en ontvangend systeem |
| F3: netwerk → bemaling | Tollebeek architectuur en bounded checks | Pilottoetsing en expliciete scenario's | Feitelijke operationele gegevens en schaaloverdracht |
| F4: netwerk → overlast/schade | Defra/Graves uitsluitend benchmark | Mechanisme en relevante receptor vastleggen | Overschrijdingskans, blootstelling en schadefunctie |
| O3/F5: waterstress → regionale watervraag | Fysieke scenario's; levering onbekend | Potentiële vraag apart rapporteren | Gedrag, bron, beschikbaarheid, daadwerkelijke levering en schaarste |

**Voorlopig oordeel:** grootste methodische lacune bij wateroverlast ligt **niet** in de definitie van runoff maar in F2 en vervolgens F4; bij droogte ligt ze in de overgang O3 → feitelijke vraag/levering → F5. Dit is een oordeel over de keten, geen kwantitatieve rangorde van maatschappelijke schade.

## Kleine typologie voor toetsing, niet voor landelijke classificatie

| Voorlopig systeemtype | Kenmerkende vraag | Noodzakelijke toets |
|---|---|---|
| A. Peilbeheerst bemalen poldergebied | Wanneer wordt extra aangevoerd water daadwerkelijk extra verpompt of veroorzaakt het capaciteitsspanning? | Routing, berging, regeling, pompbelasting; Tollebeek als één pilot |
| B. Vrij afwaterend gebied | Verandert extra perceelsafvoer de benedenstroomse piek en blootstelling? | Reistijd, berging, synchronisatie van pieken, drempels |
| C. Gedraineerd landbouwgebied met watergangen | Hoe verschuift afvoer tussen drainage, oppervlakkige route en tijd? | Drainageconfiguratie, uitlaat, lokale retentie, ontvangend systeem |
| D. Wateraanvoergebied met beperkte beschikbaarheid | Leidt potentiële extra watervraag tot werkelijke aanvoer, onttrekking of onvervuld tekort? | Beregeningsgedrag, waterbeschikbaarheid, allocatieregels en kosten |

Dit zijn **onderzoekshypothesen voor een systeemtypologie**, geen bewezen uitputtende of onderling exclusieve Nederlandse gebiedsklassen. Een gebied kan meer dan één typekenmerk hebben.

## Beslisvolgorde 2026

1. **Kies eerst het te waarderen eindpunt:** extra bemalingsenergie, wateroverlastschade, daadwerkelijke extra aanvoer of onvervuld tekort. Niet al deze eindpunten zijn automatisch optelbaar.
2. **Identificeer per eindpunt de eerstvolgende ontbrekende causale schakel.** F2 voor regionale wateroverlast, vraag/levering voor F5.
3. **Selecteer per systeemtype maximaal één concrete toetscase** waarvoor actuele data en een matched bodemreferentie beschikbaar kunnen zijn; Tollebeek mag alleen zijn eigen klasse/pilot onderbouwen.
4. **Zoek eerst empirische gegevens en eenvoudige grenzen.** Gebruik SWAP of routingmodellen alleen als ze een voor de eindkosten bepalende onzekerheid aantoonbaar kunnen verkleinen.
5. **Leg een stopregel vast:** als bron- of transferattributie niet kan worden gekwalificeerd, rapporteer de fysieke indicatie en blokkade, niet een fictief eurobedrag.
6. **Rapporteer ook niet-monetair:** gewijzigde timing, pieken, waterstress en mogelijk ecologische gevolgen, inclusief onzekerheden.

## Concrete toetsvragen aan Ab en expertgroep

- Is het doel van de eerste waterpilot vooral bemalingskosten, wateroverlastschade of de vergelijkbaarheid van bronrespons tussen soilscapes?
- Welke bestaande gebieds- en operationele gegevens maken één F2-transferrelatie toetsbaar zonder een nationaal hydrologisch model?
- Welke beregeningsgegevens onderscheiden behoefte, aanvraag, daadwerkelijke levering en niet-geleverde vraag?
- Hoe voorkomen we dat dezelfde extra waterhoeveelheid via zowel extra pompen als overstromingsschade onterecht dubbel wordt gewaardeerd?
- Zijn de voorgestelde vier systeemtypen bruikbaar, of ontbreekt een belangrijk Nederlands watersysteemtype?

## Vervolg en toelatingsgrens

De volgende inhoudelijke stap is **bronspecifieke verificatie**: open de oorspronkelijke hydrologische studies, meetreeksen en pilotgegevens en vul per schakel het bestaande evidence-register met expliciete intended use. Dit document mag niet als zelfstandig bewijs voor numerieke factoren worden gebruikt. Na review kan de typologie worden vastgelegd in de bestaande pathway-/evidence-structuur; tot dan geen nieuwe canonieke datasets, coefficients of schemawijzigingen.

## Uitwerking hydrologische bijdrage Ab 4 november 2026

**Doel en afbakening.** Ab verzorgt de hydrologische procesbeschrijving, beoordeelt hergebruik van de bestaande on-site berekeningen en werkt de eerste gebiedsberekening uit. De koppeling aan economische waardering gebeurt met de economen; nieuwe bodemklassen worden door Guido en Kees aangeleverd na controle. Onderstaande tekst is een inhoudelijk voorstel voor Ab om te beoordelen en aan te passen, geen reeds door hem geautoriseerde rapporttekst. De rol van Ab als modelleur hydrologie is bevestigd in het leidende werkplan; de concrete samenwerking met Martin moet nog worden afgestemd.

### 1. Concepttekst voor de expertbijdrage

#### Ondergrondverdichting en watertransport

Ondergrondverdichting kan de verdeling en continuïteit van poriën veranderen en de mechanische weerstand voor wortels vergroten. Voor de hydrologie zijn daarom zowel de waterretentie en doorlatendheid van de bodemlagen als de beworteling relevant. Een verandering in bulkdichtheid is op zichzelf onvoldoende om de verandering in de waterbalans te berekenen. Daarvoor moeten ook laagdiepte, laagdikte, bodemopbouw en de hydrologische omstandigheden bekend zijn. De bestaande BoVer-synthese vormt de procesbasis; een nieuwe algemene literatuurreview is voor deze bijdrage niet nodig [H1; theorie 02].

Een beperkende ondergrondlaag kan de afvoer van water uit de bovengelegen bodem vertragen. Of vervolgens water aan maaiveld blijft staan of oppervlakkig afstroomt, hangt af van de beschikbare berging, de voorafgaande natheid, neerslag, grondwaterstand en afvoermogelijkheden. Ook de bovengrond en het maaiveld bepalen hoe snel water infiltreert en het perceel verlaat. Daarom moeten twee situaties worden onderscheiden: afstroming doordat de neerslagintensiteit de opnamecapaciteit van het oppervlak overschrijdt, en afstroming doordat de beschikbare berging is uitgeput. Een verandering in de ondergrond mag niet zonder onderbouwing worden voorgesteld als een verandering van uitsluitend de infiltratiecapaciteit aan maaiveld [H2; H3].

De waterbalans reageert als geheel. Minder oppervlakkige afvoer kan samengaan met meer drainage of andere ondergrondse afvoer. Omgekeerd betekent extra oppervlakkige afvoer niet dat het watersysteem over een seizoen evenveel extra water ontvangt. Een deel van het verschil kan bestaan uit een verschuiving tussen routes, tijdelijke opslag of een verandering van verdamping. De hydrologische bijdrage beoordeelt daarom steeds hoeveelheid, tijdverloop, berging en route in samenhang [H2; formeel model 04].

#### Van perceelsafvoer naar regionale wateroverlast

Voor gevolgen buiten het perceel moet bekend zijn waar het water terechtkomt. Afvoer kan onderweg worden vertraagd, geborgen of opnieuw infiltreren. Bij vrij afwaterende gebieden zijn onder meer reistijden en het samenvallen met andere afvoeren van belang. In peilbeheerste gebieden spelen daarnaast beschikbare berging, streefpeilen, pompregeling en actuele gemaalcapaciteit een rol. De som van afzonderlijke perceelspieken is daarom geen gebiedspiek. Extra gegenereerde afvoer is evenmin automatisch extra pompvolume, inundatie of maatschappelijke schade [theorie 02; hydrologische ketentoets hierboven].

De vergelijking moet betrekking hebben op dezelfde weersperiode en gebiedscontext, met een expliciet beschreven minder verdichte referentie. Als ook maaiveldbeheer, drainage of landgebruik verandert, beschrijft de uitkomst een gecombineerd scenario. Dat kan bruikbaar zijn, maar is geen afzonderlijk effect van ondergrondverdichting. Het eerste gebiedsresultaat kan daarom beperkt blijven tot een onderbouwd verschil in gegenereerde maaiveldafvoer. Een uitspraak over belasting van het ontvangende watersysteem vereist aanvullend een getoetste verbinding en tijdsafhankelijke overdracht [04; 49; H2].

#### Waterbeschikbaarheid en droogte

Voor droogte is de voor wortels bereikbare watervoorraad relevant, samen met de aanvoer vanuit diepere lagen en de werkelijke wateropname. Dat is een andere grootheid dan het totale watervolume in de bodem. Veranderde hydrauliek en beworteling kunnen de droogtestress en beregeningsbehoefte beïnvloeden; richting en omvang moeten voor het betreffende profiel worden onderzocht. Een afname van transpiratie bewijst op zichzelf geen extra regionale watervraag [H1; H3; resultaatbalans 112].

Potentiële beregeningsbehoefte, werkelijk toegediend water en onvervulde vraag blijven afzonderlijke uitkomsten. Extra behoefte leidt alleen tot extra onttrekking of aanvoer als de boer beregent en water beschikbaar is. Bij beperkte levering kan vooral de waterstress toenemen. Grondwateronttrekking, oppervlaktewateraanvoer en regionale schaarste vragen bovendien verschillende receptorinformatie. Een verschil in percolatie onder een modelkolom is nog geen verschil in regionale grondwateraanvulling [04 §4.11; 49 O3/F5].

#### Wat deze bijdrage kan concluderen

De beschikbare projectkennis onderbouwt dat watertransport een gemeenschappelijke schakel vormt tussen bodemverdichting, gewasrespons en mogelijke gevolgen buiten het perceel. Er zijn lokale modelresultaten, maar daaruit volgt geen vaste Nederlandse afvoer- of schadefactor. Voor de eerste berekening is een gematcht profielcontrast nodig, gevolgd door een afzonderlijke beoordeling van ruimtelijke overdracht. De eerste vraag is welke van deze schakels met bestaande berekeningen en gebiedsgegevens al kunnen worden ingevuld. Pas daarna wordt besloten of aanvullende modellering nodig is [49; 50; 112; 113].

### 2. Twee bruikbare bronvoorbeelden voor het overleg

| Voorbeeld | Wat laat het zien? | Gebruik in Ab's bijdrage | Begrenzing |
|---|---|---|---|
| Schipper et al. 2015, STOWA 2015-19, §4.6 en figuren 4.7 tot 4.10 [H2] | In het samengestelde verbeteringsscenario verschuiven afvoerroutes; de keuze van infiltratiecapaciteit beïnvloedt de runoff sterk, de wortelzonedikte de beregeningsuitkomst | Motiveert waarom runoff, drainage en droogterespons apart moeten worden onderzocht | Bovengrond/infiltratie, ondergrond en wortels veranderen samen; geen geïsoleerde diepe-verdichtingsfactor |
| Groenendijk et al. 2017, WENR 2811, hoofdstukken 2 en 5 en bijlage 3 [H3] | Veldmetingen, bodemfysische parametrisatie en scenario's maken vergelijking van lokale bodemtoestanden mogelijk; keuzes aan maaiveld en in het profiel blijven relevant | Onderbouwt controle van bestaande profiel- en modelinstellingen vóór hergebruik | Geen nationaal representatieve toestand-responsrelatie; modelscenario en meting blijven verschillende bewijssoorten |

De gecontroleerde effectgetallen staan al in [112 §3 en §4](112_integrale_wetenschappelijke_tussenbalans_20261028.md), met hun toepassingsgrenzen. Zij worden hier niet als nieuw resultaat herhaald. Voor de circa 12 mm in WENR 2811 is de gecorrigeerde interpretatie in 112 leidend; de oudere omschrijving als afzonderlijk extreem-weerscenario in 110/111 wordt niet overgenomen. Het Vlaamse 9/10-mm-verschil blijft onopgelost. Beide bronnen dienen voor proces- en modelkritiek, niet als landelijke rekenfactor.

### 3. Eerste actie: bestaande berekeningen overdragen en beoordelen

**Vraag aan Martin, via afstemming door Ab:** lever één bestaand, zo volledig mogelijk huidig/referentie-paar met modelinvoer, uitvoer en korte toelichting aan. Als dat paar niet bestaat, laat dan zien welke toestanden wel zijn doorgerekend. Een bestaande export in eigen formaat volstaat; eerst geen nieuw uitvoersysteem bouwen. Beoordeel daarnaast of de beschikbare set de bodem-/gewascombinaties van één kandidaatgebied dekt.

| Benodigde informatie | Minimaal bruikbare inhoud | Waarom nodig |
|---|---|---|
| Profiel en toestand | Profiel-/categorie-ID; laaggrenzen; verdichte laag; hydraulische parameters; worteldiepte en herkomst; huidige toestand en referentie | Vaststellen wat daadwerkelijk is gewijzigd en of de uitgangstoestand al verdichting bevat |
| Context en beheer | Modelversie; weerperiode; grondwater-/onderrand; drainage; maaiveldberging; runoff-instelling; beregeningsregel en werkelijk opgelegde giften | Onbedoelde verschillen tussen scenario's uitsluiten en routes interpreteren |
| Beginconditie en voorgeschiedenis | Initialisatie of inloopperiode, beginvoorraad en eventueel drukhoogte-/vochtprofiel | Een initiële opslagafwijking onderscheiden van een respons tijdens de analyseperiode |
| Tijdas en waterbalans | Tijdstap of interval, eenheid, tekenconventie; neerslag, beregening, verdamping, oppervlakteafvoer, drainage, onderrandflux en bergingsverandering | Cumulatieve uitvoer correct naar intervallen omzetten, ontbrekende termen herkennen en balans controleren |
| Ruimtelijke koppeling | Categorie-/perceel-ID met areaal en gebieds-ID; bron van de verdichtingsfractie indien gebruikt | Vaststellen welke hectares bij het profiel en contrast horen; overlap of ontbrekende dekking zichtbaar maken |

Maak van afwezige runoff-uitvoer geen nulreeks. Scheid een werkelijk berekende nul van een uitgeschakelde runoff-optie en van ontbrekende opslag in het uitvoerbestand. Splits verdamping alleen verder uit in transpiratie, bodemverdamping en interceptie als de bestaande uitvoer dit ondersteunt. Fluxen door interne laaggrenzen zijn diagnostiek en worden niet nogmaals als externe waterbalansafvoer opgeteld.

Bij verschillende waterretentierelaties horen vochtgehalte en drukhoogte bij elkaar. Leg daarom de initialisatieregel vast; eis niet tegelijk identieke vochtgehalten én identieke drukhoogten als die bij verschillende bodems fysisch niet verenigbaar zijn. Bij een gebeurtenisvergelijking moet eventuele beginvoorraad expliciet zijn; bij een seizoensvergelijking kan een gelijk behandelde voorgeschiedenis juist toestandsafhankelijke voorraden opleveren. Dit is een te toetsen toepassingskeuze binnen de bestaande matchingregel, geen nieuwe universele instelling.

Leg bij beregening vooraf vast welke vraag wordt beantwoord. Een vaste gelijke gift vergelijkt bodems onder hetzelfde waterbeheer. Een gelijke automatische beslisregel kan verschillende giften geven en beschrijft dan ook de reactie van het beheer. Vergelijk geen automatisch onbeperkt beregende bodem met een onberegende bodem om het verschil uitsluitend aan verdichting toe te rekenen.

### 4. Berekeningsopzet voor één gebied in 2026

**Selectievoorstel:** gebruik het gebied waarvoor het passende profielcontrast én de ruimtelijke koppeling het best beschikbaar zijn. Kies niet automatisch Tollebeek omdat daar al veel documentatie over bestaat. De [Tollebeek-toets 95](95_swap_first_pair_readiness_20261028.md) toont dat lokale toestand en referentie op de gecontroleerde peildatum nog onvoldoende waren onderbouwd. Dat sluit het gebied niet uit, maar geeft het geen voorrang boven een beter gedocumenteerde bestaande casus.

Werk vervolgens in drie stappen, met een expliciete eindgrens:

1. **Perceels-/profielrespons.** Gebruik de bestaande matched verschillen uit `EQ_ATTRIBUTION_DELTA`. Beoordeel per beschikbare periode oppervlakkige afvoer, drainage, verdamping, onderrandflux en berging. Behoud negatieve verschillen en nulgebeurtenissen. Een veranderde onderrandflux bij opgelegde grondwaterstanden wordt gerapporteerd binnen die randvoorwaarde, niet als berekende regionale grondwaterstandsdaling.
2. **Gebiedssom van bronvolumes.** Koppel passende profielen aan aantoonbaar gedekte hectares. Gebruik per eenheid de bestaande omzetting `EQ_GENERATED_VOLUME` en tel alleen niet-overlappende arealen over dezelfde periode op. Als alle hectares hypothetisch een verdichtingscontrast krijgen, heet dit een gebiedsscenario; het is geen schatting van de actuele schade. Rapporteer gebiedsdekking, ontbrekende eenheden en geraamde/afgeleide gewichten afzonderlijk.
3. **Ontvangend watersysteem, alleen bij bestaande bruikbare overdracht.** Leid beide volledige toestandreeksen door hetzelfde onderbouwde netwerk en beheerconcept. Bij drempels of veranderend pompbedrijf is het afzonderlijk routeren van alleen de verschilreeks niet vanzelf gelijkwaardig. Zonder overdracht stopt het resultaat bij de gebiedssom van gegenereerde afvoer. Noem die uitkomst geen afvoer bij gemaal of gebiedsuitlaat.

Gebruik de fijnste bestaande resolutie die voor het eindpunt nodig en onderbouwd is. Daguitvoer kan dagvolumes dragen, maar geen uurpiek; maand- of jaaruitvoer alleen de overeenkomstige balans. Selecteer voor inspectie een reeds doorgerekende natte periode en, indien aanwezig, een droge periode. Vraag geen nieuwe lange klimaatreeks voordat de bestaande set is beoordeeld. De definitieve gebiedskeuze en de vraag of de begrensde bronvolumeberekening de werkplanvraag beantwoordt worden met Guido vastgelegd.

### 5. Minimale resultaatset en beoordeling van nauwkeurigheid

| Te leveren resultaat | Presentatie en eenheid | Benodigde onderbouwing |
|---|---|---|
| Huidige en referentiewaterbalans, met verschillen | Tabel per profiel en seizoen/jaar in mm; gebiedsvolumes in m³ waar areaal bekend is | Alle externe balansposten, begin-/eindberging, vaste systeemgrens en modeldefinities |
| Maaiveldafvoer en verdeling over routes | Gemeenschappelijke tijdas; cumulatief volume plus intervalwaarden bij voldoende resolutie | Oppervlakteafvoer onderscheiden van drainage en andere afvoer; geen som van maxima |
| Droogterespons | Werkelijke en potentiële transpiratie indien aanwezig, beregening en modelgedefinieerde stressindicator | Beregeningsregel, bron/beschikbaarheid en periode; onvervulde watervraag alleen als die werkelijk wordt berekend |
| Gebiedsdekking en overdracht | Bekende hectares, niet-gedekte hectares en naam van het ontvangende systeem | Profiel-/areaalkoppeling; bij uitlaatclaim getoetste routing en beheer |
| Betrouwbaarheid van het contrast | Balansresidu, beschikbare meettoets en afzonderlijke gevoeligheden | Scheid numerieke nauwkeurigheid, overeenkomst met metingen en onzekerheid over het verdichtingscontrast |

Een sluitende waterbalans bewijst interne consistentie, niet dat de afvoerroutes juist zijn. Controleer bestaande metingen waar beschikbaar op het niveau dat zij werkelijk ondersteunen. Een goede overeenkomst van totale gebiedsafvoer is geen afzonderlijke validatie van runoff, drainage of het contrafeitelijke verdichtingseffect. Bepaal of numerieke/balansafwijkingen klein genoeg zijn om het gerapporteerde verschil te onderscheiden; daarvoor wordt hier geen willekeurige universele tolerantie gekozen.

Beperk de eerste gevoeligheidsbeoordeling tot de bepalende open keuzes: bodem-/referentieparametrisatie, maaiveldberging/runoff-instelling en relevante begin- of grondwatertoestand. Gebruik bestaande varianten eerst. Geef een bron-/scenario-envelop waar de varianten dit dragen; noem die geen statistisch betrouwbaarheidsinterval. Bij uitsluitend één modelpaar zonder toets blijft de modelnauwkeurigheid onvoldoende vastgesteld. Dat is een te rapporteren beperking, geen reden om een nauwkeurigheidspercentage te verzinnen.

### 6. Koppeling aan andere experts en maatschappelijke gevolgen

Ab levert de waterhoeveelheden, tijdsbasis en routes. De nutriënten- en middelenexperts bepalen aanvullend mobilisatie, concentratie, retentie en stofspecifieke omzetting. Uit een runoffverschil volgt geen evenredige vrachtverandering. Voor gastransport levert hydrologie de relevante vocht-/verzadigingscontext; de emissie-expert beoordeelt netto productie, consumptie en uitstoot. Voor ecologie blijft een concreet habitat- of receptorverandering nodig voordat een externe consequentie wordt geclaimd.

Voor de economen worden alleen fysiek onderbouwde eindpunten overgedragen: daadwerkelijk extra pompbedrijf, veranderde overlastblootstelling, werkelijke extra levering of een aantoonbaar tekort. Zonder die schakel worden gewijzigde afvoertiming, behoefte en droogtegevoeligheid niet-monetair gerapporteerd. Onderscheid regionale landbouwafvoer van rivieroverstroming, dijkdoorbraak en stedelijke riolering. CATCH is uitsluitend een te verkennen hergebruikroute voor 2027; zie [113 §11](113_lvvn_rapportagegereedheid_bronclaimtoets_20261103.md#11-gerichte-verificatie-mogelijke-catch-hergebruikroute).

### 7. Ab's concrete oplevering en eerstvolgende besluit

**Voor het komende overleg:** Ab beoordeelt de concepttekst in §1, brengt de twee bronvoorbeelden in §2 in en bespreekt met Martin de bestaande uitvoer volgens §3. Neem een onderbouwd voorstel mee voor de eerste casus, het bereikbare eindpunt en maximaal de drie ontbrekende gegevens die dat eindpunt blokkeren. De afspraak met Martin is hier voorbereid, niet verstuurd of bevestigd.

**Voor eind 2026:** lever de geautoriseerde hydrologische tekst, een reproduceerbaar gebiedsresultaat binnen de vastgestelde grens, de bijbehorende waterbalans/afvoerfiguur en een beoordeling van nauwkeurigheid en beperkingen. Een gebiedssom van bronvolumes kan het eerste niveau zijn; het werkplanakkoord daarop moet expliciet zijn. Als het profielcontrast of de gebiedskoppeling ontbreekt, meldt Ab dat met het concrete ontbrekende bestand en de consequentie voor oplevering aan Guido. Een hypothetische systeembelasting of synthetische opslagproef vervangt geen berekend verdichtingseffect.

**Besluitvolgorde:** eerst bestaande berekeningen ontvangen, daarna het best gedekte gebied en eindpunt kiezen, vervolgens alleen de noodzakelijke aanvullende berekening uitvoeren. Geen nieuwe SWAP-keten, landsdekkende routing of extra pilots vooraf. Meerdere gebieden, landelijke off-site extrapolatie, stoftransport en volledige economische doorrekening behoren bij de verdere uitwerking in 2027.

### 8. Bronnen en controlebereik van deze aanvulling

- **H1:** Bakema et al. (2023), WENR 3225, [DOI 10.18174/583342](https://doi.org/10.18174/583342), vooral hoofdstukken 3/4. Bestaande procesbasis volgens 113; volledige PDF op 4 november niet opnieuw verworven. Geen nieuwe kwantitatieve claim uit deze bron.
- **H2:** Schipper et al. (2015), *Goede grond voor een duurzaam watersysteem*, [STOWA 2015-19](https://www.stowa.nl/sites/default/files/assets/PUBLICATIES/Publicaties%202015/STOWA%202015-19.pdf), §4.6/4.7, figuren 4.7 tot 4.10. De passages over routeverschuiving, infiltratiecapaciteit en wortelzonedikte zijn op 4 november opnieuw rechtstreeks gecontroleerd. Modelcontext blijft leidend; geen nieuwe effectgrootte toegelaten.
- **H3:** Groenendijk et al. (2017), *Effecten van verbetering bodemkwaliteit op waterhuishouding en waterkwaliteit*, [WENR 2811 / STOWA 2017-020](https://doi.org/10.18174/418283). Op 4 november publicatie en opzet opnieuw in primaire tekst gecontroleerd; verdere detailduiding ontleend aan bestaande controles 93/110/111 en de latere precisering in 112. Geen nieuwe volledige tabellenaudit geclaimd.
- **Projectbasis:** leidende werkplan, rechtstreeks gelezen in deze sessie; [02](02_theoretical_framework.md), [04](04_formal_model.md), [49](49_project_effect_pathway_matrix_v0_1.md), [50](50_evidence_ensemble_protocol_v0_1.md), [64](64_tollebeek_transferpilot_besluitnotitie_v0_1.md), [67](67_tollebeek_operationele_datagates_v0_1.md), [95](95_swap_first_pair_readiness_20261028.md), [112](112_integrale_wetenschappelijke_tussenbalans_20261028.md), [113](113_lvvn_rapportagegereedheid_bronclaimtoets_20261103.md) en [114](114_rapportblauwdruk_en_expertopdracht_20261104.md). De werkelijke modeluitvoer bij Martin is nog niet ingezien. Dit is inhoudelijke uitwerking en een uitvoeringsvoorstel, geen uitgevoerde gebiedsberekening en geen formele expertgoedkeuring.
