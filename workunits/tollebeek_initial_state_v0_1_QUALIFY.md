# Tollebeek initial state v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Capability: `DR_SM_INITIAL_STATE`
Protocol phase: QUALIFY

## Authority

- canonical start: `96e0043196f1bacf7274e6071e46d9552421dd6c`
- branch: `work/tollebeek-initial-state-v0.1`
- clean pre-checkpoint head: `8f01c47d49f4a56b938e98422ea88c6ad8a77251`
- PR: `#24`

## Qualified evidence route

- two historical BRO GLD series occur inside admitted OT.02 at `GMW000000053815`, but their monitoring screens are deep and are qualified only as piezometric historical context;
- a bounded public BRO screening for historical shallow series with screen top 0–5 m below registered ground and a registration span covering 1998-10-24 found four candidates within 10 km and zero inside admitted OT.02;
- nearby shallow observations outside OT.02 remain context only and are not interpolated into the project domain;
- historical source status/class `onbekend` is preserved;
- owner narrative antecedent wetness remains qualitative context only.

## Readiness decision

`DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE`.

No groundwater-level value, pressure-head profile, water-content profile, saturation profile, warm-up state or restart state is admitted.

## Guardrails

Rejected transformations include:

- deep piezometric head → phreatic groundwater table;
- target surface-water peil → initial groundwater level;
- narrative `fully saturated` → numerical soil-water state;
- outside shallow observations → spatially interpolated OT.02 initial state;
- missing/unknown → zero, field capacity, hydrostatic or other convenience defaults.

A warm-up/restart alternative remains blocked until the required model configuration, managed boundary, drainage and land-use context are sufficiently specified for a reproducible and matched CURRENT/REFERENCE initialization protocol.

## Qualification evidence

- generated postimage validation run `35071474635`: central project gate PASS and complete test suite `33/33` PASS; subsequent push failure was tooling-only because the Actions token lacked workflow-file update permission;
- persisted clean-head PR CI run `35072243029`: compile PASS, Status-A-light integrity gate PASS, unit/contract tests PASS;
- final branch diff contains no temporary acquisition/finalization workflows.

## Verdict

`QUALIFIED_INITIAL_STATE_OBSERVATION_ROUTE_NO_ADMIT_STATE`

## Next permitted action

After this checkpoint, only exact-head CI verification, merge/admission of the evidence-route decision, and CLOSE are permitted in this workunit. A numerical initial state requires a future workunit with new qualifying evidence or a separately qualified reproducible warm-up/restart protocol.
