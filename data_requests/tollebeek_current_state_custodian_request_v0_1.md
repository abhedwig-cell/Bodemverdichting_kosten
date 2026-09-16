# Tollebeek OT.02 current-state custodian request v0.1

Status: `READY_TO_SEND_EXTERNALLY`

Governing readiness item: `DR_SM_CURRENT_STATE`

## Request target

Raw/source-native point measurements underlying the regional Flevoland soil-compaction campaign reported in WER Rapport 3382 (`10.18174/672577`, project `5200043298`) and the SIA RAAK-PRO project *Flevo - land in beweging* (`RAAK.PRO02.021`).

The requested subset is specifically needed to determine whether any measurements fall inside the canonical Tollebeek OT.02 peilgebied.

## Minimum requested fields

For each measurement record/location, request:

- source-native location/measurement ID;
- X/Y coordinate and CRS, preferably the original field GPS coordinate;
- sampling/measurement date;
- measurement type (`bulk_density`, `penetration_resistance`, profile/context, etc.);
- exact depth or depth interval and whether it is the fixed 30 cm or field-selected variable layer;
- individual 100 cm3 ring results where shareable, otherwise their traceable mean plus replicate count/QC;
- dry bulk density units and method metadata confirming ISO 11272:2017 where applicable;
- penetration-resistance depth series or source-native values, including instrument/method settings and soil-moisture context where available;
- soil texture/lutum/context used in interpretation where shareable;
- quality flags, rejected/disturbed samples and missing-value coding;
- provenance linking the record to the campaign/project/report.

Personal land-user information is **not required**. Pseudonymized farm/field IDs are sufficient where necessary for privacy, provided within-location record relationships remain reproducible.

## Requested delivery form

Preferred: CSV/TSV/GeoPackage or another machine-readable export with data dictionary.

If coordinates cannot be shared directly for privacy reasons, request one of these alternatives in order of preference:

1. custodian performs the OT.02 polygon intersection and returns source-native records flagged `inside_OT02=true/false`, together with the exact polygon authority used;
2. privacy-preserving spatial key that still permits independently auditable OT.02 membership;
3. a custodian-produced anonymized spatial subset containing only records inside OT.02.

A map image or rounded/visually reconstructed coordinates is insufficient for scientific admission.

## Canonical selection after receipt

The received records will be intersected against:

`data/spatial/tollebeek_ot02_current.geojson`

CRS: EPSG:28992.

No point outside that polygon will be called OT.02 evidence solely because it is in the Noordoostpolder or Flevoland.

## Temporal use

The campaign dates are September 2020 through June 2021. Any admitted record represents a dated measured state for its observation date.

It will not be called a 1998 or 2026 state without a separately qualified temporal-transfer argument.

## Admission boundary

Receipt of the dataset alone does not imply `DR_SM_CURRENT_STATE = ADMITTED`.

Admission additionally requires reproducible OT.02 selection, retained depth/QC/provenance semantics, explicit relation to the admitted profile context, and a separate decision on transformation from measured compaction indicators to the hydraulic state required by SWAP.