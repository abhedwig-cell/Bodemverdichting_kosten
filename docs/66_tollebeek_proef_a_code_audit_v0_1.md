# Tollebeek proef A: code-audit en testgrenzen

**Status:** SOFTWARE_REVIEW_ONLY, 2026-10-12. Beoordeling op basis van broncode en bestaande tests in `main`; tests zijn in deze GitHub-sessie niet lokaal uitgevoerd. Geen nieuwe fysische claims.

## Gecontroleerde implementatie

- `src/transfer/volume.py`: `generated_increment_m3(area_ha, delta_runoff_mm)` berekent uitsluitend **gegenereerd** bronvolume; accepteert negatieve verschilafvoer, bewaart null.
- `src/water_system/dispatch.py`: `two_zone_two_pump_dispatch` verdeelt **reeds gerouteerde** volumes over twee pompen; assist, beschikbaarheid en responstijdvenster zijn expliciet. Pompuren worden uit volume/gemiddelde beschikbare capaciteit afgeleid.
- `src/water_system/energy.py`: `pump_energy_kwh` berekent energie met expliciete opvoerhoogte en rendement.
- `tests/test_vertical_slice.py`: controleert volume-identiteit, onbekend/nul-semantiek, assistverdeling, fractionele grenzen en energie-identiteit met synthetische software-QA.

## Belangrijkste bevinding

De huidige dispatchfunctie bevat **geen dynamisch routing- of bergingsmodel**. `response_window_h` bepaalt slechts de ratio van benodigde pompuren tot tijdvenster. Twee hydrogrammen met identiek volume maar verschillende piektiming zijn voor deze functie niet onderscheidbaar als de overige invoer gelijk is. Een claim over timinggevoelige wateroverlast of berging is daarmee niet ondersteund.

## Minimale extra softwarechecks vóór proef A

1. Nul-increment tegenover referentie: bereken verschillen door **twee volledige dispatch-scenario's** met gelijke operationele condities te vergelijken, niet door alleen een losse incrementele volumeprikkel als totaalvolume aan te bieden.
2. Massabehoud in dispatch: som van primaire en secundaire pompvolumes moet gelijk zijn aan som van de twee ingevoerde **gerouteerde** zonevolumes.
3. Monotonie onder vaste operationele parameters: extra gerouteerd volume mag geen negatieve incrementele pompvolumeclaim geven; capaciteitsspanning blijft een indicatieve ratio.
4. Null-propagatie: ontbrekende assist, capaciteit, opvoerhoogte of rendement mag geen numerieke uitkomst voor de daarvan afhankelijke grootheid opleveren.
5. Energie-identiteit: pas toepassen op werkelijk toegewezen pompvolumes; scenario-economie alleen met expliciete kostenbasis.
6. Timing/berging: markeer als **NOT_IMPLEMENTED**; geen fictieve scenario-output uit de huidige volumefunctie.

## Kleine vervolgbeslissing

De eerste softwarematige proef kan beperkt blijven tot een **statische scenariovergelijking** van gerouteerde volumes, pompuren en energie onder expliciet synthetische invoer. Pas als aangetoond wordt dat timing/berging een relevante onzekerheid in het beoogde eindpunt is én er toetsbare gegevens zijn, is een afzonderlijk dynamisch routingmodel gerechtvaardigd.

Geen productiecode gewijzigd. Geen GitHub Actions nodig voor deze audit. Geen claim van geslaagde uitvoering van tests.
