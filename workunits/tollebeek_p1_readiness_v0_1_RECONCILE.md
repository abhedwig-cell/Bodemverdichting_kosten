# Tollebeek P1 readiness v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Workunit: Tollebeek P1 source-model readiness baseline
Protocol phase: RECONCILE

## Canonical authority

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- canonical branch: `main`
- canonical start: `1e9844e6aade92f840d5539d552cdd2b6b065665`
- event: `EVT_TOL_1998_OCT`
- branch: `work/tollebeek-p1-readiness-v0.1`

No materially equivalent open readiness-baseline branch existed at branch creation.

## Current P1 status

The ten P1 source-model input roles reconcile to:

- `ADMITTED = 3`
  - `DR_SM_GEOMETRY`
  - `DR_SM_PROFILE`
  - `DR_SM_EVENT_FORCING`
- `PARTIAL_EVIDENCE = 7`
  - `DR_SM_CURRENT_STATE`
  - `DR_SM_REFERENCE_STATE`
  - `DR_SM_DRAINAGE`
  - `DR_SM_INITIAL_STATE`
  - `DR_SM_MANAGED_BOUNDARY`
  - `DR_SM_LAND_USE`
  - `DR_SM_MODEL_CONFIG`
- `MISSING = 0`

Verdict: `P1_ROUTE_COVERAGE_COMPLETE_INPUT_ADMISSION_INCOMPLETE`.

This is not a run-readiness claim. Route coverage means each required input now has an explicit evidence/acquisition/decision path; it does not mean the seven partial inputs may be replaced by defaults.

## Blocker classification

Primary external-data acquisition can proceed in parallel for CURRENT soil state, parcel drainage, 1998 managed-boundary operations, event-start shallow groundwater/soil-water observations and 1998 land-use/crop evidence.

Dependent scientific decisions must remain serial where semantics depend on unresolved evidence:

- REFERENCE state after CURRENT-state admission / explicit contrast;
- warm-up/restart initialization only after enough boundary/drainage/land-use/model configuration is known;
- concrete model configuration only after unresolved inputs are admitted or separately qualified as explicit scenario/reconstruction semantics.

## Mutations in this workunit

Governance/documentation only:

- `docs/32_tollebeek_p1_readiness_baseline_v0_1.md`
- `data_requests/tollebeek_p1_external_acquisition_package_v0_1.md`
- this checkpoint

No data-request status, evidence verdict, scientific value, schema, production implementation or model result is changed.

## Next permitted action

Review the branch diff against canonical `main`; require only documentation/governance mutations. Then qualify the snapshot through normal CI and merge as a current-canonical handoff for external acquisition.

## Exclusions

- no new scientific admission;
- no CURRENT or REFERENCE soil-state construction;
- no drainage parameter derivation;
- no 1998 boundary reconstruction;
- no crop scenario selection;
- no warm-up/restart construction;
- no runnable model configuration;
- no source-model run;
- no missing→zero or convenience defaults.
