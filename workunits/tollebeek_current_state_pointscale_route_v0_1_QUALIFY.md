# Tollebeek CURRENT-state point/field publication recovery v0.1 — QUALIFY

Capability: `DR_SM_CURRENT_STATE`

Phase: `QUALIFY`

Branch: `work/tollebeek-current-state-pointscale-route-v0.1`

Reconciled canonical base used for clean PR postimage:

`494d7e841f18ede0e93a4ec5a89c3b3d45a5eec7`

Qualified pre-checkpoint PR head:

`b5c070f1aca8f32ca38605fe680ed74696e13072`

CI run:

`35099167001` — SUCCESS

Checks:

- compile project validation/workbook tools — PASS;
- Status-A-light integrity gate — PASS;
- full unit and contract tests — PASS.

## Qualified scientific decision

Route classification:

`PROJECT_LINK_CONFIRMED_DISTINCT_2018_FIELD_DATA_ON_REQUEST`

The exact `RAAK.PRO02.021` relation is confirmed, but Van Orsouw et al. (2022) is a distinct single-field / 25-location / autumn-2018 experiment rather than the WER3382 305-location / Sep-2020–Jun-2021 regional campaign.

Public source-native coordinates or a downloadable raw-data object were not recovered; figure coordinates were not digitized. No reproducible OT.02 intersection is therefore admitted.

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`.

No soil-state record, spatial weighting, hydraulic parameterization or model input is admitted.

The current-main WER3382 source-holder handoff and receipt protocol remain authoritative and unchanged.

## Exact final diff before this checkpoint

- `docs/42_tollebeek_current_state_pointscale_route_v0_1.md`
- `workunits/tollebeek_current_state_pointscale_route_v0_1_RECONCILE.md`
- `workunits/tollebeek_current_state_pointscale_route_v0_1_CLASSIFY.md`
- `workunits/tollebeek_current_state_pointscale_route_v0_1_RECONCILE_DELTA.md`

No temporary workflow remains.

Next permitted action: require green CI on the persisted qualification head, reconcile any relevant `main` delta, then merge only from that exact qualified head or requalify if the head changes.