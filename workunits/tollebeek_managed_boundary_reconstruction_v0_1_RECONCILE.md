# Tollebeek managed-boundary reconstruction v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Capability: `DR_SM_MANAGED_BOUNDARY`
Protocol phase: RECONCILE / DESIGN

## Canonical authority

- canonical start: `main` @ `a8b62c423391bf13ff8e638a749d70f4c9ab6944`
- branch: `work/tollebeek-managed-boundary-reconstruction-v0.1`
- event: `EVT_TOL_1998_OCT`
- inherited status: `DR_SM_MANAGED_BOUNDARY = PARTIAL_EVIDENCE`
- inherited decision-surface classification: `RECONSTRUCTABLE_WITH_EXPLICIT_UNCERTAINTY`

## Qualified evidence already available

The canonical evidence base currently establishes:

1. `EV_TOL_BOUNDARY_HISTORICAL_SYSTEM`
   - near-period official pre-merger system with separate OT02 De Rietgors, OT03 De Fuut and OT04 De Kievit;
   - all with target level NAP -6.20 m;
   - listed nominal pump capacities 2.600, 0.670 and 1.000 m3/s;
   - all pump directly to the Urkervaart;
   - actual water level is documented as fluctuating around target and may rise by more than 0.20 m during heavy persistent rain.

2. `EV_TOL_BOUNDARY_POST1998_REDESIGN`
   - multiple stuwen were added after the 1998 event;
   - connecting watercourse in 2010;
   - larger culverts/embankments in 2011-2012;
   - IJsvogel opened in 2012;
   - therefore current merged OT.02/IJsvogel operation is excluded as a silent 1998 substitute.

3. `EV_TOL_BOUNDARY_1998_CRISIS`
   - days of rain and saturated ground;
   - crisis response on 27-28 October 1998;
   - large emergency pumps and about twenty smaller fire-brigade pumps deployed;
   - no exact locations, start/stop times, discharge hydrographs or level series are available in the admitted narrative evidence.

4. `EV_TOL_BOUNDARY_OWNER_ARCHIVE_ROUTE`
   - a qualified Waterschap Zuiderzeeland route exists for requesting historical levels, pump logs/runtime/discharge, stuw/inlaat operation and related archival evidence.

5. `EV_TOL_TARGET_LEVEL`
   - NAP -6.20 m is qualified as target-level context only;
   - it is not an event hydrograph, groundwater head or initial state.

## Problem definition

The project needs a managed-boundary representation shared by the matched CURRENT and REFERENCE source-model runs.

Direct 1998 telemetry would be the strongest evidence. If it remains unavailable, the project may consider a bounded historical reconstruction, but only if the reconstruction preserves:

- 1998 historical topology;
- distinction between target level and actual level;
- distinction between nominal capacity and realized discharge;
- explicit emergency intervention;
- non-identifiability and uncertainty;
- identical/equivalent boundary semantics across the CURRENT/REFERENCE pair.

## No-admission boundary

This workunit designs the reconstruction protocol only.

It does not:

- choose a numerical 1998 surface-water-level series;
- infer pump runtime or discharge;
- assign emergency-pump capacities/timing;
- treat 2006 nominal capacities as proven exact 1998 capacities;
- use IJsvogel or current merged OT.02 controls;
- change `DR_SM_MANAGED_BOUNDARY` from `PARTIAL_EVIDENCE`;
- create a runnable SWAP boundary file or model run.

## Next permitted action

Define a tiered reconstruction admissibility protocol with:

- evidence tiers;
- required variables and constraint types;
- identifiability rules;
- uncertainty representation;
- acceptance tests;
- explicit claim labels;
- stop conditions that keep the boundary data-gated when the historical system is underconstrained.