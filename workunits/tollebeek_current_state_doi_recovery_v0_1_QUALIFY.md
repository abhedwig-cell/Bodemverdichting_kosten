# Tollebeek current-state DOI/public-metadata recovery v0.1 — QUALIFY

Status: QUALIFIED_CHECKPOINT

Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → CLOSE

Governing readiness item: `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`

## Canonical reconciliation

Original acquisition baseline: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`.

Before qualification, parallel canonical work advanced `main` to `30cfc402beab780b61026f3536fa7fd6399145c7`. The DOI workunit was explicitly reconciled onto that head.

Parallel current-state source-holder work is preserved. This workunit only appends the DOI/public-metadata negative recovery result.

## Acquisition evidence

Temporary branch-only workflow run `35083443676`: SUCCESS.

Surfaces tested:

- DOI / WUR publication landing page;
- Crossref;
- DataCite direct DOI metadata plus narrow searches;
- OpenAlex;
- Zenodo narrow searches;
- candidate WUR public data-host names.

Artifact: `tollebeek-current-state-doi-probe`, id `10440518949`.

Temporary workflow removed before qualification.

## Classification

`REVIEWED_PUBLIC_DOI_METADATA_ROUTE_NO_RAW_WER3382_DATASET_RECOVERY`

No explicit machine-resolvable raw WER3382/Flevo-land dataset relation was recovered. Numeric-only false positives were rejected. This negative result does not imply non-existence or non-shareability of the source records.

## Scientific/readiness verdict

- `DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE` / `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`;
- no CURRENT-state record is created;
- no modern state is backdated to 1998;
- no area weights or hydraulic parameters are inferred;
- the qualified Aeres/WUR/Actieplan source-holder route remains the next material action.

## Clean qualification postimage

PR clean head before this checkpoint: `afea00c2a6a2ef5538481f2091039b050b798229`.

CI run `35084033947`: SUCCESS.

Passed:

- project/tool compilation;
- Status-A-light integrity gate;
- full unit and contract tests.

Final pre-checkpoint diff contained exactly:

1. `data_requests/tollebeek_current_state_data_request_v0_1.md` — additive DOI-route result only;
2. `docs/41_tollebeek_current_state_doi_recovery_v0_1.md`;
3. `workunits/tollebeek_current_state_doi_recovery_v0_1_RECONCILE.md`.

No schema, evidence verdict, readiness register, source model, workbook, workflow or numerical dataset changed.

## Next permitted action

Require SUCCESS on the exact persisted qualification head created by this checkpoint. Before merge, verify that live `main` has not introduced a conflicting change to the same current-state request/access surface. Merge only if the delta remains valid.
