# Tollebeek OT.02 current-state access route v0.1

Status: **QUALIFICATION CANDIDATE — access route only**

Governing readiness item: `DR_SM_CURRENT_STATE`

This note defines the currently supported acquisition route for the raw 2020–2021 Flevoland soil-compaction measurements underlying WER Rapport 3382 / project `5200043298` and the completed RAAK-PRO project `Flevo - land in beweging` (`RAAK.PRO02.021`).

It does **not** claim that the dataset is closed, confidential or unavailable. It records only what was and was not publicly recoverable on 2026-09-16 and which source holders can resolve the remaining access question.

## 1. Dataset existence is established

Independent public project/report sources establish that:

- a large Flevoland field-measurement campaign was performed;
- more than 300 point measurements were collected with conventional soil methods in the wider RAAK-PRO project;
- WER Rapport 3382 uses new field measurements for regional soil-compaction mapping;
- the campaign underlying Report 3382 includes direct dry-bulk-density and penetration-resistance measurements;
- the project describes the accumulated provincial measurement collection as a valuable dataset.

Therefore the current blocker is not `UNKNOWN_DATASET_EXISTENCE`.

It is:

`KNOWN_MEASUREMENT_DATASET — RAW SOURCE RECORD ACCESS / IDENTIFIER UNRESOLVED`.

## 2. Public publication route reviewed

WER Rapport 3382:

- DOI: `10.18174/672577`
- WER report number: `3382`
- project number: `5200043298`
- publication year: `2024`

The WUR publication record exposes the report/PDF but no separate raw point-data file, supplementary dataset identifier or linked public data repository was found in the bounded search.

This does not prove that no separate repository entry exists; it means none was recoverable through the publication record and targeted public searches used in this campaign.

## 3. Project dissemination route reviewed

The NWO-SIA project page for `Flevo - land in beweging` (`RAAK.PRO02.021`) states that a valuable dataset covering the province was collected and that project information/results would be made accessible through the Flevoland Actieprogramma/Actieplan Bodem en Water route.

The current Actieplan Bodem & Water website was reviewed on 2026-09-16. It provides project/programme information and a public programme contact route, but the bounded search did not locate a downloadable WER3382/Flevo-land-in-beweging raw measurement dataset.

Again, absence from the current website search is not evidence that the data do not exist or cannot be shared.

## 4. Related RAAK.PRO02.021 data-governance clue

A separate peer-reviewed study funded under the same RAAK.PRO02.021 project explicitly states that its data are available on request from the authors with anonymisation of personal information.

That publication concerns a **different 2018 field dataset** and must not be conflated with the 2020–2021 / WER3382 campaign.

Its access statement is therefore classified only as:

`RELATED_PROJECT_DATA_GOVERNANCE_CONTEXT`

It is **not** evidence that the WER3382 raw dataset has the same access policy.

## 5. Public alternative archives reviewed

The public BIS-4D bulk-density point release was separately acquired and screened.

It contains no WER3382/project provenance, no 2020/2021 year records and no bulk-density point inside the admitted OT.02 polygon. That route is canonically closed as:

`REVIEWED_PUBLIC_ALTERNATIVE_NO_OT02_CURRENT_STATE_RECOVERY`.

It must not be reopened as a convenience substitute.

Targeted public searches for exact report/project identifiers against generic dataset-repository routes did not reveal a separate raw WER3382 dataset record during this campaign.

## 6. Primary source-holder route

### A. Aeres Hogeschool / RAAK-PRO project route

Aeres Hogeschool is the lead institution shown by the completed NWO-SIA project page.

The current public Aeres researcher/project route identifies **Karin Pepers** as a soil-compaction researcher and project contact in the Sustainable Soil Management group.

Public contact:

- `k.pepers@aeres.nl`

Request purpose:

- confirm whether the final 2020–2021 point dataset underlying WER3382 is held by Aeres, WUR/WER or another consortium partner;
- request the source-native measurement table or the responsible data-holder contact;
- request any data dictionary / codebook needed to interpret IDs, coordinates, depths, ring replicates, penetration-resistance records and QC;
- request a citable dataset identifier/version if one exists.

### B. Wageningen Environmental Research / report-author route

WER Rapport 3382 is published by Wageningen Environmental Research and lists Fenny van Egmond as first author.

The current public WUR profile provides a direct contact route for Fenny van Egmond, whose expertise includes soil data, monitoring, spatial data and FAIR data.

Request purpose:

- ask whether the raw coordinate-level data used for Report 3382 are archived in a WUR/WER research-data system;
- request the canonical dataset identifier or, if shareable, the raw measurement export plus metadata;
- ask which fields/coordinates may require anonymisation or spatial generalisation because measurements were collected on private agricultural parcels.

The project should prefer a stable dataset/repository identifier over an emailed spreadsheet when one exists.

### C. Actieplan Bodem & Water Flevoland

The current public programme contact is:

- `info@bodemenwaterflevoland.nl`

This is a programme/dissemination and referral route, not presumed data authority.

Use it to locate the project-result/data landing page or correct holder if Aeres/WUR cannot supply the dataset directly.

## 7. Minimum request payload

The request should identify the target unambiguously:

- project: `Flevo - land in beweging`
- dossier: `RAAK.PRO02.021`
- WER project number: `5200043298`
- report: WER Rapport 3382
- DOI: `10.18174/672577`
- campaign period: September 2020 through June 2021
- scientific purpose: auditable Tollebeek OT.02 soil-compaction state assessment and source-model attribution

Requested source-native content should follow `data_requests/tollebeek_current_state_data_request_v0_1.md` and include, where available:

- stable location/sample IDs;
- coordinates and CRS;
- measurement date;
- exact depth/depth interval;
- individual ring measurements and/or traceable mean;
- method/ring-volume metadata;
- penetration-resistance depth series;
- relevant moisture/context measurements;
- QC/status flags;
- codebook/data dictionary;
- dataset/version/provenance identifier.

If privacy prevents release of exact coordinates, request whether a trusted spatial intersection against the canonical OT.02 polygon can be performed by the data holder and whether source-native OT.02-selected records can be supplied with suitably anonymised coordinates or stable pseudonymous location IDs.

## 8. Acceptance after receipt

Receipt alone does not admit CURRENT state.

The acquired data must still pass:

1. source/version identity;
2. coordinate and CRS verification;
3. reproducible OT.02 selection or independently auditable holder-side selection;
4. date/depth semantics;
5. direct-measurement versus derived-variable classification;
6. replicate/QC/missingness review;
7. temporal-use classification;
8. mapping to the admitted profile/state model without fabricated area weights or defaults.

## 9. Temporal boundary

The expected records are 2020–2021 measurements.

If recovered they may support a dated 2020–2021 state. They do not automatically become:

- the actual October-1998 soil state;
- a 2026 current soil state;
- a spatially complete state for all of OT.02.

A modern state pair under the admitted 1998 meteorological event remains a controlled historical-forcing stress test unless an additional temporal-transfer argument is qualified.

## 10. Current verdict

`QUALIFIED_SOURCE_HOLDER_ACCESS_ROUTE — RAW_DATA_NOT_YET_ACQUIRED`

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE` and `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`.

The next material action is a direct source-holder request, not another inferred/public proxy substitution.
