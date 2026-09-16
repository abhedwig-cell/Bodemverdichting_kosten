# Tollebeek OT.02 profile baseline v0.1

Status: `PROFILE_CONTEXT_ADMISSION_BASELINE`

Canonical dependency: admitted `TOLLEBEEK_OT02_CURRENT` peilgebied geometry.

## Admitted profile-context basis

A deterministic SoilPhys screening was performed on two 500 m grids inside the admitted OT.02 polygon. Grid B is shifted 250 m in x and y relative to Grid A.

The screening contains 117 points: 113 returned SoilPhys profile information and 4 returned no soil information. Eight distinct SoilPhys source-profile IDs were detected and all eight are retained rather than selecting one convenient or majority profile:

| SoilPhys profile | Soil mapping unit | BOFEK2020 unit | Combined valid-point screening fraction |
| --- | --- | ---: | ---: |
| 90115240 | Mn15A | 4019 | 0.6195 |
| 15100 | Mv51A | 4006 | 0.1239 |
| 15250 | Mn15Av | 4004 | 0.1150 |
| 90115270 | Mn25A | 4018 | 0.0442 |
| 11020 | Zn10A | 3005 | 0.0354 |
| 12010 | Sn13A | 3004 | 0.0265 |
| 11021 | Zn10Av | 3001 | 0.0265 |
| 90111050 | Zn50A | 3015 | 0.0088 |

The profile register is `data/soil/tollebeek_soil_profiles.csv`. The complete retained modal horizon definitions through 120 cm are in `data/soil/tollebeek_soil_layers.csv`. The screening design and coverage metadata are in `data/soil/tollebeek_profile_screening_v0_1.json`.

## Interpretation of the screening fractions

The fractions above are diagnostics from two deterministic shifted grids. They are useful for detecting whether one profile dominates and whether the detected composition is highly sensitive to a half-grid shift.

They are **not admitted exact areal weights**. They must not be multiplied by 1496.52 ha or 1497 ha and presented as exact hectares per soil profile. Four screening points returned no SoilPhys profile, and the independent current BOFEK polygon overlay was not completed because the historical direct WUR GIS download route returned HTTP 404 while the current public map route is interactive.

No missing or unresolved area is silently assigned to any profile.

## Profile properties versus soil state

SoilPhys provides derived/modal profile context. The retained layer fields include horizon geometry, texture, organic matter, Staring-series building block and modal bulk density.

`modal_bulk_density_g_cm3` belongs to `soil_layer` and is profile context.

`bulk_density_g_cm3` belongs to `soil_state` and is reserved for an explicitly qualified CURRENT, REFERENCE or scenario state.

The two fields are intentionally different. A SoilPhys modal density must not be copied into CURRENT or REFERENCE merely because it is numerically available.

## BOFEK2020 crosswalk

The official WUR BOFEK2020 translation workbook was used as an ID-level crosswalk. Exact source-profile IDs are used because the same soil mapping-unit code can occur for multiple standard profiles and can map differently.

The crosswalk is qualified for semantic profile-to-BOFEK identification. It is not an admitted BOFEK area overlay for OT.02.

## Admission boundary

`DR_SM_PROFILE` is admitted for:

- bounded OT.02 profile identities;
- depth-resolved modal profile/layer context through 120 cm;
- exact source-profile provenance;
- BOFEK2020 profile crosswalk;
- diagnostic shifted-grid screening fractions.

It does not admit:

- current anthropogenic compaction state;
- a reference soil state;
- exact profile-area weights;
- affected compaction area;
- a final reduction to one representative model profile;
- drainage, crop, event, boundary or source-model configuration.

## Next dependency

The next scientific gate is `DR_SM_CURRENT_STATE`.

Current-state work must start from the admitted eight-profile context basis and identify dated measurements or a separately qualified derivation for the state variables required by the eventual source model. If the first experiment uses a subset of profiles, that selection must be explicit and justified; the majority `Mn15A` screening result is not by itself permission to silently model all of OT.02 as one profile.
