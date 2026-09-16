# Tollebeek initial-state reconstruction v0.1 — RECONCILE checkpoint

Capability / readiness item: `DR_SM_INITIAL_STATE`

Protocol: `RECONCILE → DESIGN → QUALIFY → CLOSE`

Canonical start:

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- branch: `main`
- canonical start head: `118a2a08a27a74a8eaf9e9c356d5dd39b0072eeb`
- source branch: `work/tollebeek-initial-state-reconstruction-v0.1`

## Reconciled dependencies

Already admitted / qualified context:

- `DR_SM_GEOMETRY = ADMITTED`
- `DR_SM_PROFILE = ADMITTED`
- `DR_SM_EVENT_FORCING = ADMITTED`
- `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE`
- `DR_SM_MANAGED_BOUNDARY = PARTIAL_EVIDENCE`
- `DR_SM_DRAINAGE = PARTIAL_EVIDENCE`
- `DR_SM_LAND_USE = PARTIAL_EVIDENCE`
- `DR_SM_MODEL_CONFIG = PARTIAL_EVIDENCE`
- `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`
- `DR_SM_REFERENCE_STATE = PARTIAL_EVIDENCE`

Scenario/reconstruction classification authority:

- `DR_SM_INITIAL_STATE = RECONSTRUCTABLE_WITH_EXPLICIT_UNCERTAINTY`
- managed-boundary reconstruction protocol R0/R1/R2/R3 is canonical before this workunit.

## Existing evidence reused

- `EV_TOL_1998_ANTECEDENT`: owner narrative of days of rain / fully saturated ground; qualitative constraint only.
- `EV_TOL_1998_KNMI_FORCING`: 144-hour admitted observed event-forcing context; explicitly not a warm-up.
- `EV_TOL_INITIAL_DEEP_GLD`: two inside-OT.02 deep-screen series; hydrogeological context only.
- `EV_TOL_INITIAL_SHALLOW_SEARCH`: zero qualifying shallow historical series inside OT.02 in the bounded public BRO search.
- `EV_TOL_INITIAL_SHALLOW_NEARBY_CONTEXT`: nearby outside-OT.02 shallow series; context only.
- qualified managed-boundary historical topology and reconstruction protocol.

No evidence is reclassified or promoted by this workunit.

## Scientific issue

A matched CURRENT/REFERENCE pair requires equivalent initialization semantics, but hydraulic state variables cannot be assumed numerically identical when soil hydraulic functions differ.

This workunit therefore distinguishes:

- identical numerical initial values;
- physically equivalent initial-condition semantics;
- shared warm-up/restart protocol;
- scenario envelopes.

For the intended simple soil-state attribution, equivalent protocol semantics are required. A common warm-up may legitimately yield different final water contents/pressure heads if those differences arise solely from the admitted soil-state contrast.

## Planned decision ladder

- `I0 OBSERVED_INITIAL_STATE`
- `I1 CONSTRAINED_HISTORICAL_RECONSTRUCTION`
- `I2 ENVELOPE_INITIAL_STATE_SCENARIO`
- `I3 INADMISSIBLE_DEFAULT`

## Guardrails

This workunit must not:

- create a numerical initial groundwater level;
- create a pressure-head or water-content profile;
- create a restart file;
- call target peil an initial groundwater condition;
- infer shallow groundwater directly from deep piezometric heads;
- set the whole profile to saturation from narrative wording;
- call the 144-hour event window a warm-up;
- use arbitrary field-capacity / SWAP defaults;
- fill missing variables with zero;
- tune CURRENT and REFERENCE initial states separately for fit;
- create or execute a model run.

## Intended output

Documentation/governance only:

- one explicit reconstruction/admissibility protocol;
- this resumable checkpoint;
- no readiness/evidence/schema/data/model-output mutation.

## Current verdict

`RECONCILED_FOR_PROTOCOL_DESIGN`

Next permitted action:

`DESIGN → QUALIFY` the initial-state reconstruction protocol, while preserving `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE` and admitting no numerical initial state.
