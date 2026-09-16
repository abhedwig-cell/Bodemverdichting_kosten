# Tollebeek profile v0.1 — ACQUIRE / CLASSIFY checkpoint

Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → ADMIT → CLOSE

## Starting authority

- canonical start: `main` @ `5bd29b31745e093e82b63cc18e46f3a251b1695d`
- branch: `work/tollebeek-profile-v0.1`
- governing readiness item: `DR_SM_PROFILE`
- admitted sampling domain: `TOLLEBEEK_OT02_CURRENT`

## ACQUIRE

### SoilPhys discovery

Temporary branch-only GitHub Actions queried the WUR Soil Physical Data coordinate service at deterministic points inside the admitted OT.02 polygon.

Discovery run `35063298744`: `SUCCESS`.

The first six points already demonstrated material profile heterogeneity and returned at least `Mn15A`, `Mn15Av` and `Mv51A`, plus one no-data location.

### Shifted-grid screening

The acquisition was then expanded to two deterministic 500 m grids:

- Grid A: zero offset, 59 points inside polygon;
- Grid B: 250 m / 250 m offset, 58 points inside polygon.

Screening run `35063380870`: `SUCCESS`.

Combined result:

- 117 sampling points;
- 113 points with a SoilPhys profile;
- 4 no-data points (3.42%);
- 8 distinct SoilPhys source-profile IDs.

Detected profiles and combined valid-point screening fractions:

- `90115240` / `Mn15A`: 61.95%;
- `15100` / `Mv51A`: 12.39%;
- `15250` / `Mn15Av`: 11.50%;
- `90115270` / `Mn25A`: 4.42%;
- `11020` / `Zn10A`: 3.54%;
- `12010` / `Sn13A`: 2.65%;
- `11021` / `Zn10Av`: 2.65%;
- `90111050` / `Zn50A`: 0.88%.

The largest absolute A/B difference in fraction of all grid points is about 4.94 percentage points (`Mn15Av`); `Mn15A` differs by about 4.44 percentage points. Major composition is therefore reasonably stable for a bounded profile-screening basis, while the fractions remain too coarse to call exact areal weights.

### BOFEK2020 crosswalk

The current official WUR BOFEK2020 translation workbook was acquired successfully from `backend.wur.nl` and maps all eight detected SoilPhys profile IDs:

- `11021` / `Zn10Av` → BOFEK2020 `3001`, dominant;
- `12010` / `Sn13A` → `3004`;
- `11020` / `Zn10A` → `3005`;
- `90111050` / `Zn50A` → `3015`;
- `15250` / `Mn15Av` → `4004`;
- `15100` / `Mv51A` → `4006`, dominant;
- `90115270` / `Mn25A` → `4018`, dominant;
- `90115240` / `Mn15A` → `4019`, dominant.

The mapping is keyed by source profile ID, not by soil-code string alone, because the same soil-code label can occur for more than one standard profile.

### BOFEK spatial-overlay attempt

A direct download attempt against the historical WUR BOFEK GIS URL returned HTTP 404 in run `35063588465`.

This is a source-route staleness / execution finding, not evidence that BOFEK2020 spatial data do not exist. The current WUR product page routes the map through the interactive `bodemdata.nl` application and continues to describe BOFEK2020 as a 79-unit vector product at application scale 1:50,000–1:1,000,000.

The failed old download route is not used to infer absence or zero coverage and is not required to force an exact-area claim.

## CLASSIFY

The eight detected profiles are retained as the complete bounded OT.02 **profile-context screening basis**. No arbitrary reduction to one or a few profiles is made.

Canonical persistence includes:

- stable canonical `soil_profile_id` per SoilPhys source-profile ID;
- source soil-code and BOFEK2020 crosswalk;
- all source horizons through 120 cm;
- texture, SOM and Staring-series building-block information;
- SoilPhys modal bulk density under a dedicated `modal_bulk_density_g_cm3` field on `soil_layer`.

Strict semantic separation:

- `modal_bulk_density_g_cm3` is derived/modal profile context;
- `bulk_density_g_cm3` remains a `soil_state` field;
- no SoilPhys density is admitted as measured CURRENT anthropogenic compaction;
- no REFERENCE state is constructed here.

Screening fractions are admitted only as diagnostics of the bounded grid screening. They are not exact profile-area fractions and must not be multiplied by OT.02 system area as if they were exact areal weights.

## CLASSIFY verdict

`ADMIT_PROFILE_CONTEXT_BASIS`, subject to project/evidence/readiness/contract qualification.

This verdict is limited to profile identity, depth-resolved modal profile context and BOFEK crosswalk. It does not admit current/reference state, affected compaction area or source-model weighting.

Next permitted phase: `QUALIFY` after canonical evidence/readiness wiring and validator integration.
