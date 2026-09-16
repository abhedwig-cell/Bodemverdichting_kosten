# Tollebeek land use v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Capability: `DR_SM_LAND_USE`
Protocol phase: RECONCILE

## Canonical authority

- canonical branch: `main`
- canonical start: `629cc4d9590671f5e6c1f1140b17457511b17ec1`
- branch: `work/tollebeek-land-use-v0.1`
- fixed event: `EVT_TOL_1998_OCT`
- readiness at start: `DR_SM_LAND_USE = MISSING`

No materially equivalent open land-use branch or PR was found before branch creation.

## Existing historical context

The official Tollebeek peil documentation identifies the historical Rietgors/Fuut/Kievit areas as predominantly arable agricultural land, with forest also present in Rietgors and Kievit. This establishes broad land-use context only; it does not identify field-level crop identity for October 1998.

## Public historical LGN route

- LGN3 is a 25 m historical land-use raster based on satellite imagery from 1995 and 1997. For provinces outside Groningen, Drenthe, Overijssel, Gelderland and Limburg — including Flevoland — the agricultural classification uses 1995 imagery.
- LGN4 is based on satellite imagery from 1999 and 2000 and supports change analysis relative to LGN3.
- LGN documentation explicitly treats agricultural crop changes differently from stable land-use change because crop changes can reflect crop rotation.

Therefore LGN3 and LGN4 can bracket broad land-use context around the 1998 event, but they do not directly observe the 1998 crop state.

## Scientific boundary

A source-model vegetation/crop input requires event-relevant crop/vegetation state at the selected model-unit/profile grain. The project must not interpolate a 1998 crop class from 1995 and 1999/2000 maps, assume one representative arable crop for all OT.02, or infer bare soil merely because the event occurred in late October.

## Acquisition questions

Seek, in order:

1. 1998 parcel/crop registration or owner/farmer records spatially linkable to historical Tollebeek control areas;
2. historical field/parcel geometries with crop identity for the 1998 growing season;
3. if exact crop records are unavailable, a separately qualified model-design choice that demonstrates whether the selected hydrological experiment can be made crop-independent or use an explicitly bounded vegetation scenario rather than a claimed observation.

LGN3/LGN4 may be used as temporal/contextual constraints and as a route for checking broad land-use stability, not as a fabricated 1998 crop record.

## Verdict

`RECONCILED_LAND_USE_GATE_MISSING_EVENT_CROP`

## Explicit exclusions

- no 1995 LGN3 crop → 1998 crop substitution;
- no 1999/2000 LGN4 crop → 1998 crop substitution;
- no interpolation of crop identity through crop rotation;
- no whole-OT.02 representative crop default;
- no late-October → bare-soil assumption;
- no model crop/vegetation parameterization in this reconcile phase;
- missing remains missing.
