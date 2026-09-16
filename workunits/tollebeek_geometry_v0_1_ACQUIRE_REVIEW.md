# Tollebeek geometry v0.1 — ACQUIRE/REVIEW checkpoint

Protocol: RECONCILE → ACQUIRE → REVIEW → ADMIT → CLOSE

## Starting authority

- canonical start: `main` @ `91f41af9aae478abdcbeb60e60c0bfe106d74ea0`
- work branch: `work/tollebeek-geometry-v0.1`
- governing readiness item: `DR_SM_GEOMETRY`
- RECONCILE checkpoint: `workunits/tollebeek_geometry_v0_1_RECONCILE.md`

## ACQUIRE

Live public-source inspection on 2026-09-16 established:

1. the PDOK/HWH harmonised `Peilgebied` collection is live and reports an update date of 2026-09-14;
2. the Waterschap Zuiderzeeland owner-hosted ArcGIS directory exposes both `zzl_Peilgebieden` and `Peilbesluiten_WFL1`;
3. a separate owner-hosted layer `peilgebieden` exposes the expected GPG identity, area and peil fields, but the service metadata reports `Data Last Edit Date: 2020-10-12`;
4. existing official Tollebeek evidence remains the identity/context cross-check: OT.02 administrative area 1497 ha in the later overview and fixed target level NAP -6.20 m.

The acquisition surface is therefore stronger than the original generic PDOK route: an owner-specific route exists and should be preferred for final feature identity, with PDOK used for harmonised corroboration.

## REVIEW

### Evidence admitted for acquisition method only

A new owner-route source/evidence/qualification record is added to the canonical evidence chain:

- source: `SRC_ZZL_GIS_PEIL`;
- evidence: `EV_ZZL_GEOMETRY_OWNER_ROUTE`;
- qualification: `Q_ZZL_GEOMETRY_OWNER_ROUTE` = `BLOCKED_DATA`.

This records that the newer owner surfaces exist and that the older `peilgebieden` layer is stale for current-geometry admission unless separately reconciled.

### Geometry verdict

`NO_ADMIT_GEOMETRY`.

No explicit feature from the newer owner surfaces has yet been captured with sufficient feature/version provenance to label it the current OT.02 geometry. Therefore:

- no polygon or coordinates are persisted as canonical current geometry;
- no area derived from a candidate polygon is promoted;
- the 2020 legacy owner layer is not substituted merely to close the gate;
- 1497 ha and 1502 ha retain their existing administrative/historical meanings only.

`DR_SM_GEOMETRY` remains `PARTIAL_EVIDENCE`.

## Execution limitation versus scientific blocker

The current browser/connector path was sufficient to inspect service inventories and metadata, but not to persist a filtered feature response from the newer owner FeatureServer within this workunit. This is an execution/access limitation and is not interpreted as evidence that the OT.02 feature does not exist.

The scientific/governance blocker is narrower: an explicit current feature/version has not yet been reviewed and admitted.

## Next permitted action

Obtain the explicit OT.02 feature record from `zzl_Peilgebieden` and/or `Peilbesluiten_WFL1` through a direct GIS query/export that preserves feature ID, attributes, geometry and service/version metadata. Then:

1. reconcile code/name/peil context against official Tollebeek evidence;
2. compare area only as a diagnostic, not an equality constraint;
3. cross-check the feature against the current PDOK/HWH harmonised representation;
4. if identity and provenance are adequate, create a separate geometry-admission decision that persists the exact geometry/version and moves `DR_SM_GEOMETRY` to `ADMITTED`;
5. otherwise keep the gate blocked and document the discrepancy.

## Exclusions retained

- no affected-compaction-area inference;
- no representative soil-profile selection;
- no current/reference compaction state;
- no SWAP/source-model run;
- no drainage, event, transfer, pump or cost expansion.
