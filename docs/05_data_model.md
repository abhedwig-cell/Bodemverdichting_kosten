# 5. Data model

Status: **Status-A-light composite data-model baseline (dataset/relationship layer v0.3.1)**

## 5.1 Purpose

The data model defines scientific meaning independently of Excel, Python, databases or the future application.

Canonical machine-readable definitions live under [`../schema/`](../schema/). The current model is a composed migration baseline rather than a final v1 schema. Core field files still retain their own bounded version labels, while the current dataset/relationship graph is at the v0.3.x line. The repository-level authority is the composed schema under schema/, not the version label of one individual YAML file.

The central design rule is:

> scientific meaning is defined once and exposed through multiple interfaces.

A field should therefore mean the same thing in CSV, Excel, Python, an API and a future database.

## 5.2 Data-model layers

The canonical structure has four related layers.

### Entity layer

[`../schema/entities.yml`](../schema/entities.yml) defines the kinds of scientific/project objects that exist, such as:

- spatial unit;
- soil profile and layer;
- soil state;
- hydraulic parameterization;
- drainage configuration;
- event and model run;
- hydrological response;
- transfer event;
- water-system unit;
- pump asset and dispatch;
- valuation relation and cost estimate;
- source, evidence, claim and qualification;
- governance rule, change record and data request.

### Relationship layer

[`../schema/relationships.yml`](../schema/relationships.yml) defines important links and foreign-key semantics between those objects.

The relationship model prevents, for example, a pump-dispatch record from being interpreted without its event, source zone and pump identity.

### Dataset layer

[`../schema/datasets.yml`](../schema/datasets.yml) defines stable dataset objects and their grains.

A `dataset_id` should survive workbook sheet renaming or migration to another storage technology.

### Field layer

Field definitions currently live in:

- [`../schema/fields.yml`](../schema/fields.yml) for the core migration baseline;
- [`../schema/evidence_fields.yml`](../schema/evidence_fields.yml) for the current evidence-register extension;
- bounded vertical-slice schema files where a concept is not yet mature enough to promote globally.

Over time these should converge toward a coherent canonical field registry without incompatible duplicate definitions.

## 5.3 Grain is mandatory

Every dataset must state what one row represents.

Examples:

| Dataset | Grain |
|---|---|
| `source_register` | one row per source/version |
| `evidence_register` | one row per extractable evidence item |
| `soil_layer_register` | one row per soil profile × depth interval |
| `soil_state_register` | one row per profile × layer × state |
| `hydraulic_parameterization_register` | one row per soil state × method/version × uncertainty/member × representation |
| `event_register` | one row per event/simulation window |
| `model_run_register` | one row per controlled model execution |
| `transfer_event_register` | one row per source unit × event × transfer stage |
| `pump_dispatch_register` | one row per event × source zone × pump asset |
| `cost_estimate_register` | one row per physical effect × valuation relation × scope |

A table without a clear grain is not ready to be canonical because duplicates, aggregation and joins cannot be interpreted reliably.

## 5.4 Stable identity

Canonical IDs should identify scientific/project objects, not display locations.

Examples:

```text
source_id
spatial_unit_id
soil_profile_id
soil_layer_id
event_id
model_run_id
transfer_event_id
pump_asset_id
pump_dispatch_id
qualification_id
```

A workbook row number, sheet name or user-interface position must never function as the only identity of an object.

## 5.5 Field metadata contract

A mature canonical field should define at least:

```text
field_id
label
description
entity
datatype
unit
nullable
controlled vocabulary / allowed values when applicable
guardrail when a common misinterpretation must be prevented
```

Where relevant, additional metadata can describe:

- provenance expectations;
- whether the field is measured, derived, modelled or administrative;
- temporal/spatial scope;
- validation range;
- display format;
- relation to another canonical field.

The data dictionary and workbook header help are generated from these definitions so documentation does not drift independently from data meaning.

## 5.6 Null semantics and status

The project uses a strict principle:

> unknown is not zero.

At minimum the following meanings must remain distinguishable:

- **known zero**: observed/calculated quantity is genuinely zero;
- **unknown/null**: value has not been observed, provided or calculated;
- **blocked**: project logic does not permit a calculation because a prerequisite is missing;
- **not applicable**: the field does not apply to this object/context;
- **rejected**: a candidate value exists but is not allowed for this project use.

The current CSV and workbook baseline often encodes unknown numeric values as blank/null and carries scientific status in evidence/qualification fields. A future database may represent richer missingness/status explicitly, but it must not collapse these meanings.

## 5.7 State versus intrinsic context

The data model should reflect whether a property changes between current/reference states.

Typical profile/layer context includes:

- layer depth;
- texture;
- profile identity.

Typical state variables include:

- bulk density;
- compaction severity/state role;
- other explicitly state-dependent measured indicators.

State-specific hydraulic properties are represented through a separate `HydraulicParameterization` object when they are measured/fitted or derived from state. This preserves the distinction between measurement of physical state and transformation to model-ready retention/conductivity functions.

