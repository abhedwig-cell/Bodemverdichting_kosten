# Tollebeek current-state RhoC recovery v0.1 — QUALIFY

Status: QUALIFIED

Capability: `DR_SM_CURRENT_STATE`
Phase: QUALIFY

## Canonical reconciliation

Original workunit start:
- `main @ a3ab527769c62e2f8d5ba75c30b11e549db01ea5`

Live canonical baseline after state-delta reconciliation:
- `main @ 603016278a25aae406e4414ffbd8b1d9e89c3d65`

Reconciled branch postimage before this checkpoint:
- `f6b5569b22fee9f2f38191a8d7ea003b7f9f6afa`
- PR #46
- CI run `35102662708`: SUCCESS

The reconcile commit preserved the original workunit branch as second parent and current `main` as first parent; no newer source-holder/DOI/2018-dataset governance was overwritten.

## Acquisition evidence

### Run 35101744917

- DANS README/CSV acquisition succeeded.
- CSV parser used the wrong delimiter.
- No scientific classification is taken from that parser output.
- Execution record retained for transparency only.

### Run 35101851142

- corrected semicolon parser;
- job conclusion SUCCESS;
- DANS README file ID `98478`;
- DANS CSV file ID `98475`;
- CSV bytes `35197`;
- rows `432`;
- SHA-256 `10bcb043226544f8e92ba2b4fcec0d1d35e23004e55c9f6e597ca0bb01ba2f02`.

## Qualified source findings

- direct depth-resolved RhoC and Kopecky-ring measurements are present;
- CSV contains no geographic coordinate fields;
- README `Location_code` is a pit/profile/depth identifier, not geographic identity;
- no source-native Tollebeek/OT.02/Urk/Marknesse/Emmeloord identifier was recovered;
- `Dronten` is the depositor/institution address, not measurement-location evidence;
- README identifies project `RhoC dichtheidsmeter`, `KIEM.K21.01.080`, programme `KIEM`;
- no explicit WER3382 / `RAAK.PRO02.021` / `5200043298` provenance exists in the reviewed source files.

## Scientific verdict

`REVIEWED_PUBLIC_RHOC_DATASET_NOT_SPATIALLY_ASSIGNABLE_TO_OT02`

The dataset is method/context evidence only. It is not admitted as Tollebeek CURRENT-state evidence.

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE` / `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`.

The qualified WER3382 source-holder route remains the next material acquisition action.

## Mutations in qualified postimage

Documentation/governance only:

1. live current-state data-request contract extended with the RhoC route disposition;
2. `docs/42_tollebeek_current_state_rhoc_recovery_v0_1.md`;
3. reconciled RECONCILE checkpoint;
4. this QUALIFY checkpoint.

No evidence/readiness/schema/state/model-input mutation. Temporary workflow removed.

## Exclusions

- no figure georeferencing;
- no author-overlap provenance;
- no province-level assignment to OT.02;
- no 2022 measurement backdated to 1998 or relabelled 2026 CURRENT;
- no area weighting;
- no numerical state or model run.

## Next permitted action

Require CI SUCCESS on the exact persisted qualification head. Before merge, reconcile the base head again; merge only if no material canonical collision has appeared.