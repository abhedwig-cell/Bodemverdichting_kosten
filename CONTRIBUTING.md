# Bijdragen aan Bodemverdichting_kosten

Deze repository is de canonieke projectstaat voor theorie, formeel model, datamodel, implementatie, evidence en kwalificatie. Excel-workbooks en dashboards zijn afgeleide review-artifacts.

## Voor je begint

Lees eerst:

1. `docs/00_colleague_reader_guide.md`
2. `docs/14_documentation_status_a_light.md`
3. `docs/18_status_a_light_checkpoint_v0_1.md`

Gebruik daarna de documentatiekaart in `docs/README.md` voor het deel van het project waaraan je werkt.

## Werk per laag

Maak bij een wijziging expliciet welke laag verandert:

- theorie / inhoudelijke begrippen;
- conceptueel model;
- formeel model of vergelijking;
- datamodel / veldbetekenis / dataset-grain;
- implementatie;
- evidence / claim / qualification;
- artifact- of applicatieweergave.

Een wijziging in één laag kan een reviewtrigger voor aangrenzende lagen zijn. Een nieuwe vergelijking kan bijvoorbeeld schema-, code-, test- en traceability-aanpassingen vereisen.

## Wetenschappelijke regels

- `unknown` blijft onbekend en wordt niet stilzwijgend `0`;
- een bronfeit is niet automatisch een projectclaim;
- een projectclaim is niet automatisch gekwalificeerd voor iedere toepassing;
- historische of lokale waarden worden niet zonder expliciete kwalificatie als huidige Nederlandse parameter gebruikt;
- voeg geen numerieke default toe alleen om code, Excel of een scenario te laten draaien;
- current/reference attributie moet matched zijn: alleen de bedoelde toestand verandert;
- generated runoff, field-edge delivery, network routing en pumped volume blijven verschillende grootheden;
- budgetkosten en maatschappelijke welvaartseffecten blijven onderscheiden.

## Evidence-wijzigingen

Nieuwe inhoudelijke evidence doorloopt waar relevant:

`source → evidence item → claim → qualification`

Gebruik stabiele IDs en houd guardrails expliciet. Pas bestaande evidence niet aan om een gewenste modeluitkomst te ondersteunen; voeg een nieuwe bronversie, interpretatie of kwalificatie toe wanneer de betekenis echt verandert.

## Formeel model en code

Als wetenschappelijke semantiek verandert:

- werk `model/equations.csv` bij wanneer een formele relatie verandert of bijkomt;
- werk `model/traceability.csv` bij wanneer de capability-keten verandert;
- voeg of wijzig tests;
- documenteer wat de test bewijst en wat niet.

Softwaretests met synthetische fixtures kwalificeren implementatiesemantiek, niet automatisch de fysieke werkelijkheid.

## Datamodel en workbooks

Canonical veldbetekenis hoort in `schema/`, niet alleen in Excel. Een workbook mag uitleg, data dictionary en views genereren uit het schema, maar mag geen eigen verborgen betekenis introduceren.

Voor datasets geldt bij voorkeur: één tabel = één duidelijk dataset-object met expliciete grain en sleutel.

## Branches en pull requests

Gebruik een korte branch die de echte beslissurface beschrijft, bijvoorbeeld:

- `work/theory-...`
- `work/data-model-...`
- `work/evidence-...`
- `work/<capability>-...`

Maak niet voor iedere kleine tekstcorrectie een nieuwe wetenschappelijke workstream.

In de pull request moet minimaal staan:

- wat er verandert;
- welke wetenschappelijke semantiek wel/niet verandert;
- welke evidence of dependencies geraakt worden;
- welke tests/validators zijn uitgevoerd;
- welke onderdelen na de wijziging nog geblokkeerd of onzeker zijn.

## Lokale integriteitscontrole

Voer voor een inhoudelijke PR uit:

```bash
python tools/validate_project.py
python -m unittest discover -s tests -v
```

De projectvalidator controleert referentiële integriteit en de reviewstructuur. Een PASS is geen vervanging voor inhoudelijke wetenschappelijke kwalificatie.
