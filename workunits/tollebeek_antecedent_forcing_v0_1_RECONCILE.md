# Tollebeek antecedent forcing v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Workunit: one-year pre-event KNMI forcing acquisition/review
Canonical start: `main` @ `190404e558c65af69ae87c35c5d61ad8e9a51445`
Branch: `work/tollebeek-antecedent-forcing-v0.1`

## Inherited authorities
- `EVT_TOL_1998_OCT` remains the admitted October-1998 event.
- Its canonical observed station-forcing context remains exactly `1998-10-24T00:00:00Z` through `1998-10-30T00:00:00Z`, 144 hourly station-273 records.
- `DR_SM_EVENT_FORCING = ADMITTED` remains unchanged.
- `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE` remains unchanged.
- The initial-state reconstruction protocol requires independently sourced pre-event forcing for any future I1 warm-up/restart.

## Decision surface
Acquire and review one complete antecedent year of official KNMI station-273 hourly observations immediately preceding the admitted event context:
- target interval starts: `1997-10-24T00:00:00Z`;
- target interval ends: `1998-10-24T00:00:00Z` exclusive;
- expected hourly interval count if complete: 8760.

The acquisition request may deliberately cover a wider native date range; exact target bounds are selected from derived observation timestamps rather than inferred from KNMI request-label semantics.

## Scientific boundary
This workunit may qualify an **antecedent-forcing dataset/candidate** only. It does not:
- assert that one year is a sufficient hydrological warm-up;
- create an initial hydrological state;
- select warm-up convergence tolerances;
- fill missing drainage, managed-boundary or crop information;
- extend or overwrite the already admitted 144-hour event forcing baseline;
- authorize a SWAP run.

Warm-up adequacy remains a later numerical sensitivity/convergence decision under the I1 protocol.

## Acquisition checks
Review at minimum:
- exact station identity and source-native timestamps;
- hourly continuity across the target interval;
- native variable set and units;
- missingness by variable;
- KNMI trace-code semantics, especially `RH=-1`;
- overlap consistency with the already admitted event dataset at the boundary where applicable;
- raw and normalized checksums.

## Next permitted action
Run a temporary branch-only read-only acquisition probe against the official KNMI hourly climatology service, persist only an artifact/checkpoint during ACQUIRE/REVIEW, and remove temporary workflow tooling before any canonical merge.