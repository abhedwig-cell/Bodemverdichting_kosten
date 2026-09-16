# Tollebeek geometry v0.1 — RECONCILE checkpoint

Protocol: RECONCILE → ACQUIRE → REVIEW → ADMIT → CLOSE

## Canonical start

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- base branch: `main`
- base head: `91f41af9aae478abdcbeb60e60c0bfe106d74ea0`
- work branch: `work/tollebeek-geometry-v0.1`
- open geometry PR at start: none
- equivalent geometry-admission branch found: none
- governing request: `DR_SM_GEOMETRY`

## Existing project authority

`DR_SM_GEOMETRY` is not satisfied by the 1497 ha administrative benchmark or by the existence of a discovery service. Admission requires a specific current geometry/version with stable spatial identity, provenance and reviewable metadata. Geometry is spatial context and must not be relabelled as affected compaction area.

## External authority reconciliation

The following public surfaces were live-checked on 2026-09-16:

1. PDOK `Waterschappen Waterbeheergebieden IMWA` exposes a harmonised `Peilgebied` collection and is updated frequently. It remains a discovery/corroboration route rather than owner-specific authority for project admission.
2. Waterschap Zuiderzeeland publishes an owner-hosted ArcGIS service directory containing both `zzl_Peilgebieden` and `Peilbesluiten_WFL1`.
3. A separate owner-hosted legacy service named `peilgebieden` exposes the expected GPG fields, including `GPGIDENT`, `GPGNAAM`, area and water levels, but its layer reports a last data edit of 2020-10-12. It must therefore not be called current without reconciliation against a newer owner surface.
4. Current official peilbesluit material identifies Tollebeek OT.02 at a fixed level of NAP -6.20 m and the 2016 administrative overview records 1497 ha. These are useful identity cross-checks, not an exact geometry checksum.

## Acquisition targets

The workunit will try to resolve a candidate from the newer owner-hosted service first, with the legacy service used only as a cross-check.

- [Owner `zzl_Peilgebieden` service](https://services.arcgis.com/84oM5NriBghHdQ3Z/arcgis/rest/services/zzl_Peilgebieden/FeatureServer?f=pjson)
- [Owner `zzl_Peilgebieden` OT02/Tollebeek candidate query](https://services.arcgis.com/84oM5NriBghHdQ3Z/arcgis/rest/services/zzl_Peilgebieden/FeatureServer/0/query?where=GPGIDENT%20LIKE%20%27%25OT02%25%27%20OR%20GPGNAAM%20LIKE%20%27%25Tollebeek%25%27&outFields=*&returnGeometry=true&outSR=4326&f=geojson)
- [Owner `Peilbesluiten_WFL1` service](https://services.arcgis.com/84oM5NriBghHdQ3Z/ArcGIS/rest/services/Peilbesluiten_WFL1/FeatureServer?f=pjson)
- [Legacy owner `peilgebieden` OT02/Tollebeek candidate query](https://services.arcgis.com/84oM5NriBghHdQ3Z/ArcGIS/rest/services/peilgebieden/FeatureServer/0/query?where=GPGIDENT%20LIKE%20%27%25OT02%25%27%20OR%20GPGNAAM%20LIKE%20%27%25Tollebeek%25%27&outFields=*&returnGeometry=true&outSR=4326&f=geojson)

## Review criteria before admission

A candidate may only advance if feature identity is reviewable against owner/official context, including code/name and water-level or peilbesluit context where available. Geometry/source timestamp or version must be explicit. Area may be used only as a plausibility diagnostic, not to force equality with 1497 ha or 1502 ha.

## Fail-fast rule

If the newer owner surface cannot establish a sufficiently current and unambiguous OT.02 feature, persist the unresolved acquisition evidence and leave `DR_SM_GEOMETRY` blocked. Do not promote the 2020 legacy polygon merely to make the gate pass.
