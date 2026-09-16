# Tollebeek land-use LGN spatial acquisition v0.1 — ACQUIRE / CLASSIFY

Capability: `DR_SM_LAND_USE`

Canonical geometry dependency:
- `data/spatial/tollebeek_ot02_current.geojson`
- EPSG:28992 owner polygon remains the admitted OT.02 spatial identity.

## Public LGN acquisition route

The source-hosted MapServer accepted WCS 2.0.1 requests of the form:

- `map=/etc/mapserver/LGN3.map` or `LGN4.map`;
- `SERVICE=WCS`;
- `VERSION=2.0.1`;
- `REQUEST=GetCoverage`;
- `COVERAGEID=LGN3` or `LGN4`;
- RD-coordinate `SUBSET=x(...)` and `SUBSET=y(...)` matching the admitted OT.02 bounding box plus one-cell margin;
- `FORMAT=image/tiff`.

Full bounded acquisition run:
- run `35089251405` — SUCCESS.

Immutable source-response fingerprints from that run:
- LGN3 TIFF: 153070 bytes; SHA-256 `6d55a0b6a76569e9180b97e0eb8411743571c000f64ff29bc5220e90c64c24e2`;
- LGN4 TIFF: 153070 bytes; SHA-256 `5f535b94d38dd56bfcef4d727e56165fb9059db1fc08de4a2c1b0c2c094d4ee8`.

## Encoding classification

Run `35089449853` — SUCCESS — established that both returned TIFFs are:
- GTiff;
- three bands;
- `uint8` per band;
- RGB-rendered products;
- 222 × 229 pixels for the bounded request;
- approximately 25 m pixel spacing in the returned transform;
- without a band-1 color table;
- containing 15 unique RGB tuples inside the OT.02 polygon for each map version.

The WCS files report CRS metadata `EPSG:4326`, while their returned transform/bounds numerically occupy the RD range used in the `SUBSET` request. This metadata inconsistency is retained as a service limitation. The raster CRS tag is therefore not promoted as geodetic authority.

### Rejected provisional interpretation

The earlier acquisition script temporarily interpreted first-band values such as `51`, `115`, `178`, `229` and `255` as if they were LGN class codes. The encoding probe disproved that interpretation: those values are red-channel values from rendered RGB colors.

Consequently:
- no band-1 class counts are evidence;
- no agricultural fraction from those values is evidence;
- no such statistic may be copied into canonical land-use data or a model input.

## Server-side class-recovery attempts

### WMS GetFeatureInfo

Run `35089547412` — SUCCESS technically.

The LGN3/LGN4 WMS capabilities advertise the layers as queryable and support EPSG:28992. `GetFeatureInfo` calls at representative pixels for all observed RGB tuples returned only an empty feature shell, e.g. `Layer 'LGN3' / Feature 0`, without class attributes or values.

Verdict: GetFeatureInfo does not provide a reproducible RGB→LGN-class mapping for this route.

### WMS GetStyles

Run `35089650307` — SUCCESS technically.

For both LGN3 and LGN4, WMS 1.3.0 and 1.1.1 `GetStyles` returned an empty StyledLayerDescriptor with no rules and no `ColorMapEntry` elements.

Verdict: GetStyles does not provide a reproducible RGB→LGN-class mapping for this route.

## Scientific classification

The public server route is classified as:

`QUALIFIED_SOURCE_HOSTED_RGB_SPATIAL_CONTEXT_NO_CLASS_VALUE_ADMISSION`

This means:
- the source-hosted spatial rendering and its immutable response fingerprints are reproducible context;
- exact raster class values were not recovered through WCS, FeatureInfo or Styles;
- RGB tuple frequencies are not crop-class frequencies;
- no exact 1998 crop identity is recovered;
- no pixel-to-hectare or crop-area calculation is admitted.

`DR_SM_LAND_USE` remains `PARTIAL_EVIDENCE`.

The next material route is historical parcel/crop evidence or another source-authoritative class-value product. More RGB reverse-engineering is not a permitted substitute for source provenance.
