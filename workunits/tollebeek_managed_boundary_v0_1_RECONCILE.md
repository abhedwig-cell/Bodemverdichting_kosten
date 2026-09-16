# Tollebeek managed boundary v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Capability: `DR_SM_MANAGED_BOUNDARY`
Protocol phase: RECONCILE

## Canonical authority

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- canonical branch: `main`
- canonical start: `d43032e16b66e5255187baf7df554f5d2b4dc00d`
- fixed event: `EVT_TOL_1998_OCT`
- current readiness at start: `DR_SM_MANAGED_BOUNDARY = PARTIAL_EVIDENCE`
- admitted event forcing: 1998-10-24T00:00Z through 1998-10-30T00:00Z

No materially equivalent open managed-boundary branch or PR was found before branch creation.

## Critical historical-system distinction

The current admitted OT.02 polygon is a present-day peilgebied identity and must not be interpreted as the operational 1998 boundary system.

Official near-period documentation shows that the historical Tollebeek underbemaling consisted of separate peilgebieden/gemalen including:

- OT.02 / De Rietgors;
- OT.03 / De Fuut;
- OT.04 / De Kievit.

The later joining of these areas, the new connecting watercourse and gemaal IJsvogel are post-1998 interventions. They are not valid historical event controls unless a separate equivalence mapping is explicitly qualified.

## Existing evidence

- nominal underbemaling target around NAP -6.20 m is documented for the historical Tollebeek system;
- near-period official documentation records the separate old pumping stations and their capacities and describes normal control/inlet arrangements;
- owner retrospective material records that the 1998 system was overwhelmed, emergency pumps were deployed and major structural/control changes followed the event;
- no canonical project evidence currently provides an hourly/subdaily 1998 surface-water level, pump-status/discharge series, emergency-pump schedule, stuw operation series or downstream Urkervaart boundary time series.

## Scientific boundary

A nominal target level is not the same as the actual event water level. Pump nameplate capacity is not the same as realized time-varying discharge. Current wet-weather operating policy is not assumed to describe 1998 operations.

The paired CURRENT/REFERENCE source-model runs must receive identical or explicitly equivalent managed-boundary semantics, but that equality rule does not justify inventing the boundary itself.

## Acquisition questions

Seek, in order:

1. owner/archive water-level observations for De Rietgors, De Fuut, De Kievit and/or directly connected tochten during 1998-10-24 through 1998-10-30;
2. Urkervaart water levels over the same window;
3. pump on/off, run-time or discharge records for the historical underbemaling pumps;
4. emergency-pump location, timing and capacity records from the 1998 response;
5. stuw/inlaat operational records or a documented event-control rule applicable to 1998.

If direct time series are unavailable, a reconstruction protocol may be reviewed only if it preserves historical system topology, nominal target levels, pump capacities, downstream state and emergency interventions with explicit uncertainty and provenance.

## Current verdict

`RECONCILED_MANAGED_BOUNDARY_GATE_OPEN`

No event-specific managed-boundary series or model mapping is admitted at this checkpoint.

## Explicit exclusions

- no current IJsvogel configuration as a 1998 substitute;
- no current merged OT.02 control topology as a silent 1998 substitute;
- no NAP -6.20 constant boundary merely because it is the nominal target;
- no target peil → groundwater head conversion;
- no nameplate capacity → realized event discharge conversion;
- no modern pre-bemaling/wet-scenario policy backcast to 1998 without evidence;
- no SWAP boundary option or numerical model configuration selected here;
- no missing → zero.
