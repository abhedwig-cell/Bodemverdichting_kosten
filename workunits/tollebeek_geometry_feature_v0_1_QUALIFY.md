# Tollebeek geometry feature v0.1 — QUALIFY checkpoint

Protocol: RECONCILE → ACQUIRE → REVIEW → ADMIT → QUALIFY → CLOSE

## Qualified proposed postimage

- branch: `work/tollebeek-geometry-feature-v0.1`
- qualified content head before this checkpoint: `7941200e2a044afb8bdba4ed50093300294d9182`
- canonical base: `main` @ `01eea563b0e5fcbc291d9c244075760cf0c547b9`
- admission decision: `ADMIT_CURRENT_PEILGEBIED_GEOMETRY`
- readiness transition: `DR_SM_GEOMETRY: PARTIAL_EVIDENCE → ADMITTED`

## Qualification evidence

GitHub Actions CI run `35062824481` on head `7941200e2a044afb8bdba4ed50093300294d9182`: `SUCCESS`.

Passed:

- Python compilation, including `validate_spatial_geometry.py`;
- canonical evidence integrity;
- formal traceability integrity;
- Data Model v0.3 domain-schema integrity;
- source-model input-readiness integrity;
- admitted spatial geometry identity/hash/CRS/readiness validation;
- required project structure;
- full unit and contract test discovery.

Diff review against current `main` shows only the intended canonical postimage. Temporary acquisition and repair workflows were both removed before qualification and do not appear in the final diff.

## Serialization remediation record

The first PR CI attempt, run `35062612743`, failed before unit tests because the initially persisted large GeoJSON contained a manual JSON serialization error. Compilation itself passed and the failure was:

`spatial-geometry: cannot parse admitted geometry: Expecting ',' delimiter`

No scientific value, feature identity, geometry selection or admission decision was changed to obtain PASS.

Remediation was mechanical and source-preserving:

- a temporary branch-only repair workflow re-queried owner OBJECTID 232;
- it required `GPGIDENT=OT.02`, GLOBALID `c07f3d9b-c063-42c3-ba0a-1ff65a1b9c6a`, status `4`, and geometry SHA-256 `6a1bf94807ead57bbc347154664c003610dad4694c150ef3b1f1ad40b1b73414` before writing;
- the resulting geometry serialization was validated and committed as `7ef07b667a33c95351c0a9f67a58ede052eb432a`;
- the temporary workflow was then deleted, producing the green qualified content head `7941200e2a044afb8bdba4ed50093300294d9182`.

This is classified as a serialization repair, not a scientific requalification or workaround.

## Qualified scientific scope

Qualified for admission:

- current definitive owner-hosted OT.02 peilgebied polygon;
- stable spatial identity `TOLLEBEEK_OT02_CURRENT`;
- source feature OBJECTID/GLOBALID/status provenance;
- EPSG:28992 geometry and immutable geometry hash;
- use of the polygon as current peilgebied spatial identity and profile-sampling domain.

Not qualified or admitted:

- affected compaction area;
- `GPGOPPVL=1506` as exact polygon area;
- representative soil profile(s);
- current/reference compaction states;
- source-model subunit partitioning;
- drainage, event, model-run, transfer, pump or cost semantics.

The geometry-derived area of approximately `1496.52 ha` is consistent with the rounded official `1497 ha` administrative benchmark and is retained only as geometry metadata/cross-check.

## Verdict

`PASS_QUALIFY`

## Next permitted action

Require CI success once more on the exact head produced by this persisted QUALIFY checkpoint. If green and PR diff remains bounded, mark PR #19 ready and merge only from that exact qualified head. After merge, require post-merge `main` CI success before CLOSE.
