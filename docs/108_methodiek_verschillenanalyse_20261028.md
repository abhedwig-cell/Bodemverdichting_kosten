# Verschillenanalyse oorspronkelijke methodiek versus literatuursynthese oktober 2026

**28 oktober 2026 | METHOD_RECONCILIATION / DECISION PROPOSAL | bestaande methodiek blijft leidend**

Bronautoriteit: [49 effect-pathwaymatrix](49_project_effect_pathway_matrix_v0_1.md), [50 evidence-ensembleprotocol](50_evidence_ensemble_protocol_v0_1.md), [59 beslisschema](59_bespreekschema_werkwijze_en_einddoel_v0_1.md), [02 theorie](02_theoretical_framework.md), [04 formeel model](04_formal_model.md). Nieuwe informatie: [89 causaal netwerk v0.7](89_causaal_netwerk_v0_7.md), [93 primaire literatuurtoets](93_primaire_broncontrole_hydrologie_gewas_N2O_20261028.md), [101 Defra-audit](101_defra_appendix_h_occurrence_volledige_methodereconstructie_v0_1.md), [102 zes categorieën](102_offsite_zes_categorieen_resultatenmatrix_v0_1.md), en [103–107 gerichte brontoetsen](107_waterbeschikbaarheid_middelen_bodemleven_broncontrole_20261028.md).

## 1. Wat NIET opnieuw ontwerpen

De leidende methodiek bestaat al en wordt inhoudelijk bevestigd:

1. conditioneel onderzoek per bodem, landgebruik, toestand, plaats/tijd en relevante omstandigheden;
2. passend CURRENT/REFERENCE-contrast en expliciete attributie;
3. minimum necessary computation: direct empirisch bewijs → simpele berekening → procesmodel alleen voor materiële leemte;
4. afzonderlijke overdracht naar de feitelijke off-site receptor;
5. scheiding fysieke uitkomst, monetair waardeerbare gevolgen en niet-monetair te beoordelen effecten;
6. effect-ensembleleden blijven gescheiden waar comparator, diepte, context, weersituatie en methode verschillen;
7. expliciete within-source en between-source onzekerheid;
8. geen automatische sommatie van private kosten, publieke uitgaven en maatschappelijke welvaartsschade.

Het formele model en het ensembleprotocol hebben op deze punten geen vervanging nodig. Landelijke puntdata en SWAP staan voorlopig geparkeerd.

## 2. Werkelijke verschillen en beoordeling

| Vraag | Oude methode | Nieuwe bevinding | Actie |
|---|---|---|---|
| Opbouw effectroutes | Document 49 gebruikt F1–F6 als **stappen in hydrologische causaliteit** | Document 89/102 gebruikt zes *maatschappelijke effectcategorieën* | **Terminologie herstellen**: oude F1–F6 blijven pathway-ID's; zes categorieën krijgen eigen labels EC1–EC6 in beschrijvende views, niet als nieuwe V-codes of schemawijziging |
| Waterkwaliteit | Oud F6 'linked later' | Vrachtmetingen voor rijsporen en Nederlands preferent transport geven concrete routekennis, maar niet subsoil-attributie | Maak beoordeling nu volwaardig; kwantificering blijft data-gated |
| Broeikasgassen | Niet zelfstandig zichtbaar in oude F1–F6-opsomming | V23–V29 en gecontroleerde N₂O-/gasdiffusieliteratuur | Toon als effectcategorie EC3 met eigen causaliteit en nettoflux; geen generieke emissiecoëfficiënt |
| Bodemleven | Niet zelfstandige monetisatiepost | V36–V42; ecologische functie en vertraagde structuurfeedback | Toon zelfstandig als EC6, maar V42 is geen apart jaarlijks optelbare schadepost |
| Hydrologische schade | Deels benchmark/transfer-gated | Defra H feitelijk 7%-proportionaliteit, geen afgeronde stroomgebiedschadeberekening | Bevestig verbod op runoff% = schade%; geen herontwerp |
| Waterbeschikbaarheid | O3 en oud F5 scheiden potentiële vraag en feitelijke levering | Literatuur bevestigt dat profielwater, beregeningsvraag, aanbod en schaarste apart zijn | Geen wijziging, wel expliciete cross-reference |
| Gewasbeschermingsmiddelen | Oud F6 gezamenlijk met nutriënten | Transport is stofspecifiek; verdichting kan bypass verlagen terwijl runoff stijgt | Splits EC4 en EC5 **in effectrapportage**, niet noodzakelijk in nieuw rekenobject |
| Effectrange en aggregatie | Ensembleprotocol definieert COMPARABLE, BOUND, SCENARIO, INCOMPATIBLE | Studies betreffen vaak topsoil, wheel tracks, gestandaardiseerde laboratoriummonsters | Klasse `INCOMPATIBLE_SET` of `PROXY` toepassen in bestaande register; geen middelen |
| Niet-gemonetariseerd | Document 59 laat fysiek, kwalitatief en not-estimable toe | Ecologische effecten mogen niet verdwijnen uit onderzoeksprioriteit | In eindrapport altijd zichtbaar naast geldelijk subtotaal; geen verplichte euroomzetting |

