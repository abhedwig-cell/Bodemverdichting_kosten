# Tollebeek current state v0.1 — RECONCILE checkpoint

Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → ADMIT/CLOSE

## Starting authority

- canonical start: `main` @ `736547f03976ab1a916703e88b7ffe7504fc84a8`
- branch: `work/tollebeek-current-state-v0.1`
- governing readiness item: `DR_SM_CURRENT_STATE`
- admitted spatial domain: `TOLLEBEEK_OT02_CURRENT`
- admitted profile-context basis: eight SoilPhys/BOFEK2020 profiles from PR #20

No open or materially equivalent current-state workunit/PR was found before branch creation.

## Existing canonical boundary

`DR_SM_CURRENT_STATE` is `PARTIAL_EVIDENCE`.

The project currently defines `bulk_density_g_cm3` as a nullable `soil_state` variable. The admitted SoilPhys profile baseline deliberately stores derived/modal density separately as `modal_bulk_density_g_cm3` on `soil_layer`. Modal SoilPhys values therefore cannot be promoted into CURRENT or REFERENCE state by convenience.

## New external evidence route identified

Wageningen Environmental Research Rapport 3382 (Van Egmond et al., 2024), `Regionale kartering bodemverdichting in de provincie Flevoland`, is the strongest public current-state measurement source found in this reconciliation.

Relevant properties:

- 305 field locations in agricultural Flevoland, excluding headlands;
- fieldwork conducted September 2020 through June 2021;
- dry bulk density measured with three 100 cm3 undisturbed ring cores at 30 cm and at a field-selected variable depth;
- laboratory determination according to ISO 11272:2017;
- penetration resistance measured with a calibrated Eijkelkamp penetrologger, 1 cm2 / 60 degree cone, target insertion rate 2 cm/s;
- ten penetration measurements per location;
- exact sampling coordinates were recorded during fieldwork;
- the public report does not expose the raw coordinate/value table needed to identify measurements inside the admitted OT.02 polygon;
- the study concludes that its measured data and covariates did not yield a usable regional compaction map.

## Scientific classification at RECONCILE

The 2020–2021 Flevoland measurements are potentially valid **point-level measured-state evidence** if the raw records and coordinates can be acquired. They are not authority for an OT.02-wide current state and are not automatically representative of 2026 conditions.

The published regional interpolation must not be used as a substitute, because the source itself reports that no usable regional map could be produced.

The ongoing RhoC SOLID project (2025–2029) is a promising future acquisition route for depth-resolved bulk-density mapping, but no future deliverable may be treated as present project data.

## Reconcile verdict

`PROCEED_ACQUIRE_CURRENT_STATE_EVIDENCE_ROUTE`

No CURRENT soil-state value is admitted in this phase.

Next permitted action:

1. attempt to locate a public raw point dataset or explicit project-data access route for the 2020–2021 field campaign;
2. determine whether any identified records can be spatially joined to OT.02 with stable provenance;
3. if raw local measurements remain inaccessible, qualify the measurement/data-request route and close `DR_SM_CURRENT_STATE` as still data-gated rather than inventing or spatially interpolating values.

## Explicit exclusions

- no use of SoilPhys modal bulk density as CURRENT state;
- no use of regional interpolation as OT.02 state;
- no assignment of province-wide percentages to Tollebeek;
- no assumption that a 2020–2021 measurement is unchanged in 2026;
- no REFERENCE state construction;
- no source-model run.
