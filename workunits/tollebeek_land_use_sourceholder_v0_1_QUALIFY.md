# Tollebeek 1998 land-use source-holder route v0.1 — QUALIFY

Capability: `DR_SM_LAND_USE`

Verdict under qualification:

`QUALIFIED_CBS_PLUS_RVO_LASER_ARCHIVE_ENQUIRY_ROUTE_NO_1998_CROP_ADMISSION`

Candidate head before this checkpoint:
- `1fb824b95c3becad95c085cfb95a9a4da73dca6b`

Independent PR CI:
- run `35090589862` — **SUCCESS**;
- compile — PASS;
- Status-A-light integrity gate — PASS;
- unit/contract tests — PASS.

Qualified route boundary:
- CBS historical Landbouwtelling / maatwerk is the statistical source-holder route;
- RVO/LVVN records management through the historical LASER institutional chain is the administrative/archive enquiry route;
- CBS municipality-level 1980-2000 data remain context only;
- the absence of 1998 from the standard older-LBT microdata catalog is not treated as evidence of destruction/unavailability;
- LASER/RVO institutional succession is not treated as evidence that a spatial 1998 parcel/crop register survives;
- exact crop/parcel records must be source-native, dated 1998 and spatially assignable before they can support admission.

Scientific boundary:
- `DR_SM_LAND_USE` remains `PARTIAL_EVIDENCE`;
- exact October-1998 crop remains unresolved / `SCENARIO_ELIGIBLE_ONLY`;
- no crop value, crop area, representative crop or model input is admitted.

Mutation boundary:
- one source-holder route document;
- one data-request handoff extension;
- RECONCILE and this QUALIFY checkpoint only.

Next permitted action:
- require CI SUCCESS on this exact persisted qualification head;
- merge only from that head;
- verify post-merge `main` CI;
- CLOSE as source-holder route qualified / no 1998 crop admission.
