# Tollebeek land use v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Capability: `DR_SM_LAND_USE`
Protocol phase: QUALIFY

## Authority
- repository: `abhedwig-cell/Bodemverdichting_kosten`
- canonical start: `main` @ `629cc4d9590671f5e6c1f1140b17457511b17ec1`
- branch: `work/tollebeek-land-use-v0.1`
- clean pre-checkpoint head: `344583d7e5cdc958170421262ff4f7193724952b`
- event: `EVT_TOL_1998_OCT`

## Qualified evidence route
- official near-period Tollebeek documentation constrains broad historical land use as predominantly arable agriculture with some forest;
- LGN3 is qualified as 25 m pre-event context, with Flevoland agricultural classification based on 1995 imagery;
- LGN4 is qualified as post-event context based on 1999/2000 imagery;
- LGN crop-rotation methodology is qualified as a guardrail against temporal crop interpolation;
- the public annual RVO/PDOK Gewaspercelen archive is bounded at 2009 onward and therefore does not resolve 1998.

## Scientific verdict
`QUALIFIED_LAND_USE_HISTORICAL_ROUTE_NO_ADMIT_1998_CROP`

`DR_SM_LAND_USE = PARTIAL_EVIDENCE`.

No parcel/profile-level 1998 crop, vegetation state, rooting state, harvest state or model crop parameterization is admitted. LGN3 1995 and LGN4 1999/2000 remain context only. A future crop-independent or scenario-based model design must be separately qualified and may not be represented as observation.

## Validation evidence
- first branch-only finalizer run `35073501935`: project validator PASS and dedicated land-use gate PASS; one existing formal-traceability unit test FAILED solely because a fixed canonical guardrail sentence had been reworded;
- remediation restored the exact existing phrase `Current depth-resolved Tollebeek current/reference states are not admitted` without changing evidence, readiness status or scientific verdict;
- retry finalizer run `35073574404`: SUCCESS; central project gate and complete unit/contract suite PASS;
- temporary workflows removed from final diff;
- clean PR-head CI run `35073774673` on `344583d7e5cdc958170421262ff4f7193724952b`: SUCCESS; compilation PASS, central integrity gate PASS, full tests PASS.

## Next permitted action
Run CI on this persisted checkpoint head. If exact-head CI remains green, admit the route/no-admit decision through PR #26. Do not create a 1998 crop dataset or model vegetation parameters in this workunit.

## Exclusions retained
- no 1995 → 1998 crop substitution;
- no 1999/2000 → 1998 crop substitution;
- no crop interpolation through rotation;
- no representative crop for all OT.02;
- no October → bare-soil assumption;
- no model run;
- missing remains missing.
