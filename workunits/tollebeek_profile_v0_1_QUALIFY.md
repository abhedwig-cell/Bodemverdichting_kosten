# Tollebeek profile v0.1 — QUALIFY checkpoint

Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → ADMIT → CLOSE

## Qualified content boundary

- canonical start: `main` @ `5bd29b31745e093e82b63cc18e46f3a251b1695d`
- work branch: `work/tollebeek-profile-v0.1`
- governing readiness item: `DR_SM_PROFILE`
- exact qualified pre-checkpoint head: `08a5849ccad39d582f34ebeea4acfe337e669bef`
- GitHub Actions CI run: `35064604582`
- result: `SUCCESS`

The immediately preceding content head `13e5d67bb8db90a20dab1cf9828a735b9d420590` also passed CI run `35064594604`; the only subsequent change before the exact qualified head was the PR-ready boundary checkpoint.

## Qualification gates passed

- Python compilation: PASS;
- evidence integrity: PASS;
- formal traceability: PASS;
- Data Model/domain schema integrity: PASS;
- source-model input-readiness integrity: PASS;
- admitted OT.02 spatial geometry integrity: PASS;
- OT.02 profile-baseline identity/crosswalk/layer-contiguity/state-boundary validation: PASS;
- full unit and contract test suite: PASS.

## Qualified scientific postimage

The branch may be admitted for the following bounded capability only:

- eight SoilPhys modal profile identities detected by the deterministic two-grid OT.02 screening;
- complete retained 0–120 cm profile-layer context for those eight profiles;
- exact source-profile-ID to BOFEK2020-unit crosswalk;
- screening fractions as diagnostic sampling fractions;
- explicit separation of modal profile bulk density from `soil_state.bulk_density_g_cm3`.

## Non-admitted semantics

Qualification does not establish:

- exact profile-area weights;
- current anthropogenic compaction state;
- a REFERENCE soil state;
- affected compaction area;
- parcel-scale soil identity;
- drainage/crop/event/boundary/model configuration;
- any source-model attribution result.

Four of 117 deterministic screening points returned no SoilPhys profile. They remain explicit no-data and are not silently assigned to another profile.

The historical direct BOFEK GIS download route returned HTTP 404; this is recorded as source-route staleness and is not interpreted as missing or zero BOFEK coverage.

## QUALIFY verdict

`PASS_QUALIFY_PROFILE_CONTEXT`

Next permitted action: admit only from an exact green head that contains this checkpoint and no semantic changes beyond it.
