# Tollebeek OT.02 current-state direct-author recovery v0.1

Status: **PUBLIC RECOVERY EXHAUSTED — AUTHOR REQUEST REQUIRED**

Governing readiness item: `DR_SM_CURRENT_STATE`

This note records the next bounded acquisition route after closure of the BIS-4D alternative. It does **not** admit a CURRENT soil state.

## 1. Primary regional dataset sought

The priority remains the raw point dataset underlying:

- Van Egmond et al. (2024), *Regionale kartering bodemverdichting in de provincie Flevoland*;
- WER Rapport 3382;
- DOI `10.18174/672577`;
- WUR project number `5200043298`;
- RAAK-PRO dossier `RAAK.PRO02.021` / *Flevo-land in beweging*.

WER3382 states that more than 300 bulk-density and penetration-resistance measurements were collected for the regional study and that the point- and field-scale results had been published earlier.

No downloadable raw coordinate/value table or supplement for the regional 2020–2021 campaign was found in the public WUR publication record, indexed web results, 4TU/BIS-4D alternative, or the report itself.

## 2. Earlier point/field-scale publication identified

WER3382 cites:

Van Orsouw, T. L., Mulder, V. L., Schoorl, J. M., van Os, G. J., van Essen, E. A., Pepers, K. H. J., & Heuvelink, G. B. M. (2022), *Practical Implications of the Availability of Multiple Measurements to Classify Agricultural Soil Compaction: A Case-Study in The Netherlands*, Agronomy 12(7), 1669, DOI `10.3390/agronomy12071669`.

This paper is directly linked to grant `RAAK.PRO02.021` and therefore belongs to the same broader project family.

However, it is **not** the same dataset as the regional 2020–2021 campaign:

- its fieldwork took place in autumn 2018;
- it concerns one agricultural field in the Noordoostpolder;
- 50 sample locations were originally measured;
- the analysis retained a subset of 83 bulk-density samples from 25 locations after data loss and moisture filtering;
- measurements included dry bulk density at multiple depths, volumetric water content, and penetration resistance.

Therefore the 2018 field-study data cannot be relabelled as the WER3382 regional dataset or as OT.02 evidence without a separate spatial/provenance decision.

## 3. Data availability route

The 2022 Agronomy article states in its Data Availability Statement:

`Data is available on request from the authors. Any personal information will be anonymized in accordance with Dutch privacy regulations.`

This establishes a qualified direct-author route.

The corresponding-author route from the article and the WER3382 author/project-custodian route should be used to request:

1. the regional 2020–2021 measurement table first;
2. clarification whether the 2018 case-study records are maintained in the same project data administration;
3. source-native identifiers linking point-/field-scale records to later regional analyses where such links exist.

## 4. Required regional fields

For the regional 2020–2021 campaign, request at minimum:

- stable source-native location/sample ID;
- coordinate and CRS, where shareable;
- sampling date/time where available;
- exact depth or depth interval;
- three individual 100 cm3 ring measurements and/or their traceable mean;
- dry bulk density and units;
- fixed 30 cm versus field-selected second depth semantics;
- penetration-resistance depth series or source-native summaries;
- soil moisture and measurement-condition metadata relevant to penetration resistance;
- texture/lutum information used in interpretation, where shareable;
- QC/status flags and failed/disturbed sample indicators;
- any source-native field linking the record to the WER3382 regional analysis.

No missing field may be reconstructed as zero.

## 5. Privacy-safe spatial fallback

Exact source coordinates are preferred because canonical admission requires reproducible intersection with `data/spatial/tollebeek_ot02_current.geojson`.

If privacy/confidentiality prevents release of exact farm coordinates, the following fallback is acceptable for **route review**, but is lower authority than direct georeferenced records:

1. provide the custodian with the canonical OT.02 polygon or its exact source identity;
2. have the custodian perform the spatial intersection against the source coordinates;
3. return pseudonymized measurement IDs and all non-identifying measurement/depth/date/QC fields for records inside OT.02;
4. provide a written selection statement defining the polygon/source used, CRS, spatial predicate and number of source records selected;
5. retain a stable crosswalk under the custodian's control so the selection can be independently rechecked if needed.

A derived `inside_OT02` flag without documented selection semantics is insufficient for full admission.

Coordinates must not be reverse-engineered from published figures.

## 6. Temporal boundary

The regional campaign ran from September 2020 through June 2021.

Even if OT.02 records are recovered, they represent dated 2020–2021 observations. They are not automatically:

- October-1998 soil state;
- 2026 current state;
- a spatially complete OT.02 state.

Use under the admitted October-1998 meteorological event would be a controlled historical-forcing stress test unless a separate temporal-transfer argument is qualified.

## 7. Relationship to the 2018 field-study dataset

The 2018 dataset may be useful for:

- measurement-method corroboration;
- understanding depth-resolved triplicate-ring and penetration-resistance semantics;
- testing state-transformation and uncertainty machinery on a bounded case-study dataset.

It may **not** support OT.02 CURRENT-state admission unless source data establish that the field lies inside the admitted OT.02 polygon and its temporal/use semantics are separately qualified.

No attempt is made to infer the private field location from the published figure.

## 8. Current classification

Public recovery status:

`PUBLIC_RECOVERY_EXHAUSTED_AUTHOR_REQUEST_REQUIRED`

Readiness remains:

`DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`

The next permitted material action is receipt of source data or a source-custodian response. No soil-state row, spatial interpolation, area weighting, reference-state construction or model run is authorized by this route note.