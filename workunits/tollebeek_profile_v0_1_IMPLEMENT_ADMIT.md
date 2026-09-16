# Tollebeek profile v0.1 — IMPLEMENT / ADMIT checkpoint

Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → ADMIT → CLOSE

## Canonical start

- `main` at workunit start: `5bd29b31745e093e82b63cc18e46f3a251b1695d`
- branch: `work/tollebeek-profile-v0.1`
- admitted spatial dependency: `TOLLEBEEK_OT02_CURRENT`

## Persisted profile baseline

The bounded profile-context postimage now contains:

- `data/soil/tollebeek_soil_profiles.csv`: eight retained SoilPhys source profiles;
- `data/soil/tollebeek_soil_layers.csv`: 26 contiguous modal profile layers through 120 cm;
- `data/soil/tollebeek_profile_screening_v0_1.json`: deterministic shifted-grid method and coverage metadata;
- `schema/profile_fields_v0_1.yml`: explicit profile-context field semantics;
- `docs/24_tollebeek_profile_baseline_v0_1.md`: scientific admission scope and guardrails;
- `tools/validate_profile_baseline.py` plus unit test and central project-gate integration.

## Evidence and readiness wiring

New evidence/qualification records capture:

- the two shifted 500 m SoilPhys screening grids;
- 117 points, 113 valid profile responses and four no-data responses;
- eight distinct retained source-profile IDs;
- exact ID-level BOFEK2020 crosswalk for all eight profiles;
- the failed historical direct BOFEK GIS URL as a source-route staleness finding, not an absence/zero-area result.

`Q_SOILPHYS_ROUTE` is now qualified with limitations for bounded profile-context acquisition.

`DR_SM_PROFILE` is `ADMITTED` for the bounded profile-context use only.

## Admission semantics

Admitted:

- eight SoilPhys modal profile identities detected in the bounded screening;
- full 0–120 cm horizon geometry for each retained profile;
- texture, SOM and Staring-series profile context;
- `modal_bulk_density_g_cm3` as a `soil_layer` profile-context field;
- exact profile-ID to BOFEK2020-unit crosswalk;
- shifted-grid fractions as diagnostics of this screening design.

Not admitted:

- exact areal weights of the eight profiles;
- parcel-scale soil identity;
- current anthropogenic compaction state;
- any REFERENCE soil state;
- affected compaction area;
- silent reduction to a single majority profile;
- drainage, crop, event, boundary or model configuration.

## Key semantic invariant

`modal_bulk_density_g_cm3` is not `soil_state.bulk_density_g_cm3`.

The profile validator fails if this separation or its guardrails are removed.

## Temporary tooling

All branch-only acquisition/finalization workflows used to query SoilPhys, acquire the BOFEK translation workbook and reconcile the registry delta have been removed from the proposed canonical postimage.

## ADMIT verdict before qualification

`ADMIT_BOUNDED_PROFILE_CONTEXT_BASIS`, subject to exact-head CI qualification.

Next permitted phase: `QUALIFY`.
