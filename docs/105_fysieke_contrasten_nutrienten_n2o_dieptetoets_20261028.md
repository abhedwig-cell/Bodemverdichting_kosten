# Gerichte kwantitatieve contrasten: wat kan en mag de nationale schaderaming in?

**28 oktober 2026 | SOURCE-SCOPED FINDINGS / NO NATIONAL ADMISSION**

Vervolg op [resultatenmatrix v0.1](../evidence/offsite_results_matrix_v0_1.csv), [document 103](103_gerichte_bewijstoets_n2o_nutrienten_wateroverlast_20261028.md) en [document 104](104_kwantitatieve_contrasttoets_n2o_en_harde_datagrenzen_20261028.md). Doel is nu niet een nieuw raamwerk, maar **concrete experimentele contrasts én expliciete uitsluitingen** vast te leggen. Bronnen hieronder zijn externe publicatiepagina's/abstracts, geen integraal herberekende onderzoeksdatasets.

## A. Nieuwe fysieke kwantitatieve N/P-studies

| Referentie | Werkelijk contrast | Kwantitatief | Wat mag worden geconcludeerd? | Wat mag niet? |
|---|---|---|---|---|
| Deasy et al. 2009, *Mitigation Options for Sediment and Phosphorus Loss from Winter-sown Arable Crops*, Journal of Environmental Quality 38, 2121–2130, https://doi.org/10.2134/jeq2009.0028 | Verdichte rijsporen losmaken versus conventionele rijsporen, hellingproeven in UK gedurende vijf site-years | Gemiddelde afname **1,06 kg totaal-P/ha** volgens abstract. Interpretatie van tijdseenheid/denominator alleen zoals beschreven in paper: een gemiddelde over vijf site-years, niet vijf afzonderlijke jaarlijkse waarnemingen van ondergrondschade | DIRECT_ROW_TRACK_TP_RESPONSE; omvang aan lokale maatregelen en hydrologie gebonden | Niet `subsoil_30_100cm_delta_P`, niet landelijk Nederland |
| Quinton et al. 2024, *Mitigation measures designed to reduce soil compaction decrease the surface runoff, soil erosion and phosphorus losses from tramlines in agricultural fields*, Soil Use and Management 40, e13158, https://doi.org/10.1111/sum.13158 | Vijf Britse akkerlocaties met gecontroleerde rijsporen; maatregelen met zeer flexibele band, eg of oppervlakteprofiler; Gerlach-goten, event-gestuurde afvoerbemonstering | Total-P-fluxen in waargenomen rijspoorplots **0,8–3,9 kg/ha/jaar**; sediment **0,5–4,5 Mg/ha/jaar**. Dit zijn **belastingsniveaus**, niet overal het verschil met een niet-verdichte referentie | ROUTE_MEASURED; oppervlakkige afstroming, sediment en TP in rijsporen | Niet een ondergrondverdichtingsfactor. Eg-ingreep verandert bovenste **5–7 cm**, geen isolatie van ondergrond |
| Wesström & Joel 2022, *Effects of drainage system renewal on nutrient leaching and crop yield*, https://doi.org/10.13031/ids.202200039 | Oude drainage versus verschillende verbeterde drainageontwerpen op kleigrond | Eerste jaren: drainvernieuwing kan **N-vracht vergroten terwijl P-vracht daalt**, volgens abstract | ROUTE_SIGN_COUNTEREXAMPLE: routing en drainage veranderen N en P niet noodzakelijk gelijkgericht | Geen directe verdichtingsproef |
| Jokinen et al. 2024, *The effects of improved subsurface drainage on runoff and nitrogen leaching from a clayey field section*, https://doi.org/10.1002/ird.2965 | Verbeterde drainage in klei, vóór/na en referentiesecties | Metingen van waterafvoer, NO3-, NH4- en totaal-N-vrachten; 7 jaar vóór en 4 jaar na aanpassing volgens studie | Direct relevante methode voor flux × concentratie en contrasterende routeafvoer | Niet interpretabel als uitsluitend verdichting |

**Conclusie F4:** in de wetenschappelijke literatuur bestaan direct gemeten fysieke fosforcontrasten voor **rijspoorgerelateerde oppervlakkige verdichting**. Dat is beter dan alleen een causale hypothese, maar het gaat niet om diepere ondergrondverdichting. De nationale F4-kwalificatie blijft derhalve `NOT_ESTIMABLE`.

## B. Nieuwe informatie over N₂O uit Denemarken

