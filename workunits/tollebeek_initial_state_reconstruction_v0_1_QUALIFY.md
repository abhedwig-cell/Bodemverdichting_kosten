# Tollebeek initial-state reconstruction v0.1 — QUALIFY checkpoint

Capability / readiness item: `DR_SM_INITIAL_STATE`

Phase: `QUALIFY`

Canonical start:

- `main`: `118a2a08a27a74a8eaf9e9c356d5dd39b0072eeb`
- branch: `work/tollebeek-initial-state-reconstruction-v0.1`
- clean pre-checkpoint head: `2e6e6062c6861614f21c7ffb71fb28c849660e6b`

## Qualified protocol decision

The initial-state admissibility ladder is:

- `I0 OBSERVED_INITIAL_STATE`
- `I1 CONSTRAINED_HISTORICAL_RECONSTRUCTION`
- `I2 ENVELOPE_INITIAL_STATE_SCENARIO`
- `I3 INADMISSIBLE_DEFAULT`

`DR_SM_INITIAL_STATE` remains `PARTIAL_EVIDENCE`.

No numerical groundwater level, pressure-head profile, soil-water profile, restart file or model run is admitted.

## Core attribution rule

CURRENT and REFERENCE must use equivalent initialization protocol semantics. Numerical equality of state variables is not required when hydraulic functions differ.

A shared qualified warm-up may legitimately produce different water-content/pressure-head profiles through the admitted soil-state contrast. Separate tuning or differing initialization rules between pair members is not allowed for simple soil-state attribution.

## Historical evidence boundaries retained

- the 144-hour KNMI event forcing is observed event context, not automatically a warm-up;
- owner narrative of very wet / saturated antecedent conditions is qualitative only;
- inside-OT.02 GLD evidence is deep-screen piezometric context, not direct phreatic/root-zone initial state;
- no qualifying shallow historical public GLD series inside OT.02 was found in the bounded search;
- nearby shallow outside-OT.02 series remain context only.

## I1 admission prerequisites

A future I1 warm-up/restart requires at minimum:

- explicit state variables and depth/unit semantics;
- independently sourced pre-event forcing;
- at least R1-qualified historical boundary semantics where relevant;
- sufficiently specified drainage and land-use semantics;
- pinned model executable/configuration authority;
- equivalent CURRENT/REFERENCE initialization protocol;
- explicit spin-up/convergence diagnostics;
- uncertainty/sensitivity for non-identifying evidence;
- no default filling of missing scientific inputs.

## I3 guardrails

The following remain inadmissible closure mechanisms:

- target peil as initial groundwater;
- shallow groundwater inferred directly from deep heads;
- whole-profile saturation from narrative wording;
- the 144-hour event window treated as sufficient warm-up by definition;
- arbitrary field-capacity / standard SWAP profile;
- arbitrary legacy restart;
- null to zero;
- separate CURRENT/REFERENCE tuning.

## Qualification evidence

Clean PR head `2e6e6062c6861614f21c7ffb71fb28c849660e6b`:

- CI run `35077119841`: `SUCCESS`
- compile project validation/workbook tools: PASS
- Status-A-light integrity gate: PASS
- full unit and contract tests: PASS

Diff boundary before this checkpoint:

- `docs/35_tollebeek_initial_state_reconstruction_protocol_v0_1.md`
- `workunits/tollebeek_initial_state_reconstruction_v0_1_RECONCILE.md`

No register, evidence verdict, readiness status, schema, model input, production implementation or output changed.

## Verdict

`QUALIFIED_INITIAL_STATE_RECONSTRUCTION_PROTOCOL_NO_NUMERICAL_STATE_ADMISSION`

Next permitted action:

Run exact-head CI on this persisted checkpoint. If green, merge this protocol only. Any later numerical I1/I2 state requires a separate bounded workunit and the dependencies specified by the protocol.
