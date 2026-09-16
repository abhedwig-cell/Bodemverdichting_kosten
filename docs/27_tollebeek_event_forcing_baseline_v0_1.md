# Tollebeek event forcing baseline v0.1

Status: **ADMISSION CANDIDATE — observed station forcing**

## Purpose

This baseline closes only `DR_SM_EVENT_FORCING` for the first bounded Tollebeek extreme-event experiment. It does not close the other run-control gates.

## Event selection

The selected event is the October 1998 Tollebeek water-overload event because it is directly tied to the managed water system under study. Owner documentation identifies the night of 27–28 October 1998 as the critical event, reports 87.5 mm within 24 hours at Marknesse, and describes days of antecedent rainfall and saturated conditions.

The canonical numerical forcing is not reconstructed from those narrative totals. It comes from official KNMI hourly observations at station 273 Marknesse.

## Canonical forcing context

- event ID: `EVT_TOL_1998_OCT`
- station: KNMI 273 Marknesse
- context: `1998-10-24T00:00:00Z` through `1998-10-30T00:00:00Z`
- resolution: 60 minutes
- records: 144 contiguous hourly intervals
- time standard: UTC/UT
- forcing dataset: `data/events/tollebeek_1998_marknesse_hourly.csv`
- forcing SHA-256: `6c4ca1277523af73f26f6340ec8ebce5d52f42b6040085f7d50ecc78c5ca3c8a`
- acquired KNMI raw-response SHA-256: `71f2b135769bfed476bbc9ee55282d7e5e9766e2eaf444aa1b8694d382d08dde`

The context deliberately includes three full antecedent days, the event itself and the immediate post-event period. It is a forcing context, not a hydrological warm-up and not an assumed initial state.

## Event core

The objective maximum rolling 24-hour rainfall window in the acquired series is:

- start: `1998-10-27T06:00:00Z`
- end: `1998-10-28T06:00:00Z`
- rainfall: **88.4 mm**

This strongly corroborates the independent owner report of 87.5 mm within 24 hours at Marknesse. The values are not forced to equality because the owner narrative does not specify the same exact UTC rolling interval.

Daily station rainfall in the lead-in was 14.0 mm on 24 October, 12.8 mm on 25 October and 9.1 mm on 26 October, followed by 43.6 mm on 27 October and 46.4 mm on 28 October. This supports the owner chronology of antecedent wetting, but does not itself define the soil-water initial state.

## Native source semantics

The canonical forcing file normalizes column names but preserves KNMI native values and native units. `precipitation_amount_0_1_mm = -1` retains the KNMI trace code meaning less than 0.05 mm. It is not missing and is not rewritten to a physical negative rainfall amount. Trace values may be interpreted as zero only in explicitly labelled derived rainfall sums. Source-missing fields remain blank/null.

Across the 144-hour context, wind direction/speed/gust, air temperature, dewpoint, sunshine duration, global radiation, precipitation duration/amount, visibility and relative humidity are complete. Station pressure, cloud/weather-code fields and several indicators are source-missing for this station/period and remain missing. `T10N` has its source-native sparse cadence and is not gap-filled.

## Spatial boundary

Station 273 is an observed point forcing baseline and is not asserted to equal the spatial rainfall field over every OT.02 source unit. No radar blend, areal correction or interpolation is introduced here.

## Model boundary

This baseline does **not** convert KNMI native units into SWAP input units, select a SWAP version or numerical configuration, define evapotranspiration preprocessing, define the initial groundwater or soil-water state, define managed boundary/control behaviour, fill drainage parameters, choose crop/land-use state or run CURRENT/REFERENCE simulations.

Those remain separate gates. The next direct dependency is `DR_SM_INITIAL_STATE`, followed in parallel by managed-boundary and model-configuration qualification.
