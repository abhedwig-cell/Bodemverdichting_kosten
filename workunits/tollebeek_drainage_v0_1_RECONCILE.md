# Tollebeek drainage v0.1 — RECONCILE checkpoint

Phase: RECONCILE

Canonical base: `main` @ `4f7e59a33f79866865cfcfbb43c96cd2b378baf4`

Work branch: `work/tollebeek-drainage-v0.1`

## Scope

Resolve `DR_SM_DRAINAGE` only far enough to determine whether current OT.02 drainage configuration can be admitted for the first matched source-model experiment.

This workunit distinguishes:

1. parcel subsurface drainage / tile-drain geometry;
2. kavelsloten and other open-water drainage geometry;
3. current managed surface-water level/context;
4. model parameters such as drainage resistance, which require a separate qualified mapping/derivation.

## Canonical inherited evidence

- `EV_FW50_TILE_RES`: historical NOP SWAP tile-drain resistance 100 d, method prior only;
- `EV_FW50_SURF_RES`: historical surface-drainage representation around 30 d, method prior only;
- `CL_FW50_PRIOR`: neither may be copied as a current OT.02 parameter;
- current definitive OT.02 geometry and target peil are already admitted;
- `DR_SM_DRAINAGE = PARTIAL_EVIDENCE` at workunit start.

## Live external authority reconciliation — 2026-09-16

Owner-public Waterschap Zuiderzeeland ArcGIS services expose at least:

- `zzl_Drainage` FeatureServer;
- `leggerkavelsloten` FeatureServer;
- `Legger_watersysteem_2024_Noord_oostpolder__WFL1` FeatureServer;
- `zzl_Watergangen` / current Legger-related water-system services.

The owner service directory is therefore a credible current acquisition route for managed/open drainage assets, but service presence alone does not establish that `zzl_Drainage` represents agricultural parcel tile drains inside OT.02.

Historical/context evidence remains relevant but non-current:

- Waterschap Zuiderzeeland water-erfgoed documentation describes NOP parcel drainage installed mainly 1946–1955, with spacing dependent on soil and drains discharging to kavelsloten;
- secondary NOP historical documentation reports typical parcel-drain geometry around 0.9–1.2 m depth and spacing commonly in the order of 8–16 m, but these values are not current OT.02 asset authority;
- the current municipal drainage guidance concerns urban/public drainage design and is not a substitute for agricultural parcel-drain configuration.

## Current classification

`DR_SM_DRAINAGE` remains `PARTIAL_EVIDENCE` pending direct interrogation of the owner services inside the admitted `TOLLEBEEK_OT02_CURRENT` polygon.

The next permitted action is a read-only owner-service acquisition probe that must determine:

- what `zzl_Drainage` actually contains and its freshness/field semantics;
- whether any such features intersect OT.02;
- current kavelsloot/open-water features intersecting OT.02 and their source IDs/geometry/provenance;
- whether the available owner data are sufficient to derive source-model drainage geometry without inventing tile-drain spacing, depth or resistance.

## Explicit exclusions

- no use of 100 d or 30 d as current defaults;
- no inference that historical tile-drain spacing/depth remains unchanged;
- no conflation of open-water geometry with subsurface tile drainage;
- no SWAP drainage resistance derivation without a separately qualified relation;
- no model run;
- no missing-to-zero substitutions.
