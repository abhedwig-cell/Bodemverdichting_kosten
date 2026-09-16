# Tollebeek geometry feature v0.1 — RECONCILE checkpoint

Protocol: RECONCILE → ACQUIRE → REVIEW → ADMIT → QUALIFY → CLOSE

## Canonical start

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- base branch: `main`
- base head: `01eea563b0e5fcbc291d9c244075760cf0c547b9`
- work branch: `work/tollebeek-geometry-feature-v0.1`
- governing readiness item: `DR_SM_GEOMETRY`
- open materially equivalent geometry-feature PR at start: none
- earlier `work/tollebeek-geometry-v0.1` is historical and already merged through PR #18; it qualified the acquisition route only and explicitly did not admit geometry.

## Reconciled live owner authority

Live public inspection resolves the owner service more precisely than the previous route-level checkpoint:

- owner: Waterschap Zuiderzeeland;
- ArcGIS service: `zzl_Peilgebieden`;
- service item id: `b5db31163fa74c09825de1d42bb12ce8`;
- layer 0: `Peilgebieden Besluit`;
- geometry type: polygon;
- spatial reference: RD New / EPSG:28992 (service WKID 28992);
- primary identity/name fields include `GPGIDENT` and `GPGNAAM`;
- relevant attributes include area, summer/winter level, status, beheer, peilbesluit memo, creation/edit metadata, `GLOBALID`, and shape area/length;
- the status vocabulary includes a current definitive state (`vigerend definitief`);
- the owner layer metadata reports a data/schema last edit of 2025-05-12.

This is materially newer and more suitable for current feature identity than the separate legacy owner `peilgebieden` layer whose data-last-edit date is 2020-10-12.

## Legal/context reconciliation

The 2010 Tollebeek peilbesluit remains valid historical identity/design context but is not sufficient current geometry authority by itself. The later Urk peilbesluit states that earlier decisions, including Onderbemaling Tollebeek (2010), are withdrawn insofar as incorporated into that later decision. Current feature admission therefore requires reconciliation against a current owner feature/version and current harmonised context, not silent reuse of the 2010 polygon/context.

The existing 1497 ha and 1502 ha values retain their existing meanings only: administrative/later benchmark and historical design-area context respectively. Neither is admitted as affected compaction area or canonical model geometry.

## Current acquisition blocker

The public owner query endpoint is reachable and exposes the normal ArcGIS query contract, but the currently available browser/network path has not yet produced a captured filtered feature response for OT.02 with an explicit OBJECTID/GLOBALID, attributes and geometry.

This is an execution/access limitation, not evidence that the OT.02 feature is absent.

## Verdict

`PASS_RECONCILE`

Geometry status remains `BLOCKED_DATA` / `PARTIAL_EVIDENCE`.

No feature id, polygon, coordinates, derived area or spatial-unit record is admitted by this checkpoint.

## Next permitted action

Continue bounded acquisition through the owner service or another owner-backed/exported route until an explicit OT.02 feature record can be captured with:

1. feature identity (`GPGIDENT`, OBJECTID and/or GLOBALID);
2. feature name/status and relevant peil attributes;
3. polygon geometry in a declared CRS;
4. owner service item/layer provenance and edit/version context;
5. reconciliation against current PDOK/HWH and official Tollebeek context.

Only after those conditions are met may a separate REVIEW/ADMIT decision consider moving `DR_SM_GEOMETRY` to `ADMITTED`.

## Exclusions

- no geometry inferred from area alone;
- no legacy 2020 polygon promoted for convenience;
- no affected-area inference;
- no profile, current/reference soil-state, drainage, event, model-run, transfer, pump or cost work.
