# Tollebeek CURRENT-state point/field publication route v0.1

Status: **ROUTE REVIEW — no CURRENT-state admission**

Governing readiness item: `DR_SM_CURRENT_STATE`

## Purpose

Review the point/field-scale publication route explicitly referenced by WER Rapport 3382 as a possible recovery path for measured soil-compaction records from the `Flevo-land in beweging` project family.

The candidate publication is:

Van Orsouw, T.L. et al. (2022), *Practical Implications of the Availability of Multiple Measurements to Classify Agricultural Soil Compaction: A Case-Study in The Netherlands*, Agronomy 12(7):1669, DOI `10.3390/agronomy12071669`.

This review asks whether the publication recovers the regional 2020–2021, 305-location campaign underlying WER3382 or provides source-native observations that can be assigned to the admitted OT.02 polygon.

## Source acquisition

The publisher HTML/XML route returned HTTP 403 during branch-only probing. The WUR eDepot copy at `https://edepot.wur.nl/577746` was publicly and reproducibly acquired and parsed.

Temporary acquisition run `35098231879` succeeded for the WUR PDF route. The PDF was 5,318,065 bytes.

The HTTP 403 responses are access-route behaviour only and have no scientific meaning.

## Exact project-family relation

The paper explicitly states that the research and article processing charge were funded by Taskforce for Applied Research (SIA), a subsidiary of NWO, under grant:

`RAAK.PRO02.021`

and by the Province of Flevoland.

This confirms that the study belongs to the same funded project family as `Flevo-land in beweging`.

That relation is important provenance context but is **not** sufficient to identify the study records with the later regional WER3382 sampling campaign.

## Study design and timing

The source-native article text describes:

- one agricultural study site at the edge of Emmeloord;
- 25 measurement locations within that field;
- selection of the field because of heterogeneous compaction associated with a heavy compaction event in 2017;
- fieldwork in autumn 2018, after maize harvest;
- soil moisture approximately at field capacity during sampling;
- use of bulk-density and penetration-resistance measurements among the compaction indicators.

The article also discusses satellite imagery from 2018 and 2021, but those image dates do not change the 2018 field-sampling date.

## Relation to WER3382 regional campaign

The WER3382 regional campaign is separately documented as:

- 305 agricultural sampling locations across Flevoland;
- fieldwork from September 2020 through June 2021;
- regional sampling design intended for provincial mapping/assessment.

Therefore the Van Orsouw et al. study is **not the same sampling campaign**:

| Property | Van Orsouw et al. 2022 field study | WER3382 regional campaign |
|---|---|---|
| scale | single field | province-wide agricultural locations |
| disclosed measurement locations | 25 | 305 |
| fieldwork | autumn 2018 | Sep 2020–Jun 2021 |
| design context | heterogeneous field after 2017 compaction event | regional Flevoland campaign |

Shared grant/project provenance does not override these explicit differences.

## Data availability

The article states:

> Data is available on request from the authors.

It also notes that personal information would be anonymized in accordance with Dutch privacy rules.

No public downloadable CSV/XLSX/ZIP/repository object was recovered from the public article/eDepot route during this workunit.

Accordingly, the publication provides an actionable **secondary data-request route**, not an immediately ingestible canonical dataset.

## Spatial admission boundary

The article identifies the study site in prose as being at the edge of Emmeloord and shows measurement locations in a figure.

This workunit does **not** digitize coordinates from that figure. A figure-derived point is not a source-native coordinate when underlying coordinates can instead be requested from the authors.

No source-native public coordinate record or data-object was recovered that permits a reproducible intersection with canonical `data/spatial/tollebeek_ot02_current.geojson`.

Therefore no observation from this publication is admitted as OT.02 CURRENT-state evidence.

## Scientific classification

Route classification:

`PROJECT_LINK_CONFIRMED_DISTINCT_2018_FIELD_DATA_ON_REQUEST`

Meaning:

1. exact `RAAK.PRO02.021` project-family provenance is confirmed;
2. the study is a real direct-measurement soil-compaction dataset route;
3. it is demonstrably a distinct 2018, 25-location field experiment rather than the 2020–2021, 305-location regional campaign;
4. raw data are not publicly recovered here but are explicitly available on request;
5. OT.02 membership is unresolved and must not be inferred from prose or a printed map.

## Guardrails

This route must not be used to:

- relabel the 2018 field data as the WER3382 regional dataset;
- infer OT.02 membership from `Emmeloord` or from figure placement;
- digitize map coordinates and treat them as source-native measurements;
- use article summary statistics as a local soil state;
- transfer one field's bulk density or penetration resistance across OT.02;
- backdate a 2018 or 2020–2021 observation to the 1998 event;
- promote `DR_SM_CURRENT_STATE` without actual records satisfying the canonical admission contract.

## Current decision

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`.

The primary acquisition route remains the raw 2020–2021 WER3382 / Flevo-land regional point dataset.

The Van Orsouw 2018 field dataset is retained as a secondary request route and methodological/project-family context. If source-native records are later obtained, they must be independently checked for coordinates, dates, depths, methods, QC and reproducible OT.02 intersection before any state admission.
