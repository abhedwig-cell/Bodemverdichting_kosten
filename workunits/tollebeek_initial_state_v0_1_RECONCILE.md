# Tollebeek initial state v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Capability: `DR_SM_INITIAL_STATE`
Protocol phase: RECONCILE

## Canonical authority

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- canonical branch: `main`
- canonical start: `96e0043196f1bacf7274e6071e46d9552421dd6c`
- fixed event: `EVT_TOL_1998_OCT`
- admitted forcing context: `1998-10-24T00:00:00Z` through `1998-10-30T00:00:00Z`
- event core: `1998-10-27T06:00:00Z` through `1998-10-28T06:00:00Z`
- current readiness at start: `DR_SM_INITIAL_STATE = MISSING`

No materially equivalent open initial-state PR/workunit was found before branch creation.

## Required scientific object

The gate requires either:

1. an observed or otherwise independently qualified event-specific hydrological state at the model start, expressed at the variables/grain required by the eventual source model; or
2. a reproducible warm-up/restart protocol that produces the state without convenience defaults and is applied identically/equivalently to the matched CURRENT and REFERENCE runs.

For SWAP, documented initialization routes include a depth-resolved pressure-head profile, hydrostatic equilibrium from an initial groundwater level, or restart from a previous SWAP state. Availability of an option is not evidence that any specific option/value is valid for Tollebeek in October 1998.

## Existing evidence and boundary

- The admitted KNMI forcing window provides antecedent meteorological forcing but **does not** define soil-water pressure heads, water contents or groundwater level.
- Waterschap Zuiderzeeland historical context states that it had rained for days and that the soil was fully saturated before the extreme 27–28 October 1998 rainfall. This supports a qualitative very-wet antecedent-state interpretation only; it does not provide a numerical groundwater level or depth-resolved state.
- The OT.02 target surface-water level is managed-boundary context, not an initial groundwater profile.
- The current drainage configuration remains data-gated, so no equilibrium depth may be inferred from drain geometry or resistance.
- Current/reference soil-state admission is separately data-gated; initial hydrological state must not be used to smuggle in missing compaction-state values.

## Acquisition routes to test

A. Historical observed groundwater route
- identify DINO/BRO or owner groundwater-monitoring wells in/near admitted OT.02;
- require stable well/tube identity, coordinates/CRS, screen metadata, measurement datum and a dated observation sufficiently close to 1998-10-24;
- spatially reconcile any candidate observation with OT.02 before project use.

B. Historical owner water-level/field-observation route
- search owner archives/reporting for event-period groundwater or local water-level observations with explicit time/datum semantics;
- surface-water level is not interchangeable with groundwater level.

C. Reproducible warm-up/restart route
- consider only after the model implementation/configuration and required boundary/drainage/land-use inputs for the warm-up period are explicitly available;
- no arbitrary hydrostatic groundwater level, field capacity profile or fixed saturation profile may be introduced merely to start a run.

## Current verdict

`RECONCILED_INITIAL_STATE_GATE_OPEN`

No initial hydrological state is admitted at this checkpoint.

## Next permitted action

Attempt routes A and B first. If no event-specific observation can be resolved, classify the evidence gap explicitly and define the minimum contract for a later warm-up/restart qualification. Do not set `DR_SM_INITIAL_STATE` to `ADMITTED` without a concrete qualified state or reproducible qualified initialization protocol.

## Explicit exclusions

- no inference of groundwater level from OT.02 target peil;
- no use of antecedent rainfall totals as soil-water state;
- no `fully saturated` → numerical pressure-head conversion;
- no field-capacity convenience default;
- no missing → zero;
- no drainage/current-state/model-config admission;
- no source-model run.