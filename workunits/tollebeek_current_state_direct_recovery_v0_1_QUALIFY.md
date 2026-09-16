# Tollebeek current-state direct recovery v0.1 — QUALIFY checkpoint

Capability / readiness item: `DR_SM_CURRENT_STATE`

Phase: `QUALIFY`

Canonical start:

- `main`: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`
- branch: `work/tollebeek-current-state-direct-recovery-v0.1`
- clean pre-checkpoint head: `eb755898e80bce58c78b8311e2f515355fd85f41`

## Qualified public-recovery findings

1. WER3382 / DOI `10.18174/672577` remains the regional 2020–2021 measurement authority.
2. WER3382 explicitly states that point- and field-scale results had been published earlier.
3. Van Orsouw et al. (2022), Agronomy 12(7), 1669, DOI `10.3390/agronomy12071669`, is directly funded under `RAAK.PRO02.021` and is therefore a valid same-project author/data-custodian route.
4. The 2022 paper's Data Availability Statement says data are available on request from the authors and personal information will be anonymized.
5. The 2022 paper uses autumn-2018 measurements on one Noordoostpolder field; it is not the regional September-2020-to-June-2021 WER3382 dataset.
6. No downloadable raw coordinate/value table or supplement for the regional 2020–2021 measurements was recovered from the reviewed public routes.
7. Exact/private field location must not be inferred from published figures.
8. A privacy-safe custodian-performed OT.02 intersection is acceptable for route review when selection semantics, stable pseudonymous IDs, record counts, measurement dates/depths/values/QC and source control are retained.

## Scientific classification

`PUBLIC_RECOVERY_EXHAUSTED_AUTHOR_REQUEST_REQUIRED`

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE` / `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`.

No CURRENT-state record, spatial interpolation, area weight, hydraulic parameter, reference-state value or model input is admitted.

## Qualification evidence

Clean PR head `eb755898e80bce58c78b8311e2f515355fd85f41`:

- CI run `35079007153`: `SUCCESS`
- compile project validation/workbook tools: PASS
- Status-A-light integrity gate: PASS
- full unit and contract tests: PASS

Final clean diff before this checkpoint:

- `data_requests/tollebeek_current_state_data_request_v0_1.md`
- `docs/38_tollebeek_current_state_direct_author_recovery_v0_1.md`
- `workunits/tollebeek_current_state_direct_recovery_v0_1_RECONCILE.md`

No readiness/schema/state-data mutation is present.

## Verdict

`QUALIFIED_PUBLIC_RECOVERY_EXHAUSTED_AUTHOR_REQUEST_REQUIRED`

Next permitted action:

Run exact-head CI on this persisted checkpoint. If green, merge the acquisition-route decision. Material scientific progress after merge requires receipt of source data or a source-custodian response; do not fabricate a state from published figures or summaries.
