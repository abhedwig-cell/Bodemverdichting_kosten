# Eerste SWAP-proef voor ondergrondverdichting: uitvoeringsgereedheid en blokkades

**28 oktober 2026 | READINESS_RECONCILIATION | geen modelrun, geen nieuwe parameter-admission.**

Voortbouwend op [protocol 94](94_swap_verdichtingsprofielen_brongetoetst_protocol_v0_1.md), [source-input baseline 23](23_source_model_input_baseline_v0_1.md), de [architectuurstatus 58](58_project_architecture_status_v0_1.md) en de bestaande `data_requests/`-registers. Dit document inventariseert wat daadwerkelijk in Git aanwezig is en wat nog nodig is voor één fysisch interpreteerbare CURRENT/REFERENCE-proef. Het introduceert geen nieuwe data-architectuur.

## 1. Verifieerbare beschikbare gegevens

| Reeds aanwezig | Concrete inhoud | Betekenis / grens |
|---|---|---|
| `data/soil/tollebeek_soil_profiles.csv` | Acht SoilPhys-kandidaatprofielen voor OT.02, inclusief profielidentiteit en screeningfracties | Profielcontext, niet verdichtingsstatus en niet exact areaalgewicht |
| `data/soil/tollebeek_soil_layers.csv` | Laagdiepten, textuur, organische stof, modal bulk density, Staringreeks/BOFEK-koppeling | Afgeleide profielkenmerken zijn geen gemeten CURRENT- of REFERENCE-toestand |
| `data/soil/tollebeek_profile_screening_v0_1.json` | 117 screengridpunten, 113 met profiel, 8 onderscheiden kandidaatprofielen | Profielselectie en dekking; niet landelijk representatief |
| `data/spatial/tollebeek_ot02_current.geojson` | Geometrie van het beheerde peilgebied | Geen verdicht areaal |
| `data_requests/data_request_register.csv` en specifieke aanvragen | De tien vereiste inputrollen en eisen voor de eerste matched pair | Vastlegging van ontbrekende gegevens, geen bewijs dat zij zijn geleverd |
| `examples/tollebeek_vertical_slice/README.md` | Expliciete waarschuwing tegen verzonnen voorbeeldinstellingen | Nog geen uitvoerbare wetenschappelijke invoerset |

**Eerste observatie:** de profielbestanden bevatten modal bulk density. Die mag niet als actuele meetwaarde worden gepresenteerd of gebruikt om de mate van antropogene verdichting vast te stellen.

## 2. Voorgesteld kleinste eerste experiment

Selecteer **één** geschikt bestaand mineraalbodemprofiel, alleen na controle van landgebruik, actuele verdichtingslaag, bodemfysische referentie en hydrologische randvoorwaarden. Tollebeek kan een geschikte *systeemcontext* zijn, maar mag geen nationale transferfactor opleveren.

Vergelijk gepaard:

- **REFERENCE:** een bodemtype- en laagdiepte-consistente toestand zonder schadelijke ondergrondverdichting, niet een abstracte optimaal losse bodem;
- **CURRENT:** dezelfde context met gemeten of onderbouwde schadelijke verdichtingslaag.

Gebruik dezelfde gewascondities, neerslag, hydrologische beginconditie en beheerinstellingen, behalve waar de verdichtingsingreep zelf een afhankelijke toestand verandert en die wijziging expliciet moet worden doorgerekend.

Voer pas na basiskwalificatie diagnostische H (hydrauliek), R (wortelmechanisch) en HR (gecombineerd) varianten uit. Bij onvoldoende wortelgegevens mag de eerste proef **alleen** hydraulische respons demonstreren, niet totale opbrengstschade.

## 3. Readiness: welke stap is daadwerkelijk nog geblokkeerd?

