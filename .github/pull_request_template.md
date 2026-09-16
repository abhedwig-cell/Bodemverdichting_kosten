## Samenvatting

Beschrijf kort wat deze PR verandert en waarom.

## Geraakte laag/lagen

- [ ] Theorie / begrippen
- [ ] Conceptueel model
- [ ] Formeel model / vergelijking
- [ ] Datamodel / schema / dataset-grain
- [ ] Implementatie
- [ ] Evidence / claim / qualification
- [ ] Workbook / dashboard / applicatie-interface
- [ ] Alleen documentatie zonder semantische wijziging

## Wetenschappelijke semantiek

- [ ] Geen verborgen numerieke defaults toegevoegd
- [ ] `unknown` blijft onderscheiden van `0`
- [ ] Bronfeit, projectclaim en qualification zijn onderscheiden
- [ ] Current/reference of andere counterfactual-logica blijft matched waar van toepassing
- [ ] Generated runoff, transfer, routing en pumping zijn niet stilzwijgend samengevoegd
- [ ] Historische/lokale benchmarks zijn niet opgewaardeerd tot huidige parameters zonder kwalificatie

Beschrijf eventuele semantische wijziging:

## Traceability en evidence

- [ ] Relevante evidence/claims/qualifications bijgewerkt of niet van toepassing
- [ ] `model/equations.csv` bijgewerkt of niet van toepassing
- [ ] `model/traceability.csv` bijgewerkt of niet van toepassing
- [ ] Dependencies en bekende beperkingen expliciet vastgelegd

## Verificatie

- [ ] `python tools/validate_project.py`
- [ ] `python -m unittest discover -s tests -v`
- [ ] Eventuele aanvullende domein-/kwalificatietests vermeld

## Resterende onzekerheid / blokkades

Wat is na deze PR bewust nog niet gekwalificeerd, niet geïmplementeerd of data-gated?

## Artifact-impact

Beschrijf of gegenereerde workbooks, dashboards of applicatieviews hierdoor veranderen. Artifacts zijn geen bron van waarheid.