1. **Bommisetty et al. 2026**, preprint vanaf 30 mei 2026 op SSRN, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6854021, *Influence of tillage intensity and soil compaction on N2O emissions under field conditions*: twee Deense sites, meerdere bewerkingssystemen, additioneel wielspooreffect op één site; 2023–2025. De journalabstract vermeldt significant hogere emissie bij ploegen versus direct seeding in één periode en andere niet-significante intervallen. Dit **is een combinatie van bodembewerking en rijspoorbehandeling**, geen isolatie van een verdichte 30–100 cm-laag. Volledig paper niet toegankelijk in deze ronde. **CANDIDATE_FIELD_EMISSION, NOT_SUBSOIL_ONLY.**
2. **Bimantara et al. 2026**, https://doi.org/10.1016/j.still.2026.107323, *Tractor-induced soil compaction drives nitrous oxide emissions*. Aarhus vermeldt journalvolume **december 2026**, maar een onafhankelijke index vermeldt een beschikbaar artikel op **9 juni 2026**. **Publicatiestatus en online-first-datum moet worden gereconcilieerd**, dus niet zonder meer van alle bewijs van vóór 28 oktober uitsluiten op grond van het december-journalvolume. Studie: 10 fluxkamers, wielspoor versus naastgelegen bodem, eerste 0–5 cm kernen. In samenvatting is de cumulatieve N₂O-flux in wielsporen circa 4,8 maal die van controle. Dit is **een veldcontrast van wielsporen en topsoilstructuur, niet een geïsoleerd subsoilcontrast**.
3. **Geoderma 2026**, *Nitrous oxide emissions from digestate as influenced by soil compaction and water dynamics*, https://doi.org/10.1016/j.geoderma.2026.117970, publicatie september 2026. De onderzoekers rapporteerden dat emissierichting en tijdverloop afhangen van digestaatgiften, vocht en hervernatting; **topsoil** werd bemonsterd en de analyses konden geen constante verhoging door verdichting alleen verklaren. Geen ondergrond-emissiefactor.

**Conclusie F3:** meer onafhankelijke veldgegevens maken wielspoor/topsoil-emissies aannemelijk, maar ze reduceren het identificeerbaarheidsprobleem van **ondergrond-specifieke** netto emissies niet voldoende. Pulido-Moncada (2024) blijft primaire kandidaat voor ondergrondmechanisme (poriën/gasdiffusie), niet voor een landelijke veldflux.

## C. Wateroverlast: kwantitatieve rijspoorflux geen overstromingsschade

Quinton et al. en Deasy et al. tonen een meetstrategie om afstroming uit specifieke rijsporen en sediment-/P-vrachten per gebeurtenis te verzamelen. Zij hebben geen direct toepasbaar `delta_damage_eur` van Nederlandse ondergrondverdichting berekend. De vorige identificatieketen `compaction -> q_edge(t) -> transfer -> peak -> exposure -> damage` blijft de grens.

**Niet extrapoleren:** 1,06 kg TP/ha (rijspoormaatregel) × totale Nederlandse verdichte hectares; en niet 4,8 maal N₂O in wielsporen × Nederlandse landbouw-N₂O-baseline. Beide zouden oppervlakte-, diepte- en behandelingsoverdracht veronderstellen die de studies niet onderbouwen.

## D. Beslislog

| Vraag | Antwoord nu | Actie |
|---|---|---|
| Zijn er directe gemeten P-vrachten verbonden aan oppervlakkige verdichting? | **Ja**: Deasy en Quinton, rijspoorplots en maatregelen | Behoud als directe maar **topsoil/wheel-track-specific** empirische evidence |
| Zijn er extra Deense netto N₂O-veldcontrasten? | **Ja**: verschillende recent gepubliceerde of als preprint beschikbare studies | Afzonderlijk classificeren naar treatment, diepte, site en jaar, niet poolen |
| Kunnen we F3/F4 monetariseren voor Nederlandse ondergrond? | **Nee, nog niet** | Eerst subsoil-behandelingscontrast en transport/uitstoot naar receptor |
| Is F1 nu kwantitatief via Nederlandse wateroverlast mogelijk? | **Nog niet** | Perceels-/afvoer- en beheersysteemdata voor een concrete case, geen Defra-proportionaliteit |

**Bronstatus:** primary full texts Deasy/Quinton/Jokinen niet volledig statistisch herbeoordeeld; samenvattingen en methodesecties van publicatiepagina's gecontroleerd. Geen nieuwe schadefactoren admitted. Geen wijzigingen aan causaal netwerk v0.7, matrix v0.1 of WUR-notitie.
