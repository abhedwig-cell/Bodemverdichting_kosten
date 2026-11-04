# Brontoets bestaande hydrologische ensembles: WENR 2811

**28 oktober 2026 | PRIMARY_SOURCE_CHECK | behoud bestaande methode en registers**

Doel: controle van de **reeds bestaande** kandidaten `ENS_F1_RUNOFF_LOCAL` en `ENS_O3_IRRIGATION_DRY` uit `evidence/evidence_ensemble_register_v0_1.csv`. Primaire bron: Groenendijk et al. (2017), *Effecten van verbetering bodemkwaliteit op waterhuishouding en waterkwaliteit*, WENR 2811, DOI https://doi.org/10.18174/418283, met name gedrukte rapportpagina's **10, 16 en 27**, en de secties *Oppervlakkige afstroming* en *Samenvattend*. De PDF is rechtstreeks gecontroleerd; verder teruggrijpen naar onderliggende Schipper et al. (2015) en Van den Bolt et al. (2016) blijft een afzonderlijke broncontrole.

## Wat de bron zegt en wat het register bedoelt

| Bestaand ensemblelid | Primaire passage WENR 2811 | Correcte interpretatie | Niet toegestaan |
|---|---|---|---|
| `H04_VK_RUNOFF_MAIZE`: 10–12 mm/jaar | Samenvatting, *Oppervlakkige afstroming*, p. 10: langjarig gemiddeld effect bodemverdichting circa **10 mm/jaar** bij snijmaïs; onder extremere weersituaties circa **12 mm/jaar** | Berekende, contextgebonden **extra oppervlakkige afstroming aan de bronzijde** in modelverkenning *Vruchtbare Kringloop*. Twee weerscontexten, **geen confidence interval** en geen empirische Nederlandse populatieband | Niet 10–12 mm/jaar als nationale schade, niet een reeds gekwalificeerde min-maxverdeling, niet automatisch afvoer bij systeemuitlaat |
| `EV_RUNOFF_VLAANDEREN`: 9 mm/jaar | Zelfde rapport, p. 10: jaarlijkse oppervlakkige afstroming van **5 naar 14 mm** bij verdichting in Vlaamse modelcontext, uurneerslag | **9 mm/jaar berekend verschil** tussen twee modeltoestanden. De bron beschrijft hogere diepte van verdichte lagen en relatief kleinere effecten op verdamping | Niet een Nederlands brongeval, niet exact hetzelfde profiel en referentie als Vruchtbare Kringloop |
| `H07_GRASS_IRRIGATION`: 50–90 mm | Samenvatting p. 16, tabel 1.1 en toelichting: bij grasland in **een droog jaar** reductie beregeningsbehoefte na bodemverbetering circa **50 mm voor veldpodzol** en **60–90 mm voor ooivaaggrond** | Modelafhankelijke **potentiële vraagvermindering** onder bepaalde irrigatieregels en bodemverbeteringsaannames | Niet mm feitelijk toegediend, niet regionale zoetwateraanvoer, niet jaargemiddelde, niet direct schade door verdichting alleen |

## Extra inhoudelijke verificatie

- WENR 2811 p. 16 stelt dat grootste effecten optreden bij een **ondiepere** verdichte laag; bij dieper gelegen lagen in Vlaanderen waren de effecten geringer.
- Tabel 1.1 op p. 10 waarschuwt dat de beregeningsuitkomst afhangt van de **definitie van optimale vochtvoorziening / irrigatiecriteria**.
- WENR 2811 p. 27 en figuur 2.6: bij snijmaïs variëren oppervlakkige-afstromingsuitkomsten door het **weer en de aangenomen maaiveldberging**. De effecten van de worteldiepte zijn niet verwaarloosbaar. Daardoor zijn de 10 en 12 mm niet automatisch met alleen diepere verdichting verklaard.
- De eigen samenvatting vermeldt expliciet dat de modellering van oppervlakkige afstroming **niet gestandaardiseerd** is en dat aannames over verzadigde doorlatendheid van de toplaag en oppervlakteruwheid sterk doorwerken.

## Kwalificatie volgens het bestaande protocol (doc. 50)

- `H04_VK_RUNOFF_MAIZE`: **PROXY / SCENARIO_ENSEMBLE** met twee **weerspecifieke resultaten**. Bronorde en toepassingsrichting bevestigd, maar nog niet een voor Nederland over te nemen effectrange.
- `EV_RUNOFF_VLAANDEREN`: **PROXY / afzonderlijk Vlaams scenario**. De 9 mm is een berekend verschil, niet de gerapporteerde waarde van één toestand.
- `H07_GRASS_IRRIGATION`: **BOUND / SINGLE_SOURCE_ONLY** voor droog-jaar-potentiële behoefte onder *bodemverbetering*, niet een direct opgehoogde of daadwerkelijk geleverde beregeningshoeveelheid.

**Belangrijk:** dit is een controle van informatie in *één WENR-syntheserapport*, niet de onafhankelijke kwalificatie van alle oorsprongsproeven of een formele landelijke probabilistische synthese.

## Consequentie voor ons werk

**Behouden:** oorspronkelijke methodiek 02/04/49/50/59 en de ensembleleden, inclusief bestaande legacy-status. **Niet optellen of middelen:** de Vlaamse 9 met de Nederlandse 10/12; evenmin 50–90 mm omzetten in regionale aanvoer of economische kosten. **Wel rapporteren:** afzonderlijke brongebonden lokale modeluitkomsten, hun aanname-/weerscontext en toepassingsbeperkingen.

**Minimale nog zinvolle bronstap:** controleer Schipper et al. 2015 voor profielkeuze, maaiveldberging en beregeningsregel, en de oorspronkelijke Vlaamse bodemhydrauliekstudie voor de dikte/diepte van de verdichte laag en de volledige huidige/referentieprofielen. De landelijke meetdataset en SWAP-uitvoering blijven geparkeerd.

**Besluit:** `SOURCE_CHECKED_CONDITIONAL_PHYSICAL_SCENARIOS`, `NOT_ADMITTED_NATIONAL_SUBSOIL_EFFECT`. Geen wijziging aan canonieke evidence/qualification, causaal netwerk v0.7 of WUR-notitie.
