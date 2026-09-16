# Tollebeek current-state access v0.1 — RECONCILE checkpoint

Capability / readiness item: `DR_SM_CURRENT_STATE`

Protocol: `RECONCILE → REVIEW ACCESS → QUALIFY → CLOSE`

Canonical start:

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- `main`: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`
- source branch: `work/tollebeek-current-state-access-v0.1`

## Current status

- `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`
- route classification: `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`
- the BIS-4D public alternative is already reviewed and closed negative for OT.02/WER3382 recovery.
- no numerical CURRENT state is admitted.

## Reconciled access facts

Public report/project sources establish that the Flevo-land-in-beweging / WER3382 measurement dataset exists and that more than 300 conventional point measurements were collected across Flevoland.

The WUR publication record for WER Report 3382 exposes the report/PDF but no separate raw point-data file or linked dataset identifier was recovered in the bounded search.

The NWO-SIA project page says the accumulated provincial dataset/results would be disseminated through the Flevoland Actieprogramma/Actieplan Bodem en Water route. The current ABW site provides programme/project information and contact but no raw WER3382 dataset was located.

A separate 2018 study funded under the same RAAK.PRO02.021 project states that its own data are available on request from the authors. That is a different field dataset and is retained only as related project data-governance context, not as proof of WER3382 access policy.

## Candidate source holders / routing

- Aeres Hogeschool / Sustainable Soil Management project route; current public researcher/project contact Karin Pepers.
- Wageningen Environmental Research / WER3382 author route; current public WUR profile for Fenny van Egmond.
- Actieplan Bodem & Water Flevoland as programme/dissemination referral route.

## Guardrails

This workunit must not:

- claim the WER3382 dataset is confidential, closed or request-only without exact evidence;
- conflate the separate 2018 RAAK field dataset with the 2020–2021 WER3382 campaign;
- promote author overlap to dataset provenance;
- substitute BIS, SoilPhys, maps or predictions for missing raw measurements;
- change `DR_SM_CURRENT_STATE` readiness;
- create soil-state rows or model inputs.

## Intended output

Documentation/governance only:

- explicit source-holder/data-access route;
- this resumable checkpoint;
- optional clarification in the existing current-state request;
- no evidence/status/schema/model-output mutation.

## Verdict

`RECONCILED_KNOWN_DATASET_PUBLIC_RAW_ACCESS_UNRESOLVED`

Next permitted action:

`REVIEW ACCESS → QUALIFY` the source-holder acquisition route while preserving the current-state gate.
