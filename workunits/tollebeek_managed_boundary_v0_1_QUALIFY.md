# Tollebeek managed boundary v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Capability: `DR_SM_MANAGED_BOUNDARY`
Protocol phase: QUALIFY

## Authority

- canonical start: `d43032e16b66e5255187baf7df554f5d2b4dc00d`
- branch: `work/tollebeek-managed-boundary-v0.1`
- clean pre-checkpoint head: `8bebb38194437188acb4da19ba5a97b062439565`
- PR: `#25`

## Qualified historical boundary route

- official near-period system evidence distinguishes De Rietgors (OT02), De Fuut (OT03) and De Kievit (OT04), all with nominal streefpeil NAP -6.20 m;
- listed near-period nominal pump capacities are 2.600, 0.670 and 1.000 m3/s, with direct discharge to the Urkervaart;
- target and actual water level are explicitly distinct, and larger deviations can occur during persistent heavy rainfall;
- owner retrospective evidence establishes that the modern connecting watercourse and IJsvogel are post-1998 changes and cannot be backcast silently;
- owner 1998 crisis context establishes material emergency intervention but does not provide a numerical control schedule;
- the owner water-information route is qualified for acquisition of missing historical levels and control records.

## Readiness decision

`DR_SM_MANAGED_BOUNDARY = PARTIAL_EVIDENCE`.

No event-specific surface-water-level series, Urkervaart level series, realized pump-discharge series, stuw/inlaat schedule, emergency-pump series or source-model boundary option is admitted.

## Guardrails

Rejected transformations include:

- current IJsvogel/current merged OT.02 controls → 1998 boundary;
- NAP -6.20 streefpeil → actual event hydrograph or groundwater head;
- nominal/nameplate pump capacity → realized event discharge;
- modern wet-weather policy → historical 1998 control rule;
- current OT.02 polygon → single uniform 1998 control domain without historical mapping;
- missing dynamic controls → zero or convenience defaults.

Once qualified in a future workunit, managed-boundary semantics must be identical or explicitly equivalent across matched CURRENT and REFERENCE source-model runs.

## Qualification evidence

- temporary finalizer run `35072948882`: generated postimage PASS, central Status-A-light project gate PASS, full unit/contract suite PASS, non-workflow postimage persisted;
- clean-head PR CI run `35073055337`: compile PASS, Status-A-light integrity gate PASS, unit/contract tests PASS;
- final diff contains no temporary finalizer and no managed-boundary dataset.

## Verdict

`QUALIFIED_MANAGED_BOUNDARY_HISTORICAL_ROUTE_NO_ADMIT_BOUNDARY`

## Next permitted action

Only exact-head CI verification, merge/admission of this route/no-admit decision, and CLOSE are permitted in this workunit. A numerical/event boundary requires new historical owner evidence or a separately qualified reconstruction protocol and model mapping.
