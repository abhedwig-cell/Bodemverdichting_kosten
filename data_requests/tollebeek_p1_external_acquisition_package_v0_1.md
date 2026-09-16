# Tollebeek P1 external acquisition package v0.1

Date: 2026-09-16
Canonical project baseline: `1e9844e6aade92f840d5539d552cdd2b6b065665`
Event: `EVT_TOL_1998_OCT`

Status: `CONSOLIDATED_OPEN_ACQUISITION_PACKAGE`

## Purpose

Bundle the still-open external-data requirements for the first Tollebeek source-model pair without changing any scientific readiness status. This package does not replace the detailed request contracts; it provides one operational handoff grouped by source holder / acquisition route.

The current P1 register has `ADMITTED=3`, `PARTIAL_EVIDENCE=7`, `MISSING=0`. Route coverage is complete, but the model is not run-ready.

## Package A — WUR/WER / Flevo-land-in-beweging: measured soil-compaction state

Governing item: `DR_SM_CURRENT_STATE`.

Detailed contract: `data_requests/tollebeek_current_state_data_request_v0_1.md`.

Primary target is the raw point dataset underlying the September 2020–June 2021 Flevoland field campaign reported in WER Rapport 3382 / Flevo-land-in-beweging.

Request source-native records with, at minimum:

- stable measurement/location ID;
- field GPS coordinates and CRS;
- sampling date;
- exact sample depth/depth interval and fixed-versus-field-selected semantics;
- individual dry-bulk-density ring measurements and/or traceable mean;
- ring volume/method metadata needed to confirm ISO 11272:2017 use;
- penetration-resistance depth series or native summary values where available;
- measurement moisture/context where available;
- sample/field QC, disturbed/failed sample flags and other quality notes;
- soil-profile/BRO/soil-description links where available;
- texture/lutum interpretation fields where shareable;
- management/land-use metadata only where privacy/confidentiality allows.

Acceptance path after receipt:
1. preserve raw identifiers/values/QC;
2. intersect source coordinates reproducibly with `data/spatial/tollebeek_ot02_current.geojson`;
3. retain 2020–2021 measurement dates explicitly;
4. review whether the OT.02 subset is sufficient for a dated measured state;
5. make any later temporal-transfer decision separately.

Do not reconstruct coordinates from figures, infer area fractions from sparse point counts, convert penetration resistance to bulk density without a qualified relation, or substitute SoilPhys modal density.

## Package B — Waterschap Zuiderzeeland: parcel drainage configuration

Governing item: `DR_SM_DRAINAGE`.

Detailed contract: `data_requests/tollebeek_drainage_data_request_v0_1.md`.

For selected OT.02 source-model units / parcels, request source-native drainage records with:

- stable asset/drainage-unit ID;
- parcel/spatial-unit link or geometry and CRS;
- actual drain spacing or drain-density equivalent;
- drain depth/elevation and vertical datum/reference;
- installation/renewal date;
- material/type where hydraulically relevant;
- outlet point or receiving ditch/watercourse;
- operational/maintenance status where relevant;
- source-system/version and extraction date;
- missing-value semantics and QC/status flags.

Design drawings or drainage plans are usable evidence when source document/asset identity is preserved. Missing fields remain missing.

Acceptance path after receipt:
1. validate source/version/field semantics;
2. spatially join to admitted OT.02 and selected model units;
3. preserve source-native raw values and missing flags;
4. classify temporal applicability;
5. qualify any physical-to-SWAP parameter mapping separately.

Explicit non-substitutes: owner spacing `0`, historical FutureWater 100 d / ~30 d resistances, open-water density, target peil as drain level, or missing→0.

## Package C — Waterschap Zuiderzeeland archives: 1998 managed boundary and operations

Governing item: `DR_SM_MANAGED_BOUNDARY`.

Detailed contract: `data_requests/tollebeek_managed_boundary_data_request_v0_1.md`.

Requested window: `1998-10-24T00:00:00Z` through `1998-10-30T00:00:00Z`, highest priority 27–28 October.

