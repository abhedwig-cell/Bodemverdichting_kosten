# Brontoets hydrologische scenario's: Schipper 2015 en Van der Bolt 2016

**28 oktober 2026 | PRIMARY-METHOD-CHECK | geen nieuwe effecten toegelaten.**

Aansluiting op [document 110](110_broncontrole_hydrologische_ensembles_wenr2811_20261028.md) en het oorspronkelijke [ensembleprotocol](50_evidence_ensemble_protocol_v0_1.md). Geraadpleegde primaire publicaties: Schipper et al. (2015), STOWA 2015-19, https://www.stowa.nl/sites/default/files/assets/PUBLICATIES/Publicaties%202015/STOWA%202015-19.pdf; Van der Bolt et al. (2016), Alterra 2725, DOI https://doi.org/10.18174/387766. De gedetailleerde numerieke controles hieronder zijn voor Schipper rechtstreeks in STOWA 2015-19 gedaan en voor Vlaanderen mede via het WENR-rapport 2811 en het officiële publicatieabstract; het volledige PDF van Alterra 2725 kon in deze sessie niet integraal worden gelezen (WUR eDepot 403). Maak dat onderscheid zichtbaar.

## 1. Schipper et al. 2015, wat werd daadwerkelijk veranderd?

STOWA 2015-19, hoofdstuk 3.3 en figuur 3.2 (gedrukte p.18) onderscheiden een basis-/referentiebodem, een verbeterde en een verdichte bodem; daarbij verschilt niet alleen de bodemverdichting maar kunnen ook organische stof, bewortelingsdiepte en bodemleven deel van het scenario zijn. De bodemkaart-/referentiecategorieën omvatten veldpodzol en ooivaaggrond, gras en snijmaïs, droog/nat, en piekafvoer op een 4-uurs (zomer) of 24-uurs (winter) tijdsvenster. Een reductie in piekafvoer na 'bodemverbetering' is daarmee **niet altijd een geïsoleerd, diep antropogeen verdichtingscontrast**.

Het rapport geeft op p. 18 expliciet aan dat de maaiveldmicroreliëf en helling de weerstand voor oppervlakkige afstroming beïnvloeden. Het vervolg WENR 2811 meldt (bijlage 3, gedrukte p. 113) dat de bodemfysische rekenparameters van verdichte versus verbeterde toestand in Schipper gebaseerd waren op *aannames van een deskundige* (Jan van den Akker), niet op plaatselijk gemeten gepaarde waterretentie en wortelparameters.

**Beoordeling:** de in 2811 samengevatte 10 mm/jaar langjarig en circa 12 mm/jaar onder extreme weersituatie voor snijmaïs zijn **conditionele modeluitkomsten onder scenario-aannames**, geen onzekerheidsinterval, geen causale empirische meetband voor puur 30–100 cm ondergrondverdichting. De piekafvoerpercentages uit figuur 3.2 mogen evenmin met jaarlijkse afstromingsdiepten worden verward.

**Extra relevant voor F4:** Schipper 2015, gedrukte p. 40 (waterkwaliteit), merkt op dat de modelketen SWAP-WOFOST-ANIMO het onderscheid tussen oppervlakkige afstroming en ondiepe interflow onvoldoende goed behandelde om N/P-vrachtveranderingen betrouwbaar af te leiden. Dat is een mechanistische *guardrail*, niet een N/P-effectfactor.

## 2. Van der Bolt et al. 2016, gemeten bodemfysica en gemodelleerde effecten

Officiële publicatiemetadata: 26 percelen, ongestoorde bodemmonsters op twee locaties en drie diepten per perceel; zes percelen met bodemvocht-/grondwatermonitoring, vijf Vlaamse stroomgebieden doorgerekend met SWAP. De uitkomsten zijn dus **meer op gemeten bodemfysische toestanden gebaseerd** dan Schipper 2015, maar de runoff-uitkomst blijft een modelrespons en geen waargenomen verandering in maatschappelijke schade.

WENR 2811, hoofdstuk 3, beschrijft dat de vergelijking verdicht/niet-verdicht wordt opgebouwd uit bodemfysische data en pedotransferfuncties; de ondergrond kan op meerdere diepten verdicht zijn en hydrologische doorwerking is plaats-, klimaat- en profileigenschapafhankelijk. Het officiële abstract van Van der Bolt noemt dat de effecten op stroomgebiedschaal veelal beperkt zijn, met mogelijk grote lokale verschillen. Klimaatscenario's versterken de droogte- en runoff-respons.

**Numerieke broninconsistentie die moet blijven staan:** WENR 2811 **samenvatting** schrijft bij het Vlaanderenvoorbeeld 5 → 14 mm/jaar (**+9 mm/jaar**), terwijl **tabel 1.1** voor het 2008-voorbeeld 4 → 14 mm/jaar (**+10 mm/jaar**) vermeldt. De exacte herkomst en definities van beide voorbeelden moeten in **Alterra 2725** worden gecontroleerd voordat `EV_RUNOFF_VLAANDEREN` als definitief gemeten/berekend contrast wordt behandeld. Dit is niet een reden om de verschillen te middelen tot +9,5 mm/jaar. Gebruik in de tussentijd beide waarden als **niet-gereconcilieerde bronvermeldingen**.

## 3. Beslissing binnen bestaand ensembleprotocol

| Bronlid | Member role | Vergelijkbaarheid | Toegestaan | Niet toegestaan |
|---|---|---|---|---|
| H04_VK_RUNOFF_MAIZE | PROXY / SCENARIO | modelkeuzes + weer + bodemverbeteringsreferentie | magnitude check voor passende modelcontext | 10–12 mm als betrouwbaar nationaal undergrondverlies |
| EV_RUNOFF_VLAANDEREN | PROXY / SCENARIO | gemeten bodemfysische context, modelmatig gebied | afzonderlijke toets van ondergrondmechanisme | definitieve +9 mm zonder 4/5 mm-basiscontrole |
| H07_GRASS_IRRIGATION | BOUND / SINGLE_SOURCE_ONLY | droogjaar, veldpodzol/ooivaaggrond en irrigatieregel | modelgebonden potentiële irrigatievraag | geleverde wateraanvoer of schade-euro |

**Conclusie:** de bronnen bevatten goede *mechanism and scenario evidence*, maar **geen nu toelaatbare uniforme hydrologische schadeband** voor Nederlandse ondergrondverdichting. De oorspronkelijke methodiek was correct om deze als contextafhankelijke proxy/scenario te bewaren.

## 4. Concrete controle voor later

De ontbrekende, werkelijk materiële stap is geen nieuwe SWAP-campagne, maar een bronpagina-voor-bronpagina verificatie van Alterra 2725 voor (a) laagdiepte en dikte van bemonsterde verdichting; (b) de selectie van 'niet-verdichte' referentie; (c) welk klimaatscenario de 4/5 → 14 mm jaarlijks vertegenwoordigt; (d) gebruikte oppervlakkige berging, run-off parameterisatie en schaal van aggregatie. De landelijke meetset en SWAP-executie blijven geparkeerd.

**Status:** `SCHIPPER_METHOD_VERIFIED`; `VAN_DER_BOLT_PRIMARY_ABSTRACT_VERIFIED`; `FLEMISH_NUMERIC_BASELINE_CONFLICT_OPEN`; `NO_NATIONAL_COEFFICIENT`. Geen wijzigingen aan methodische authorities 02/04/49/50/59, de bronregisters, v0.7 of WUR-notitie.
