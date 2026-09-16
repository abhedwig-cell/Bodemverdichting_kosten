# Data Model v0.3 contract

Status: **IMPLEMENTATION WORKUNIT**

Data Model v0.3 is a bounded architecture step between the current Status-A-light conceptual/formal model and later production data workflows.

It does **not** introduce new hydrological, economic or Tollebeek science. Its purpose is to make already documented scientific objects and control relations machine-readable enough that future runs, evidence links and generated artifacts cannot silently collapse different meanings.

## 1. What v0.3 changes

The v0.2 migration baseline already separates soil state, events, model runs, hydrological responses, transfer, pump dispatch, valuation and evidence. v0.3 strengthens four gaps:

1. documented objects must also exist as stable datasets when they need independent identity and grain;
2. model runs must be reconstructable from explicit controlled context;
3. current/reference attribution must be reconstructable without inventing a premature attribution-pair entity;
4. relationships must cover the core scientific graph rather than only the first Tollebeek vertical slice.

## 2. Run-control contract

A controlled model run is interpreted through explicit identifiers for:

- spatial unit;
- event or simulation window;
- soil state;
- model configuration;
- where relevant, land-use/crop context and drainage configuration.

For a simple soil-state attribution, current and reference runs must share the controlled dimensions except for the admitted soil-state change. The data model does not label two arbitrary runs as a valid attribution pair merely because both exist.

The current conceptual decision is retained: a matched pair is **not yet a separate canonical entity**. Pairing is reconstructable from run identity and controlled dimensions. A future pair entity is justified only if repeated workflows require independent pair-level provenance, review or persistence.

## 3. Stable domain datasets added in v0.3

### `land_use_crop_register`

Entity: `land_use_crop`  
Grain: one row per spatial unit × period/context × crop or land-use classification.

This dataset makes crop/land-use context independently addressable instead of hiding it in a model-run label or workbook column.

### `model_configuration_register`

Entity: `model_configuration`  
Grain: one row per versioned model/boundary/numerical configuration.

A model configuration identifies controlled model semantics. It is not evidence that the configuration is scientifically appropriate for a given project use; that remains a qualification question.

## 4. Relationship contract

The v0.3 relationship graph explicitly includes:

- spatial unit → soil profile;
- soil profile → soil layer;
- soil layer → soil state;
- spatial unit → land-use/crop context;
- spatial unit/event/state/model configuration → model run;
- model run → hydrological response;
- hydrological response → transfer event;
- transfer event → water-system unit;
- event/source zone/pump asset → pump dispatch.

Where the current schema cannot yet express a relation with a mature canonical foreign-key field, the relationship remains documented rather than populated with an invented value.

## 5. Null and blocked semantics

v0.3 preserves the existing contract:

- `0` is a known numerical zero;
- blank/null is unknown or unavailable;
- blocked means a calculation is intentionally not permitted because a prerequisite is missing;
- not-applicable is not the same as unknown.

No new default is introduced for current/reference matching, transfer, availability, assist fraction, response window, head, efficiency or affected area.

## 6. Evidence boundary

Schema presence is not scientific admission.

A registered model configuration, soil state, event, pump asset or valuation relation may exist while still being unqualified for a particular calculation. Source → evidence → claim → qualification remains the route by which project use is admitted.

## 7. Artifact boundary

Excel, dashboards and later applications consume these canonical semantics. They do not define them.

A generated workbook may expose `land_use_crop_register` or `model_configuration_register` later, but v0.3 does not require adding sheets merely because the canonical datasets now exist.

## 8. Scientific boundary

This workunit does not qualify:

- current/reference Tollebeek hydrological attribution;
- a current/reference SWAP result;
- current OT.02 geometry or current compaction state;
- current pump availability, assist fraction, total dynamic head or efficiency;
- current pumping or societal cost.

Those remain evidence/data-gated.
