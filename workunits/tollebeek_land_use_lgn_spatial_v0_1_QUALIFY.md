# Tollebeek land-use LGN spatial acquisition v0.1 — QUALIFY

Capability: `DR_SM_LAND_USE`

Verdict under qualification:

`QUALIFIED_SOURCE_HOSTED_RGB_SPATIAL_CONTEXT_NO_CLASS_VALUE_ADMISSION`

## Qualified postimage before this checkpoint

Candidate head:
- `48c565b9053218625d34825d1fae577b6c174916`

Independent PR CI:
- run `35090043731` — **SUCCESS**;
- compile project validation/workbook tools — PASS;
- Status-A-light integrity gate — PASS;
- unit and contract tests — PASS.

## Evidence inherited from bounded acquisition

- run `35089251405`: bounded LGN3/LGN4 WCS acquisition — technical SUCCESS;
- LGN3 TIFF SHA-256 `6d55a0b6a76569e9180b97e0eb8411743571c000f64ff29bc5220e90c64c24e2`;
- LGN4 TIFF SHA-256 `5f535b94d38dd56bfcef4d727e56165fb9059db1fc08de4a2c1b0c2c094d4ee8`;
- run `35089449853`: three-band RGB encoding established; no class-value band or color table;
- run `35089547412`: WMS GetFeatureInfo returned no class attribute;
- run `35089650307`: WMS GetStyles returned no class/color mapping.

## Explicit invalidated interpretation

The provisional first-band-as-class interpretation from the earlier acquisition script is rejected. No class counts, agricultural fractions, class-change statistics or derived hectares from that interpretation are part of this qualification.

## Scientific boundary

- LGN3 remains pre-event Flevoland context reflecting 1995 agricultural classification, not exact 1998 crop identity;
- LGN4 remains post-event 1999/2000 context;
- rendered RGB tuple counts are diagnostics only;
- `DR_SM_LAND_USE` remains `PARTIAL_EVIDENCE`;
- exact 1998 crop remains unresolved and `SCENARIO_ELIGIBLE_ONLY`;
- no land-use/crop model input or SWAP run is admitted.

## Mutation boundary

The candidate diff contains only:
- `docs/42_tollebeek_lgn_spatial_context_v0_1.md`;
- RECONCILE / ACQUIRE / this QUALIFY checkpoint;
- a route note in the existing land-use data request.

No workflow, raster binary, readiness register, schema, model configuration or scientific result is changed.

Next permitted action:
- require CI SUCCESS on this exact persisted qualification head;
- merge only from that exact head;
- verify post-merge `main` CI;
- CLOSE as spatial context qualified / no 1998 crop admission.
