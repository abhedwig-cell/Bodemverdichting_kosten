# Tollebeek drainage v0.1 — QUALIFY checkpoint

Phase: QUALIFY

Branch: `work/tollebeek-drainage-v0.1`

Canonical base: `main` @ `4f7e59a33f79866865cfcfbb43c96cd2b378baf4`

## Qualified decision

`QUALIFY_DRAINAGE_OWNER_ROUTE_NO_ADMIT_CONFIGURATION`

The branch qualifies an owner-backed drainage inventory/open-water topology route and an explicit configuration data gate. It does not qualify a current source-model drainage configuration.

## Acquisition evidence

Read-only owner-service probes:

- `35066516211`: SUCCESS;
- `35066665265`: SUCCESS;
- final probe artifact digest `sha256:2506b5abbc0627a1aeb1f548a4562337dc8863bf10174a65e281e4e8417bdf29`.

Key observations:

- 74 `zzl_Drainage` polygons intersect OT.02;
- clipped union 1425.807934 ha = about 95.27% of the admitted OT.02 polygon;
- all 74 spacing attributes are `0`, interpreted as unavailable/sentinel-like rather than physical zero;
- all 74 depth and installation-date attributes are null;
- drainage layer last edited 2021-06-27;
- owner NOP Legger service last edited 2025-08-27 supplies current-ish open-water topology, including 127 Afvoervakken and 258 culvert features intersecting OT.02;
- open-water topology does not determine subsurface drain geometry or SWAP resistance.

## Qualification runs

Initial PR head `e04b64e323b04908c2bb3e180ddf0ec9df01dcc4`:

- CI run `35067233808`: FAILED at the central project gate;
- compilation passed;
- failure was only a validator wording defect: the gate required literal word `zero`, while the canonical boundary encoded `spacing 0` and `sentinel-like`;
- no scientific evidence or readiness status was changed to obtain PASS.

Remediation commit `550b3fffa020fae8ee7fb93c85d4cb1abab54e40` changed only the validator semantics check so it accepts the actual bounded representation (`spacing 0`, `sentinel`, or `unavailable`).

CI run `35067305202` on `550b3fff...`: SUCCESS.

Passed:

- compilation;
- evidence integrity;
- formal/domain/input-readiness integrity;
- spatial geometry and profile gates;
- current-state gate;
- new drainage route/configuration gate;
- full unit and contract tests.

## Scientific boundary

`DR_SM_DRAINAGE = PARTIAL_EVIDENCE`.

`CAP_MULTI_DRAIN = DATA_GATED`.

No canonical Tollebeek drainage configuration dataset exists.

Not admitted:

- drain spacing/density;
- drain depth/elevation;
- installation/renewal state;
- SWAP drainage resistance;
- historical 100 d / ~30 d values as current defaults;
- open-water topology as a subsurface drainage proxy;
- any source-model result.

## Next permitted action

Merge only after this persisted checkpoint head itself passes CI. After closure, obtain current or explicitly dated source-native parcel-drain records for selected OT.02 units and separately qualify the physical-to-model drainage mapping.
