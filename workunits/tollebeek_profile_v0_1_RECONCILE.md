# Tollebeek profile v0.1 — RECONCILE checkpoint

Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → ADMIT → CLOSE

## Starting authority

- canonical start: `main` @ `5bd29b31745e093e82b63cc18e46f3a251b1695d`
- work branch: `work/tollebeek-profile-v0.1`
- governing readiness item: `DR_SM_PROFILE`
- admitted spatial domain: `data/spatial/tollebeek_ot02_current.geojson`
- geometry authority: current definitive owner OT.02 peilgebied feature admitted by PR #19

## Live equivalence check

No open branch or pull request materially equivalent to a current OT.02 profile-selection / BOFEK / SoilPhys admission workunit was found.

## Existing canonical evidence

`DR_SM_PROFILE` is `PARTIAL_EVIDENCE`.

Already qualified method evidence includes:

- `EV_SOILPHYS_ROUTE`: coordinate queries to WUR Soil Physical Data return derived/modal soil-profile attributes;
- `EV_GROEN_PROFILE_GEOMETRY`: compacted-layer depth/thickness and overlying storage depth matter for hydrological response;
- `SRC_WUR_BOFEK2020`: BOFEK2020 is the national soil-physical-unit framework available for spatial profile context.

## External source reconciliation

Public WUR documentation reviewed on 2026-09-16 establishes:

1. Soil Physical Data of the Netherlands exposes a coordinate API using latitude/longitude.
2. Its profiles are modal values for 368 soil mapping units derived from observations and are explicitly not field observations.
3. BOFEK2020 clusters the national soil-physical variation into 79 units, each linked to a schematised standard profile and Staring-series layer properties.
4. BOFEK2020 is intended for water/solute model input and is used within NHI for models including SWAP.
5. BOFEK2020 has an application scale of approximately 1:50,000 to 1:1,000,000; therefore it supports profile-domain stratification but does not prove parcel-scale current compaction state.

## Decision surface

This workunit may:

- screen the admitted OT.02 polygon spatially using SoilPhys and/or BOFEK2020;
- identify soil/profile classes and their spatial prevalence;
- persist candidate derived/modal profile definitions with provenance;
- qualify a representative profile set if coverage and sampling stability are sufficient;
- update `DR_SM_PROFILE` accordingly.

This workunit must not:

- interpret modal/derived bulk density as measured current anthropogenic compaction;
- create CURRENT or REFERENCE soil-state contrasts;
- infer affected compaction area;
- select crop, drainage, event or model numerical configuration;
- run source-model attribution.

## Acquisition design

Use the admitted OT.02 polygon as the sole spatial sampling domain. Prefer a deterministic regular-grid screening with at least one shifted-grid sensitivity check. Query SoilPhys only for points inside the polygon and retain raw API responses/provenance. If a sufficiently reproducible BOFEK spatial source can also be acquired, use it as an independent spatial stratification/cross-check.

Do not promote one convenient coordinate to the representative Tollebeek profile.

## RECONCILE verdict

`PASS_RECONCILE`

Next permitted phase: `ACQUIRE`.
