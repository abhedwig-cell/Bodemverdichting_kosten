# Tollebeek antecedent forcing v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Branch: `work/tollebeek-antecedent-forcing-v0.1`

## Qualified decision
Verdict: `QUALIFIED_ANTECEDENT_FORCING_SOURCE_WITH_PRECIPITATION_GAP`

The official KNMI station-273 record provides a reproducible one-year antecedent meteorological source basis for `1997-10-24T00:00:00Z` through `1998-10-24T00:00:00Z` exclusive, with complete hourly timestamps and exact consistency at the subsequent event boundary.

It is **not** admitted as complete warm-up forcing because `DR` and `RH` are source-missing for 108 contiguous hours (`1998-09-03T00:00:00Z`–`1998-09-07T12:00:00Z`).

Station 269 has observed precipitation for all 108 affected hours but is diagnostic only; no cross-station replacement rule is qualified here.

## Immutable acquisition evidence
- run `35093815232`: one-year station-273 acquisition/review — SUCCESS;
- 8760/8760 target hours, no time gaps or duplicates;
- raw SHA-256 `aac1c6082105e685d594aae518e2dcfe080513e4485b546e177499005b74f52b`;
- normalized candidate SHA-256 `5ed2c604f6cce2c09c7379eeb3f745fed6b4f46a4778bb6c0fbb20098ada0272`;
- boundary comparison with admitted event forcing: 24 rows, 0 mismatches;
- run `35093938445`: precipitation-gap diagnosis — SUCCESS;
- station-273 `DR`/`RH` missing block: 108 hours;
- station 269 has 0 missing `RH` hours over the reviewed year and observed `RH` for all 108 station-273 gap hours.

## Clean qualification
Pre-checkpoint clean branch head: `73a28b69f4c389a31f8a63cbf138a1deabe19186`.
CI run `35094131309`: SUCCESS.
- compilation PASS;
- Status-A-light integrity gate PASS;
- unit/contract suite PASS.

## Scientific boundary
No mutation to:
- `DR_SM_INITIAL_STATE` (`PARTIAL_EVIDENCE` retained);
- `DR_SM_EVENT_FORCING` or its 144-hour admitted dataset;
- event register or forcing schema;
- drainage, boundary, land-use or model configuration;
- model inputs or model outputs.

No one-year warm-up adequacy claim is made.

## Next permitted action
A separate bounded workunit may qualify a precipitation-gap treatment or alternative observed precipitation source. Null-to-zero, interpolation and silent station substitution remain forbidden.