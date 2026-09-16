# Tollebeek current state v0.1 — QUALIFY checkpoint

Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → ADMIT/CLOSE

## Qualified pre-checkpoint boundary

- canonical start: `main` @ `736547f03976ab1a916703e88b7ffe7504fc84a8`
- work branch: `work/tollebeek-current-state-v0.1`
- governing readiness item: `DR_SM_CURRENT_STATE`
- qualified pre-checkpoint head: `73a9b47637d7d07296588becae9a9a75f44abf9e`
- PR: #21
- CI run: `35065908915`
- result: `SUCCESS`

## Qualification gates passed

- Python compilation: PASS;
- evidence integrity: PASS;
- formal traceability: PASS;
- domain-schema integrity: PASS;
- source-model input-readiness integrity: PASS;
- admitted OT.02 spatial geometry integrity: PASS;
- admitted profile-baseline integrity: PASS;
- current-state route/gate integrity: PASS;
- full unit and contract test suite: PASS.

## Qualified postimage

Qualification supports only the following bounded capability:

- WER Rapport 3382 / Flevo - land in beweging is a qualified route to direct 2020–2021 Flevoland field measurements;
- the documented bulk-density and penetration-resistance protocol is suitable for candidate point-state evidence when source records are acquired;
- the source study's failed regional interpolation is a qualified guardrail against substituting a regional map for local state;
- the official project metadata establishes a raw-data acquisition route, presently `BLOCKED_DATA` because a public source-native coordinate/value table was not found;
- the project now has a concrete raw-data request contract and an automated gate preventing premature state admission.

## Scientific non-admission

No Tollebeek CURRENT state is qualified by this workunit.

Specifically not qualified:

- any bulk-density number for an OT.02 profile/layer;
- any penetration-resistance number for an OT.02 profile/layer;
- a province-wide percentage transferred to Tollebeek;
- a regional interpolated value;
- a visually reconstructed map point;
- SoilPhys modal density as CURRENT state;
- automatic transfer of a 2020–2021 observation to 2026.

`DR_SM_CURRENT_STATE` therefore remains `PARTIAL_EVIDENCE`.

## QUALIFY verdict

`PASS_MEASUREMENT_ROUTE_CURRENT_STATE_BLOCKED`

Next permitted action: admit the measurement-route/evidence-gate postimage only from an exact green checkpoint head. Actual current-state admission requires external raw source records and a separate local/temporal qualification.
