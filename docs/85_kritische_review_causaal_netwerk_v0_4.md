# Kritische inhoudelijke beoordeling causaal netwerk v0.4

**Datum:** 12 oktober 2026  
**Status:** REVIEW_FINDINGS, geen empirische validatie of admission.  
**Beoordeeld:** [document 84](84_causaal_netwerk_geactualiseerd_na_expertoverleg_v0_4.md), tegen [matrix 81](81_causaal_netwerk_volledig_gecodeerd_v0_3.md) en [review 82](82_kritische_review_causaal_netwerk_v0_3.md).  

## Hoofdoordeel

De v0.4 heeft een bruikbare inhoudelijke uitbreiding, maar is **nog niet geschikt als eenduidig rekennetwerk of finale presentatiefiguur**. Van de 13 X-pijlen zijn verscheidene slechts uitsplitsingen of boekhoudkundige/agrarische gevolgverbindingen. De figuur bevat tevens vijf ongecodeerde kandidaatverbindingen. Dat is inconsistent met het principe één code per causale pijl. De 28 oorspronkelijke C-relaties zijn behouden. De beoordeling hieronder is deskundige plausibiliteitsanalyse op mechanistisch niveau, geen systematische literatuurtoets.

## Besluitvoorstel per kandidaat

| Code | Oordeel | Motivering | Voorstel |
|---|---|---|---|
| X01 | Behouden, herdefiniëren | Interne percolatie en netto grondwateraanvulling zijn verschillende fluxen. | Splits waterbalansflux en regionale aanvulling; specificeer diepte/onderrand. |
| X02 | Behouden, herbenoemen | Beworteling beïnvloedt wateropname maar is niet hetzelfde als potentiële verdamping. | Naar **actuele transpiratie en wortelwateropname**. |
| X03 | Niet als simpele directe pijl | ET en percolatie worden tegelijk bepaald door neerslag, berging, runoff en drainage; balansrelatie is geen onafhankelijke mechanistische oorzaak. | Waterbalans als gekoppeld submodel, niet als autonome directe causaliteit. |
| X04 | Behouden als hypothese met gebiedscontext | Diepe percolatie op percelen is niet altijd aquiferaanvulling of beschikbare onttrekking. | Vereis grondwaterstroming, reistijd, opslag, kwel en receptor. |
| X05 | Herwerken | Capillaire nalevering volgt uit hydraulische gradiënten en eigenschappen, niet alleen uit bodemvocht als enkelvoudige oorzaak. | Laat afhangen van profiel, grondwaterstand en hydraulische eigenschappen; toets mogelijke baten. |
| X06 | Behouden als verklarende on-site schakel | Wortelbeperking kan opbrengst beïnvloeden, maar opbrengstrespons is seizoens- en gewasafhankelijk. | Geen aparte opbrengstschade optellen bij empirische yield reduction. |
| X07 | Behouden als geaggregeerde schakel | Bodemvocht alleen dekt zuurstof-, nutriënten- en mechanische stress niet. | Label als samengestelde gewasrespons, niet als unieke opbrengstverklaring. |
| X08 | Voorwaardelijk behouden | Een verdichte laag kan weerstand/draagkracht verhogen, maar berijdbaarheid en schade zijn vocht- en diepteafhankelijk. | Splits draagkracht en berijdbaarheid; positief en negatief expliciet. |
| X09 | Als uitsplitsing van C18 behouden | Redox beïnvloedt, maar bepaalt niet zelfstandig koolstofsubstraat of methaanpotentieel. | Neem waterverzadiging, organisch substraat en microbiële omzettingen op. |
| X10 | Als uitsplitsing van C18 behouden | Netto CH4 is resultante van productie, oxidatie en transport. | C18 vervangen door expliciet pad wanneer deskundig geaccepteerd; nooit beide routes onafhankelijk tellen. |
| X11 | In huidige vorm afwijzen | NH3-vervluchtiging volgt niet rechtstreeks uit algemene stikstofomzettingen; blootstelling NH4+, pH, temperatuur, mestplaatsing domineren. | Verwijderen uit hoofdfiguur; als afzonderlijke literatuurvraag parkeren. |
| X12 | Behouden ter vervanging van C05 | Perceelsrandafvoer is geen levering aan regionaal netwerk; connectiviteit ontbreekt in C05. | Verbind perceelsrand met overdracht/berging/routing. |
| X13 | Behouden ter vervanging van C05 | Netwerkrespons volgt uit levering én systeemtoestand/beheer. | Voeg systeemcontext toe; C05 als samengevouwen legacy relatie markeren. |

