# Tollebeek current-state RhoC recovery v0.1 — RECONCILE

Status: RECONCILED

Capability: DR_SM_CURRENT_STATE
Phase: RECONCILE
Canonical source branch/head: main @ a3ab527769c62e2f8d5ba75c30b11e549db01ea5
Work branch: work/tollebeek-current-state-rhoc-recovery-v0.1

## Why this workunit exists

The direct 2020–2021 WER3382/Flevo-land-in-beweging point data remain unavailable through the reviewed public routes. A separate 2024 peer-reviewed RhoC validation study by Pepers et al., with Van Egmond and Teuling among the authors, openly publishes its field data in DANS under DOI `10.17026/PT/BYVPLB`.

This is a genuinely separate source/provenance decision surface. Author overlap alone is not provenance and does not make the RhoC dataset part of WER3382.

## Bounded question

Does the DANS RhoC validation dataset contain a directly measured, source-georeferenced Flevoland field location that can be reproducibly shown to fall inside the admitted OT.02 polygon and therefore potentially contribute dated CURRENT-state evidence?

## Known public metadata before acquisition

- dataset DOI: `10.17026/PT/BYVPLB`;
- DANS dataset title: `RhoC validation data from 'Validation of a new Soil Bulk Density sensor'`;
- public CSV + README;
- study: two agricultural fields, one in Flevoland and one in Gelderland;
- Flevoland measurements: 14–23 March 2022;
- 10 locations per field, three replicate profiles per location, six depths from 10 to 60 cm;
- Kopecky ring dry bulk density is the reference measurement method.

## Admission boundary

A RhoC/Kopecky observation can only become OT.02 evidence if source-native location information is sufficient to intersect the admitted polygon reproducibly. A map image, province label, author affiliation, landscape similarity or project relationship is not sufficient.

If the dataset lacks usable coordinates/exact location identifiers, close this route as contextual external evidence only. Do not infer a Tollebeek location from the publication figure.

## Guardrails

- do not treat RhoC data as WER3382 unless explicit provenance says so;
- do not georeference from a publication map figure;
- do not call a Flevoland-wide/unknown Flevoland point an OT.02 observation;
- keep measurement date 2022 explicit; do not backdate to 1998 or silently relabel as 2026 CURRENT;
- preserve Kopecky-ring measurements separately from RhoC sensor estimates;
- no area weighting from sparse locations;
- no soil-state admission unless exact spatial provenance and state semantics pass review.

## Next permitted action

ACQUIRE the public DANS README/CSV read-only; inspect schema, provenance, location/date/depth/method fields and exact-location evidence. Temporary acquisition tooling must be removed before any canonical merge.