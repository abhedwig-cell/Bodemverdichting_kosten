# Tollebeek current-state source-holder handoff v0.1 — RECONCILE

Status: `RECONCILED`

Protocol: `RECONCILE → PACKAGE → QUALIFY → CLOSE`

Canonical start:

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- branch: `main`
- head: `bf8bde57e86ffdc06cf0278a2c885554e1feddce`

Governing readiness item: `DR_SM_CURRENT_STATE`.

## Inherited authorities

The following current-canonical results are inherited and are not reopened:

1. The 2020–2021 Flevoland field campaign underlying WER Rapport 3382 is a real direct-measurement source candidate with dry bulk density and penetration-resistance measurements.
2. The exact raw source records needed for Tollebeek OT.02 have not been recovered from public publication/download surfaces.
3. The public BIS-4D bulk-density archive has been screened and is not an OT.02/WER3382 recovery route.
4. DOI/public-metadata routes through the WUR landing page, Crossref, DataCite, OpenAlex, Zenodo and guessed WUR data hosts did not expose a provenance-qualified raw campaign dataset.
5. The qualified remaining route is direct source-holder acquisition through Aeres / RAAK-PRO and WUR/WER, with Actieplan Bodem & Water Flevoland as a referral route.
6. `DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE` / `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`.
7. No 2020–2021 measurement may be relabelled as October 1998 or as a 2026 current state without a separate temporal-transfer decision.

## Purpose of this workunit

Turn the already qualified acquisition route into a direct execution handoff. This workunit packages:

- unambiguous request identifiers;
- ready-to-send Dutch request text per source-holder route;
- privacy-preserving OT.02 selection fallback;
- minimum requested metadata/data fields;
- raw-file receipt and provenance-preservation procedure;
- acceptance steps after receipt.

It does **not**:

- send an email;
- claim access permission;
- admit any CURRENT-state observation;
- create a synthetic soil state;
- digitise figures;
- change readiness status;
- run SWAP.

## Current source-holder order

1. Aeres Hogeschool / RAAK-PRO project route — Karin Pepers (`k.pepers@aeres.nl`).
2. Wageningen Environmental Research / WER3382 author/data-holder route — Fenny van Egmond via the current WUR public profile/contact route; no email address is invented in this repository.
3. Actieplan Bodem & Water Flevoland referral route — `info@bodemenwaterflevoland.nl`.

## Exact dataset identifiers to include

- project title: `Flevo - land in beweging`
- RAAK-PRO dossier: `RAAK.PRO02.021`
- WER project number: `5200043298`
- report: `WER Rapport 3382`
- report DOI: `10.18174/672577`
- campaign period: September 2020 through June 2021
- target scientific area: Tollebeek OT.02
- canonical target geometry: `data/spatial/tollebeek_ot02_current.geojson`

## Guardrails

- Prefer a stable repository/dataset identifier over an emailed spreadsheet when one exists.
- Preserve source-native file bytes before transformation.
- Unknown or unavailable fields remain missing; never substitute zero.
- Do not infer OT.02 membership from a map image if source coordinates or holder-side spatial selection are possible.
- If coordinates are privacy-sensitive, accept a holder-side reproducible OT.02 selection with stable pseudonymous IDs and auditable selection metadata.
- Receipt alone does not move `DR_SM_CURRENT_STATE` to `ADMITTED`.

## Next permitted action

Create the executable source-holder handoff package and qualify that it is internally consistent with the existing canonical data request and current-state access/DOI/BIS conclusions.