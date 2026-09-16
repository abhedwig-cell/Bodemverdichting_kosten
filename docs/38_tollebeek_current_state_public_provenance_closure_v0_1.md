# Tollebeek current-state public provenance closure v0.1

Status: **PUBLIC RECOVERY ROUTE REVIEWED — DIRECT CUSTODIAN REQUEST REQUIRED**

Governing readiness item: `DR_SM_CURRENT_STATE`

Canonical start: `main = a3ab527769c62e2f8d5ba75c30b11e549db01ea5`.

## 1. Purpose

Determine whether the raw 2020–2021 Flevoland soil-compaction measurements underlying WER Rapport 3382 can be recovered from indexed/public project outputs without asking the source custodians directly.

This review does **not** create a CURRENT-state dataset and does not change `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`.

## 2. Public source chain reviewed

### WER Rapport 3382

Authority: Van Egmond et al. (2024), *Regionale kartering bodemverdichting in de provincie Flevoland*, WER Rapport 3382, DOI `10.18174/672577`, project number `5200043298`.

The report states that:

- the regional analysis is based on new field measurements of dry bulk density and penetration resistance;
- more than 300 measurements were collected across Flevoland;
- part of the research was carried out within the SIA RAAK-PRO project *Flevoland in Beweging*;
- point- and field-scale results had already been published before the regional report.

No raw coordinate/value table, supplementary dataset, dataset DOI, archive identifier or machine-readable appendix is exposed through the report landing page or report itself.

### NWO-SIA project record

Authority: dossier `RAAK.PRO02.021`, *Flevo - land in beweging*.

The project record states that more than 300 point measurements were made and that a valuable province-wide dataset was collected. The project record does not expose the raw point dataset as a download.

### Van Orsouw et al. (2022)

Authority: Van Orsouw et al., *Practical Implications of the Availability of Multiple Measurements to Classify Agricultural Soil Compaction: A Case-Study in The Netherlands*, Agronomy 12(7):1669, DOI `10.3390/agronomy12071669`.

This publication is under the same RAAK-PRO grant but is **not** the 2020–2021 regional campaign dataset:

- one agricultural field in the eastern Noordoostpolder;
- 25 measurement locations;
- fieldwork in autumn 2018 after maize harvest;
- separate point/field-scale research question.

Its Data Availability Statement says the data are available on request from the authors and that personal information will be anonymized in accordance with Dutch privacy regulations.

This provides a project-specific precedent that raw field data may be request-only rather than deposited publicly.

### BIS-4D alternative

The public BIS-4D bulk-density point archive was independently reviewed in PR #33 and does not recover the required campaign:

- zero OT.02 bulk-density points in the reviewed public file;
- zero records with `year` 2020/2021;
- no WER3382 / RAAK.PRO02.021 / project-5200043298 provenance identity.

## 3. Classification

Public indexed recovery is classified:

`PUBLIC_PROVENANCE_RECOVERY_EXHAUSTED_DIRECT_CUSTODIAN_REQUEST_REQUIRED`

This means:

- the existence of the regional measurements is well supported;
- the public routes reviewed do not provide the source-native point table required for OT.02 intersection;
- absence from those routes is not evidence that the data do not exist;
- direct source-custodian acquisition is now the primary route.

## 4. Source-custodian priority

Request in this order while keeping one identical field contract:

1. WER Rapport 3382 authors / Wageningen Environmental Research project `5200043298`;
2. Aeres Hogeschool / *Flevo - land in beweging* project custodians under `RAAK.PRO02.021`;
3. project co-funders/partners only for routing to the data custodian, not as substitute data authority.

A request may explicitly allow anonymization or pseudonymization of land-user identity. The scientific requirement is source-native measurement ID, coordinate or reproducible spatial key, date, depth, measured value, method/QC and provenance — not personal identity.

## 5. Scientific guardrails

- Do not infer coordinates from published maps while source coordinates can be requested.
- Do not treat the 2018 single-field dataset as the regional 2020–2021 campaign.
- Do not infer OT.02 membership from `Noordoostpolder` or `Flevoland` labels.
- Do not infer area fractions from point counts.
- Do not backdate 2020–2021 measurements to the 1998 event.
- Do not treat project number `5200043298` alone as unique dataset identity: multiple outputs share it.
- Do not use regional interpolated maps as measured CURRENT state.
- Preserve nulls and QC explicitly.

## 6. Current verdict

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`.

No `soil_state` row, OT.02 current-state measurement, reference state or model input is admitted by this review.

Next permitted material action: obtain the source-native regional measurement table through the custodian request contract and reproducibly intersect it with canonical `data/spatial/tollebeek_ot02_current.geojson`.