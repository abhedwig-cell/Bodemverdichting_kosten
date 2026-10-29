# BoVer-broncontrole: rapporten 3404, 3225 en 3069

**28 oktober 2026 | SOURCE_IDENTIFIED / PARTIAL_METHOD_REVIEW | geen kwantitatieve parameter toegelaten**

Vervolg op [readiness 95](95_swap_first_pair_readiness_20261028.md) en [SWAP-protocol 94](94_swap_verdichtingsprofielen_brongetoetst_protocol_v0_1.md). Deze notitie registreert **direct bevestigde gegevens uit publiek beschikbare WUR-metadata en geïndexeerde primaire tekstfragmenten**. De PDF van rapport 3404 is in deze sessie niet volledig toegankelijk geweest (downloadblokkade); tabellen, fits, statistiek en de resultaten van alle appendices zijn daarom **niet** integraal geverifieerd. Beschrijf ze niet als vastgesteld.

## Geïdentificeerde primaire rapporten

| Bron | Identificatie | Bevestigde functie |
|---|---|---|
| BoVer eindrapport | Bakema, Bakker, Heinen, Van Egmond & Van den Elsen (2024), WENR 3404, DOI [10.18174/675719](https://doi.org/10.18174/675719), 173 p. | Veld-, kolom- en laboratoriumexperimenten met ondergrondverdichting, plantontwikkeling en bodemfysica |
| Literatuurstudie BoVer | Bakema, Bakker, Cruijsen, Van Egmond, Van den Elsen, Heinen & Schneider (2023), WENR 3225, DOI [10.18174/583342](https://doi.org/10.18174/583342) | Concepten voor samenhang bulkdichtheid, waterretentie, hydraulische geleidbaarheid, zuurstofdiffusie en wortels |
| Voorkomen / opheffen | Bakema, Van den Akker & Van Egmond (2021), WENR 3069, DOI [10.18174/542089](https://doi.org/10.18174/542089) | Voorkomen en bestrijden van ondergrondverdichting, herstel en Flevoland-context |

## Rapport 3404: relevante primaire bronpassage

In **appendix A3, p. 71 volgens de gedrukte rapportpaginering**, staat expliciet dat de studie de invloed van droge bulkdichtheid op waterretentie en waterdoorlatendheid wil onderzoeken en de relatie tussen bulkdichtheid en **Mualem–Van Genuchtenparameters** wil toetsen. Volgens het methodefragment is voor de zandbehandeling homogeniseerde bovengrond verzameld van de Bornsesteeg in Wageningen. Daarmee is de onderzoeksopzet relevant voor **V01–V04**, maar het fragment bewijst nog niet dat het gemeten materiaal representatief is voor blijvend verdichte ondergrond tussen 30 en 100 cm.

Het eindrapport vermeldt bovendien experimenten met wortelontwikkeling en dat wortels op verdichte bodems kunnen reageren of zich deels aanpassen. Dit raakt **V03, V05–V07 en V42**, maar levert zonder afzonderlijke methode- en resultatentoets geen algemeen gewasverliespercentage of herstelcoëfficiënt.

**Belangrijk kritisch onderscheid:** een proef die homogeniseerde *bovengrond* met kunstmatig verhoogde dichtheid gebruikt kan waardevolle procesinformatie leveren, maar is niet automatisch directe validatie voor de structuur, anisotropie en macroporiën van een reeds jarenlang verdichte ondergrond.

## Voorlopige kwalificatie per beoogd gebruik

| Beoogd gebruik | Toestand | Waarom |
|---|---|---|
| Onderbouwen dat laboratoriumrelaties bulkdichtheid–retentie–geleidbaarheid zijn onderzocht | **SOURCE_CONFIRMED** | Appendix A3 vermeldt expliciet de onderzoeksopzet |
| Selecteren van welke MVG-parameters relevant zijn voor de SWAP-profielvergelijking | **METHOD_CANDIDATE** | Bijlage onderzoekt parameterrelaties; tabelresultaten en fitkwaliteit nog te controleren |
| Overnemen van numerieke regressies / fits uit 3404 | **BLOCKED_PENDING_FULL_TABLE_REVIEW** | Ruwe waarden, meetdiepten, eenheden, betrouwbaarheidsmarges en geldigheidsbereik nog niet gecontroleerd |
| Directe Nederlandse ondergrond-coëfficiënt voor 30–100 cm | **NOT_SUPPORTED_YET** | Onder meer proefmateriaal (bovengrond bij zandexperiment), diepte en fabricage van monsters behoeven toetsing |
| Aantonen van universeel opbrengstverlies of biologisch herstel | **NOT_SUPPORTED** | Verschillende mechanismen, gewassen en tijdschalen |

## Nu gericht te controleren in de primaire bronnen

1. **Appendix A3 (3404):** exacte behandeling per bodemsoort; dichtheidstraject, monsterherkomst/diepte, monstervoorbereiding, meetprotocol en metingen van theta(h), Ks en K(h).
2. **Tabellen / figuren A3:** welke MVG-parameters statistisch samenhangen met droge bulkdichtheid, inclusief richting, regressie, replicatie en onzekerheid; zo nodig de uitkomst per bodemtype splitsen.
3. **Kolom- en veldproeven (3404):** wortelgroei, water-/zuurstofstress, hydrologische randvoorwaarden en de mate waarin afzonderlijke mechanismen zijn geïsoleerd.
4. **Literatuurstudie 3225:** door de auteurs vooraf voorgestelde functies en de precieze grens tussen mechanistische hypothese en Nederlandse validatie.
5. **Ruwe data:** voor eventuele modelinvoer bij voorkeur gepaarde retentie-/geleidbaarheidsmetingen, dichtheid, monsteridentiteit en eenheden in plaats van alleen een fitvergelijking.

## Gevolg voor de eerdere data-aanvraag

[Het bestaande laboratoriumgegevensverzoek](../data_requests/laboratorium_verdichting_hydraulische_respons_v0_1.md) en [issue #66](https://github.com/abhedwig-cell/Bodemverdichting_kosten/issues/66) blijven nuttig, maar moeten **eerst expliciet naar BoVer/WENR 3404 en appendix A3 verwijzen**. Vraag alleen ontbrekende oorspronkelijke gegevens wanneer vaststaat wat het rapport al publiceert. Er is nog geen reden om een volledig nieuwe acquisitiecampagne te starten.

## Besluit

Rapport 3404 is een **primaire bronkandidaat van hoge relevantie** voor de SWAP-parametrisatie, maar de stap van rapport naar toegelaten profielparameters is nog niet gezet. Het causale netwerk v0.7 en de vier canonical evidence-registers blijven ongewijzigd. Eerst volledige bronverificatie; daarna eventueel één fysisch samenhangende diagnostische proef.