**Besluitniveau:** voorlopige aanbevelingen voor experts, geen definitieve verwijdering of admission van codes.

## Vijf ongecodeerde pijlen in de figuur

1. Regionaal watersysteem → systeemblootstelling.
2. Systeemblootstelling → wateroverlast.
3. N/P-vracht → ecologische blootstelling en respons.
4. Middelenvracht → ecologische blootstelling en respons.
5. Ecologische blootstelling en respons → ecologische toestand ontvangend water.

Deze verbindingen dupliceren of splitsen C07, C27 en C28. **Beslis expliciet:** óf alleen annotaties zonder pijl gebruiken, óf elke formele causale pijl een eigen ID geven en oude C-relaties vervangen. Niet een tussenvorm hanteren in een ‘volledig gecodeerd’ netwerk.

## Bestaande C-relaties die inhoudelijke correctie vragen

- **C05:** onderscheid generatie, perceelsrand, levering aan sloot, routing en watersysteemrespons. Gebruik X12–X13 niet parallel als twee extra onafhankelijke effecten.
- **C06–C07:** systeemrespons is niet gelijk aan extra pompenergie of schade. Werkelijke bediening, overlastkans, blootgestelde objecten en kwetsbaarheid ontbreken.
- **C09–C12:** ‘potentiële watervraag’ is een misleidend gezamenlijk knooppunt voor gewasbehoefte, irrigatievraag en regionaal leveringsbesluit. Voorstel: scheid actuele wortelopname, watervraag, geleverd water en onvervuld tekort.
- **C17–C18:** N2O vereist productie én reductie; CH4 vereist methanogenese, oxidatie en transport. Beide nettofluxen mogen niet uit één algemene redoxfactor worden afgeleid.
- **C20:** ‘redox → stoftransport’ niet zonder stofspecifieke uitleg toepassen op gewasbeschermingsmiddelen.
- **C26:** ‘externe ecologie’ niet zonder onafhankelijke receptor aannemen. Lokale biodiversiteitsimpact blijft relevant.
- **C27–C28:** vracht alleen is onvoldoende voor receptorrespons; blootstelling, retentie en dosis-respons zijn nodig.

## Belangrijke ontbrekende kruisverbanden

**Waterbalans:** infiltratie, maaiveldberging, runoff, drainafvoer, evapotranspiratie, capillaire opstijging en percolatie delen dezelfde massabalans. Dit zijn niet zes afzonderlijke schadeposten. In een gerichte procesfiguur één waterbalans-control volume gebruiken.

**Stoftransport:** waterroute, sedimenttransport, stofbron/toediening, sorptie, reactie en ontvangend water bepalen gezamenlijk N/P en middelenvracht. Bodemverdichting kan routes verleggen, niet noodzakelijk de totale vracht vergroten.

**Klimaat/biogeochemie:** organisch substraat, stikstofaanbod, temperatuur, pH, redoxdynamiek en gasdiffusie bepalen gezamenlijk fluxen. **NH3 niet onder ‘broeikasgassen’ presenteren**.

**Bodemleven:** direct lokale effecten en de mediërende effecten via wortels/stoffen onderscheiden. Een verschil in lokaal bodemleven is niet automatisch aparte maatschappelijke off-site schade.

**Baten:** toegenomen draagkracht, capillaire nalevering of minder verticale nitraatuitspoeling mogen als mogelijke richtingen staan, maar mogen niet als aangetoonde netto baten worden verkocht.

## Economische en methodologische controle

