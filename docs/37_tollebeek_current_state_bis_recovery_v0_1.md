# Tollebeek OT.02 current-state BIS recovery v0.1

Status: **ROUTE REVIEWED — NO OT.02 / WER3382 CURRENT-STATE RECOVERY**

Governing readiness item: `DR_SM_CURRENT_STATE`

This note records a bounded provenance-recovery attempt against the public BIS-4D point-data publication. The purpose was to determine whether the raw 2020–2021 Flevo-land-in-beweging / WER Rapport 3382 bulk-density measurements could be recovered indirectly from the public BIS point archive.

No CURRENT soil state is admitted by this workunit.

## 1. Public dataset reviewed

4TU dataset article UUID:

`c90215b3-bdc6-4633-b721-4c4a0259d6dc`

Target bulk-density file:

- name: `tbl_cal_BD_gcm3.csv`
- file UUID: `e6a9e9c9-53ea-48ba-b95a-44e432d5dae9`
- bytes: `913870`
- MD5: `4208fe0d0d54ed17db121be6007bc1e3`
- SHA-256: `e9924a1f83b4615ad9366cbf6cffdfae2ddab278f3d6c54aa19a457346fa7ff1`
- rows: `15871`

The recovered source columns are:

- `BIS_tbl`
- `BIS_type`
- `sample_id`
- `site_id`
- `X`
- `Y`
- `hor_nr`
- `hor`
- `d_upper`
- `d_lower`
- `d_mid`
- `year`
- `BD_gcm3`

The 4TU README states that coordinates use EPSG:28992 / RD New, `BIS_tbl` identifies the BIS dataset table, and `BIS_type` identifies observation quality (`lab` versus `field`). It describes bulk-density inputs from BIS profile-description / soil-boring datasets and identifies the BIS-4D project context separately from the Flevo-land-in-beweging campaign.

## 2. Exact provenance screen

The source CSV was searched for the following exact/near-exact campaign identifiers:

- `5200043298`
- `RAAK.PRO02.021`
- `Flevo-land in beweging`
- `Flevo - land in beweging`
- `672577`
- `WER 3382`
- `3382`
- `van egmond`
- `teuling`

CSV result: **zero hits for every token**.

The README likewise contains no WER3382 / RAAK.PRO02.021 / project-number identification. The surname `Teuling` occurs in the README project acknowledgements/context, but that is not evidence that the Flevo-land-in-beweging measurements are present in the point file.

Author or contributor overlap is therefore explicitly rejected as a provenance bridge.

## 3. Temporal screen

A first broad text probe reported ten strings containing `2020` or `2021`. A stricter second probe tested the actual `year` column.

Result:

**zero records have `year = 2020` or `year = 2021`.**

The first broad hits were therefore false positives from unrestricted text matching and are not retained as temporal evidence.

## 4. OT.02 spatial screen

The source-native `X`/`Y` coordinates were interpreted in EPSG:28992 as specified by the README and intersected directly with canonical:

`data/spatial/tollebeek_ot02_current.geojson`

Result:

**zero of the 15,871 bulk-density records fall inside the admitted OT.02 polygon.**

Consequently:

- there is no BIS bulk-density point in this public file that can be admitted as a Tollebeek OT.02 CURRENT-state observation;
- there is no 2020–2021 OT.02 subset to compare with WER3382;
- no sparse-point area weighting or profile assignment is attempted.

## 5. Acquisition evidence

Temporary branch-only workflow runs:

### Run `35078024672`

Purpose: acquire the exact 4TU file, checksum it, inspect schema and search provenance tokens.

Result: `SUCCESS`.

Key findings:

- exact file acquisition succeeded;
- 15,871 rows;
- no campaign/project token matches;
- broad text year probe was intentionally treated as provisional.

### Run `35078143439`

Purpose: exact `year`-column screen, canonical OT.02 spatial intersection and README/source-code review.

Result: `SUCCESS`.

Key findings:

- `year=2020/2021`: 0 records;
- OT.02 intersection: 0 records;
- WER3382 / RAAK provenance: not established;
- README confirms BIS PFB/BPK-style source semantics and EPSG:28992 coordinate meaning.

The temporary workflow is not canonical evidence by itself and must be removed before final admission of this route-review decision.

## 6. Scientific classification

The BIS-4D public point archive is classified as:

`REVIEWED_PUBLIC_ALTERNATIVE_NO_OT02_CURRENT_STATE_RECOVERY`

This is a **negative route result**, not evidence that no bulk-density observations have ever been collected in Tollebeek.

It establishes only that this specific public BIS bulk-density release does not recover the required OT.02 / WER3382 campaign records.

## 7. Consequence for CURRENT-state gate

`DR_SM_CURRENT_STATE` remains `PARTIAL_EVIDENCE`.

The primary unresolved acquisition route remains the raw georeferenced dataset underlying WER Rapport 3382 / Flevo-land-in-beweging, or another independently qualified direct observation dataset with source-native coordinates, dates, depth semantics, measurement method and QC that intersects OT.02.

No BIS map, BIS field estimate, modal SoilPhys property or spatial prediction may be substituted for that missing evidence.

## 8. Temporal guardrail

Even if the 2020–2021 WER3382 measurements are acquired later, they represent a dated 2020–2021 measured state. They are not automatically:

- the actual October-1998 state;
- a 2026 current state;
- an areally complete OT.02 state.

Use outside the observation period requires an explicit temporal-transfer or scenario decision.

## 9. Verdict

`BIS_ROUTE_REVIEWED_NO_WER3382_OR_OT02_CURRENT_STATE_RECOVERY`

Next action: continue the direct WER3382/Flevo-land-in-beweging raw-data acquisition request rather than reopening BIS-4D as a substitute.
