# Tollebeek OT.02 current-state RhoC recovery v0.1

Status: **REVIEWED PUBLIC ALTERNATIVE — NOT SPATIALLY ASSIGNABLE TO OT.02**

Governing readiness item: `DR_SM_CURRENT_STATE`

## 1. Purpose

This bounded review tested whether the openly archived RhoC field-validation dataset can independently supply dated measured bulk-density evidence for the admitted Tollebeek OT.02 domain.

The review was deliberately separate from the WER3382/Flevo-land-in-beweging acquisition route. Shared authorship is not dataset provenance.

## 2. Source authority

Dataset DOI: `10.17026/PT/BYVPLB`

Dataset title: `RhoC validation data from 'Validation of a new Soil Bulk Density sensor'`

DANS raw-file identifiers used for reproducible review:

- README file ID: `98478`;
- CSV file ID: `98475`.

Corrected acquisition run `35101851142` retrieved and parsed the semicolon-delimited CSV successfully.

Exact CSV properties:

- bytes: `35197`;
- rows: `432`;
- SHA-256: `10bcb043226544f8e92ba2b4fcec0d1d35e23004e55c9f6e597ca0bb01ba2f02`;
- delimiter: `;`.

The first probe run `35101744917` acquired the same files but parsed the CSV with the wrong delimiter. That run is retained only as an execution record; no scientific conclusion is based on its parser output.

## 3. Dataset schema and measurement semantics

The corrected CSV exposes:

- `Depth_cm`;
- `Pit_nr`;
- `Profile_nr`;
- `Extra`;
- `Location_code`;
- `Field_BD_RhoC (kg/l)`;
- `Dry_BD_RhoC (kg/l)`;
- `Moisture_RhoC (%)`;
- `Field_BD_Rings (kg/l)`;
- `Dry_BD_Rings (kg/l)`;
- `Moisture_Rings (%)`;
- `Soil_texture`.

The README defines `Location_code` as a combination of pit, profile and depth. It is therefore a within-experiment sample identifier, **not** a geographic coordinate or spatial site identifier.

The README distinguishes RhoC-sensor quantities from reference laboratory measurements made with Kopecky rings. The ring-based bulk-density values are direct physical measurements within this experiment, while RhoC-derived values remain sensor estimates/derived quantities.

Depths represented are 10, 20, 30, 40, 50 and 60 cm below ground level.

## 4. Provenance classification

The README identifies this dataset as belonging to:

- project: `RhoC dichtheidsmeter`;
- project number: `KIEM.K21.01.080`;
- programme: `KIEM`;
- data collection period: March 2022 – March 2023.

No explicit provenance was found linking this dataset to:

- WER Rapport 3382;
- `RAAK.PRO02.021`;
- project `5200043298`;
- `Flevo-land in beweging`.

Therefore this dataset must remain a separate experiment/source, notwithstanding overlap in authorship with the Flevoland compaction work.

## 5. Spatial review

The CSV contains **no coordinate fields** and no source-native geographic field identifier from which a reproducible intersection with canonical `data/spatial/tollebeek_ot02_current.geojson` can be performed.

The source files contain no `Tollebeek`, `OT.02`, `Urk`, `Marknesse` or `Emmeloord` identifier.

`Dronten` appears in the README as the depositor/institution address (`De Drieslag 4, 8251 JZ, Dronten`), not as a measurement-field coordinate or field identity. It must not be interpreted as the sample location.

The associated publication describes one agricultural field in Flevoland and one in Gelderland, but that province-level distinction is insufficient to assign any observation to OT.02. A publication map or figure must not be reverse-georeferenced to create missing source coordinates.

## 6. Scientific usability

The dataset is useful as:

- independent method/context evidence that paired RhoC and Kopecky-ring bulk-density profiles were measured over multiple depths;
- a methodological benchmark for depth-resolved bulk-density measurement and sensor validation;
- contextual evidence about plausible field measurement structure.

It is **not** usable as:

- an observed Tollebeek OT.02 CURRENT state;
- an OT.02 spatial sample;
- a substitute for the WER3382 2020–2021 raw point dataset;
- a source for OT.02 area weights;
- evidence of the actual 1998 state;
- an automatically current 2026 state.

## 7. Decision

Route verdict:

`REVIEWED_PUBLIC_RHOC_DATASET_NOT_SPATIALLY_ASSIGNABLE_TO_OT02`

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`.

No `soil_state` record, model input, spatial weight or Tollebeek-specific bulk-density value is admitted by this review.

The direct WER3382/Flevo-land raw point-data request remains the active route because that campaign is documented as having actual GPS-linked measurements and the required spatial assignment cannot be reconstructed from this RhoC dataset.

## 8. Reuse boundary

This DANS DOI does not need to be re-investigated for OT.02 assignment unless a later source adds a traceable mapping from its pit/sample identifiers to source-native field coordinates. Any such mapping would constitute new evidence and require a separate bounded reconciliation.