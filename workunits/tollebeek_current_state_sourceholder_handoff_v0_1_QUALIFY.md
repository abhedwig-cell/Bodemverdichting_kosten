# Tollebeek current-state source-holder handoff v0.1 — QUALIFY

Status: `QUALIFIED`

Protocol: `RECONCILE → PACKAGE → QUALIFY → CLOSE`

## Canonical start

`main = bf8bde57e86ffdc06cf0278a2c885554e1feddce`

## Clean package head

`462d0ece4f909d900edf5644bd36a52433cb69a3`

Independent PR CI:

- run `35095679801`
- conclusion: `SUCCESS`
- compile project validation/workbook tools: PASS
- Status-A-light integrity gate: PASS
- unit and contract tests: PASS

## Qualified content

The handoff contains:

- exact target dataset/project/report identifiers;
- ready-to-send Dutch request text for Aeres, WUR/WER and Actieplan referral routes;
- minimum source-native field/codebook/version request;
- privacy-preserving holder-side OT.02 intersection option;
- raw-byte preservation and SHA-256 receipt procedure;
- explicit ACQUIRED ≠ ADMITTED boundary;
- post-receipt acceptance sequence.

## Scientific boundary

This qualification does not:

- send a request;
- acquire a file;
- admit a CURRENT soil state;
- change `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`;
- infer a 1998 or 2026 state from 2020–2021 measurements;
- create a model input or run.

## Verdict

`QUALIFIED_READY_TO_SEND_SOURCE_HOLDER_HANDOFF`

## Merge rule

Merge only if CI also succeeds on this persisted qualification head. After merge, the next material action is external source-holder contact and subsequent source-native data receipt, not another proxy-data search.