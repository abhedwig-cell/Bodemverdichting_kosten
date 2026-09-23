# Canonical schema

Deze map bevat de machineleesbare betekenis van het projectdatamodel.

Huidige status: **Status-A-light composite baseline**. De dataset- en relationshiplaag staat op de v0.3.x-lijn. Oudere kern- en domeinbestanden houden hun eigen begrensde versienummer, omdat ze op verschillende momenten zijn ingevoerd. Eén los schema_version-veld is daarom niet de projectbrede authority.

De canonieke compositie bestaat uit:

- entities.yml: project- en domeinentiteiten met hun grain;
- relationships.yml: belangrijke relaties en foreign-key-semantiek;
- datasets.yml: stabiele datasetobjecten, rollen, grains, keys en waar relevant opslaglocaties;
- fields.yml plus domein-fieldbestanden: velddefinities, eenheden, nullability en guardrails;
- controlled_vocabularies.yml: gedeelde statussen en vocabularies;
- workbook_contract.yml: afgeleid artifactcontract voor Excel;
- artifacts/: concrete, niet-canonieke workbook/artifactspecificaties.

Belangrijke regel: een veld- of datasetdefinitie hoort hier te staan voordat een workbook of applicatie er een eigen betekenis aan geeft.

De projectbrede effect-pathway-, evidence-ensemble- en bounded-calculation-oppervlakken worden als expliciete datasetobjecten geregistreerd. Tollebeek-specifieke schema's blijven begrensde pilot-/adapteruitbreidingen en vervangen geen generieke kernentiteiten.

Gebruik tools/validate_architecture_contract.py en tools/validate_domain_schema.py om de samengestelde schema-integriteit te controleren.
