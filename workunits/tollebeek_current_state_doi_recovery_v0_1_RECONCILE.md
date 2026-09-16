# Tollebeek current-state DOI/public-metadata recovery v0.1 — RECONCILE

Status: RESUMABLE_CHECKPOINT

Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → CLOSE

Original canonical start: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5` (`main` after PR #33)

Live canonical reconciled after acquisition: `30cfc402beab780b61026f3536fa7fd6399145c7`

Governing readiness item: `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`

## Goal

Test one narrow public provenance route for the raw 2020–2021 Flevoland soil-compaction measurements underlying WER Report 3382 / DOI `10.18174/672577` and the `Flevo - land in beweging` project (`RAAK.PRO02.021`, project `5200043298`).

This workunit does not infer measurement values from report figures and does not create a CURRENT-state dataset unless an exact public machine-resolvable dataset/repository object can be tied to the campaign by explicit metadata or related identifiers.

## Acquisition performed

Temporary branch-only workflow run `35083443676` completed SUCCESS.

The probe tested:

- DOI resolution for `10.18174/672577`;
- WUR publication-page hyperlinks and possible data/supplement links;
- Crossref relation/link metadata;
- DataCite direct DOI metadata and narrow searches for DOI/project identifiers/title terms;
- OpenAlex DOI metadata;
- Zenodo narrow searches;
- candidate public WUR data-host names.

Artifact: `tollebeek-current-state-doi-probe`, artifact id `10440518949`.

The temporary workflow was removed before canonical qualification.

## Classification result

`REVIEWED_PUBLIC_DOI_METADATA_ROUTE_NO_RAW_WER3382_DATASET_RECOVERY`

Key findings:

- DOI resolves to the WUR publication page and that page contains project number `5200043298`;
- no campaign-specific raw-data or supplement link was exposed;
- Crossref contained no dataset relation and no raw-data link;
- DataCite contained no related dataset identifier for the report DOI;
- narrow DataCite searches found no provenance-qualified WER3382/Flevo-land dataset; numeric-only `672577` hits were unrelated false positives;
- narrow Zenodo searches returned no candidate records;
- guessed `researchdata.wur.nl` and `data.wur.nl` hosts did not resolve in the acquisition environment.

This is negative route evidence only. It does not imply that the source data do not exist or cannot be shared.

## Parallel-main reconciliation

While the DOI probe was running, `main` advanced by 15 commits and qualified a stronger source-holder access route for CURRENT state, drainage and managed boundary. In particular:

- `data_requests/tollebeek_current_state_data_request_v0_1.md` gained privacy-aware selection rules and a qualified source-holder order;
- `docs/38_tollebeek_current_state_access_route_v0_1.md` now identifies Aeres/WUR/Actieplan access routes;
- CURRENT-state readiness remains `PARTIAL_EVIDENCE` / `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`.

The DOI result is complementary to that access route. It must be appended to the latest data request, not overwrite or replace the qualified source-holder route.

## Admission rule

A future candidate dataset counts as recovered only if its provenance is explicit: DOI relation, repository metadata, project identifier, dataset title/description, or another source-native relation must identify the WER3382 / Flevo-land campaign. Author overlap, subject similarity, geographic proximity, matching years or a plausible file name are insufficient.

## Exclusions

- no map digitisation;
- no inferred GPS from figures;
- no author-overlap provenance;
- no generic BIS/SoilGrids/map product as CURRENT state;
- no null→0;
- no temporal backdating to 1998;
- no model run;
- no readiness promotion from a negative public-route review.

## Next permitted action

Persist the DOI recovery note against current canonical, append the result to the live data-request contract, run normal CI, and close this route. The direct qualified source-holder request remains the next material action.
