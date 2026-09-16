# Tollebeek antecedent forcing v0.1 — ACQUIRE / REVIEW checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Canonical start: `main` @ `190404e558c65af69ae87c35c5d61ad8e9a51445`
Branch: `work/tollebeek-antecedent-forcing-v0.1`

## Acquisition

Temporary branch-only probe `35093815232` acquired official KNMI hourly station-273 observations and reviewed the exact interval `1997-10-24T00:00:00Z` through `1998-10-24T00:00:00Z` exclusive.

Evidence:
- 8760 expected hours / 8760 returned target rows;
- zero timestamp gaps;
- zero duplicate timestamps;
- raw SHA-256 `aac1c6082105e685d594aae518e2dcfe080513e4485b546e177499005b74f52b`;
- normalized candidate SHA-256 `5ed2c604f6cce2c09c7379eeb3f745fed6b4f46a4778bb6c0fbb20098ada0272`;
- artifact ID `10444928948`;
- artifact ZIP SHA-256 `8b3a0d2deed4a26234b00c97cff7931429c9e17397f89766da60eec7cc43991e`;
- independent 24-hour boundary re-acquisition against the admitted event dataset: 0 mismatches.

## Missingness finding

The target time axis is complete, but `DR` and `RH` are both source-missing for 108 hours.

Diagnostic probe `35093938445` shows the missing precipitation is one contiguous block:
- `1998-09-03T00:00:00Z` through `1998-09-07T12:00:00Z` exclusive;
- 108 hours.

Station 269 Lelystad Airport has precipitation observations for all 108 affected hours and zero missing `RH` hours over the reviewed year, but no cross-station substitution is admitted here.

Diagnostic artifact ID `10445003877`, artifact ZIP SHA-256 `3a277ba3ea5b6c68dfe57c7921b8247312bf601d0c67d6a0cae410171fbffd5d`.

## Classification

`QUALIFIED_ANTECEDENT_FORCING_SOURCE_WITH_PRECIPITATION_GAP`

This is a qualified source/data route with an explicit hydrologically material limitation. It is not a complete model forcing and does not change `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE`.

## Mutations
- added RECONCILE checkpoint;
- added `docs/45_tollebeek_antecedent_forcing_review_v0_1.md`;
- no event register mutation;
- no forcing-schema mutation;
- no initial-state data;
- no model configuration or run.

## Next permitted action
Separately qualify a precipitation-gap treatment or obtain an alternative observed source. Preserve provenance per affected hour. Do not use null→0, interpolation or station substitution by convenience.

## Exclusions retained
- no one-year-spin-up adequacy claim;
- no initial state/restart;
- no drainage/boundary/crop defaults;
- no cross-station precipitation fill;
- no change to the admitted 144-hour event-forcing baseline.