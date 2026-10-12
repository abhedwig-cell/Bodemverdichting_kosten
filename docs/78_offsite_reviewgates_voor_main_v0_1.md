# Technische reviewgates voor concept-PR off-site

**Status:** REVIEW_CHECKLIST, 12 oktober 2026. Geen formele toelating van wetenschappelijke resultaten.

## Consolidatie

De expertgroep krijgt in eerste instantie uitsluitend `docs/76_reviewpakket_expertgroep_offsite_v0_1.md`. De pijlen C01–C14 zijn uitgelegd in `docs/75_offsite_causaal_netwerk_en_effectmatrix_v0_1.md`. De zes onderzoeksdossiers staan in `docs/61_offsite_effectketens_toetsingsdossiers_v0_1.md`. Overige documenten blijven werkhistorie.

## Nog open vóór main

1. **Causaliteit:** iedere pijl en vooral de gebundelde C05, C09 en C14 op subvragen beoordelen; geen automatische interpretatie als bewezen schade.
2. **Bronnen:** onderscheid volledige broncontrole van abstracts, projectdocumentatie en mechanistische plausibiliteit. Geen nieuwe kwantitatieve bronclaims zonder intended-use review.
3. **Figuur:** de hoofdfiguur is didactisch; voor bewijssterkte geldt de technische matrix. Controleer Mermaid-rendering en links.
4. **Software:** voer de exacte `tests/test_vertical_slice.py` en `tests/test_tollebeek_proef_a_synthetic.py` uit. De eerder handmatig gereconstrueerde rekencontrole is geen volledige testsuite.
5. **Tollebeek:** proef A blijft softwarematig, geen gekwalificeerde wateroverlast- of verdichtingsschade. G2–G4 zijn operationele datagates.
6. **Review:** expertgroep bevestigt werkverdeling, ontbrekende effecten en onderzoeksprioriteiten voor 2026.

## Acceptatie

De draft PR wordt pas merge-klaar verklaard na technische testresultaten en een expliciet besluit over de status van de literatuurclaims en expertfeedback. Tot dan geen automatische wijziging van `main`, evidence-registers of rekenparameters.
