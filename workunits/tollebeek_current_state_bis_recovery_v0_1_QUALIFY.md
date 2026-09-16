# Tollebeek current-state BIS recovery v0.1 — QUALIFY checkpoint

Capability / readiness item: `DR_SM_CURRENT_STATE`

Phase: `QUALIFY`

Canonical start:

- `main`: `aaac0aba5a82572b3ea1d8fd7392d126fe92e7a5`
- branch: `work/tollebeek-current-state-bis-recovery-v0.1`
- clean pre-checkpoint head: `fdfdeb23f3389bbb44e81cde5ee67fe7270cbf3b`

## Acquisition authority

Public 4TU/BIS-4D bulk-density file:

- article UUID `c90215b3-bdc6-4633-b721-4c4a0259d6dc`
- file `tbl_cal_BD_gcm3.csv`
- file UUID `e6a9e9c9-53ea-48ba-b95a-44e432d5dae9`
- bytes `913870`
- rows `15871`
- MD5 `4208fe0d0d54ed17db121be6007bc1e3`
- SHA-256 `e9924a1f83b4615ad9366cbf6cffdfae2ddab278f3d6c54aa19a457346fa7ff1`

Temporary acquisition runs:

- `35078024672`: exact file/schema/checksum/provenance-token probe — SUCCESS
- `35078143439`: exact year, README/source-code and OT.02 spatial screening — SUCCESS

Temporary workflow is absent from the clean final diff.

## Qualified findings

1. CSV contains no exact WER3382 / RAAK.PRO02.021 / project 5200043298 / campaign provenance token.
2. README does not establish WER3382 campaign provenance.
3. `Teuling` in README context is not accepted as a provenance bridge.
4. Exact `year` field contains zero 2020 or 2021 records.
5. Source-native RD coordinates use EPSG:28992.
6. Direct intersection with canonical OT.02 polygon returns zero bulk-density records inside OT.02.
7. BIS README describes PFB/BPK-style point sources and `lab`/`field` quality semantics, but this does not recover the required campaign.

## Scientific classification

`REVIEWED_PUBLIC_ALTERNATIVE_NO_OT02_CURRENT_STATE_RECOVERY`

This is a negative route result only. It does not imply absence of Tollebeek observations elsewhere.

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE` and `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`.

No soil-state row, area fraction, hydraulic parameter or model input is admitted.

## Qualification evidence

Clean PR head `fdfdeb23f3389bbb44e81cde5ee67fe7270cbf3b`:

- CI run `35078385152`: `SUCCESS`
- compile project validation/workbook tools: PASS
- Status-A-light integrity gate: PASS
- full unit and contract tests: PASS

Final clean diff before this checkpoint:

- `data_requests/tollebeek_current_state_data_request_v0_1.md`
- `docs/37_tollebeek_current_state_bis_recovery_v0_1.md`
- `workunits/tollebeek_current_state_bis_recovery_v0_1_RECONCILE.md`

No temporary workflow, schema mutation, readiness promotion, state dataset or model output is present.

## Verdict

`QUALIFIED_BIS_ROUTE_REVIEWED_NO_WER3382_OR_OT02_CURRENT_STATE_RECOVERY`

Next permitted action:

Run exact-head CI on this persisted checkpoint. If green, merge the negative route decision. Continue direct WER3382/Flevo-land-in-beweging raw-data acquisition rather than reopening BIS-4D as a substitute.
