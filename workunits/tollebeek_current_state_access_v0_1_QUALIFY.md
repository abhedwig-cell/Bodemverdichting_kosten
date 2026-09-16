# Tollebeek current-state access v0.1 — QUALIFY checkpoint

Capability / readiness item: `DR_SM_CURRENT_STATE`

Phase: `QUALIFY`

Canonical start:

- `main`: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`
- branch: `work/tollebeek-current-state-access-v0.1`
- clean pre-checkpoint head: `84e7e2371919538185fb0156b75a2e06a8f2dbc2`

## Qualified access decision

Dataset existence is established, but raw coordinate-level WER3382/Flevo-land-in-beweging source records and a canonical public dataset identifier have not been acquired.

Access classification:

`QUALIFIED_SOURCE_HOLDER_ACCESS_ROUTE — RAW_DATA_NOT_YET_ACQUIRED`

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE` and `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`.

## Qualified routing

1. Aeres Hogeschool / RAAK-PRO project route: source-native measurement table/codebook or responsible holder contact.
2. WER/WUR Report 3382 author/data route: canonical archive/dataset identifier or shareable raw export with privacy handling.
3. Actieplan Bodem & Water Flevoland: programme/dissemination referral route if the final dataset landing page or holder cannot be resolved directly.

Request identity must include:

- `Flevo - land in beweging`
- `RAAK.PRO02.021`
- project `5200043298`
- WER Report 3382
- DOI `10.18174/672577`
- campaign September 2020–June 2021

## Claim boundaries

- no claim that WER3382 data are confidential, closed or request-only;
- the separate 2018 RAAK.PRO02.021 paper is related data-governance context only and is not the WER3382 dataset;
- no BIS/SoilPhys/map/prediction proxy substitution;
- receipt of data does not itself admit CURRENT state;
- exact/private coordinates may be replaced only by an independently auditable holder-side OT.02 selection with stable identifiers, not by reconstructed coordinates;
- 2020–2021 measurements remain dated observations and are not silently relabelled as 1998 or 2026 state.

## Qualification evidence

Clean PR head `84e7e2371919538185fb0156b75a2e06a8f2dbc2`:

- CI run `35079026112`: `SUCCESS`
- compile project validation/workbook tools: PASS
- Status-A-light integrity gate: PASS
- full unit and contract tests: PASS

Pre-checkpoint diff:

- `docs/38_tollebeek_current_state_access_route_v0_1.md`
- `workunits/tollebeek_current_state_access_v0_1_RECONCILE.md`
- clarified `data_requests/tollebeek_current_state_data_request_v0_1.md`

No readiness status, evidence verdict, schema, soil-state dataset, implementation or model output changed.

## Verdict

`QUALIFIED_WER3382_SOURCE_HOLDER_ACCESS_ROUTE_NO_RAW_DATA_ADMISSION`

Next permitted action:

Run exact-head CI on this persisted checkpoint. If green, merge the access-route qualification. Material CURRENT-state progress then requires actual source-holder data receipt or a new independently qualified direct observation dataset.
