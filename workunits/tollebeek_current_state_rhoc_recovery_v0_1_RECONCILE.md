# Tollebeek current-state RhoC recovery v0.1 — RECONCILE

Status: RECONCILED_AFTER_CANONICAL_DELTA

Capability: `DR_SM_CURRENT_STATE`
Phase: RECONCILE → ACQUIRE → CLASSIFY
Original canonical start: `main @ a3ab527769c62e2f8d5ba75c30b11e549db01ea5`
Canonical delta reconciled against: `main @ 603016278a25aae406e4414ffbd8b1d9e89c3d65`
Work branch: `work/tollebeek-current-state-rhoc-recovery-v0.1`

## Bounded question

Does the open DANS RhoC validation dataset DOI `10.17026/PT/BYVPLB` contain source-native geographic information sufficient to assign any direct bulk-density observation reproducibly to the admitted OT.02 polygon?

## Why this was a separate source decision

The dataset is a peer-reviewed/open bulk-density field dataset with overlapping authorship, but author overlap is not provenance. It is only relevant to Tollebeek if its own source-native metadata support OT.02 assignment.

## Acquisition

Temporary branch-only probe workflow acquired DANS README file `98478` and CSV file `98475`.

Execution evidence:

- run `35101744917`: source acquisition succeeded, but the CSV was parsed with an incorrect comma delimiter; parser output is not scientific evidence;
- run `35101851142`: corrected semicolon parser; SUCCESS and authoritative for classification.

Corrected CSV authority:

- 432 rows;
- 35197 bytes;
- SHA-256 `10bcb043226544f8e92ba2b4fcec0d1d35e23004e55c9f6e597ca0bb01ba2f02`;
- columns include depth, pit/profile/sample code, RhoC values, Kopecky-ring values, moisture and soil texture;
- no coordinate fields.

## Classification

The README defines `Location_code` as pit/profile/depth identity, not geographic identity.

The README identifies:

- project `RhoC dichtheidsmeter`;
- project number `KIEM.K21.01.080`;
- programme `KIEM`;
- collection period March 2022 – March 2023.

No source-native Tollebeek/OT.02 identifier or coordinate was recovered. `Dronten` occurs only as the depositor/institution address and is not measurement-location evidence.

Verdict candidate:

`REVIEWED_PUBLIC_RHOC_DATASET_NOT_SPATIALLY_ASSIGNABLE_TO_OT02`

## Canonical delta during execution

While this workunit was open, `main` advanced by 65 commits. Relevant new canonical decisions include:

- qualified WER3382 source-holder access route;
- explicit privacy-preserving holder-side OT.02-selection option;
- DOI/public-metadata recovery with no raw campaign dataset recovered;
- classification of a separate 2018 `RAAK.PRO02.021` point-scale compaction dataset.

These are semantically compatible with the RhoC verdict. They strengthen, rather than replace, the conclusion that the direct WER3382 source-holder route is authoritative.

Because `data_requests/tollebeek_current_state_data_request_v0_1.md` changed materially on `main`, the old branch copy must not be merged. The RhoC route note is transplanted into the live request contract instead.

## Guardrails retained

- no author overlap as provenance;
- no figure/map reverse-georeferencing;
- no province-level location relabelled OT.02;
- no RhoC sensor estimate substituted for a direct ring measurement;
- no 2022 value backdated to 1998 or silently relabelled 2026 CURRENT;
- no area weighting from sparse samples;
- no `soil_state` row or model input admitted;
- no older data-request content allowed to overwrite newer canonical source-holder governance.

## Readiness consequence

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE` / `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`.

## Next permitted action

QUALIFY this reconciled negative-route decision against current `main`. If green, merge documentation only and retain the direct source-holder request as the next material action.