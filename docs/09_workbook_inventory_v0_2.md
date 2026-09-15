# 9. Workbook inventory and migration baseline v0.2

## Why this inventory was done

Before defining a canonical workbook format, the existing prototype line was inspected rather than assumed to be cumulative.

The inventory used the actual workbook structures of:

- `Bodemverdichting_Cost_Framework_v3_8_TollebeekReconciled.xlsx`
- `Bodemverdichting_Cost_Framework_v4_4_CapacityReconciliation_DataRequest.xlsx`

The raw inventories are stored under `artifacts/inventory/`.

## Important finding: the workbook lineage has split

The inspected v3.8 workbook is a broad **full framework snapshot** with **109 worksheets**.

The inspected v4.4 workbook is a **bounded Tollebeek module** with **24 worksheets**.

Therefore v4.4 is not a cumulative replacement for v3.8. The version number describes development chronology, not inheritance of all workbook content.

This distinction is now part of the artifact model and should be preserved during migration.

## v3.8 full snapshot

Observed sheet roles:

- 1 metadata/guide sheet;
- 75 numbered framework tables/modules;
- 13 dashboard/view sheets;
- 9 provenance/governance sheets;
- 11 application-oriented sheets.

The workbook contains several semantic layers in one artifact:

1. scientific variables/rules/parameters;
2. spatial and soilscape configuration;
3. evidence and provenance;
4. scenario and result schemas;
5. execution/engine contracts;
6. crop and economic valuation logic;
7. case studies and pilot definitions;
8. dashboards;
9. governance and review surfaces.

This broad coverage is valuable as design history, but it is not yet a normalized data model.

## v4.4 bounded module

Observed sheet roles:

- 1 metadata/guide sheet;
- 19 data/evidence/governance module sheets;
- 4 application views.

Its focus is narrower:

- current geometry acquisition;
- historical Noordoostpolder SWAP priors;
- pump topology and dispatch;
- capacity-source reconciliation;
- external data request.

This workbook should be treated as a **bounded evidence/capability module**, not as the project master workbook.

## Migration principle

We will migrate **semantics**, not worksheet order.

The old sheet name is a lineage locator. It is not automatically the future `dataset_id`.

Examples:

- `PROV_01_Sources` maps naturally toward canonical `source_register`.
- `PROV_02_Claims` maps toward `claim_register`.
- `PROV_06_ModelEquations` maps toward `model_equation_register`.
- `PROV_04_Checks` and later governance sheets map toward `governance_rule` / `qualification_check`.
- current Tollebeek capacity-source sheets map toward `evidence_item`, `claim`, `pump_asset` and `qualification`, not one giant 'Tollebeek table'.

## Canonical dataset families for v0.2

The migration baseline groups workbook content into these canonical families:

### Scientific structure

- `variable_definition`
- `model_rule`
- `model_equation`
- `parameter_definition`
- `scenario_definition`

### Spatial and physical state

- `spatial_unit`
- `soil_profile`
- `soil_layer`
- `soil_state`
- `land_use_crop`
- `drainage_configuration`
- `water_system_unit`

### Simulation

- `event`
- `model_configuration`
- `model_run`
- `hydrological_response`

### Transfer and managed system

- `transfer_event`
- `pump_asset`
- `pump_dispatch`

### Valuation

- `valuation_relation`
- `cost_estimate`

### Evidence and governance

- `source`
- `evidence_item`
- `claim`
- `qualification`
- `governance_rule`
- `change_record`
- `data_request_item`

### Artifact administration

- `artifact`
- `artifact_dataset`
- `field_definition`

## Normalization findings

Several workbook columns are repeated across many sheets, especially `status`, `notes`, `unit`, `source_id`, `priority`, `value_low`, `value_base`, `value_high`, and identifiers such as `rule_id`, `claim_id` and `crop_group_id`.

These repeats are useful signals, but they do not mean the fields have one universal meaning. v0.2 therefore distinguishes:

- canonical field definitions where meaning is stable;
- dataset-specific fields;
- legacy aliases that still require reconciliation.

The raw field inventory currently contains more than one thousand observed header occurrences. It is evidence for migration, not the field dictionary itself.

## Immediate migration priorities

1. Preserve and normalize the provenance architecture first.
2. Normalize the core physical entities and current/reference run semantics.
3. Normalize off-site transfer and pump dispatch.
4. Normalize valuation only after physical-effect identity is stable.
5. Treat dashboards and APP sheets as views, never as source-of-truth tables.
6. Keep old workbooks immutable as lineage artifacts during migration.

## Admission level

Data Model v0.2 is a **migration baseline**, not canonical v1.

A dataset becomes canonical only after:

- its grain is explicit;
- identifiers are stable;
- fields are reconciled to the field dictionary;
- provenance/status semantics are defined;
- important legacy mappings are documented;
- at least one implementation or test exercises the schema.
