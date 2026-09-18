# On-site maize × soil crosswalk v0.1

Status: **ARCHITECTURE READY — RAW DATA AND SOIL-CODE MAPPING GATED**  
Parent calculation surface: `52_onsite_bounded_calculation_surface_v0_1.md`  
Input routes: `53_onsite_crop_and_valuation_input_routes_v0_1.md`

## 1. Purpose

Resolve one specific blocker in the bounded on-site maize calculation:

> How much definitive 2025 silage-maize area lies in each soil class relevant to the CC-NL six-class reporting framework?

The intended calculation is:

```text
BRP 2025 definitive crop parcels
  filtered to silage maize
×
versioned BRO Bodemkaart polygons
  explicitly translated to CC-NL6
=
maize area by CC-NL6 soil class
```

This workunit does **not** determine compaction exposure or crop damage.

## 2. Crop source contract

Primary source:

`SRC_BRP2025_PDOK`

Verified target semantics:

- dataset: BRP Gewaspercelen 2025 definitief;
- crop: `Mais, snij-`;
- `gewascode = 259`;
- `jaar = 2025`;
- `status = Definitief`.

The source contains parcel geometry and declared crop.

The builder accepts a locally persisted source file and applies these filters again. This avoids relying on a filename or upstream query alone.

## 3. Soil source contract

Primary source:

`SRC_BRO_SGM`

The BRO Bodemkaart is a versioned national soil model at approximately 1:50,000 scale.

The download exposes, among other attributes:

- `soil_unit_code`;
- `soil_classification`;
- `main_soil_classification`;
- upper-profile soil characteristics;
- geometry.

Every downloaded model used by this project must retain:

- exact source/version metadata;
- original raw file;
- SHA-256;
- original layer name if applicable.

## 4. Critical scientific distinction: CC-NL6 is not a ready-made current polygon layer

The six CC-NL reporting classes are:

| ID | Class |
|---|---|
| ZE | sandy soils with an eerd layer >= 30 cm |
| ZO | other sandy soils |
| K | clay soils |
| L | loam soils |
| M | organic-mineral / moerige soils |
| V | peat soils |

The published 2018 land-use × soil areas were **domain estimates based on LSK profile descriptions from 1994–2001**.

Therefore a present-day BRP × BRO overlay is not a reconstruction of historical LSK membership.

The valid interpretation is:

`CURRENT_SPATIAL_APPROXIMATION_TO_CCNL6_REPORTING_CLASSES`

not:

`CCNL2018_DOMAIN_RECONSTRUCTION`.

This matters especially for peat and organic-mineral soils, for which the 2018 report itself warns that classification may have changed.

## 5. Explicit soil-code mapping layer

The repository contains:

- `config/ccnl6_class_definition_v0_1.csv`;
- `config/bro_sgm_to_ccnl6_mapping_v0_1.csv`.

The second file is deliberately empty at v0.1.

Each BRO `soil_unit_code` encountered under silage-maize geometry must be reviewed and recorded as:

- `QUALIFIED`;
- `REVIEW_REQUIRED`; or
- `REJECTED`.

A qualified row must carry a mapping basis.

### No residual catch-all

A soil code that is unknown is **not** automatically:

- other sand;
- the dominant class in the polygon;
- the nearest known code.

In particular, `ZO` may only be used after the unit is positively established as sandy mineral soil that does not meet the ZE criterion.

## 6. Executable overlay

Builder:

`tools/build_onsite_maize_soil_crosswalk.py`

Example once raw inputs and mappings are ready:

```bash
python tools/build_onsite_maize_soil_crosswalk.py \
  --brp raw/brp_gewaspercelen_2025.gpkg \
  --soil raw/bro_bodemkaart_sgm.gpkg \
  --soil-layer <layer-name>
```

The builder:

1. checks required BRP/BRO attributes;
2. converts both sources to EPSG:28992;
3. filters BRP again to crop 259 / year 2025 / definitive;
4. identifies BRO soil codes that actually intersect maize parcels;
5. aborts if any intersecting code is missing or not `QUALIFIED`;
6. overlays maize and soil polygons;
7. computes area by CC-NL6 class;
8. checks spatial area closure;
9. persists source and mapping SHA-256 values;
10. generates a result manifest.

No proportional correction is applied when closure fails.

## 7. Area-closure gate

Let:

- (A_M) = summed target maize parcel area;
- (A_S) = summed maize × soil intersection area.

The default gate is:

```text
abs(A_S - A_M) / A_M <= 0.005
```

i.e. 0.5% relative closure error.

A failed closure is a diagnostic problem, not a reason to scale the output to 100%.

Possible causes include:

- soil-map gaps;
- invalid geometry;
- overlapping soil polygons;
- CRS problems;
- incomplete map coverage.

## 8. Scale interpretation

The BRO Bodemkaart is suitable for national/regional applications but is not a parcel-scale field survey.

Accordingly:

- a parcel intersection can contribute area to a national/regional soil class;
- it must not be reported as newly observed soil truth for that individual farm parcel.

This crosswalk is intended for aggregated area allocation.

## 9. Independent closure/context check

CBS national silage-maize area remains an independent context check.

It must not be used to redistribute the crosswalk.

Valid use:

```text
BRP geometry aggregate
  compared with
CBS national crop area
  → explain dataset/definition/year differences
```

Invalid use:

```text
scale BRP×BRO soil-class areas until they equal CBS
```

without a separately justified reconciliation method.

## 10. Qualification sequence

The workunit follows:

```text
ACQUIRE
  ↓
HASH / IDENTIFY
  ↓
EXTRACT INTERSECTING BRO CODES
  ↓
REVIEW BRO → CCNL6 MAPPING
  ↓
QUALIFY ALL USED MAPPINGS
  ↓
OVERLAY
  ↓
AREA-CLOSURE CHECK
  ↓
NATIONAL CONTEXT CHECK
  ↓
QUALIFY / ADMIT CROP-SOIL SHARE
```

## 11. Current state

As of this v0.1 checkpoint:

- BRP public route: **QUALIFIED**;
- BRP target crop code 259: **VERIFIED**;
- BRO SGM source route: **QUALIFIED_WITH_LIMITATIONS**;
- CC-NL6 class definition: **QUALIFIED**;
- historical LSK/current-BRO distinction: **QUALIFIED**;
- raw BRP file in repository/workspace: **NOT MATERIALIZED**;
- raw BRO model in repository/workspace: **NOT MATERIALIZED**;
- qualified BRO `soil_unit_code` mapping rows: **0**;
- overlay result: **NOT GENERATED**;
- run authorization: **FALSE**.

Verdict:

`ARCHITECTURE_READY_DATA_AND_MAPPING_GATED`

## 12. What a colleague should do next

The next work is bounded and concrete:

1. download/persist the definitive 2025 BRP dataset or a source-native maize selection;
2. download/persist a versioned BRO SGM GeoPackage;
3. hash both raw files before transformation;
4. run the builder once to obtain the list of intersecting unmapped soil codes;
5. review those codes against official BRO classification/profile information;
6. populate and review `bro_sgm_to_ccnl6_mapping_v0_1.csv`;
7. rerun until mapping and area closure pass;
8. compare the resulting national maize-area total with CBS as a non-corrective context check;
9. only then promote the resulting crop-share terms into the bounded calculation surface.

No SWAP, WOFOST or other process model is needed for this step.
