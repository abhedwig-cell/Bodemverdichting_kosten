# Tollebeek OT.02 current-state data request v0.1

Status: `OPEN_DATA_REQUEST`

Governing readiness item: `DR_SM_CURRENT_STATE`

## Purpose

Obtain measured or otherwise independently qualified soil-compaction state data that can be spatially and temporally assigned to the admitted OT.02 domain and, where scientifically justified, to the admitted profile-context basis.

The immediate priority is the raw point dataset underlying the 2020–2021 Flevoland field campaign reported by Van Egmond et al. (2024), WER Rapport 3382.

## Minimum requested fields

For each measurement location, retain the source-native identifiers and request at minimum:

- stable measurement/location ID;
- actual field GPS coordinate and CRS;
- sampling/measurement date;
- fixed versus field-selected variable sampling depth;
- exact depth or depth interval represented by each record;
- individual dry-bulk-density ring measurements and/or their traceable mean;
- ring volume and method metadata sufficient to confirm ISO 11272:2017 use;
- penetration-resistance depth series or source-native summary values where available;
- soil moisture/context recorded for penetration measurements where available;
- field QC/quality flags, including plasticity, disturbed/failed samples or other sample-quality notes;
- link to the associated soil-profile/BRO observation or soil description where available;
- texture/lutum information used for interpretation where shareable;
- management or land-use metadata only where it can be shared without breaching privacy/confidentiality.

## Required selection procedure

Raw points must be intersected against canonical `data/spatial/tollebeek_ot02_current.geojson`.

A measurement outside the admitted polygon is not Tollebeek OT.02 evidence merely because it lies in the Noordoostpolder.

Coordinates must not be reconstructed from a printed figure when source coordinates are available or can be requested.

## Temporal rule

The reported campaign was measured between September 2020 and June 2021. These observations may support a **dated measured state for their measurement date**.

They must not silently be relabelled as a 2026 CURRENT state. A later use as a current-state proxy requires an explicit temporal-transfer argument, including management/state-change uncertainty, or a newer measurement campaign.

## Measurement semantics

Dry bulk density from undisturbed ring samples is a direct measured state variable when the record has sufficient provenance and QC.

Penetration resistance is a state indicator but is moisture-, texture- and method-sensitive. It must retain its measurement conditions and must not be converted to bulk density through an undocumented relation.

SoilPhys `modal_bulk_density_g_cm3` is excluded from this request as CURRENT-state evidence. It remains profile context only.

## Public routes identified

- WER Rapport 3382 / DOI 10.18174/672577 documents the campaign and measurement protocol.
- NWO-SIA project `Flevo - land in beweging`, dossier `RAAK.PRO02.021`, states that a valuable province-wide measurement dataset was collected.
- The Actieplan Bodem & Water Flevoland website provides a public programme contact route.
- WUR provides a public contact page for first author Fenny van Egmond.

The public search performed on 2026-09-16 did not locate a downloadable raw coordinate/value table. This is a data-access blocker, not evidence that the records do not exist.

## Reviewed alternative: BIS-4D public bulk-density points

A bounded provenance-recovery campaign reviewed the public 4TU/BIS-4D point dataset `c90215b3-bdc6-4633-b721-4c4a0259d6dc`, specifically `tbl_cal_BD_gcm3.csv`.

The exact recovered file contains 15,871 bulk-density rows with source-native RD coordinates, horizon/depth context, year and `lab`/`field` quality semantics, but:

- no WER3382 / `RAAK.PRO02.021` / project `5200043298` provenance could be established from the CSV or README;
- the exact `year` column contains zero 2020 or 2021 records;
- direct EPSG:28992 intersection with canonical OT.02 returns zero records inside the admitted polygon.

Therefore this specific public BIS release is classified as `REVIEWED_PUBLIC_ALTERNATIVE_NO_OT02_CURRENT_STATE_RECOVERY` and must not be substituted for the requested WER3382 raw dataset.

Detailed route evidence: `docs/37_tollebeek_current_state_bis_recovery_v0_1.md`.

This negative route result does not imply that no Tollebeek observations exist in non-public or other archives.

## Secondary request route: RAAK.PRO02.021 2018 field-scale dataset

Van Orsouw et al. (2022), DOI `10.3390/agronomy12071669`, is explicitly funded under the same SIA grant `RAAK.PRO02.021` and by the Province of Flevoland. The paper states that its underlying data are available on request from the authors.

This dataset is **not** the WER3382 regional campaign. Source-native publication metadata describe a distinct single-field experiment at the edge of Emmeloord with 25 measurement locations and autumn-2018 fieldwork after a 2017 heavy-compaction event. The later WER3382 campaign instead contains 305 regional locations sampled from September 2020 through June 2021.

Accordingly, the Van Orsouw dataset is a secondary request route for project-family/methodological evidence only. If obtained, it must retain source-native coordinates, date/depth/method/QC fields and be independently intersected with OT.02. No OT.02 membership may be inferred from the article figure or from the word `Emmeloord`.

Detailed route evidence: `docs/38_tollebeek_current_state_pointscale_route_v0_1.md`.

## Admission criteria after acquisition

`DR_SM_CURRENT_STATE` may only move toward `READY_FOR_REVIEW` or `ADMITTED` when the candidate records:

1. have source-native location IDs and coordinates;
2. intersect the admitted OT.02 polygon reproducibly;
3. retain measurement dates and depth semantics;
4. retain direct-measurement versus derived-variable provenance;
5. retain QC and missingness explicitly;
6. can be mapped to a model state representation without replacing missing values by defaults;
7. do not infer area weights from sparse point counts;
8. include an explicit temporal-use decision if used outside the 2020–2021 observation period.
