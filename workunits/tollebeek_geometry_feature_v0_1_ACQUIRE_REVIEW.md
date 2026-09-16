# Tollebeek geometry feature v0.1 — ACQUIRE/REVIEW checkpoint

Protocol: RECONCILE → ACQUIRE → REVIEW → ADMIT → QUALIFY → CLOSE

## Starting authority

- canonical start: `main` @ `01eea563b0e5fcbc291d9c244075760cf0c547b9`
- work branch: `work/tollebeek-geometry-feature-v0.1`
- governing readiness item: `DR_SM_GEOMETRY`
- RECONCILE checkpoint: `workunits/tollebeek_geometry_feature_v0_1_RECONCILE.md`

## ACQUIRE

Because the ordinary browser path exposed the ArcGIS query form but could not submit/capture a parameterised response, acquisition used a temporary branch-only GitHub Actions probe. The workflow had read-only repository permission, performed read-only public HTTP GET queries, uploaded short-retention artifacts, and was deleted before review/PR admission.

Acquisition evidence:

- workflow run `35061837398`: SUCCESS;
  - owner layer `zzl_Peilgebieden/FeatureServer/0` scanned;
  - 290 features retrieved;
  - candidate attributes and geometry artifact id `10431874585`;
  - artifact digest `sha256:310beddfb835a4d74eb56c5cb018bf6bdd65093492e4a205f447febbbd9d2f59`.
- workflow run `35061934978`: SUCCESS;
  - repeated owner feature acquisition and additionally scanned all layers of `Peilbesluiten_WFL1`;
  - artifact id `10432777315`;
  - artifact digest `sha256:1462d74ff24370fcb42c7f4df9a4a8e7c74ce7d623c694e289ecb0b4881fd0f9`.

The temporary workflow is not part of the proposed canonical postimage.

## Owner feature acquired

The current owner layer `zzl_Peilgebieden`, layer 0 `Peilgebieden Besluit`, returned the following definitive OT.02 feature:

- `OBJECTID = 232`;
- `GPGIDENT = OT.02`;
- `GPGNAAM = OT02`;
- `GLOBALID = c07f3d9b-c063-42c3-ba0a-1ff65a1b9c6a`;
- `IWS_GPGSTATU = 4`, whose layer domain/template labels the state `vigerend definitief`;
- summer and winter peil both `-6.2 m NAP`;
- feature `LAST_EDITED_DATE = 2025-05-12T11:47:43.064Z`;
- owner layer data-last-edit metadata `2025-05-12T11:48:03Z`;
- polygon CRS `EPSG:28992`;
- source `Shape__Area = 14965219.570419312 m2`, i.e. about `1496.521957 ha`;
- source `Shape__Length = 23996.24385283598 m`;
- geometry SHA-256 after canonical JSON serialization: `6a1bf94807ead57bbc347154664c003610dad4694c150ef3b1f1ad40b1b73414`.

The exact feature is persisted at `data/spatial/tollebeek_ot02_current.geojson` with stable project spatial-unit id `TOLLEBEEK_OT02_CURRENT` and source provenance.

## Cross-checks

### Owner peilbesluit surfaces

`Peilbesluiten_WFL1` service item `50d59218775449eba09c9405cbbfe62d` contains Winterpeil and Zomerpeil layers. Both contain a status-4 OT.02 record with the same `Shape__Area`, `Shape__Length` and `-6.2 m` peil as the admitted owner polygon.

The same surfaces also make alternative records distinguishable:

- older OT.02 variants have status `11` and are explicitly marked `vervallen`;
- `P-OT.02` is a separate status-1 practice record and has a different geometry/area;
- neither is selected as current definitive geometry.

### Official administrative context

The 2016 Urk peilbesluit context lists OT.02 at `1497 ha` and `-6.20 m NAP`. The owner polygon's geometry-derived area is approximately `1496.52 ha`, which is consistent with that rounded administrative benchmark.

The source field `GPGOPPVL = 1506` does not match the current polygon area. No explanation is invented. That field is retained as source metadata but is not admitted as exact geometry area.

## REVIEW verdict

`ADMIT_CURRENT_PEILGEBIED_GEOMETRY`

Admission scope is deliberately narrow:

- admitted: current definitive OT.02 peilgebied polygon as spatial identity/sampling domain;
- not admitted: affected compaction area;
- not admitted: representative soil profile(s);
- not admitted: current or reference compaction state;
- not admitted: model-unit subdivision merely because the peilgebied polygon exists.

`DR_SM_GEOMETRY` may therefore move from `PARTIAL_EVIDENCE` to `ADMITTED`.

`DR_SM_PROFILE` becomes the next dependency and remains `PARTIAL_EVIDENCE` until a representative profile/soil-unit selection is reviewed.

## Canonical mutations prepared

- exact polygon: `data/spatial/tollebeek_ot02_current.geojson`;
- source provenance strengthened in `evidence/sources.csv`;
- evidence: `EV_TOL_OT02_CURRENT_GEOMETRY`;
- evidence: `EV_TOL_OT02_PEILBESLUIT_CROSSCHECK`;
- qualifications: `Q_TOL_OT02_CURRENT_GEOMETRY`, `Q_TOL_OT02_PEILBESLUIT_CROSSCHECK`;
- claim: `CL_TOL_GEOMETRY_CURRENT`;
- `CL_SPATIAL_GATE` revised so only downstream profile/state gates remain blocked;
- `DR_SM_GEOMETRY = ADMITTED`;
- geometry integrity validator and unit test added and wired into the central project gate.

## Next permitted action

QUALIFY the exact proposed postimage. Merge only if evidence integrity, input-readiness, geometry hash/identity checks and the full project/unit-test gate pass.

After successful CLOSE, the next scientific acquisition may operate `DR_SM_PROFILE` using the admitted OT.02 polygon as the sampling domain.
