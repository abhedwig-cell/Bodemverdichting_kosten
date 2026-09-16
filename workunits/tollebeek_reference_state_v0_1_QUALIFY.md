# Tollebeek reference-state v0.1 — QUALIFY checkpoint

Capability / readiness item: `DR_SM_REFERENCE_STATE`

Phase: `QUALIFY`

Canonical start:

- `main`: `4b69e4090607e7d412b802c2bd2d485d7dc7dbee`
- branch: `work/tollebeek-reference-state-v0.1`
- clean pre-checkpoint head: `6a3aee5c5ed0ff063ae0a57a6747deb73c848e00`

## Qualified protocol decision

Reference-state ladder:

- `RF0 OBSERVED_PAIRED_REFERENCE`
- `RF1 EVIDENCE_DERIVED_COUNTERFACTUAL`
- `RF2 REFERENCE_ENVELOPE_SCENARIO`
- `RF3 INADMISSIBLE_REFERENCE_DEFAULT`

`DR_SM_REFERENCE_STATE` remains `PARTIAL_EVIDENCE` and `DEPENDENT_INTERNAL_DECISION`.

No numerical reference state, hydraulic parameter set or model run is admitted.

## Core matching rule

For simple soil-compaction attribution, CURRENT and REFERENCE keep external dimensions matched: spatial/profile identity, intrinsic layer context, forcing, land-use/crop, drainage, managed boundary, model configuration, initialization semantics and output conventions.

The intended contrast is limited to admitted compaction-related state variables and traceably derived hydraulic properties.

## Temporal rule

A CURRENT state observed in 2020–2021 is a dated modern state. Applying a paired modern CURRENT/REFERENCE contrast under the observed October-1998 meteorological forcing is a controlled historical-forcing scenario unless a separate temporal-transfer argument is qualified. Historical forcing does not silently backdate modern soil observations.

## Guardrails retained

- no pristine/zero-traffic automatic reference;
- no arbitrary percentage density reduction;
- no SoilPhys modal density copied directly into `soil_state`;
- no BOFEK class treated as an observed uncompacted state;
- no simultaneous crop/drainage/boundary/initialization changes in a simple soil-state attribution claim;
- no null→0;
- no independently tuned hydraulic parameters detached from a traceable state transformation;
- no reference selection based on desired model response.

## Qualification evidence

Clean PR head `6a3aee5c5ed0ff063ae0a57a6747deb73c848e00`:

- CI run `35077445250`: `SUCCESS`
- compile project validation/workbook tools: PASS
- Status-A-light integrity gate: PASS
- full unit and contract tests: PASS

Diff boundary before this checkpoint:

- `docs/36_tollebeek_reference_state_construction_protocol_v0_1.md`
- `workunits/tollebeek_reference_state_v0_1_RECONCILE.md`

No register, evidence verdict, readiness status, schema, state data, model input, implementation or output changed.

## Verdict

`QUALIFIED_REFERENCE_STATE_CONSTRUCTION_PROTOCOL_NO_REFERENCE_ADMISSION`

Next permitted action:

Run exact-head CI on this persisted checkpoint. If green, merge this protocol only. Numerical RF0/RF1/RF2 construction requires a separate bounded workunit after CURRENT-state evidence and the intended Track H / Track S semantics are fixed.