## 3. Noodzakelijke naamreconciliatie

**Belangrijk:** `F1` in document 49 is *perceelsrunoff/drainage*, terwijl `F1` in de aanvullende CSV `evidence/offsite_results_matrix_v0_1.csv` is gebruikt voor de **categorie wateroverlast**. Op vergelijkbare wijze hebben F2–F6 verschillende betekenissen. Het is dus fout om deze twee F-codefamilies automatisch te joinen of bij reken- en evidence-resultaten dezelfde sleutel te gebruiken.

**Beslissing voor huidige documentatie:** hanteer de expliciete prefixes
- `PATH_F1`–`PATH_F6`: bestaande stappen uit document 49, ongewijzigde inhoud en bestaande technische keys;
- `EC1`–`EC6`: zes maatschappelijke off-site categorieën (EC1 wateroverlast; EC2 wateraanvoer en -beschikbaarheid; EC3 N₂O/CH₄; EC4 N/P-waterkwaliteit; EC5 middelenwaterkwaliteit; EC6 bodemleven/ecologie).

Dit zijn **uitsluitend presentatie-aliases** in deze analyse totdat de formele data-/systeemcontracten op downstream referenties zijn onderzocht. Geen automatische hernummering in model of registers.

## 4. Waar in bestaande methodiek inpluggen?

- **EC1 wateroverlast:** PATH_F1 → PATH_F2 → PATH_F3/PATH_F4, met afzonderlijke hydraulische transfer en schadefunctie.
- **EC2 wateraanvoer/beschikbaarheid:** O3 + PATH_F5, regionale vraag/levering gescheiden van privéberegening.
- **EC3 N₂O/CH₄:** gedeelde bodemtoestand → redox/gastransport → netto stofspecifieke flux → klimaatwaardering, maar niet uit runoff afleiden.
- **EC4 N/P:** gedeelde hydrologie + biogeochemie → stof/route-specifieke vracht → ontvangend water → extra schade.
- **EC5 middelen:** gedeelde hydrologie + stofeigenschappen → vracht per route → receptor/ecotoxicologische gevolgen.
- **EC6 bodemleven:** bodemstructuur → biologische toestand/functies en mogelijke externe ecologische receptor; biologische terugkoppeling V42 op langere termijn, niet een bijkomende onafhankelijke jaarlijkse kostenfactor.

De oude F1–F6 zijn dus veelal **herbruikbare interne processtappen** voor meer dan één van de maatschappelijke categorieën, geen zes afzonderlijke optelbare posten.

## 5. Beslissing over bijstellen versus behouden

**BEHOUDEN:** docs 02, 04, 49, 50, 59 als methodische autoriteiten, zonder versievervanging. **VERDUIDELIJKEN:** naamconflict tussen pathway-F-codes en de zes effectcategorieën in de werkmatrix en toelichtingen. **AANVULLEN:** effectrapportage voor EC3, EC5, EC6 en expliciete niet-monetaire eindpunten. **NIET DOEN:** nieuwe kostformules, schadeparameters, datasets, numerieke onzekerheidspercentages of schema-migratie verzinnen voordat concrete gekwalificeerde inputs beschikbaar zijn.

**Kleinste vervolgstap:** werk uitsluitend de categorie-identificatie en een review-view op `evidence/offsite_results_matrix_v0_1.csv` bij, met behoud van oude records en expliciet compatibiliteitsbesluit. Daarna de bestaande ensemblekwalificaties daadwerkelijk gebruiken voor de inhoudelijke effecten.

## 6. Open beslispunten voor experts

1. Zijn de zes maatschappelijke categorieën voldoende voor volledige effectrapportage, ook als geen geldwaarde beschikbaar is?
2. Welke causale overlappen tussen on-site beregening/bedrijfskosten en regionale wateraanvoer, en tussen waterkwaliteit/ecologie, moeten in de einduitkomst apart worden behandeld?
3. Welke broncontrasten betreffen aantoonbaar ondergrond in plaats van bovengrond of alleen rijsporen?
4. Is de referentietoestand per bodemcontext voldoende expliciet voor interpretatie van een schadeband?
5. Welke additionele empirische gegevens leveren daadwerkelijk reductie van onzekerheid, in plaats van alleen meer bronnotities?

**Status:** METHOD_PRESERVED; REPORTING_GAP_IDENTIFIED; ID_COLLISION_IDENTIFIED; NO SCIENTIFIC ADMISSION. Geen aanpassing van de canonieke input, huidige Word-notitie of v0.7.
