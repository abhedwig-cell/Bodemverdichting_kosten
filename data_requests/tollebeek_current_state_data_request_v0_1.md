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

If privacy prevents release of exact coordinates, request a holder-side reproducible OT.02 selection plus stable pseudonymous location IDs and enough spatial/provenance metadata to audit the selection without reconstructing private farm locations.

## Temporal rule

The reported campaign was measured between September 2020 and June 2021. These observations may support a **dated measured state for their measurement date**.

They must not silently be relabelled as a 2026 CURRENT state. A later use as a current-state proxy requires an explicit temporal-transfer argument, including management/state-change uncertainty, or a newer measurement campaign.

They also must not be silently backdated to the October-1998 event. A 2020–2021 CURRENT/REFERENCE pair under observed 1998 forcing is a controlled historical-forcing scenario unless a separate temporal-transfer argument is qualified.

## Measurement semantics

Dry bulk density from undisturbed ring samples is a direct measured state variable when the record has sufficient provenance and QC.

Penetration resistance is a state indicator but is moisture-, texture- and method-sensitive. It must retain its measurement conditions and must not be converted to bulk density through an undocumented relation.

SoilPhys `modal_bulk_density_g_cm3` is excluded from this request as CURRENT-state evidence. It remains profile context only.

## Public routes identified

- WER Rapport 3382 / DOI `10.18174/672577` documents the campaign and measurement protocol.
- NWO-SIA project `Flevo - land in beweging`, dossier `RAAK.PRO02.021`, states that a valuable province-wide measurement dataset was collected.
- The WER report records project number `5200043298`.
- The Actieplan Bodem & Water Flevoland website provides a public programme contact/referral route.
- Aeres Hogeschool is the project lead institution shown by the NWO-SIA project page.
- WUR/WER is the publisher/research partner for Report 3382.

The bounded public search performed on 2026-09-16 did not locate a downloadable raw coordinate/value table or a separate public dataset identifier linked from the report/project routes. This is a data-access/identifier blocker, not evidence that the records do not exist or cannot be shared.

Detailed source-holder route: `docs/38_tollebeek_current_state_access_route_v0_1.md`.

## Qualified source-holder request order

1. **Aeres Hogeschool / RAAK-PRO project route** — request the source-native final measurement table, codebook or the responsible data-holder contact. Current public project/researcher contact: Karin Pepers (`k.pepers@aeres.nl`).
2. **Wageningen Environmental Research / WER3382 author route** — request the canonical archive/dataset identifier or shareable raw measurement export underlying Report 3382, preserving any required anonymisation or spatial privacy restrictions. Current public WUR profile route: Fenny van Egmond.
3. **Actieplan Bodem & Water Flevoland** — programme/dissemination referral route (`info@bodemenwaterflevoland.nl`) if the project-result landing page or data holder cannot be resolved through Aeres/WUR.

The request should identify all of: `Flevo - land in beweging`, `RAAK.PRO02.021`, WER project `5200043298`, Report 3382, DOI `10.18174/672577`, and the September-2020 through June-2021 campaign.

A stable repository/dataset identifier is preferred over an emailed spreadsheet when one exists.

## Related-project access context

A separate peer-reviewed 2018 field study funded under `RAAK.PRO02.021` states that its own data are available on request from the authors with anonymisation of personal information.

That is **not** the WER3382 2020–2021 dataset. It is retained only as `RELATED_PROJECT_DATA_GOVERNANCE_CONTEXT` and must not be cited as proof that the WER3382 dataset is request-only.

## Reviewed alternative: BIS-4D public bulk-density points

A bounded provenance-recovery campaign reviewed the public 4TU/BIS-4D point dataset `c90215b3-bdc6-4633-b721-4c4a0259d6dc`, specifically `tbl_cal_BD_gcm3.csv`.

The exact recovered file contains 15,871 bulk-density rows with source-native RD coordinates, horizon/depth context, year and `lab`/`field` quality semantics, but:

