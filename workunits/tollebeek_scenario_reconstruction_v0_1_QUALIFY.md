# Tollebeek scenario/reconstruction admissibility v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Protocol phase: QUALIFY

## Authority

- canonical start: `main` @ `8ef90b123dbce0b9c855cd9a008405806ad6451b`
- branch pre-checkpoint qualified head: `0935606adcd8c669a21398c7ae0fec98afa60b1f`
- pull request: `#29`
- PR-head CI: `35076216600` — SUCCESS

## Qualified decision

Verdict: `SCENARIO_RECONSTRUCTION_DECISION_SURFACE_QUALIFIED_NO_INPUT_ADMISSION`

The seven current `PARTIAL_EVIDENCE` P1 roles are classified as:

- `DR_SM_CURRENT_STATE` — `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`
- `DR_SM_REFERENCE_STATE` — `DEPENDENT_INTERNAL_DECISION`
- `DR_SM_DRAINAGE` — `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`
- `DR_SM_INITIAL_STATE` — `RECONSTRUCTABLE_WITH_EXPLICIT_UNCERTAINTY`
- `DR_SM_MANAGED_BOUNDARY` — `RECONSTRUCTABLE_WITH_EXPLICIT_UNCERTAINTY`
- `DR_SM_LAND_USE` — `SCENARIO_ELIGIBLE_ONLY`
- `DR_SM_MODEL_CONFIG` — `DEPENDENT_INTERNAL_DECISION`

## Claim boundary

Two future tracks are now distinguished:

1. `Track H — historical attribution`: actual or defensibly reconstructed 1998 context; historical-data gates remain binding.
2. `Track S — bounded scenario analysis`: conditional mechanism/sensitivity experiments with explicit `SCENARIO_ONLY` semantics.

Track S outputs may not be used as evidence that scenario conditions occurred in Tollebeek in 1998.

## Mutations

Only documentation/governance files are added. No evidence status, qualification verdict, data-request readiness value, schema, implementation, model input dataset or model output is modified.

The canonical P1 readiness counts remain:

- `ADMITTED = 3`
- `PARTIAL_EVIDENCE = 7`
- `MISSING = 0`

## Tests

PR-head `0935606adcd8c669a21398c7ae0fec98afa60b1f`:

- CI run `35076216600`: SUCCESS
- compile gate: PASS
- Status-A-light integrity gate: PASS
- full unit/contract suite: PASS

## Next permitted action

After this checkpoint receives exact-head CI, merge only this decision surface. A future Track S experiment, managed-boundary reconstruction, reference-state construction or other implementation requires a separate bounded workunit because each creates a new scientific decision surface.

No model run is authorized here.