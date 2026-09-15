# 10. Data model v0.2 migration plan

## Objective

Move from a workbook-centric prototype to a repository-centric scientific data model without losing the design history encoded in the workbook lineage.

## Migration layers

### Layer 1: evidence and provenance

First-class objects:

`source → evidence_item → claim → qualification`

This layer is migrated first because every later parameter, relation or model result should be able to point back to evidence and intended use.

### Layer 2: physical system

Core chain:

`spatial_unit → soil_profile → soil_layer → soil_state`

with linked:

- `land_use_crop`
- `drainage_configuration`
- `water_system_unit`

### Layer 3: controlled simulation

Core chain:

`event + model_configuration + soil_state → model_run → hydrological_response`

A current/reference comparison is a relationship between controlled runs, not a free-standing coefficient.

### Layer 4: transfer and operation

`hydrological_response → transfer_event → water_system_unit → pump_dispatch`

Generated runoff, field-edge delivery, network routing and pumped volume remain separate quantities.

### Layer 5: valuation

`qualified physical effect + valuation_relation → cost_estimate`

Private cost, public budget cost and societal welfare effect remain separate valuation categories.

## Identifier rules

Canonical records require stable IDs. IDs should:

- be unique within entity type;
- survive workbook regeneration;
- avoid encoding mutable display names;
- not use Excel row numbers as identity.

## State and null semantics

Unknown values stay null.

`0` is a scientific value and must not be used for:

- missing measurements;
- non-ingested data;
- not-applicable fields;
- blocked calculations.

State and status should be represented through controlled vocabularies, not blank-text conventions.

## Relationship to implementation

Schemas under `schema/` are the definition layer.

Python models, database tables, workbook generators and the eventual application should implement those definitions. They may use different physical storage shapes, but meaning and grain must remain compatible.

## Next qualification step

The next data-model workunit should take a small coherent vertical slice and implement it end-to-end. Recommended slice:

**Tollebeek source → transfer → pump dispatch**

with:

- spatial unit;
- event;
- current/reference hydrological response;
- transfer stage;
- water-system zone;
- pump asset;
- pump dispatch;
- evidence and qualification links.

This slice is complex enough to test the architecture, but bounded enough to avoid migrating all 109 legacy sheets at once.
