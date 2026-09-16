# Tollebeek CURRENT-state point/field publication recovery v0.1 — RECONCILE

Capability: `DR_SM_CURRENT_STATE`

Phase: `RECONCILE`

Canonical start:
- repository: `abhedwig-cell/Bodemverdichting_kosten`
- main: `a3ab527769c62e2f8d5ba75c30b11e549db01ea5`
- branch: `work/tollebeek-current-state-pointscale-route-v0.1`

## Persisted dependencies

- `DR_SM_GEOMETRY = ADMITTED`; canonical OT.02 polygon is the only spatial admission surface.
- `DR_SM_PROFILE = ADMITTED`; SoilPhys/BOFEK modal properties remain profile context only.
- `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`; direct WER3382 / Flevo-land-in-beweging raw point data remain the active measurement route.
- PR #33 closed the public BIS-4D bulk-density archive as `REVIEWED_PUBLIC_ALTERNATIVE_NO_OT02_CURRENT_STATE_RECOVERY`.
- No current-state row, area weight or model input is admitted.

## New provenance clue

WER Rapport 3382 explicitly states that results at point and field scale had already been published before the regional report. Its bibliography cites:

Van Orsouw, T.L. et al. (2022), *Practical Implications of the Availability of Multiple Measurements to Classify Agricultural Soil Compaction: A Case-Study in The Netherlands*, Agronomy 12(7):1669, DOI `10.3390/agronomy12071669`.

The article is a Flevoland agricultural-field study using bulk density and penetration resistance. This establishes a plausible project-family/publication route, but does **not** establish that its records are the regional 2020–2021 305-location campaign, that its field lies in OT.02, or that underlying point data are public.

## Bounded question

Determine, from source-native article metadata/full text/supplement links where publicly accessible:

1. whether the 2022 study is explicitly funded by / part of `Flevo-land in beweging` / `RAAK.PRO02.021`;
2. measurement dates and spatial identity/coordinates at the level publicly disclosed;
3. whether the measurements are a subset of the later regional campaign or a distinct point/field-scale experiment;
4. whether raw or supplementary bulk-density / penetration-resistance records are publicly downloadable;
5. whether any such records can be assigned to admitted OT.02 without reconstructing coordinates from figures.

## Guardrails

- author overlap is not dataset identity;
- project-family membership is not proof that records belong to WER3382 regional sampling;
- no coordinate digitisation from maps/figures;
- no private/agricultural parcel identity inference beyond source-native disclosure;
- no use of summary statistics as CURRENT state;
- no modern record backdated to 1998;
- null/missing remains null;
- no readiness promotion unless actual source records satisfy the existing admission contract.

Next permitted action: temporary read-only public-source acquisition/provenance probe, then CLASSIFY. Temporary workflows must be removed before any canonical PR admission.