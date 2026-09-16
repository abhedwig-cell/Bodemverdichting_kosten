# Tollebeek CURRENT-state source-holder acquisition v0.2 — QUALIFY checkpoint

Capability: `DR_SM_CURRENT_STATE`

Phase: `QUALIFY`

Date: 2026-09-16

## Scope qualified

This checkpoint qualifies only the repository-side external-acquisition control surface for the already-qualified WER3382 / `Flevo - land in beweging` source-holder route.

No source-native measurement file or holder-side OT.02 extract has been received.

## Canonical and branch state

Canonical start:

- `main @ 621b6d487f721e0bbb83616540d51542d7f1b53e`

Acquisition branch:

- `work/tollebeek-current-state-sourceholder-acquisition-v0.2`

Pre-qualification implementation head:

- `d4a11969ac95045b8631d19512b9422f461978ff`

PR:

- `#51`

## Qualified acquisition-control artifacts

- `data_requests/tollebeek_current_state_sourceholder_handoff_v0_1.md` — unchanged request-text authority from PR #43;
- `artifacts/acquisition/tollebeek_current_state_sourceholder_dispatch_v0_2.json` — exact dispatch-state manifest;
- `artifacts/acquisition/tollebeek_current_state_contact_verification_v0_2.json` — public-contact endpoint verification dated 2026-09-16;
- `artifacts/acquisition/tollebeek_current_state_receipt_contract_v0_1.json` — machine-readable receipt, fail-fast and acceptance contract;
- `workunits/tollebeek_current_state_sourceholder_acquisition_v0_2_RECONCILE.md`;
- `workunits/tollebeek_current_state_sourceholder_acquisition_v0_2_ACQUIRE.md`.

## Public contact verification

Current public routes were checked on 2026-09-16:

1. Aeres Hogeschool publicly lists Karin Pepers as researcher/teacher in Sustainable Soil Management and publishes `k.pepers@aeres.nl`.
2. WUR publishes the current Fenny van Egmond profile/contact route under Soil data and sensing / Soil, Water and Land Use. No unpublished email address is inferred.
3. Actieplan Bodem & Water Flevoland publicly publishes `info@bodemenwaterflevoland.nl`.

This verification concerns contact routing only and has no scientific/evidentiary effect on CURRENT-state status.

## Qualification evidence

Pre-qualification head:

- `d4a11969ac95045b8631d19512b9422f461978ff`

CI:

- run `35116734866`: `SUCCESS`
- compile project validation and workbook tools: `SUCCESS`
- Status-A-light integrity gate: `SUCCESS`
- unit and contract tests: `SUCCESS`

## Contract checks

The receipt contract preserves the controlling scientific boundaries:

- receipt is `ACQUIRED`, not `ADMITTED`;
- raw bytes and hashes precede transformation;
- dataset identity, location/CRS or auditable holder-side OT.02 selection, depth, date, measurement and QC semantics must be established;
- null/sentinel/default-to-zero closure is prohibited;
- figure digitisation/private-location reconstruction is prohibited;
- 2020–2021 observations are not silently backdated to 1998 or promoted to 2026;
- bulk-density evidence does not itself admit hydraulics;
- no SWAP run is authorised by receipt alone.

## Scientific status

- `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`
- source-holder route = `QUALIFIED_AND_DISPATCH_READY`
- source-native CURRENT observations = `NOT_YET_RECEIVED`
- data acquired = `false`
- hydraulic parameterization = `DATA_GATED`
- SWAP execution = `NOT_AUTHORIZED`

Qualification verdict:

`QUALIFIED_CURRENT_STATE_EXTERNAL_ACQUISITION_CONTROL_SURFACE_NO_DATA_RECEIVED`

## Resume boundary

The workunit is intentionally not admitted/closed because the scientific acquisition event has not occurred.

Next permitted action remains an actual external source-holder dispatch. After a real response or file receipt, continue on this same branch/PR using:

`ACQUIRE/RECEIPT → IDENTIFY → HASH → SCHEMA/QC → SPATIAL VERIFY → TEMPORAL CLASSIFY → STATE MAPPING → QUALIFY → ADMIT/CLOSE`

Do not create a new proxy-search or numerical scenario merely to bypass the external source-holder boundary.