- Kies een expliciete *counterfactual*: huidige bodem met bestaande verdichting tegenover dezelfde representatieve bodem zonder **schadelijke antropogene ondergrondverdichting**. De classificatie ‘natuurlijk’ op basis van bulkdichtheid alleen is onvoldoende.
- Bij on-site is empirische opbrengstderving leidend; mechanistische routes verklaren mogelijke variatie. Tel waterstress-gerelateerde opbrengstderving niet apart bij opbrengstverlies op.
- Off-site vereist receptor, schaal en aanvullende systeemtransfer. Extra gegenereerde afvoer ≠ extra overstromingsschade of gemaalkosten.
- Maatschappelijke schade, beheerkosten en vermeden kosten van toekomstig doelbereik niet zonder expliciet en consistent beleidsscenario optellen.
- Toerekening van schade aan bodemverdichting moet vanuit beide richtingen controleerbaar zijn: oorzaak → gevolg én bestaand gevolg → counterfactuale bijdrage.
- Geen selectie van relevantie uitsluitend op monetaire opbrengst; ecologische effecten met ontoereikende monetarisering apart houden.

## Aanbevolen ontwerp voor een v0.5-presentatieschema

1. **Overzicht:** één bron ‘ondergrondverdichting’, drie gemeenschappelijke proceskernen **bodemstructuur**, **waterbalans / beworteling**, **gas- en stofprocessen / bodemleven**.
2. **Zes eindcategorieën:** wateroverlast, wateraanvoer, broeikasgassen, nutriëntenwaterkwaliteit, gewasbeschermingsmiddelenwaterkwaliteit, ecologie. Zet geen ‘klimaat’-label direct op zuurstofcondities; emissies pas op het eindpunt.
3. **Uitvergrotingen:** water en transfer; waterkwaliteit; broeikasgassen; bodemleven.
4. **Aparte waarderingslaag:** blootstelling en receptor → privaat/publiek/maatschappelijk effect → geldband of kwalitatieve uitkomst.
5. **Codering:** preserveer C01–C28 in v0.4; stel een expliciete C/X crosswalk op voor v0.5 vóór hernummering. Geen ongenummerde formele pijlen.
6. **Evidencestatus:** conceptueel, literatuuronderbouwd, lokaal empirisch getoetst, landelijk toepasbaar apart kwalificeren. Een stippellijn mag alleen kandidaatstatus betekenen, niet tegelijkertijd ‘zwak effect’ of ‘onzekere richting’.

## Gerichte expertvragen

- **Hydrologie:** hoe definiëren we een consistente referentie in bestaande bodemfysische invoer en welke percolatie-/drainage-/runoffverschillen zijn observeerbaar?
- **Gewas:** welke empirische relaties tussen verdichtingsklasse en opbrengstderving zijn overdraagbaar naar gewas, bodem en jaar?
- **Broeikasgassen:** op welke ondergrondmetingen berusten veranderingen in netto N2O en CH4, en kan X11 vervallen?
- **Waterkwaliteit:** welke wijzigingen in middel- en nutriëntenvracht bereiken daadwerkelijk het ontvangende water?
- **Ecologie:** welke van C23–C26 hebben een onderbouwde externe receptor?
- **Economie:** welke eindpunten zijn onafhankelijk, welke waardering en welke schadekosten mogen gecombineerd worden?

## Acceptatiecriterium

Vóór nieuwe PPT: (a) formele pijlentelling en gecodeerde relaties consistent, (b) geen dubbel parallel C/X voor identieke mechanismen, (c) onzekere routes zichtbaar als hypothesen, (d) zes categorieën expliciet, (e) duidelijke scheiding fysiek mechanisme, receptor en economische waardering, (f) verklaring van iedere overgang en van de tegenfeitelijke referentie. De inhoudelijke kwalificatie blijft afhankelijk van literatuur en externe experts.

**Niet uitgevoerd:** geen bron-per-pijl-literatuurreview, geen herberekening, geen wijziging van C01–C28 in de v0.3-bronbestanden.
