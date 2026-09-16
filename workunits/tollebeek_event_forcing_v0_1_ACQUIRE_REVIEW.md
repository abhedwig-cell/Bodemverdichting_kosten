# Tollebeek event forcing v0.1 — ACQUIRE / REVIEW checkpoint

Date: 2026-09-16
Capability: `DR_SM_EVENT_FORCING`

## Acquisition

Official KNMI hourly climatology data were requested for station 273 Marknesse around the October 1998 Tollebeek event.

Initial probe run `35068407343` failed before scientific processing because the temporary parser incorrectly required at least 27 columns while the KNMI `ALL` response contained the documented 25 native fields. No scientific data or decision was modified to obtain a pass.

The parser row-width check was corrected only. Probe run `35068470628` then succeeded.

Successful acquisition evidence:
- raw KNMI response SHA-256: `71f2b135769bfed476bbc9ee55282d7e5e9766e2eaf444aa1b8694d382d08dde`;
- 216 station-273 hourly records returned by the deliberately wide acquisition request;
- no missing `RH` values in that acquisition window;
- acquisition artifact ID `10435371800`;
- artifact zip SHA-256 `75c3421f8528ead05f04ce874e41e2a466b53bcc91644cf748ecc7d58e1509a9`.

The service end-parameter yielded data through `1998-11-02T00:00Z`; canonical time bounds are therefore defined from observation timestamps rather than inferred from the request label.

## Review and canonical subset

Canonical forcing context:
- `1998-10-24T00:00Z` through `1998-10-30T00:00Z`;
- 144 contiguous hourly records;
- station 273 only;
- normalized column names with source-native values/units retained;
- canonical forcing SHA-256 `6c4ca1277523af73f26f6340ec8ebce5d52f42b6040085f7d50ecc78c5ca3c8a`.

Objective maximum rolling 24-hour rainfall:
- `1998-10-27T06:00Z` through `1998-10-28T06:00Z`;
- 88.4 mm.

Independent owner context:
- 87.5 mm within 24 hours reported at Marknesse;
- days of antecedent rain and saturated ground described before the night 27–28 October event.

The owner magnitude and KNMI rolling maximum are treated as corroborating, not mathematically identical records.

## Completeness review

Complete across all 144 context hours: wind direction, wind speed/gust, air temperature, dewpoint, sunshine duration, global radiation, precipitation duration/amount, visibility and relative humidity.

Source-missing and retained as missing: sea-level pressure, cloud cover, present-weather/weather-station codes and M/R/S/O/Y indicators. `T10N` is source-sparse and is not filled.

## Verdict

`ADMIT_STATION_EVENT_FORCING_BASELINE`

This verdict is limited to an observed station-based forcing baseline. It does not qualify spatial representativeness, model-specific conversion, initial hydrological state or a SWAP run.
