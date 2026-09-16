# Tollebeek antecedent forcing review v0.1

Status: **QUALIFICATION CANDIDATE — source forcing only**

Dependency: `DR_SM_INITIAL_STATE`
Event: `EVT_TOL_1998_OCT`

## Purpose

Review whether official KNMI station-273 observations can provide a reproducible pre-event meteorological forcing basis for a future I1 warm-up/restart reconstruction.

This review does **not** create or admit an initial hydrological state and does not assert that one year is a sufficient spin-up period.

## Acquisition window

Official KNMI hourly climatology observations were acquired for station 273 Marknesse using `vars=ALL` and a deliberately wider source request. The reviewed target interval is exactly:

- start: `1997-10-24T00:00:00Z`;
- end exclusive: `1998-10-24T00:00:00Z`;
- expected hours: 8760.

Probe run `35093815232` returned:

- exactly 8760 target rows;
- zero duplicate timestamps;
- zero missing hourly timestamps;
- raw response SHA-256 `aac1c6082105e685d594aae518e2dcfe080513e4485b546e177499005b74f52b`;
- normalized candidate SHA-256 `5ed2c604f6cce2c09c7379eeb3f745fed6b4f46a4778bb6c0fbb20098ada0272`;
- normalized candidate size 1,112,539 bytes.

A separately acquired 24-hour boundary sample for `1998-10-24` was compared with the already admitted event-forcing dataset. All compared native forcing values matched exactly: boundary mismatch count = 0.

This confirms source continuity with the admitted event-forcing authority without changing or extending that authority.

## Native missingness

Across the one-year target interval:

- `DD`, `FH`, `FF`, `FX`, `T`, `TD`, `SQ`, `Q`, `VV`, `U`: 0 source-missing hours;
- `T10N`: 7300 missing hours, consistent with its source-sparse cadence and not filled;
- `P`, `N`, `WW`, `IX`, `M`, `R`, `S`, `O`, `Y`: unavailable for all 8760 hours at station 273 in this historical period and retained missing;
- `DR`: 108 source-missing hours;
- `RH`: 108 source-missing hours;
- `RH=-1` occurs 578 times and retains the KNMI trace meaning `<0.05 mm`, not missing and not physical negative rainfall.

The precipitation missingness is scientifically material for a hydrological warm-up.

## Precipitation-gap diagnosis

Probe run `35093938445` isolated all 108 missing `DR`/`RH` hours to one contiguous block:

- start: `1998-09-03T00:00:00Z`;
- end exclusive: `1998-09-07T12:00:00Z`;
- duration: 108 hours.

The same diagnostic requested KNMI precipitation for station 269 Lelystad Airport:

- both station 273 and station 269 contain all 8760 hourly timestamps over the reviewed year;
- station 269 has zero missing `RH` hours;
- station 269 has an available `RH` value for each of the 108 hours missing at station 273.

KNMI source-header metadata in the diagnostic response identify:

- station 273 Marknesse: longitude 5.888, latitude 52.703, elevation -3.30 m;
- station 269 Lelystad Airport: longitude 5.520, latitude 52.458, elevation -3.70 m.

Station 269 availability is **diagnostic only**. This review does not authorize replacing station-273 values with station-269 values.

## Classification

The station-273 one-year record is classified as:

`QUALIFIED_ANTECEDENT_FORCING_SOURCE_WITH_PRECIPITATION_GAP`

It is suitable as a reproducible source basis for subsequent reconstruction design, but it is not a complete run-ready meteorological forcing because the 108-hour precipitation gap remains unresolved.

## Guardrails

The following are not admitted:

- filling the 108 hours with zero rainfall;
- linear interpolation of hourly rainfall;
- copying station 269 values without a separately qualified cross-station gap-fill rule;
- treating trace value `RH=-1` as missing or negative rainfall;
- calling the one-year period a sufficient hydrological warm-up merely because it spans 8760 hours;
- changing the already admitted 144-hour event forcing baseline;
- creating an initial state, restart or SWAP run.

## Next permitted action

A separate bounded workunit may evaluate a precipitation-gap treatment, including whether a station-269 substitution or another observed precipitation source is scientifically defensible. Such a workunit must quantify the implications of source mixing and preserve provenance at every filled hour.

Even after precipitation continuity is resolved, I1 warm-up admission remains dependent on the managed-boundary, drainage, land-use and concrete model-configuration semantics required by the initial-state reconstruction protocol.