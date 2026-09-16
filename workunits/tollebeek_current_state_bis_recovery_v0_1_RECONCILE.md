# Tollebeek current-state BIS recovery v0.1 — RECONCILE checkpoint

Capability / readiness item: `DR_SM_CURRENT_STATE`

Protocol: `RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → CLOSE`

Canonical start:

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- `main`: `aaac0aba5a82572b3ea1d8fd7392d126fe92e7a5`
- source branch: `work/tollebeek-current-state-bis-recovery-v0.1`

## Current canonical status

- `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`
- route classification: `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`
- admitted OT.02 geometry and eight-profile context remain dependencies.
- no numerical CURRENT state is admitted.

## Existing direct-measurement route

WER Rapport 3382 / Flevo-land-in-beweging documents a 2020–2021 Flevoland field campaign with direct dry-bulk-density ring measurements and penetration resistance, but the public project/report route has not exposed the raw coordinate/value table needed for an auditable OT.02 spatial join.

## New recovery candidate

The public BIS-4D point-data publication at 4TU contains georeferenced Dutch soil-property point data and exposes a bulk-density file `tbl_cal_BD_gcm3.csv`.

This workunit tests only whether that public point dataset contains records whose source/provenance can be tied exactly to the WER3382 / Flevo-land-in-beweging campaign, or otherwise provides separately classifiable direct bulk-density observations inside OT.02.

No inclusion is assumed from author overlap, geography, date range or similarity of measurement values.

## Required checks

1. recover 4TU dataset file metadata and exact file UUID/checksum;
2. download the source-native bulk-density CSV without rewriting it;
3. inspect column schema and documented identifiers;
4. search exact/near-exact provenance tokens including `5200043298`, `RAAK.PRO02.021`, Flevo-land-in-beweging and WER3382 identifiers where available;
5. inspect date fields for 2020–2021 records;
6. inspect coordinate fields and CRS semantics;
7. if candidate rows exist, intersect them reproducibly with canonical `data/spatial/tollebeek_ot02_current.geojson`;
8. retain method/depth/provenance semantics and missing values;
9. distinguish exact campaign recovery from unrelated BIS observations.

## Guardrails

- BIS-4D maps/predictions are not CURRENT-state evidence for OT.02;
- no point is attributed to WER3382 without exact source/provenance evidence;
- no geographic/date coincidence is sufficient by itself;
- no modal/predicted bulk density is promoted as direct CURRENT state;
- no sparse points are converted to exact areal fractions;
- 2020–2021 observations remain dated 2020–2021 state, not automatically 1998 or 2026 state;
- null/missing values remain missing;
- no CURRENT-state admission occurs in ACQUIRE.

## Execution discipline

A temporary branch-only GitHub Actions workflow may query the public 4TU API and download the sub-1MB source CSV because the browser environment blocks the API endpoint. The temporary workflow must be removed before any final PR diff.

## Verdict

`RECONCILED_FOR_BIS_POINT_DATA_PROVENANCE_RECOVERY`

Next permitted action: `ACQUIRE` the exact public BIS bulk-density point file and classify provenance before considering any state admission.
