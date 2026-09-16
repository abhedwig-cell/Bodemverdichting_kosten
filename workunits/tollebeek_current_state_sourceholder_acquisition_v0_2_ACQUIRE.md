# Tollebeek CURRENT-state source-holder acquisition v0.2 — ACQUIRE checkpoint

Capability: `DR_SM_CURRENT_STATE`

Phase: `ACQUIRE`

Date: 2026-09-16

## Source state

Canonical start:

- `main @ 621b6d487f721e0bbb83616540d51542d7f1b53e`

Reconcile checkpoint:

- `24e6bddf8c4359a582df4116a9dbf76304102012`

Dispatch manifest:

- `artifacts/acquisition/tollebeek_current_state_sourceholder_dispatch_v0_2.json`
- dispatch-manifest commit: `6fffe02225044e8c779aafdba06e6c39941ff4a2`

Qualified request authority remains:

- `data_requests/tollebeek_current_state_sourceholder_handoff_v0_1.md`
- originating qualified handoff: PR #43

## Acquisition execution reached in this workunit

The repository-side acquisition state is fully prepared and provenance-pinned.

Three previously qualified routes are retained in order:

1. Aeres Hogeschool / RAAK-PRO — Karin Pepers, `k.pepers@aeres.nl`;
2. WUR/WER — Fenny van Egmond through the current public WUR contact/profile route;
3. Actieplan Bodem & Water Flevoland — `info@bodemenwaterflevoland.nl` as referral route.

No source-holder response or source-native data file is present in the repository at this checkpoint.

Therefore `data_acquired=false` and this phase cannot scientifically advance to source classification.

## External action boundary

The next action is an actual external dispatch of the already-qualified request text. GitHub itself cannot constitute that dispatch or fabricate a response.

A future receipt must preserve, before transformation:

- sender/source-holder identity;
- received timestamp/date;
- original message context and terms/restrictions;
- original filename/archive structure;
- raw file bytes;
- SHA-256 per raw file;
- dataset/version/archive identifier if supplied;
- any holder-side OT.02 selection method and privacy/generalisation metadata.

## Resume contract after response

Resume from this checkpoint, not from a new proxy search.

Required sequence:

`ACQUIRE/RECEIPT → IDENTIFY → HASH → SCHEMA/QC → SPATIAL VERIFY → TEMPORAL CLASSIFY → STATE MAPPING → QUALIFY → ADMIT/CLOSE`

Do not promote receipt to admission.

## Scientific status

- `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`
- source-holder route = `QUALIFIED_AND_DISPATCH_READY`
- source-native CURRENT observations = `NOT_YET_RECEIVED`
- hydraulic parameterization = `DATA_GATED`
- SWAP execution = `NOT_AUTHORIZED`

## Exclusions

No:

- proxy substitution;
- map/figure digitisation;
- inference of OT.02 membership without source-native coordinates or auditable holder-side selection;
- temporal backcast to 1998;
- silent present-day interpretation of 2020–2021 measurements;
- null/sentinel to zero;
- CURRENT-state or hydraulic admission;
- model run.

Verdict: `ACQUIRE_BLOCKED_AT_EXTERNAL_SOURCEHOLDER_DISPATCH_NO_DATA_RECEIVED`

Next permitted action: externally send the qualified request(s), then persist the actual response/receipt before any scientific transformation.
