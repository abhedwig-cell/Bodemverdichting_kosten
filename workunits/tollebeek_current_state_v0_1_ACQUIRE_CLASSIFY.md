# Tollebeek current state v0.1 — ACQUIRE / CLASSIFY checkpoint

Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → ADMIT/CLOSE

## Starting authority

- canonical start: `main` @ `736547f03976ab1a916703e88b7ffe7504fc84a8`
- branch: `work/tollebeek-current-state-v0.1`
- governing readiness item: `DR_SM_CURRENT_STATE`
- admitted spatial identity: `TOLLEBEEK_OT02_CURRENT`
- admitted profile-context basis: eight SoilPhys/BOFEK2020 profiles

## ACQUIRE

The strongest public measured-state route identified is Van Egmond et al. (2024), WER Rapport 3382, based on the Flevo - land in beweging field campaign.

The public record supports the following acquisition facts:

- 305 agricultural field locations in Flevoland;
- measurements collected September 2020 through June 2021;
- source GPS coordinates were recorded;
- dry bulk density was measured from three undisturbed 100 cm3 ring samples per sampled depth;
- a fixed 30 cm sampling depth plus a field-selected variable depth were used;
- laboratory bulk-density determination followed ISO 11272:2017;
- penetration resistance was measured with a calibrated Eijkelkamp penetrologger;
- ten penetration measurements were taken per location;
- the official NWO-SIA project record confirms that a valuable province-wide point-measurement dataset was assembled.

Public-source review on 2026-09-16 did not locate the source-native coordinate/value table required for a reproducible intersection with the admitted OT.02 polygon.

## Negative evidence / transfer limit

WER Rapport 3382 explicitly reports that the available measurement data and spatial covariates did not produce a usable regional map of compacted layers.

Therefore the project does not:

- use a regional interpolated map as Tollebeek CURRENT state;
- assign province-wide percentages to OT.02;
- reconstruct point coordinates visually from a printed figure;
- treat nearby Noordoostpolder observations as OT.02 observations without a source-coordinate polygon join.

## Temporal classification

The field data are dated 2020–2021 observations.

If raw records are acquired, they may support a measured state at their observation date. They do not automatically establish 2026 CURRENT conditions. A 2026 use would require either newer observations or an explicit temporal-transfer qualification accounting for possible management/state change.

## Canonical acquisition contract

`data_requests/tollebeek_current_state_data_request_v0_1.md` specifies the required source-native fields, including stable location ID, coordinates/CRS, date, depth semantics, replicate measurements, method/QC information and the reproducible OT.02 spatial join.

Missing or inaccessible source fields remain missing; they are never replaced by zero or convenience defaults.

## CLASSIFY

Three bounded evidence objects are retained:

- `EV_FLEVO_COMPACTION_FIELD_PROTOCOL`: direct-measurement protocol, qualified with local/temporal limitations;
- `EV_FLEVO_COMPACTION_MAP_LIMIT`: qualified guardrail against regional interpolation as local state;
- `EV_FLEVO_COMPACTION_DATASET_ROUTE`: confirmed dataset-acquisition route, `WAIT_DATA` / blocked pending raw records.

Project claim `CL_TOL_CURRENT_STATE_GATE` makes local georeferencing, date, depth, method and QC mandatory before state admission.

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`.

## CLASSIFY verdict

`QUALIFY_MEASUREMENT_ROUTE_NO_ADMIT_CURRENT_STATE`

The direct-measurement method and raw-data acquisition route are strong enough to persist and qualify. They are not sufficient to populate a canonical CURRENT soil-state dataset.

No `data/soil/tollebeek_current_soil_states.csv` is created.

## Automated guardrail

`tools/validate_current_state_gate.py` checks that:

- the three route evidence records and gate claim remain linked;
- SoilPhys `modal_bulk_density_g_cm3` remains `soil_layer` profile context;
- `bulk_density_g_cm3` remains a `soil_state` field;
- `DR_SM_CURRENT_STATE` cannot be `ADMITTED` without a canonical current-state dataset;
- a current-state dataset may not appear while the readiness item remains non-admitted;
- the current blocked state retains raw-coordinate, 2020–2021 and modal-density guardrails.

Next permitted phase: `QUALIFY` the route/gate postimage. No scientific state values are in scope for this workunit.
