# Tollebeek model configuration v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Capability: `DR_SM_MODEL_CONFIG`
Protocol phase: QUALIFY

## Authority
- project canonical start: `main` @ `f6aba17c016a4b860f750a17678cc4ec51875a3f`
- branch: `work/tollebeek-model-config-v0.1`
- clean pre-checkpoint head: `7c0090348f27351c37a615f72dc76c5b7062dc11`
- event: `EVT_TOL_1998_OCT`

## Qualified authority chain
- SWAP5 scientific executable authority: `50346642bd565f79134ea17d5462e544b354998c`
- scientific production tree: `3b085d7dea3d3f3fce42ad9d8f259a8350205846`
- Status-A acceptance authority: `992a5c657bfe10a10100f92e0cb77c4825ae65b6`
- live canonical/governance head reviewed: `80c6faaa8a277d9596a6da7bc5d2244c0df1bb82`

The moving live governance head is deliberately not substituted for the pinned scientific executable authority.

## Scientific/configuration verdict
`QUALIFIED_SWAP5_EXECUTION_AUTHORITY_NO_ADMIT_TOLLEBEEK_CONFIGURATION`

`DR_SM_MODEL_CONFIG = PARTIAL_EVIDENCE`.

No concrete `model_configuration` row/dataset and no CURRENT/REFERENCE model run is admitted. Remaining partial inputs must not be closed with SWAP defaults or convenience assumptions. A future admitted configuration must explicitly bind all controlled model, boundary, drainage, initialization, crop/vegetation, forcing-conversion, numerical and output dimensions and preserve CURRENT/REFERENCE equality except for the admitted soil-state contrast.

## Validation evidence
- initial finalizer run `35074357126`: generated intended postimage but central evidence integrity rejected the new non-vocabulary provenance label `SOFTWARE_AUTHORITY`; no commit occurred;
- remediation changed provenance classification only to existing controlled value `SOFTWARE_QA`; authority SHAs, readiness state and scientific verdict were unchanged;
- retry finalizer run `35074440690`: SUCCESS; central Status-A-light project gate and complete unit/contract suite PASS; postimage committed;
- temporary workflows removed;
- clean PR-head CI run `35074581205` on `7c0090348f27351c37a615f72dc76c5b7062dc11`: SUCCESS; compilation PASS, central integrity gate PASS, full tests PASS.

## Next permitted action
Run CI on this persisted qualification head. If exact-head CI remains green, admit the authority-route/no-config decision via PR #27.

## Exclusions retained
- no runnable Tollebeek config;
- no drainage/default resistance;
- no initial groundwater/profile default;
- no lower-boundary convenience choice;
- no representative/default crop;
- no modal profile density as CURRENT state;
- no model run;
- missing/partial scientific inputs remain explicit.
