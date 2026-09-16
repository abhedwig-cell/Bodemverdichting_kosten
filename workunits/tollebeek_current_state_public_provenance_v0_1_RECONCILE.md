# Tollebeek current-state public provenance v0.1 — RECONCILE

Capability: `DR_SM_CURRENT_STATE`

Phase: `RECONCILE → ACQUIRE → CLASSIFY`

Canonical start: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`

## Relevant unchanged dependencies

- `DR_SM_GEOMETRY = ADMITTED`;
- `DR_SM_PROFILE = ADMITTED`;
- `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`;
- WER3382 measurement protocol and direct-data request already qualified;
- BIS-4D recovery route closed in PR #33 as negative.

## State delta reviewed

Public indexed provenance was reviewed specifically for the raw regional 2020–2021 campaign:

1. WER Rapport 3382 / DOI `10.18174/672577` / project `5200043298`;
2. NWO-SIA *Flevo - land in beweging* / `RAAK.PRO02.021`;
3. WUR Research Portal dataset listings and report landing pages;
4. earlier point/field-scale project publication Van Orsouw et al. (2022), DOI `10.3390/agronomy12071669`;
5. previously qualified BIS-4D alternative route.

## Findings

- WER3382 exposes the report, not a raw measurement table or dataset DOI.
- The SIA project record confirms a valuable province-wide measurement dataset exists but provides no raw download.
- Van Orsouw et al. (2022) is a distinct 2018 single-field, 25-location case study, not the 2020–2021 regional campaign.
- That article explicitly states its data are available on request from the authors and privacy-related personal information will be anonymized.
- Project number `5200043298` is shared by multiple outputs and is not unique dataset identity.
- No public source-native table was found that can be reproducibly intersected with OT.02.

## Verdict at this checkpoint

`PUBLIC_PROVENANCE_RECOVERY_EXHAUSTED_DIRECT_CUSTODIAN_REQUEST_REQUIRED`

No current-state values are admitted. `DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`.

## Persisted artifacts

- `docs/38_tollebeek_current_state_public_provenance_closure_v0_1.md`
- `data_requests/tollebeek_current_state_custodian_request_v0_1.md`

## Next permitted action

QUALIFY this documentation-only decision surface. After merge, material progress requires receipt of source-native regional measurement records from WER/Aeres/project custodians or another independently identified archive with equivalent provenance.

## Exclusions

- no model run;
- no soil-state row;
- no printed-map coordinate reconstruction;
- no substitution of 2018 case-study measurements;
- no temporal backdating;
- no area weighting from sparse points.