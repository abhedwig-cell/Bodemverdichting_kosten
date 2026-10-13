# Tollebeek proef A: uitvoerbaar toetsprotocol (zonder verdichtingsattributie)

**Status:** PROTOCOL_DRAFT, 2026-10-12. Aanvulling op `docs/64_tollebeek_transferpilot_besluitnotitie_v0_1.md`. Geen nieuwe fysische parameters of kostenclaims.

## Onderzoeksvraag

Onder welke operationele en hydrologische condities verandert een **expliciet hypothetische** extra afvoer aan de perceelsrand de afvoer via het lokale netwerk, de gemaalbelasting en eventuele capaciteitsdruk in een bemalen systeem als Tollebeek?

**Niet onderzocht in proef A:** of de extra afvoer daadwerkelijk door ondergrondverdichting ontstaat. Die attributie is proef B en vereist een gekwalificeerde current/reference bodemvergelijking.

## Inputcontract

1. Systeemidentiteit en geometrie: canonieke OT.02-geometrie, bronzones en relevante afvoerverbindingen, met datum en provenance.
2. Basisafvoer: gebeurtenisgebonden referentiehydrogram of expliciet synthetische basisreeks; nooit een stilzwijgend aangenomen werkelijk hydrogram.
3. Prikkel: `delta_q_field_edge(t)`, niet-negatieve en desgewenst verschoven puls(en), als **scenario** met expliciete volumebalans, tijdstap, ruimtelijke herkomst en bronstatus.
4. Berging/routing: bekende peil- en watergangconfiguratie, dynamiek en onzekerheidsgrenzen; onbekend blijft onbekend.
5. Gemalen: tijdafhankelijke beschikbare capaciteit, bedrijfsregels, Q-H-relatie, opvoerhoogte en rendement waar nodig voor energiekosten. Geïnstalleerde capaciteit alleen als bovengrens/metadata, niet als feitelijke beschikbaarheid.
6. Receptor: incrementele pompenergie, uren, capaciteitsdruk of waterstand/overlast. Kies één primair eindpunt per toets.

## Testontwerp

- **T0, nulprikkel:** controle op nul incrementele output bij gelijk gehouden toestand.
- **T1, volumepuls:** vaste expliciet synthetische extra hoeveelheid met een gekozen aankomsttijd.
- **T2, tijdsverschuiving:** hetzelfde extra volume op een ander tijdstip; test niet-lineariteit door samenloop met basisbelasting.
- **T3, bergingsgevoeligheid:** zelfde puls bij afzonderlijk gedocumenteerde bergingsscenario's, geen ongefundeerde feitelijke waardetoekenning.
- **T4, beschikbaarheid:** zelfde puls bij scenario's voor operationele capaciteit en regeling.
- **T5, massabalans:** voor ieder scenario `extra input = extra uitstroom + verandering opslag + overige expliciete verlies-/uitwisselingsstromen`, binnen vooraf bepaalde numerieke tolerantie.

De scenario's zijn softwarematige of methodologische gevoeligheidsproeven zolang de werkelijke invoer niet gekwalificeerd is.

## Minimale outputs

| Output | Eenheid | Interpretatie |
|---|---|---|
| Extra perceelsrandafvoer | m³ per gebeurtenis en m³/s tijdreeks | opgelegde prikkel, niet door verdichting bewezen |
| Extra netwerkafvoer | m³ en m³/s | route-afhankelijke respons |
| Verandering systeemopslag | m³ | buffering, geen schade |
| Extra gemaalvolume en draaiuren | m³ en uren | alleen bij toegelaten operationele context |
| Verandering maximale belasting / waterstand | m³/s of m | risico-indicator, niet automatisch overlast |
| Extra energie | kWh | alleen met gekwalificeerde Q-H/efficiëntie/bedrijfsvoering |
| Eventuele kosten | € per gebeurtenis | pas na kwalificatie economische receptor, prijsjaar en overlap |

## Go/no-go vóór een echte casusrun

- **GO voor softwarematige demonstratie:** synthetische invoer, expliciete aannames, massabalans, geen geografische schadeclaim.
- **GO voor fysische Tollebeek-toets:** gebeurtenisgebonden referentiebelasting, systeemtopologie, berging, regelgedrag en voldoende operationele gegevens onafhankelijk onderbouwd.
- **NO-GO voor verdichtingsattributie:** zonder gekoppelde, gekwalificeerde actuele/referentie bodemtoestand en respons.
- **NO-GO voor economische schade:** zonder toerekenbare systeemrespons en passende economische waardering.

## Controle op beschikbare gegevens

De repository registreert een huidige peilgebiedgeometrie, historische peilbesluiten, gemaalbeschrijvingen en een KNMI-forcing voor oktober 1998. Volgens de bestaande kwalificatie ontbreken nog noodzakelijke gebeurtenisspecifieke operationele en bodemtoestandsgegevens. Een 1998-gebeurtenis mag niet stilzwijgend worden uitgevoerd met de huidige pompregeling of een bodemtoestand uit 2020–2021.

Issue #36 behandelt specifiek de externe bronhouderroute voor de WER3382-verdichtingsmetingen. Die kwestie is geen reden om proef A als **zuiver synthetische softwarematige demonstratie** te blokkeren, maar verhindert wel de lokale verdichtingsattributie in proef B.

## Acceptatiecriteria

1. Alle invoer en scenario's hebben herleidbare provenance en tijdcontext.
2. Geen ontbrekende gegevens worden als nul of standaardparameter gepresenteerd.
3. Massabalans en nulpulstest slagen.
4. Timinggevoeligheid is zichtbaar en niet gereduceerd tot een vaste volumefactor.
5. Elke output is gelabeld `SOFTWARE_QA_ONLY`, `SCENARIO_ONLY` of, pas na review, voor een specifiek fysisch intended use gekwalificeerd.
6. Resultaten worden niet naar nationale eurokosten geëxtrapoleerd.

## Eerstvolgende technische handeling

Controleer de bestaande bounded source-transfer-dispatch code en tests op deze zes criteria. Voeg alleen ontbrekende *softwarematige* testgevallen toe; geen nieuwe SWAP-runs, geen GitHub Actions starten als lokale verificatie mogelijk is. Dit protocol zelf bevat geen doorgerekende casusresultaten.
