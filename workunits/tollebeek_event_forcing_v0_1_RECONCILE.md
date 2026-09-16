# Tollebeek event forcing v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Capability: `DR_SM_EVENT_FORCING`
Protocol: RECONCILE → ACQUIRE → CLASSIFY → QUALIFY → ADMIT → CLOSE

## Canonical start

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- branch: `main`
- canonical head: `c5943df2a5e0dc340690ea748c72202955b83016`
- no open pull requests at reconcile time
- no pre-existing event-forcing work branch found in the current branch inventory

## Current canonical state

`DR_SM_EVENT_FORCING` is `PARTIAL_EVIDENCE`.

Current method evidence:
- `EV_GROEN_HOURLY_FORCING`
- `CL_THEORY_TEMPORAL_FORCING`

Current blocker:
- no concrete Tollebeek event series is admitted;
- hourly/sub-daily forcing is a baseline requirement, not an assertion that hourly resolution is universally sufficient.

## Event candidate identified for acquisition

The October 1998 Tollebeek water-overload event is the primary candidate because it is directly tied to the project water system rather than being chosen from a generic wet-day ranking.

Public owner/historical evidence reviewed before acquisition states:
- extreme rainfall caused water overload in Tollebeek in the night of 27–28 October 1998;
- Waterschap Zuiderzeeland reports 87.5 mm within 24 hours at Marknesse;
- owner historical material reports days of antecedent rainfall and about 75 mm in the night of 27–28 October;
- KNMI station 273 Marknesse has hourly observations covering 1998 and provides precipitation plus meteorological variables including temperature, radiation, humidity and wind.

The exact event/simulation window is not admitted from narrative text. It must be reconstructed from the hourly observations and source chronology.

## Reconcile verdict

`PROCEED_EVENT_FORCING_ACQUISITION`

## Required acquisition/qualification boundary

Before `DR_SM_EVENT_FORCING` may become `ADMITTED`:

1. obtain a reproducible KNMI station-273 hourly series spanning the antecedent wet period, main event and immediate recovery;
2. preserve KNMI-native timestamps and explicitly document that KNMI climatological hour data use UT/UTC conventions;
3. preserve native units and trace-level/missing-value semantics before any model conversion;
4. objectively identify the event core from the observations, with narrative sources used as chronology corroboration rather than to manufacture timestamps;
5. record source/retrieval metadata, variables, completeness/QC and checksum;
6. keep meteorological-source admission separate from later SWAP-specific variable mapping and interpolation to Tollebeek source-model units.

## Explicit exclusions

- no precipitation value inferred from prose when hourly observations are available;
- no use of 87.5 mm as a synthetic hourly distribution;
- no missing-to-zero substitution;
- no station-to-field spatial correction or radar blending without separate qualification;
- no current/reference soil-state construction;
- no drainage parameter construction;
- no initial hydrological-state default;
- no managed-boundary default;
- no crop/land-use default;
- no SWAP version/model configuration selection in this phase;
- no source-model run.
