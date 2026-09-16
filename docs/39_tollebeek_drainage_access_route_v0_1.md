# Tollebeek drainage source-holder access route v0.1

Status: **QUALIFICATION CANDIDATE — access route only**

Governing readiness item: `DR_SM_DRAINAGE`

Canonical start: `main = a02e0810e2a1bfd9d4d8c5c5f418a012c8d55206`

## 1. Purpose

Qualify the owner-backed route for obtaining the missing physical drainage attributes required for a reproducible OT.02 source-model drainage configuration.

This note does not admit spacing, drain depth, installation date, drainage resistance or a SWAP drainage configuration.

## 2. Existing owner evidence

Canonical drainage reconciliation already established that:

- 74 owner `zzl_Drainage` polygons intersect admitted OT.02;
- clipped union coverage is about 95.27% of the OT.02 polygon;
- the public layer exposes spacing, installation date and depth fields;
- all 74 intersecting records expose spacing `0` and null depth/date values;
- that `0` is treated as missing/sentinel-like, not as a physical zero;
- the newer owner watersystem-legger provides open-water topology but not the missing subsurface-drain detail.

Therefore the blocker is not lack of a drainage inventory. It is:

`OWNER_DRAINAGE_INVENTORY_KNOWN — PHYSICAL DETAIL ATTRIBUTES UNRESOLVED`.

## 3. Formal owner access route

Waterschap Zuiderzeeland publishes a dedicated `Waterinformatie aanvragen` route for information that cannot be found through its public maps/GEO information.

The published route explicitly covers map material and measurement/information questions and asks requesters to describe the relevant location and requested information as specifically as possible.

Zuiderzeeland separately states in its Woo guidance that requesters should first submit an ordinary information request because many records/documents can be supplied without a formal Woo decision.

Therefore the qualified routing order is:

1. ordinary Zuiderzeeland water-information request;
2. technical clarification/data-holder referral if the public `zzl_Drainage` fields are placeholders or incomplete extracts;
3. Woo-contact route only if the relevant records/documents require formal disclosure.

## 4. Request identity

The request should identify:

- peilgebied `OT.02`;
- canonical project geometry `TOLLEBEEK_OT02_CURRENT`;
- owner layer `zzl_Drainage`;
- 74 intersecting drainage polygons;
- current public values: spacing `0`, null depth, null installation date;
- need for source-native field definitions and missing-value semantics.

Requested content follows `data_requests/tollebeek_drainage_data_request_v0_1.md`.

Preferred delivery is a source-native GIS/table export with stable object IDs, coordinates/geometry, field definitions, extraction/version date and any linked drainage-plan/document identifiers.

## 5. Privacy / ownership boundary

Parcel-level drainage data may be operationally or privately sensitive. If exact public release is not possible, acceptable acquisition alternatives include:

- an OT.02-selected extract with fields needed for model qualification;
- pseudonymous stable drainage-unit IDs;
- holder-side spatial selection against canonical OT.02 geometry;
- source document/asset identifiers plus auditable summary fields.

Privacy-preserving delivery does not relax the scientific requirements for spacing/depth/date semantics.

## 6. Admission boundary

`DR_SM_DRAINAGE` remains `PARTIAL_EVIDENCE` and `CAP_MULTI_DRAIN` remains data-gated.

Records received from the owner must still be checked for:

- source/version identity;
- whether spacing `0` is placeholder, unknown or a coded value;
- vertical datum/reference for drain depth/elevation;
- temporal validity / installation or renewal date;
- relation to the selected source-model spatial unit;
- missingness/QC;
- explicit mapping from physical drainage evidence to any SWAP-specific parameter.

Historical FutureWater 100 d / ~30 d resistances remain method priors only.

## 7. Current verdict

`QUALIFIED_ZZL_SOURCE_HOLDER_ACCESS_ROUTE — PHYSICAL_DRAINAGE_ATTRIBUTES_NOT_YET_ACQUIRED`

The next material drainage step is owner-data delivery and qualification, not another proxy/default parameter search.
