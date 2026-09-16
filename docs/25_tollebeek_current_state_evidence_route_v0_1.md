# Tollebeek current-state evidence route v0.1

Status: `MEASUREMENT_ROUTE_QUALIFIED_STATE_BLOCKED`

## 1. Scope

This note defines what is currently known about direct soil-compaction state evidence for the first Tollebeek current/reference source-model experiment.

It does **not** define a CURRENT soil state and does not populate `soil_state` values.

## 2. Canonical prerequisites already closed

The project already has:

- an admitted current OT.02 peilgebied polygon;
- an admitted eight-profile SoilPhys/BOFEK2020 profile-context basis;
- explicit separation between modal profile properties and soil-state variables.

The remaining problem is observational state evidence.

## 3. Strongest public measurement source found

Van Egmond et al. (2024), WER Rapport 3382, reports a field campaign across agricultural Flevoland with 305 calibration/validation locations.

Fieldwork was performed from September 2020 through June 2021.

At each location the campaign used:

- dry bulk density from undisturbed 100 cm3 ring samples;
- three replicate rings per sampled depth;
- a fixed 30 cm depth;
- a second field-selected variable depth aimed at the suspected compacted/transition layer;
- ISO 11272:2017 laboratory determination;
- penetration-resistance profiles using a calibrated Eijkelkamp penetrologger;
- ten penetration measurements per location;
- recorded GPS coordinates for the field locations.

This is methodologically relevant direct-measurement evidence.

## 4. Why it cannot yet populate Tollebeek CURRENT

The public report does not expose the source point table with coordinates and values needed to perform an auditable OT.02 spatial join.

The report also concludes that the available measurements and covariates did not support a useful regional map of compacted layers. Therefore:

- no regional interpolation from the report is admitted as an OT.02 state;
- no province-wide compaction percentage is assigned to Tollebeek;
- no visual reading of a printed point map is used as a substitute for source coordinates;
- no nearby Noordoostpolder point is assumed to fall inside OT.02.

## 5. Temporal limitation

The field campaign is dated 2020–2021.

A point measurement from that campaign can, if acquired with full provenance, represent a measured state at its observation date. It is not automatically a 2026 current state because tillage, trafficking, remediation, crop rotation, moisture history and other management may alter the state.

A later experiment may use these data only under one of two explicit designs:

1. a matched historical experiment using the measurement period as its state date; or
2. an explicitly qualified temporal-transfer assumption supported by additional evidence.

## 6. Current-state variables

The canonical project currently has `bulk_density_g_cm3` as a nullable `soil_state` variable.

The public Flevoland campaign supports dry bulk density as a direct measured state variable if raw records are obtained.

Penetration resistance is relevant supporting state evidence but is moisture-, texture- and protocol-sensitive and therefore needs its original conditions/QC retained. This workunit does not add a penetration-resistance state field before the raw-data/model-input contract is reviewed.

## 7. Data-access route

The NWO-SIA project page for `Flevo - land in beweging` states that a valuable provincial measurement dataset was collected. Public searches on 2026-09-16 did not identify a raw downloadable coordinate/value table.

The actionable next step is therefore acquisition rather than interpolation:

- request the raw georeferenced 2020–2021 point data from the project/research holders;
- intersect source coordinates with `TOLLEBEEK_OT02_CURRENT`;
- preserve measurement date, depth, replicate/QC and measurement-method provenance;
- review whether any resulting OT.02 points are sufficient for the intended source-model state representation.

The detailed request contract is `data_requests/tollebeek_current_state_data_request_v0_1.md`.

## 8. Decision

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`.

The measurement method and acquisition route are qualified. The state itself is not admitted.

This is a deliberate data gate, not a missing-value problem to be filled from SoilPhys modal density, provincial interpolation, literature thresholds or assumed compaction classes.