Request, preserving source-native timestamps/timezone, location identity, datum, units, QC and provenance:

- surface-water levels at or representative of De Rietgors (OT02), De Fuut (OT03), De Kievit (OT04) and associated tochten;
- Urkervaart water level for the same period;
- historical Rietgors/Fuut/Kievit pump on/off, runtime, setpoint, capacity-state or realized-discharge records;
- stuw/inlaat operations materially affecting the historical control areas;
- emergency-pump location, start/stop, nominal/realized capacity and receiving water;
- operator logs, calamity reports or event reconstructions distinguishing ordinary control from emergency intervention.

Near-period target levels and nameplate capacities may constrain later reconstruction but are not telemetry. Current IJsvogel / merged OT.02 operation is post-1998 and is not an acceptable silent substitute.

## Package D — historical shallow groundwater / soil-water observations for event initialization

Governing item: `DR_SM_INITIAL_STATE`.

Detailed contract: `data_requests/tollebeek_initial_state_data_request_v0_1.md`.

Use BRO/DINO and owner/archive routes to seek a shallow/phreatic groundwater or soil-water observation inside, or demonstrably representative of, OT.02 near `1998-10-24T00:00:00Z`.

Required metadata:

- stable observation/well ID;
- coordinates and CRS;
- observation date/time and timezone;
- vertical datum and local ground elevation;
- screen/depth interval;
- source-native value and unit;
- quality/assessment status;
- provenance.

Existing deep piezometric series and nearby shallow series remain hydrogeological context only. The NAP -6.20 m target peil is not an initial groundwater level.

If no direct state can be recovered, stop at that evidence boundary. A warm-up/restart route is a later scientific/configuration decision and must not be fabricated from this package.

## Package E — historical 1998 parcel/field crop or vegetation evidence

Governing item: `DR_SM_LAND_USE`.

Detailed contract: `data_requests/tollebeek_land_use_data_request_v0_1.md`.

Seek dated 1998 growing-season parcel/field evidence spatially linkable to historical Tollebeek control areas / selected source-model units. Preserve where available:

- parcel/field ID;
- geometry/coordinates and CRS;
- crop code/name or vegetation class;
- reference date/year;
- source provenance;
- management/phenology information required by the eventual model design.

Qualified context that is **not** exact 1998 crop evidence:
- LGN3 / 1995 Flevoland classification;
- LGN4 / 1999–2000 classification;
- public BRP/Gewaspercelen archive from 2009 onward;
- broad arable/forest descriptions.

Do not interpolate through crop rotation, assign one representative crop to all OT.02, or infer bare soil from the late-October date. If direct 1998 crop evidence is not recoverable, a crop-independent or scenario-based model design requires a separate scientific qualification and must be labelled non-observational.

## Dependent decisions — not external acquisition requests

### `DR_SM_REFERENCE_STATE`

Do not construct the Tollebeek reference state before an admissible CURRENT state and explicit causal contrast are available. The reference is not synonymous with pristine, zero traffic or arbitrary low bulk density.

### `DR_SM_MODEL_CONFIG`

The SWAP5 authority chain is already qualified:
- scientific executable authority `50346642bd565f79134ea17d5462e544b354998c`;
- production tree `3b085d7dea3d3f3fce42ad9d8f259a8350205846`;
- Status-A acceptance authority `992a5c657bfe10a10100f92e0cb77c4825ae65b6`.

Detailed internal contract: `data_requests/tollebeek_model_config_data_request_v0_1.md`.

A concrete configuration must wait until unresolved scientific inputs are admitted or separately qualified as explicit scenario/reconstruction semantics. SWAP defaults are not evidence.

## Package-wide receipt rule

For every received dataset or archive extract:
1. preserve source-native IDs, units, timestamps, datum/CRS, missingness and QC;
2. store provenance/extraction date before any transformation;
3. never map missing to zero;
4. separate raw evidence from model-specific derivations;
5. qualify spatial and temporal applicability before admission;
6. update only the governing readiness item after review.

This package is an acquisition handoff, not an admission decision.
