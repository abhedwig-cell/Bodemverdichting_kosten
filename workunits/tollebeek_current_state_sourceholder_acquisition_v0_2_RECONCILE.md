# Tollebeek CURRENT-state source-holder acquisition v0.2 — RECONCILE

Capability: `DR_SM_CURRENT_STATE`

Phase: `RECONCILE`

Date: 2026-09-16

## Canonical state

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- canonical start: `main @ 621b6d487f721e0bbb83616540d51542d7f1b53e`
- preceding post-merge CI: `35114776678` — `SUCCESS`
- current-state acquisition branch: `work/tollebeek-current-state-sourceholder-acquisition-v0.2`

## Reused qualified authority

The authoritative source-holder execution handoff remains:

`data_requests/tollebeek_current_state_sourceholder_handoff_v0_1.md`

It was qualified and closed through PR #43 with final verdict:

`CLOSED_READY_TO_SEND_SOURCE_HOLDER_HANDOFF_CURRENT_STATE_STILL_EXTERNAL`

The handoff identifies the target source as the 2020–2021 regional field campaign underlying:

- `Flevo - land in beweging`
- `RAAK.PRO02.021`
- WER project `5200043298`
- WER Rapport 3382
- DOI `10.18174/672577`
- campaign September 2020 through June 2021
- target spatial domain Tollebeek OT.02

Qualified request order remains:

1. Aeres Hogeschool / RAAK-PRO — Karin Pepers, `k.pepers@aeres.nl`;
2. WUR/WER — Fenny van Egmond through the current public WUR contact/profile route;
3. Actieplan Bodem & Water Flevoland — `info@bodemenwaterflevoland.nl` as referral route.

## Relevant state delta since PR #43

No source-native WER3382 regional measurement file, archive identifier or holder-supplied OT.02 extract has entered canonical evidence since PR #43.

Subsequent CURRENT-state work has not superseded this route:

- PR #45 classified the separate 2018 Van Orsouw field dataset as distinct and available only by request;
- PR #46 closed the public DANS RhoC route because records cannot be spatially assigned to OT.02;
- PR #50 preserved `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE` and identified external CURRENT-state records as a primary remaining blocker.

No new evidence supports a proxy substitution, map digitisation, point-count area weighting, temporal backcast or modal SoilPhys-density substitution.

## Reconciled decision

The PR #43 handoff is still the shortest scientifically qualified route to material CURRENT-state progress.

No request-text redesign, proxy-data search or numerical state construction is warranted before holder contact/response.

## Next permitted action

Execute the qualified source-holder contact outside GitHub, preserving the exact dataset identifiers and minimum field request from the handoff.

When any response or attachment is received, resume with:

`ACQUIRE/RECEIPT → IDENTIFY → HASH → SCHEMA/QC → SPATIAL VERIFY → TEMPORAL CLASSIFY → STATE MAPPING → QUALIFY → ADMIT/CLOSE`

Receipt alone is `ACQUIRED`, not `ADMITTED`.

## Exclusions

- no broad public proxy search;
- no figure digitisation;
- no interpolation from unrelated point datasets;
- no null/sentinel to zero;
- no 2020–2021 state backdated to 1998 or silently relabelled as present-day 2026 state;
- no hydraulic parameterization from absent CURRENT data;
- no SWAP run.

Verdict: `RECONCILED_CURRENT_STATE_SOURCEHOLDER_ROUTE_STILL_AUTHORITATIVE_EXTERNAL_SEND_REQUIRED`
