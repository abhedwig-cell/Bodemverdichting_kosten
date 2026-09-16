# Tollebeek CURRENT-state DOI / public-metadata recovery v0.1

Status: **REVIEWED PUBLIC ROUTE — NO RAW CAMPAIGN DATASET RECOVERED**

Governing readiness item: `DR_SM_CURRENT_STATE`

Original acquisition baseline: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`

Canonical reconciliation baseline: `30cfc402beab780b61026f3536fa7fd6399145c7`

## Purpose

Test whether the raw 2020–2021 Flevoland soil-compaction measurements underlying WER Report 3382 can be recovered through machine-resolvable publication metadata, DOI relations, public dataset registries, or an explicit supplement/data link from the publication landing page.

The workunit requires explicit provenance. A title, author, subject, geographic or year match alone is not sufficient to identify a dataset as the WER3382 / `Flevo - land in beweging` campaign.

## Publication authority

Report DOI: `10.18174/672577`.

DOI resolution returned HTTP 200 and resolved to:

`https://research.wur.nl/en/publications/regionale-kartering-bodemverdichting-in-de-provincie-flevoland/`

The landing page contained report identifier `672577`, project number `5200043298`, bodemverdichting terms and bulk-density wording. It did not contain `RAAK.PRO02.021` or the literal project-title variants probed.

The page exposed only a generic WUR datasets navigation link among data-related links. No campaign-specific CSV, ZIP, XLSX, GeoPackage, shapefile, supplement, repository object or dataset DOI was exposed.

## Registry results

### Crossref

The Crossref record for `10.18174/672577` had no declared dataset `relation` entries and no downloadable-data `link` object identifying the raw field dataset.

### DataCite

Direct DataCite DOI lookup did not expose a related dataset identifier for the report DOI.

Narrow DataCite searches were performed for:

- `10.18174/672577`;
- `672577`;
- `RAAK.PRO02.021`;
- `5200043298`;
- `Flevo - land in beweging`;
- `Regionale kartering bodemverdichting`.

No result could be explicitly tied to the WER3382 campaign. Two results returned for the bare number `672577` were unrelated false positives: a scientific-collection image object and a crystallographic dataset. They are excluded.

### Zenodo

Narrow Zenodo API searches for the report DOI, `RAAK.PRO02.021`, `5200043298`, and the project-title phrase returned no candidate records.

### Candidate WUR data hosts

The guessed hosts `researchdata.wur.nl` and `data.wur.nl` did not resolve in the acquisition environment. This is only a route observation; it is not evidence that WUR has no internal or externally hosted research-data service.

## Acquisition evidence

Temporary branch-only workflow run:

- `35083443676` — SUCCESS.

The probe queried DOI/WUR landing metadata, Crossref, DataCite, OpenAlex, Zenodo and candidate WUR data hosts.

Artifact:

- `tollebeek-current-state-doi-probe`;
- artifact id `10440518949`.

The temporary workflow was removed before qualification.

## Classification

`REVIEWED_PUBLIC_DOI_METADATA_ROUTE_NO_RAW_WER3382_DATASET_RECOVERY`

This means:

- the publication and project metadata are publicly resolvable;
- no explicit machine-resolvable relation to the raw 2020–2021 measurement table was recovered from the tested metadata surfaces;
- the direct source-holder route remains necessary unless another independently identified repository object is found.

It does **not** mean that the raw measurements do not exist or cannot be shared.

## Relationship to the qualified source-holder access route

Parallel canonical work has already qualified `docs/38_tollebeek_current_state_access_route_v0_1.md`.

That route identifies Aeres Hogeschool / RAAK-PRO, WUR/WER and Actieplan Bodem & Water Flevoland as source-holder/referral paths. The present DOI review does not replace that route; it strengthens the conclusion that another generic public-repository search is lower value than contacting those source holders with the exact identifiers.

## Readiness consequence

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE` / `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`.

No CURRENT-state row, bulk-density value, penetration-resistance value, area weight, hydraulic transformation or model input is created by this workunit.

## Guardrails retained

- no figure digitisation;
- no project-number coincidence as dataset identity;
- no author overlap as provenance;
- no numeric false positive accepted because it contains `672577`;
- no modern 2020–2021 observation backdated to 1998;
- no missing value replaced by zero or a model default.

## Next material action

Use the qualified source-holder acquisition route and the canonical request contract to obtain the georeferenced source-native WER3382 / Flevo-land measurement records or a stable repository/dataset identifier. A future public repository candidate must be verified by explicit source-native provenance before use.