| Vereiste input | Reeds zichtbaar in Git | Huidige status voor de eerste SWAP-pair |
|---|---|---|
| Ruimtelijke eenheid | Tollebeek OT.02-geometrie | Context beschikbaar, verdicht areaal onbekend |
| Bodemprofiel en laaggeometrie | Acht modal SoilPhys-profielen | Kandidaten beschikbaar, nog geen geselecteerde gekwalificeerde CURRENT-pair |
| Actuele verdichtingsgraad en -diepte | Geen gemeten Tollebeek-locatiebewijs in onderzochte profieltabel | **BLOCKED** |
| Fysisch verdedigbare referentie | Methode beschreven; geen erkend gekoppeld profiel | **BLOCKED** |
| Consistente hydraulische parameters `theta(h)`/`K(h)` | Textuur en modal dichtheid; niet beide complete state-specifieke functies | **BLOCKED** |
| Gewas en wortelbegrenzing | Land-use request en theoretische opties | Voor gewas-/opbrengstclaim **BLOCKED** |
| Drainage-/peilbeheer | Documentatie en historische context | Actueel operationeel scenario nog kwalificeren |
| Neerslag en initiële toestand | Data-request en eventarchitectuur | Exacte paar-run context nog bevestigen |
| SWAP-versie/configuratie | Config-request en bestaande modelvoorbereiding | Geen in deze toets geverifieerde reproduceerbare runconfiguratie |
| Perceelsrandrespons versus regionale transfer | Werkpakket F1–F5 en pilotarchitectuur | Eerst lokale respons, geen directe schadeclaim |

Deze statussen volgen uit de gecontroleerde bestanden en documenten; zij zijn geen uitspraak dat elders bij collega's geen data beschikbaar zijn.

## 4. Verantwoord berekeningscontract

Voor elke werkelijk uitgevoerde paar-run worden vastgelegd:

`profile_id, state_id, reference_rule, soil_layer_top/bottom_cm, source_id, layer_parameter_source, weather_id, time_zone, drainage_id, initial_state_id, model_version, model_configuration_id, root_parameterisation, macropore_assumption, input_hash, output_hash, water_balance_error`.

Vergelijk per evenement én seizoen:

- maaiveldafvoer en drainafvoer, inclusief pieken, timing en volume;
- grondwaterstand/drukhoogte, bodemvocht en opslagverandering;
- wortelwateropname, transpiratie, bodemverdamping en interceptie;
- verticale flux door en onder de verdichte laag en waterbalanssluiting.

**Geen gelijkstelling:** flux onder de wortelzone ≠ netto regionale grondwateraanvulling; perceelsrunoff ≠ extra pompenergie; extra runoff ≠ middelenvracht; veranderde ET ≠ bewezen opbrengstderving.

## 5. Toets op nut en onderzoeksdoel

De eerste proef is alleen gerechtvaardigd als zij een reële onzekerheid over de **fysische bronrespons** verkleint. Het model moet niet worden ingezet omdat het kan rekenen. De centrale wetenschappelijke uitkomst is eerst: onder welke bodem-, weer- en randvoorwaardelijke omstandigheden verandert de waterbalans en hoeveel?

Dit sluit aan bij de toekomstige maatschappelijke schadeberekening, maar de koppeling naar waterbeheerkosten en waterkwaliteit blijft een apart, data-gated traject. De resultaten mogen niet automatisch worden vermenigvuldigd met het nationale verdichte areaal.

## 6. Concrete werkvolgorde zonder nieuwe projectarchitectuur

1. Reconcileer de actuele data-request-status van het beoogde proefprofiel; selecteer pas wanneer er onderbouwde toestand- en referentiegegevens zijn.
2. Verifieer bij de betrokken bodemfysische onderzoekers welke laboratoriumproeven werkelijk gepaarde dichtheid–retentie–geleidbaarheid-data leveren, inclusief laagdiepte.
3. Controleer of de bestaande SWAP/runoff-configuraties reeds historische verdichting weerspiegelen; leg herkomst en versie vast.
4. Leg de wortelrespons voorlopig apart; test hydrauliek eerst wanneer wortelmechanische relaties ontbreken.
5. Kwalificeer daarna één lokale gepaarde waterbalansrun met identieke forcing, sluitende balans en controle van runoff/drainage/percolatie.
6. Bepaal pas dan of de extra modelinformatie voldoende is om een F2-transfercase of gerichte stoftransportanalyse te rechtvaardigen.

## 7. Beslissing en beperkingen

**Beslissing op documentniveau:** *NOT_READY_FOR_SCIENTIFIC_CURRENT_REFERENCE_RUN* op basis van de in deze sessie gecontroleerde GitHub-data. De repository bevat voldoende structuur en profielcontext om invoeracquisitie gericht voort te zetten, maar nog geen volledig onderbouwd state-pair. Daarom zijn geen hydrologische verschillen, schadepercentages of kosten berekend.

Het causale netwerk v0.7 en het bestaande bewijsregister blijven ongewijzigd. Dit document is een aanvullende readiness-toets, geen nieuwe parameterbron.
