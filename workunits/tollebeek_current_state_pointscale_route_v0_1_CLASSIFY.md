# Tollebeek CURRENT-state point/field publication recovery v0.1 — CLASSIFY

Capability: `DR_SM_CURRENT_STATE`

Phase: `CLASSIFY`

Branch: `work/tollebeek-current-state-pointscale-route-v0.1`

Canonical start: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`

## Acquisition evidence

Temporary read-only GitHub Actions probes:

- run `35098231879`: SUCCESS
  - WUR eDepot PDF `577746` acquired, 5,318,065 bytes;
  - exact SIA grant `RAAK.PRO02.021` confirmed;
  - data availability classified as available on request from the authors;
  - autumn-2018 fieldwork and 25-location single-field design recovered.
- run `35098469362`: SUCCESS
  - source-native location wording screened;
  - study area described as eastern Flevoland / Noordoostpolder, at the edge of Emmeloord;
  - no public source-native coordinate values, downloadable coordinate table or stable public data-object recovered;
  - measurement coordinates appear only in a figure and are not digitized.

Publisher HTML/XML returned HTTP 403 in both probes. WUR eDepot acquisition succeeded; the 403 responses are route behaviour only.

## Classification

`PROJECT_LINK_CONFIRMED_DISTINCT_2018_FIELD_DATA_ON_REQUEST`

Rationale:

- exact project-family membership is confirmed by `RAAK.PRO02.021`;
- the article reports a real direct-measurement compaction dataset;
- source-native design is one field / 25 locations / autumn 2018 / post-2017 compaction event;
- WER3382 regional design is 305 locations / Sep 2020–Jun 2021;
- therefore the datasets are distinct despite common project provenance;
- raw 2018 records are a secondary request route, not recovered public data;
- no reproducible OT.02 intersection is possible from public source-native records.

## Readiness verdict

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`.

No `soil_state` row, area weight, hydraulic parameter or model input is created.

Primary active route remains acquisition of the raw 2020–2021 WER3382 regional point dataset.

## Persisted canonical outputs prepared

- `docs/38_tollebeek_current_state_pointscale_route_v0_1.md`
- updated `data_requests/tollebeek_current_state_data_request_v0_1.md`

Next permitted action: remove temporary workflow, verify clean diff, normal CI qualification, then CLOSE without state admission.