# Tollebeek drainage v0.1 — ACQUIRE / CLASSIFY checkpoint

Phase: ACQUIRE → CLASSIFY

Branch: `work/tollebeek-drainage-v0.1`

Base: `main` @ `4f7e59a33f79866865cfcfbb43c96cd2b378baf4`

## Owner-service acquisition

Read-only GitHub Actions probes:

- run `35066516211`: initial service metadata and OT.02 intersection screening — SUCCESS;
- run `35066665265`: completeness and coverage screening — SUCCESS;
- second artifact digest: `sha256:2506b5abbc0627a1aeb1f548a4562337dc8863bf10174a65e281e4e8417bdf29`.

The admitted OT.02 polygon area used for all intersections is 1496.521957 ha.

### `zzl_Drainage`

Owner service item: `dd48ed818ae44b6d9a64d189036511dc`.

Layer 0 `Drainage` is polygonal and exposes:

- `DRGIDENT`;
- `IWS_AFSTAND_HART_OP_HART`;
- `IWS_AANLEGDATUM`;
- `IWS_DIEPTELIGGING`;
- `IWS_OPMERKING`;
- `GLOBALID`.

OT.02 screening result:

- 74 drainage polygons intersect the admitted OT.02 geometry;
- union of clipped intersections: 1425.807934 ha;
- polygon coverage fraction: 0.9527477546 (95.27% of OT.02);
- non-zero spacing values: 0 / 74;
- all spacing values returned as `0`;
- non-null depth values: 0 / 74;
- non-null installation dates: 0 / 74;
- layer data last edit: 2021-06-27T10:31:05.926Z.

Interpretation: the owner service is strong evidence that parcel-scale drainage inventory units exist across most of OT.02, but it does **not** supply the current spacing, depth or installation-age values required for source-model parameterization. `0` in the spacing field is not interpreted as a real zero spacing.

### `leggerkavelsloten`

Owner service item: `ec3879b431634c00acc1901ff8ab6947`.

OT.02 screening:

- 77 kavelsloot features intersect OT.02;
- clipped length about 44.216 km;
- layer data last edit 2019-07-05.

This is useful for open-drainage topology/history, not current parcel-drain parameters.

### `Legger_watersysteem_2024_Noord_oostpolder__WFL1`

Owner service item: `cf10c95387724cf0b3f3af0339dc87b5`.

Service data last edit is 2025-08-27. Within the admitted OT.02 polygon the probe found at least:

- 127 `Afvoervak` line features, about 55.566 km clipped length;
- 258 `Duiker` features, about 3.064 km clipped line length;
- 12 stuw points;
- 5 put points;
- plus other water-system structures.

Owner public documentation explains that the 2024 watersystem-legger programme records locations, normative profiles and maintenance obligations of water-system works. The publicly found March–May 2025 notice concerns the second **draft** 2024 watersystem legger. Therefore the owner-maintained service is used here as a current topology/acquisition route, without overstating legal finality of every feature.

## Historical context

Waterschap Zuiderzeeland water-erfgoed documentation states that NOP parcel drainage was installed mainly during 1946–1955 and that drain spacing varied by soil. This confirms the structural importance of tile drainage but does not establish current OT.02 spacing/depth or hydraulic resistance.

Historical FutureWater values of 100 d tile-drain resistance and about 30 d surface-drainage resistance remain method priors only.

## Classification

Verdict: `QUALIFY_DRAINAGE_OWNER_ROUTE_NO_ADMIT_CONFIGURATION`.

`DR_SM_DRAINAGE` must remain `PARTIAL_EVIDENCE`.

Reason:

- current/open-system topology is substantially better resolved;
- an owner parcel-drainage inventory covers most of OT.02;
- however the fields needed to parameterize parcel drainage are empty or sentinel-like for every intersecting drainage polygon;
- data freshness of the drainage polygon layer is 2021;
- no qualified mapping from those polygons to SWAP drainage depth/spacing/resistance exists.

## Next permitted action

Acquire source-native current parcel-drain records or owner/landholder asset evidence containing actual spacing, drain depth/elevation and installation/renewal state for selected OT.02 units. Only then derive a model configuration under a separately qualified drainage-parameter mapping.

## Exclusions retained

- no `0 m` drain spacing interpretation;
- no invented drain depth;
- no 100 d / 30 d current default;
- no assumption that 1946–1955 installation geometry remains unchanged;
- no conversion of open-water network length into subsurface drain resistance;
- no SWAP run.
