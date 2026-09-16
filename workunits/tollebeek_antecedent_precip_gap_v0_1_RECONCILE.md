# Tollebeek antecedent precipitation gap v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Canonical start: `main` @ `bf8bde57e86ffdc06cf0278a2c885554e1feddce`
Branch: `work/tollebeek-antecedent-precip-gap-v0.1`

## Inherited authority
PR #42 qualified the one-year KNMI station-273 antecedent forcing source for `1997-10-24T00:00:00Z` through `1998-10-24T00:00:00Z` exclusive, but identified one hydrologically material source gap:
- variables: `DR` and `RH`;
- start: `1998-09-03T00:00:00Z`;
- end exclusive: `1998-09-07T12:00:00Z`;
- duration: 108 hours.

Station 269 Lelystad Airport was found to have observed precipitation for all 108 affected hours, but no cross-station substitution was admitted.

## Decision surface
Determine whether the precipitation gap can be handled by a scientifically traceable observed-source reconstruction, or whether only an explicit multi-member/sensitivity envelope is defensible.

This is not permission to fill the gap by convenience.

## Analysis requirements
1. Query official KNMI hourly precipitation for all available stations across a bounded comparison window surrounding the September-1998 gap.
2. Recover source-station coordinates from KNMI metadata.
3. Rank stations with complete 108-hour gap coverage by distance to the admitted OT.02 domain and/or station 273.
4. For the nearest credible candidates, compare precipitation behaviour against station 273 during surrounding periods where both stations have observations.
5. Use diagnostic metrics only; do not turn correlation or proximity into observational identity.
6. Quantify candidate rainfall totals during the 108-hour gap to expose spatial non-identifiability.

## Permitted classifications
- `G0_DIRECT_LOCAL_OBSERVATION_RECOVERY`: a source-native Marknesse/OT.02 observation is recovered for the missing interval.
- `G1_CONSTRAINED_CROSS_STATION_RECONSTRUCTION`: a separately justified observed-source reconstruction with explicit provenance/uncertainty.
- `G2_MULTI_STATION_ENVELOPE_SCENARIO`: multiple observed stations define an uncertainty envelope; scenario/sensitivity use only.
- `G3_INADMISSIBLE_GAP_DEFAULT`: zero fill, interpolation, undocumented single-station copy or tuned fill.

## Guardrails
- no null→0 for the 108 missing hours;
- no interpolation of rainfall totals/intensity;
- no nearest-station rule solely because a station is geographically closest;
- no silent spatial transfer from airport/station rainfall to OT.02;
- no relabelling reconstructed rainfall as station-273 observation;
- KNMI `RH=-1` remains trace `<0.05 mm`; diagnostic conversions must be explicitly labelled;
- no initial state, warm-up adequacy claim or SWAP run.

## Next permitted action
Run a temporary branch-only read-only KNMI multi-station diagnostic and persist the evidence before any reconstruction/admission decision.