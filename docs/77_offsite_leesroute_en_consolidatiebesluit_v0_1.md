# Leesroute en consolidatiebesluit off-site onderzoek

**Datum:** 12 oktober 2026. **Status:** REVIEW_DRAFT. Dit document maakt onderscheid tussen documenten voor de expertgroep en interne onderbouwing.

## Leesroute

1. **Begin hier:** [76_reviewpakket_expertgroep_offsite_v0_1.md](76_reviewpakket_expertgroep_offsite_v0_1.md). Overzicht in gewone taal en hoofdfiguur.
2. **Bekijk de causale relaties:** [75_offsite_causaal_netwerk_en_effectmatrix_v0_1.md](75_offsite_causaal_netwerk_en_effectmatrix_v0_1.md). Iedere pijl C01–C14 is gekoppeld aan één tabelregel.
3. **Verdiep per effect:** [61_offsite_effectketens_toetsingsdossiers_v0_1.md](61_offsite_effectketens_toetsingsdossiers_v0_1.md). De zes onderzoekslijnen en open vragen.
4. **Onderliggende projectautoriteit:** [02_theoretical_framework.md](02_theoretical_framework.md) en [49_project_effect_pathway_matrix_v0_1.md](49_project_effect_pathway_matrix_v0_1.md).

## Welke documenten zijn primair?

| Bestand | Rol | Besluit |
|---|---|---|
| 76 | Toegankelijke reviewtekst | Primair voor expertgroep |
| 75 | Volledige figuur en C01–C14-matrix | Technische bijlage |
| 61 | Dossiers per effect | Achtergrond / expertverdieping |
| 60, 62, 64–74 | Werknotities, bronnenverkenningen, voorlopige besluiten en pilotgrenzen | Bewaren als werkhistorie; niet apart verspreiden als reviewpakket |
| test_tollebeek_proef_a_synthetic.py | Synthetische softwarechecks | Behouden, niet presenteren als fysische validatie |

## Kritische controlepunten vóór samenvoeging

- Controleer dat elke C-code exact één relatie of expliciet gemarkeerde bundel representeert. C05 en C09 zijn nog bundels; C14 is gemeenschappelijk voor alle eindpunten.
- Controleer of de gebruikte literatuur daadwerkelijk het bedoelde diepte- en behandelingscontrast ondersteunt. Abstract-screening is geen full-text kwalificatie.
- De hoofdfiguur is een **didactische vereenvoudiging**. Pijlen in deze figuur hebben geen bewijsstatus; daarvoor is de matrix nodig.
- Review de rol van bodembiodiversiteit: lokaal ecologisch effect versus zelfstandige off-site receptor.
- Controleer de exacte Python-testsuite en GitHub-status voordat de PR gereed wordt verklaard.
- Laat de expertgroep prioriteren op potentiële relevantie, bewijssterkte en informatiewinst; niet alleen op geldwaarde.

## Voorgestelde Git-afhandeling

Deze branch en draft PR blijven vooralsnog open. De 15 oorspronkelijke onderzoeksdocumenten worden **niet verwijderd of automatisch tot canonieke autoriteit verheven**. Eerst expertfeedback en technische validatie, daarna een afzonderlijk besluit welke conceptdocumenten in `main` worden opgenomen en welke als historische werknotities blijven bestaan.

Geen nieuwe schadecoëfficiënten of numerieke claims worden met deze consolidatie toegelaten.
