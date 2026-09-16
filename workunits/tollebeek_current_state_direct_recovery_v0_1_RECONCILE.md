# Tollebeek current-state direct recovery v0.1 — RECONCILE checkpoint

Capability / readiness item: `DR_SM_CURRENT_STATE`

Phase: `RECONCILE → ACQUIRE → CLASSIFY`

Canonical start:

- `main`: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`
- branch: `work/tollebeek-current-state-direct-recovery-v0.1`

## Inherited authority

- `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`
- admitted OT.02 geometry remains the required spatial selection domain;
- SoilPhys modal density remains profile context only;
- BIS-4D alternative is canonically closed as not recovering WER3382 provenance or OT.02 bulk-density points;
- primary target remains the raw 2020–2021 WER3382 / Flevo-land-in-beweging point dataset.

## Public recovery performed

Public search/reconciliation checked:

1. WER3382 / DOI `10.18174/672577` publication record and report;
2. WUR Research Portal and project-number context `5200043298`;
3. NWO-SIA dossier `RAAK.PRO02.021`;
4. indexed public dataset/supplement routes;
5. the earlier point-/field-scale publication identified by WER3382:
   Van Orsouw et al. (2022), Agronomy 12(7), 1669, DOI `10.3390/agronomy12071669`.

## Material finding

WER3382 explicitly states that point- and field-scale results had been published earlier.

The 2022 Agronomy paper:

- is funded under `RAAK.PRO02.021`;
- uses autumn-2018 data from one agricultural field in the Noordoostpolder;
- originally sampled 50 locations and retained 83 samples from 25 locations for its analysis after data-quality filtering;
- includes bulk-density, volumetric-water-content and penetration-resistance measurements;
- states that data are available on request from the authors and that personal information will be anonymized.

This is a qualified direct-author/data-custodian route, but it is not the regional 2020–2021 dataset and cannot be substituted for it.

## Public-data verdict

No downloadable raw coordinate/value table or supplement for the regional 2020–2021 WER3382 measurements was recovered from the reviewed public routes.

Classification:

`PUBLIC_RECOVERY_EXHAUSTED_AUTHOR_REQUEST_REQUIRED`

This does not imply the regional raw data do not exist.

## Privacy-safe fallback

If exact farm coordinates cannot be released, a custodian-performed spatial intersection against canonical OT.02 may be used for route review if the returned subset retains pseudonymized stable IDs, measurement/depth/date/QC fields and a documented spatial-selection statement.

Coordinates must not be reverse-engineered from publication figures.

## Mutations

- added `docs/38_tollebeek_current_state_direct_author_recovery_v0_1.md`;
- refined `data_requests/tollebeek_current_state_data_request_v0_1.md` with the author-request route, 2018/2020–2021 distinction and privacy-safe fallback.

No readiness, schema, evidence verdict, state dataset, hydraulic parameter or model input is changed.

## Next permitted action

Qualify this documentation/data-request delta. After merge, material progress on `DR_SM_CURRENT_STATE` requires a source-data or custodian response; do not fabricate a numerical state from the published figures or summaries.
