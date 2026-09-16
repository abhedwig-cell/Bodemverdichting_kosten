# Tollebeek P1 readiness v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Protocol phase: QUALIFY

## Authority
- repository: `abhedwig-cell/Bodemverdichting_kosten`
- canonical start: `main` @ `1e9844e6aade92f840d5539d552cdd2b6b065665`
- branch: `work/tollebeek-p1-readiness-v0.1`
- clean pre-checkpoint head: `107107a4f20c55987381a86f103b34c0ffaf35ef`
- event: `EVT_TOL_1998_OCT`

## Qualified governance verdict

`P1_ROUTE_COVERAGE_COMPLETE_INPUT_ADMISSION_INCOMPLETE`

Current ten P1 roles:
- `ADMITTED = 3` — geometry, profile context, event forcing;
- `PARTIAL_EVIDENCE = 7` — current state, reference state, drainage, initial state, managed boundary, land use, model configuration;
- `MISSING = 0`.

This is a route/readiness inventory verdict only. It is not a scientific admission or model run-readiness verdict.

## Deliverables
- `docs/32_tollebeek_p1_readiness_baseline_v0_1.md`
- `data_requests/tollebeek_p1_external_acquisition_package_v0_1.md`
- `workunits/tollebeek_p1_readiness_v0_1_RECONCILE.md`
- this QUALIFY checkpoint

The consolidated acquisition package preserves the existing detailed request contracts and groups external evidence acquisition for CURRENT state, drainage, 1998 managed boundary, event-start initial-state observations and 1998 land use. REFERENCE-state construction and concrete model configuration remain dependent internal scientific decisions.

## Qualification evidence
- compare against canonical `main`: only three governance/documentation files before this checkpoint; no data-request status, evidence verdict, schema, implementation or model output changed;
- PR #28 clean-head CI run `35075041501` on `107107a4f20c55987381a86f103b34c0ffaf35ef`: compilation PASS, Status-A-light integrity gate PASS, full unit/contract suite PASS.

## Next permitted action
Run CI on this persisted checkpoint head. If exact-head CI remains green, merge PR #28 and record the current-canonical external-acquisition handoff.

## Exclusions retained
- no new scientific admission;
- no state/reference construction;
- no drainage derivation;
- no historical boundary reconstruction;
- no crop scenario selection;
- no warm-up/restart construction;
- no runnable model configuration;
- no source-model run;
- no missing→zero/default substitution.
