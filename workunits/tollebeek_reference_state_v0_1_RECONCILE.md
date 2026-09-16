# Tollebeek reference-state v0.1 — RECONCILE checkpoint

Capability / readiness item: `DR_SM_REFERENCE_STATE`

Protocol: `RECONCILE → DESIGN → QUALIFY → CLOSE`

Canonical start:

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- `main`: `4b69e4090607e7d412b802c2bd2d485d7dc7dbee`
- source branch: `work/tollebeek-reference-state-v0.1`

## Reconciled status

- `DR_SM_REFERENCE_STATE = PARTIAL_EVIDENCE`
- route classification: `DEPENDENT_INTERNAL_DECISION`
- `DR_SM_CURRENT_STATE = PARTIAL_EVIDENCE`
- no Tollebeek-specific reference state is admitted.

Relevant canonical principles already qualified:

- reference is contextual and is not synonymous with pristine soil, zero traffic or a universal optimum;
- CURRENT/REFERENCE attribution requires matched forcing, crop, geometry and boundary/system context;
- modal SoilPhys bulk density is profile context, not CURRENT state;
- the initial-state protocol requires equivalent initialization semantics across the pair;
- scenario/reconstruction governance separates historical attribution (Track H) from `SCENARIO_ONLY` analysis (Track S).

## Core scientific issue

A reference cannot be selected independently of:

1. the admitted/qualified CURRENT state;
2. the causal question;
3. temporal applicability;
4. the state-to-hydraulic-property mapping.

A future 2020–2021 measured CURRENT state paired with October-1998 forcing would be a controlled stress-test scenario unless a separate temporal-transfer argument supports historical use. Historical forcing must not silently backdate modern soil measurements.

## Planned reference ladder

- `RF0 OBSERVED_PAIRED_REFERENCE`
- `RF1 EVIDENCE_DERIVED_COUNTERFACTUAL`
- `RF2 REFERENCE_ENVELOPE_SCENARIO`
- `RF3 INADMISSIBLE_REFERENCE_DEFAULT`

## Fixed-versus-changed rule

For a simple soil-state attribution pair, external dimensions remain matched unless explicitly included in another research question:

- profile/spatial identity;
- layer geometry/intrinsic context;
- forcing;
- crop/land use;
- drainage;
- managed boundary;
- executable/numerical configuration;
- initialization protocol;
- output/accounting conventions.

Only admitted compaction-related state variables and traceably derived hydraulic properties form the intended contrast.

## Guardrails

This workunit must not:

- invent a numerical REFERENCE state;
- use SoilPhys modal density as reference by default;
- use BOFEK class as an observed uncompacted state;
- assume pristine soil or zero traffic;
- impose an arbitrary percentage bulk-density reduction;
- choose a reference to maximize model response;
- change crop/drainage/boundary/initialization together with soil state in a simple attribution claim;
- hide missing values or convert null to zero;
- admit hydraulic parameters without a traceable state-to-parameter relation;
- create or execute a model run.

## Intended output

Documentation/governance only:

- one counterfactual/reference construction protocol;
- this resumable checkpoint;
- no readiness/evidence/schema/state/model-output mutation.

## Current verdict

`RECONCILED_FOR_REFERENCE_PROTOCOL_DESIGN`

Next permitted action:

`DESIGN → QUALIFY` the RF0/RF1/RF2/RF3 construction protocol while preserving `DR_SM_REFERENCE_STATE = PARTIAL_EVIDENCE`.