This separation matters because the matched counterfactual normally changes soil state while preserving profile context and transformation semantics.

### 5.7a Scenario and context semantics

A scenario is not automatically a new canonical entity. At the current maturity level, most scenario meaning should be reconstructed from explicit existing dimensions such as:

```text
soil_state_id
land_use_crop_id
event_id / forcing context
drainage_configuration_id
model_configuration_id
water-system context
valuation_relation_id
time/frequency semantics where relevant
```

This avoids opaque labels that hide which assumptions changed.

A separate scenario entity should only be introduced when scenarios require independent stable identity, provenance, qualification, versioning or reuse across multiple workflows. Until that need exists, adding a universal scenario table would create framework structure without adding scientific information.

## 5.8 Evidence model

The evidence datasets are canonical machine-readable project records rather than annotations attached informally to Excel cells.

The current chain is:

```text
source_register
      ↓
evidence_register
      ↓
claim_register
      ↓
qualification_register
```

### Source register

Records a source/version and its locator.

### Evidence register

Stores atomic extractable facts or relations. One source can support many evidence items.

### Claim register

Stores the project interpretation. A claim may refer to multiple evidence items and is intentionally separate from those facts.

### Qualification register

Records whether an evidence item supports one intended use, which dependencies matter, what review was performed and what limitation remains.

This architecture enables a single source fact to be admissible for one use and inappropriate for another.

## 5.9 Artifacts and datasets

`Artifact` and `ArtifactDataset` explicitly separate the product delivered to a user from the canonical data objects it exposes.

For example, a generated workbook can contain:

- canonical source/evidence rows;
- blank data-gated model templates;
- a derived readiness view.

The workbook is one artifact. The scientific datasets inside it retain separate identities.

This is why artifact version is not a substitute for dataset version or schema version.

## 5.10 Workbook contract

The preferred workbook structure is defined in [`../schema/workbook_contract.yml`](../schema/workbook_contract.yml).

A generated workbook starts with:

- `00_METADATA`;
- `01_GUIDE`;
- `DATA_DICTIONARY`.

Dataset sheets expose dataset metadata before the table:

```text
dataset_id
entity
role
grain
primary_key
canonical_status
source/derivation
```

The principle is:

> one table = one clearly defined dataset object.

Views, summaries and dashboards must be identifiable as views rather than masquerading as source tables.

## 5.11 Legacy workbook migration

The prototype workbook lineage contains many sheets that combine reference data, rules, evidence, views and calculations. Those sheets are treated as **migration evidence**, not as an architecture to reproduce verbatim.

The migration process is:

```text
legacy sheet/table
    ↓ inspect grain and meaning
candidate canonical dataset
    ↓ map fields and provenance
schema / register
    ↓ qualify semantic compatibility
generated artifact or application view
```

Relevant migration documentation:

- [`09_workbook_inventory_v0_2.md`](09_workbook_inventory_v0_2.md)
- [`10_data_model_v0_2_migration.md`](10_data_model_v0_2_migration.md)

## 5.12 Current Tollebeek vertical slice

The Tollebeek slice is the first concrete end-to-end use of the model.

Populated canonical datasets currently include source, evidence, claim and qualification registers. The generated workbook exposes those records directly from repository state.

The physical/model datasets remain intentionally blank where scientific inputs are still blocked:

```text
SPATIAL_UNIT          WAIT current geometry
HYDRO_RESPONSE        WAIT paired current/reference attribution
TRANSFER_EVENT        WAIT event transfer/routing evidence
PUMP_ASSET            PARTIAL evidence, asset configuration not yet complete
PUMP_DISPATCH         WAIT event-specific operation data
```

This is a desired property of the data model: the schema can exist before a scientifically legitimate value exists.

## 5.13 Database direction

A future persistent database can map these dataset objects to relational tables or another appropriate storage system. The repository should not commit prematurely to a database engine.

A likely relational structure would use:

- stable primary keys from the schema;
- foreign keys from `relationships.yml`;
- versioned configuration/reference records;
- long/event tables for high-frequency simulation or telemetry where needed;
- views for common application queries.

Large time-series and raster data may remain in specialised stores/files with canonical metadata and IDs in the project database.

The important requirement is semantic compatibility, not forcing every byte into one database.

## 5.14 Promotion toward v1

The current composite data model can move toward v1 when:

- key entity grains no longer depend on legacy workbook layout;
- field definitions cover the first production workflows without incompatible overlays;
- current/reference model runs and transfer events can be persisted without ambiguous state;
- evidence links can be carried to important model inputs and outputs;
- workbook and application adapters consume the same schema;
- schema validation and migration tests protect backwards compatibility or make breaking changes explicit.

Until then, the `MIGRATION_BASELINE` and `PROVISIONAL` statuses should remain visible rather than being renamed `CANONICAL` for convenience.
