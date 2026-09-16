# Current/reference source-model input baseline v0.1

Status: **INPUT_READINESS_BASELINE**

This baseline turns the next scientific milestone into an explicit acquisition and review surface. It does not run the source model and does not populate missing scientific values.

## 1. Scientific target

The first source-model experiment is a matched CURRENT/REFERENCE comparison at explicit spatial/profile and event context. Its scientific endpoint is a qualified source response such as runoff, drainage and evapotranspiration differences.

Downstream transfer, pump dispatch and cost are intentionally outside this gate.

## 2. Minimum prerequisite set

The canonical `data_request_register` currently requires ten roles:

1. `SPATIAL_GEOMETRY`;
2. `SOIL_PROFILE_CONTEXT`;
3. `CURRENT_SOIL_STATE`;
4. `REFERENCE_SOIL_STATE`;
5. `DRAINAGE_CONFIGURATION`;
6. `EVENT_FORCING`;
7. `INITIAL_HYDROLOGICAL_STATE`;
8. `MANAGED_BOUNDARY`;
9. `LAND_USE_CROP_CONTEXT`;
10. `MODEL_CONFIGURATION`.

These roles make explicit what has to be known or decided before two model runs can be interpreted as a soil-state attribution pair.

## 3. Current readiness

No row in this baseline is promoted to `ADMITTED` merely because related literature, historical settings or discovery services exist.

### Partial evidence already exists

- OT.02 administrative area context and a PDOK/IMWA geometry-discovery route;
- a SoilPhys profile-screening route;
- historical Noordoostpolder drainage settings as method priors;
- theoretical guidance for contextual reference states and depth-resolved profiles;
- method guidance for sub-daily forcing;
- managed-system/target-level context and lower-boundary sensitivity.

### Still missing as project inputs

- a reviewed current spatial feature set for the first source-model units;
- a selected representative profile set;
- admitted current depth-resolved compaction states;
- a Tollebeek-specific matched reference-state construction;
- current drainage configuration for the selected units;
- a concrete event forcing series and initial hydrological state;
- event-specific managed-boundary/control semantics;
- land-use/crop context for the selected units/event where model-relevant;
- a pinned source-model implementation/version and configuration.

## 4. Geometry is not affected area

Admitting an OT.02 or sub-unit geometry only establishes spatial identity/context. It does not establish the area affected by compaction.

The existing 1497 ha administrative benchmark and 1502 ha historical design context must therefore not be inserted into `affected_area_ha` without a separate scientific basis.

## 5. Current state versus profile context

A profile description may provide layer geometry, texture, organic matter and derived/modal bulk-density information. That does not automatically establish the current compaction state.

The project must keep intrinsic/profile context separate from state variables and preserve whether a value is measured, derived, modal or otherwise inferred.

## 6. Reference-state admission

The reference state is a scientific decision, not a missing lookup value. It should only be constructed after the current profile/state and causal question are fixed.

A valid first pair must document:

- which variables differ between CURRENT and REFERENCE;
- why those differences represent the intended compaction contrast;
- which dimensions remain identical or demonstrably equivalent;
- what evidence supports the reference construction.

## 7. Event and boundary control

For runoff attribution the event forcing, initial state, drainage and managed boundary are controlled dimensions. A target water level by itself is not an event-specific groundwater initial condition or complete lower-boundary rule.

The selected forcing must retain source, timestamps, timezone, units, temporal resolution and QC/missing-data handling.

## 8. Model-configuration gate

This baseline deliberately does not choose a SWAP version, executable or numerical default. Before the first paired run, the project must pin the source-model implementation/version and record a reproducible `model_configuration_id`.

The pair may only be labelled a simple soil-state attribution when the controlled model dimensions are identical or explicitly demonstrated equivalent.

## 9. Qualification semantics

The register validator checks:

- unique request IDs and input roles;
- complete coverage of the bounded first-source-model prerequisite set;
- controlled requirement-kind, readiness and priority values;
- valid capability, evidence and claim references;
- non-empty requirement, acceptance, blocking and next-action fields.

Passing these checks proves that the gate register is internally coherent. It does not prove that any missing scientific input has been acquired or qualified.

## 10. Next permitted scientific action

Work through the P1 requests from spatial identity toward an executable matched pair. A sensible dependency order is:

```text
spatial geometry
  → profile context
  → current state
  → reference state
  → drainage + land-use context
  → event forcing + initial state + managed boundary
  → pinned model configuration
  → paired runs
  → response qualification
```

This order is a dependency guide, not permission to fill downstream fields before upstream evidence is admitted.
