# Tollebeek event forcing v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Capability: `DR_SM_EVENT_FORCING`
Protocol phase: QUALIFY

## Candidate scientific postimage

The candidate admits only an observed station-based forcing baseline for the first bounded Tollebeek extreme-event experiment.

Canonical forcing identity:
- event: `EVT_TOL_1998_OCT`;
- source: KNMI station 273 Marknesse;
- context: `1998-10-24T00:00:00Z` through `1998-10-30T00:00:00Z`;
- grain: 144 contiguous hourly intervals;
- core: `1998-10-27T06:00:00Z` through `1998-10-28T06:00:00Z`;
- core rainfall: 88.4 mm;
- canonical forcing SHA-256: `6c4ca1277523af73f26f6340ec8ebce5d52f42b6040085f7d50ecc78c5ca3c8a`;
- acquired KNMI raw-response SHA-256: `71f2b135769bfed476bbc9ee55282d7e5e9766e2eaf444aa1b8694d382d08dde`.

`DR_SM_EVENT_FORCING = ADMITTED` in the candidate postimage.

`CAP_ATTRIB` remains `DATA_GATED` and retains the explicit pre-existing guardrail:

> Current depth-resolved Tollebeek current/reference states are not admitted

Other run-control inputs remain open.

## Qualification history

### Acquisition/tooling failures that did not change science

1. KNMI probe run `35068407343` failed before scientific processing because the temporary parser expected at least 27 columns while the KNMI `ALL` response contains 25 source fields. Only the row-width expectation was corrected.
2. KNMI probe run `35068470628` then succeeded and established the source checksum, chronology and 88.4-mm rolling 24-hour maximum.
3. An early temporary finalizer workflow was rejected at YAML/workflow parsing before a job ran. No postimage was produced.
4. Finalizer run `35069587830` successfully built and checksum-verified the intended 19-file scientific/data postimage locally, but GitHub rejected the push because an Actions token cannot modify `.github/workflows/ci.yml` without workflow permission. The data/science postimage was not changed to work around this. The bounded data postimage was subsequently pushed without `ci.yml`; the one-line CI compilation addition was applied separately through the GitHub connector.

Temporary acquisition/finalization workflows and helper code are absent from the clean qualification head.

### Pull-request qualification

Initial PR CI run `35069846103` on head `ec5dcc1a7265b245beb6619edcb5b5f048885b95`:
- compilation: PASS;
- integrated Status-A-light project gate: PASS;
- dedicated event-forcing gate: PASS;
- unit/contracts: FAIL one test only.

Failure cause:
- an existing traceability regression test requires the literal guardrail text `Current depth-resolved Tollebeek current/reference states are not admitted`;
- the candidate had semantically equivalent but reworded/lower-case text.

Remediation commit `0d12a51f5b331f445fe083b0b2f5132508c09634` changed only the `CAP_ATTRIB.broken_link` wording so the existing guardrail remains literal while preserving the new event-forcing admission statement. No evidence, status, source data, checksum, event window or scientific boundary changed.

A concurrent/stray commit `c0a15a24dfb93853c1ac4b3792518959b453501b` added only a temporary one-shot finalizer workflow. CI run `35069979886` was fully green, but that head was not accepted as the clean qualification postimage because the temporary workflow was unnecessary repository noise.

The stray workflow was removed in `e9f76353667bb20d10fdbe27f365193f68917bc5`.

Clean-head PR CI run `35070065732` on `e9f76353667bb20d10fdbe27f365193f68917bc5`:
- compilation: PASS;
- integrated Status-A-light integrity gate: PASS;
- event-forcing gate: PASS;
- full unit and contract suite: PASS.

## Scientific qualification verdict

`QUALIFIED_EVENT_FORCING_BASELINE`

The candidate is qualified for admission as the bounded observed station-forcing baseline only.

## Explicit non-admissions

This qualification does not admit:
- an areally exact OT.02 precipitation field;
- radar blending, spatial correction or station-to-field interpolation;
- hydrological initial state or a warm-up state;
- managed surface-water boundary/control behaviour;
- current parcel-drain parameters;
- current or reference compaction state;
- crop/land-use state;
- a SWAP version or numerical/model configuration;
- KNMI-native-to-SWAP input conversion semantics;
- any CURRENT or REFERENCE model run;
- any hydrological attribution result.

KNMI `RH=-1` remains the native trace code (<0.05 mm), not missing and not a physical negative rainfall amount. Source-missing fields remain missing.

## Next permitted action

After exact-head CI on this persisted checkpoint passes, the PR may be marked ready and merged from that exact head.

After canonical admission, the next direct event-specific scientific gate is `DR_SM_INITIAL_STATE`. `DR_SM_MANAGED_BOUNDARY` and `DR_SM_MODEL_CONFIG` may be reconciled independently, but no source-model pair run is permitted until all required controlled inputs are admitted.
