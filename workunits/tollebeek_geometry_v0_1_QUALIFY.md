# Tollebeek geometry v0.1 — QUALIFY checkpoint

Protocol: RECONCILE → ACQUIRE → REVIEW → ADMIT → CLOSE

## Qualified branch state

- branch: `work/tollebeek-geometry-v0.1`
- pre-checkpoint qualified content head: `cc43fc8d9d9a5a456c32410ed82a511f2b92b02c`
- GitHub Actions run: `35043934292`
- result: `success`

Passed gates:

- Python/project validation compilation: PASS;
- Status-A-light integrated project gate: PASS;
- evidence source/foreign-key/controlled-vocabulary integrity: PASS through the project gate;
- source-model input-readiness reference integrity: PASS through the project gate;
- unit and contract tests: PASS.

## Review verdict

`ROUTE_QUALIFIED_GEOMETRY_NOT_ADMITTED`.

The tested change is limited to:

- adding an owner-hosted geometry acquisition source;
- recording owner-service inventory/freshness evidence;
- recording a BLOCKED_DATA qualification for that acquisition route;
- strengthening `DR_SM_GEOMETRY` with owner-first acquisition instructions and a 2020 legacy-layer staleness guardrail;
- persisting the workunit evidence and decision boundary.

No polygon, coordinates, feature ID, area, profile, current/reference state, hydrological parameter or model output is introduced.

## Admission condition

This branch may be merged as a canonical acquisition-route and guardrail update after this checkpoint head also passes CI. Merge must not be described as admission of OT.02 geometry.

`DR_SM_GEOMETRY` remains `PARTIAL_EVIDENCE` and the geometry verdict remains `NO_ADMIT_GEOMETRY`.