- no WER3382 / `RAAK.PRO02.021` / project `5200043298` provenance could be established from the CSV or README;
- the exact `year` column contains zero 2020 or 2021 records;
- direct EPSG:28992 intersection with canonical OT.02 returns zero records inside the admitted polygon.

Therefore this specific public BIS release is classified as `REVIEWED_PUBLIC_ALTERNATIVE_NO_OT02_CURRENT_STATE_RECOVERY` and must not be substituted for the requested WER3382 raw dataset.

Detailed route evidence: `docs/37_tollebeek_current_state_bis_recovery_v0_1.md`.

This negative route result does not imply that no Tollebeek observations exist in non-public or other archives.

## Reviewed alternative: DOI / public metadata relations

A bounded DOI/public-metadata provenance probe reviewed DOI `10.18174/672577`, the WUR publication landing page, Crossref, DataCite, OpenAlex, Zenodo and candidate WUR data-host routes.

The DOI resolves correctly to the WUR publication page and that page exposes project number `5200043298`, but:

- no campaign-specific downloadable data or supplement link was exposed on the publication page;
- Crossref contained no dataset `relation` entry and no raw-data link;
- direct DataCite lookup exposed no related dataset identifier;
- narrow DataCite searches for the DOI, `RAAK.PRO02.021`, `5200043298` and title terms produced no provenance-qualified campaign dataset;
- numeric-only DataCite hits for `672577` were unrelated false positives and were excluded;
- narrow Zenodo searches returned no candidate records;
- guessed WUR data-host names did not resolve in the acquisition environment.

This route is classified as `REVIEWED_PUBLIC_DOI_METADATA_ROUTE_NO_RAW_WER3382_DATASET_RECOVERY`.

Detailed route evidence: `docs/41_tollebeek_current_state_doi_recovery_v0_1.md`.

This strengthens the qualified source-holder route but does not prove that no public or shareable source-native dataset exists elsewhere.

## Reviewed alternative: DANS RhoC validation dataset

A bounded provenance review inspected the open DANS dataset DOI `10.17026/PT/BYVPLB`, titled `RhoC validation data from 'Validation of a new Soil Bulk Density sensor'`.

The exact source CSV contains 432 semicolon-delimited depth-resolved records with RhoC and Kopecky-ring bulk-density measurements over 10–60 cm. However:

- the CSV contains no geographic coordinate fields;
- README `Location_code` is only a pit/profile/depth sample identifier;
- no source-native `Tollebeek`, `OT.02`, `Urk`, `Marknesse` or `Emmeloord` identifier is present;
- `Dronten` occurs only as the depositor/institution address, not a measurement-field location;
- the README identifies project `RhoC dichtheidsmeter`, project number `KIEM.K21.01.080`, programme `KIEM`, rather than WER3382 / `RAAK.PRO02.021` / `5200043298`;
- author overlap with Flevoland compaction research is not dataset provenance.

Therefore this dataset is classified as `REVIEWED_PUBLIC_RHOC_DATASET_NOT_SPATIALLY_ASSIGNABLE_TO_OT02`. It is useful as method/context evidence only and must not be substituted for the requested WER3382 source-native point data or reverse-georeferenced from a publication figure.

Detailed route evidence: `docs/42_tollebeek_current_state_rhoc_recovery_v0_1.md`.

## Admission criteria after acquisition

`DR_SM_CURRENT_STATE` may only move toward `READY_FOR_REVIEW` or `ADMITTED` when the candidate records:

1. have source-native location IDs and coordinates, or an independently auditable privacy-preserving OT.02 selection;
2. intersect the admitted OT.02 polygon reproducibly;
3. retain measurement dates and depth semantics;
4. retain direct-measurement versus derived-variable provenance;
5. retain QC and missingness explicitly;
6. can be mapped to a model state representation without replacing missing values by defaults;
7. do not infer area weights from sparse point counts;
8. include an explicit temporal-use decision if used outside the 2020–2021 observation period;
9. retain a source/version/dataset authority sufficient to reproduce the acquisition.
