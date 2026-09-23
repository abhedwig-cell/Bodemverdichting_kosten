# Source code

Deze map bevat gedeelde wetenschappelijke code die niet afhankelijk hoort te zijn van Excel, dashboards of één specifieke pilot.

## Huidig geïmplementeerd

- transfer/volume.py: omzetting van een gekwalificeerd bronverschil in waterdiepte naar gegenereerd volume;
- water_system/dispatch.py: expliciete twee-zone/twee-pomp allocatiesemantiek zonder verborgen availability- of assist-defaults;
- water_system/energy.py: pompenergie met expliciete head en efficiency.

De functies zijn generiek geschreven. De huidige tests gebruiken de Tollebeek vertical slice als eerste concrete toepassing, maar de code mag Tollebeek-specifieke waarden niet als universele defaults vastleggen.

## Nog geen geïmplementeerde package

Hydrologie/modeladapters, waardering en I/O/application services zijn in de architectuur beschreven, maar bestaan nog niet als algemene src-packages. Documentatie mag zulke toekomstige namespaces niet presenteren alsof ze al geïmplementeerd zijn.

Nieuwe code hoort pas naar src/ wanneer een formele relatie of adapter daadwerkelijk herbruikbaar is. Een case-specifieke acquisitie- of reviewtool kan onder tools/ blijven.

Do not duplicate scientific equations independently in multiple interfaces when a shared tested implementation is possible.
