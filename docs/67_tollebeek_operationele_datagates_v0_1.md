# Proef A: operationele datagates en uitvoeringsbesluit

Datum 2026-10-12. Status: REVIEW_DRAFT, geen nieuwe data-admission.

## Geverifieerd tegen bestaande Git-autoriteit

- `src/transfer/volume.py`: alleen gegenereerd bronvolume.
- `src/water_system/dispatch.py`: allocatie van reeds gerouteerde zonevolumes, zonder routing/berging of tijdreeks.
- `src/water_system/energy.py`: energie-identiteit, met expliciete opvoerhoogte en rendement.
- `tests/test_vertical_slice.py`: softwarematige rekenidentiteiten, geen fysische validatie.
- `docs/58_project_architecture_status_v0_1.md`: Tollebeek is een begrensde pilot, geen nationaal transfermodel.
- Issue #36: WER3382-bronhouderroute is reeds uitgewerkt. Niet opnieuw starten voor Proef A.

## Datagates

| Gate | Benodigde inhoud | Wat nu beschikbaar is | Status |
|---|---|---|---|
| G1 | Gebiedsidentiteit en systeemtopologie | OT.02 geometrie en beschrijvingen Kievit/IJsvogel | CONTEXT_AVAILABLE |
| G2 | Gebeurtenisspecifiek referentiehydrogram | Historische KNMI-forcing, maar geen bewezen netwerkhydrogram | NOT_QUALIFIED |
| G3 | Routing en tijdelijke berging | Conceptuele verbindingen, geen dynamisch operationeel model | NOT_IMPLEMENTED |
| G4 | Regelgedrag en gemaaltelemetrie | Nominale/historische capaciteit, geen voldoende actuele operationele reeks | NOT_QUALIFIED |
| G5 | Opvoerhoogte en rendement | Formule aanwezig; geen toegelaten gebeurtenisspecifieke invoer | NOT_QUALIFIED |
| G6 | Current/reference ondergrondverdichting | Bronhouderroute issue #36, geen toegelaten lokale bodemtoestand | BLOCKED_FOR_ATTRIBUTION |

## Uitvoerbare reikwijdte

**Nu:** synthetische, statische dispatch- en energie-QA met expliciete scenario-aannames; bestaande tests plus `tests/test_tollebeek_proef_a_synthetic.py` op de onderzoeksbranch.

**Niet nu:** fysische validatie van Tollebeek-routing, tijdsafhankelijke piekbelasting, verdichtingsattributie of maatschappelijke schadebedragen.

## Aanbevolen volgorde

1. Voer de bestaande en nieuwe unit tests lokaal uit op de onderzoeksbranch. Rapporteer aantallen en eventuele fouten; geen GitHub Actions nodig.
2. Beoordeel of een onafhankelijk gemeten netwerk-/gemaalreeks voor één concrete gebeurtenis aanwezig is. Zonder zo'n reeks geen dynamische Tollebeek-claim.
3. Houd bronattributie en systeemtransfer als twee afzonderlijke kwalificatiebesluiten.
4. Ga voor landelijke offsite-methodiek parallel verder met een kleine watersysteemtypologie en de andere vijf expertsporen; laat Tollebeek geen blokkade voor de volledige studie worden.

## Stopregel

Wanneer G2–G4 niet zijn gekwalificeerd, sluit Proef A als **softwarematige demonstratie met open operationele datagates**. Geen verzonnen routingfactoren, pompuren of eurokosten.
