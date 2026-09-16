# Tollebeek OT.02 LGN spatial context v0.1

Status: **qualification candidate — spatial context only**

Governing readiness item: `DR_SM_LAND_USE`

## 1. Purpose

This note records what can and cannot be recovered reproducibly from the public LGN3/LGN4 MapServer for the admitted Tollebeek OT.02 polygon.

It does not identify the crop grown in October 1998 and does not create a land-use model input.

## 2. Temporal meaning of the two LGN versions

The already-qualified source interpretation remains unchanged:
- LGN3 is pre-event land-use context; for Flevoland its agricultural classification reflects 1995 rather than October 1998;
- LGN4 is post-event context based on 1999/2000 information.

Neither version is relabelled as an observation of the 1998 crop. Crop rotation makes interpolation or majority-crop substitution scientifically unsafe without additional evidence.

## 3. Reproducible source-hosted spatial access

The public LGN MapServer accepted WCS 2.0.1 `GetCoverage` requests for LGN3 and LGN4 bounded to the admitted OT.02 domain using RD-coordinate x/y subsets.

Acquisition run `35089251405` returned TIFF responses with stable fingerprints:
- LGN3: SHA-256 `6d55a0b6a76569e9180b97e0eb8411743571c000f64ff29bc5220e90c64c24e2`;
- LGN4: SHA-256 `5f535b94d38dd56bfcef4d727e56165fb9059db1fc08de4a2c1b0c2c094d4ee8`.

These fingerprints qualify the exact public responses used in the acquisition campaign. The TIFF binaries themselves are not admitted as canonical model input.

## 4. Encoding result

Encoding run `35089449853` established that the WCS TIFFs are rendered RGB images, not one-band LGN class rasters:
- three `uint8` bands;
- 15 unique RGB tuples within the OT.02 polygon in each version;
- no usable class-value color table;
- approximately 25 m returned pixel spacing.

The response metadata reports `EPSG:4326`, while the returned transform/bounds numerically remain in the RD coordinate range supplied to the WCS subset request. That inconsistency is retained as a service limitation and is another reason not to treat the returned TIFF metadata as a canonical class-raster contract.

## 5. Explicitly rejected interpretation

A provisional probe had interpreted red-channel values such as 51, 115, 178, 229 and 255 as LGN class codes. That was wrong. The later encoding check demonstrated that these are RGB channel values.

Therefore all provisional crop/class counts, agricultural fractions and cross-version class-agreement metrics based on the first band are rejected and excluded from canonical evidence.

## 6. Attempts to recover an authoritative RGB→class mapping

### GetFeatureInfo

Run `35089547412` queried representative locations for all observed RGB tuples. The server returned an empty feature shell without underlying class attributes.

### GetStyles

Run `35089650307` queried LGN3 and LGN4 styles using WMS 1.3.0 and 1.1.1. The returned StyledLayerDescriptors contained no style rules or color-map entries.

These routes therefore do not provide a source-authoritative class mapping.

## 7. Admission boundary

Qualified:
- public source-hosted LGN3/LGN4 spatial-rendering route;
- bounded OT.02 WCS acquisition syntax;
- exact response checksums;
- RGB encoding diagnosis;
- negative result for FeatureInfo/Styles class recovery.

Not admitted:
- raster class values;
- crop shares or areas;
- exact 1998 parcel/crop identity;
- interpolation between LGN3 and LGN4;
- a representative OT.02 crop;
- a SWAP crop/vegetation input.

## 8. Current verdict

`DR_SM_LAND_USE` remains `PARTIAL_EVIDENCE` and `SCENARIO_ELIGIBLE_ONLY` for the unresolved 1998 crop dimension.

The public LGN route is closed at:

`QUALIFIED_SOURCE_HOSTED_RGB_SPATIAL_CONTEXT_NO_CLASS_VALUE_ADMISSION`

Further material progress should target historical parcel/crop records or a source-authoritative class-value export. Additional reverse-engineering of rendered RGB values is not an acceptable substitute for provenance.
