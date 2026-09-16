# Tollebeek P1 readiness v0.2 — RECONCILE checkpoint

Capability: `CAP_TOLLEBEEK_P1_READINESS_V0_2`

Phase: `RECONCILE`

Date: 2026-09-16

## Canonical state

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- canonical `main`: `cac711c05ef340a2f6369717892805445c11af1a`
- preceding post-merge CI: `35110961136` — `SUCCESS`
- open pull requests at reconcile: none
- relevant predecessor: PR #49, `CLOSED_ANTECEDENT_GAP_RECONSTRUCTION_PACKAGE_QUALIFIED_SCENARIO_ONLY_NOT_RUN_READY`

## Relevant state delta only

The only readiness-relevant delta since the v0.1 P1 baseline is the admitted repository presence of the trace-aware antecedent precipitation-gap reconstruction package.

Qualified package properties inherited from PR #49:

- 108 source-missing station-273 antecedent precipitation hours have reproducible `SCENARIO_ONLY` reconstruction members;
- source-native KNMI snapshots and receipt are persisted;
- trace semantics remain explicit;
- candidate members preserve uncertainty and are not historical observations;
- `run_authorized=false`;
- no historical warm-up, restart or numerical initial state was admitted;
- `DR_SM_INITIAL_STATE` remained `PARTIAL_EVIDENCE`.

No new evidence or semantic mutation has occurred for CURRENT state, REFERENCE state, drainage, managed boundary, land use, hydraulic numerical parameterization or runnable model configuration.

## Reconciled readiness consequence

The antecedent package advances one forcing subdependency for future scenario/reconstruction work, but it does not change the P1 role counts:

- `ADMITTED=3`
- `PARTIAL_EVIDENCE=7`
- `MISSING=0`

In particular, it does not satisfy the minimum I1 warm-up contract because managed-boundary, drainage, land-use and runnable configuration dependencies remain unresolved, and warm-up adequacy has not been demonstrated.

## Next permitted action

Prepare a bounded P1 readiness delta v0.2 that:

1. records the antecedent precipitation package as qualified `SCENARIO_ONLY` supporting material;
2. leaves all ten role statuses scientifically unchanged;
3. distinguishes reduced acquisition uncertainty from actual input admission;
4. preserves the external-data blockers and dependency order;
5. explicitly prohibits a SWAP run or numerical initial-state construction from this delta alone.

## Exclusions

- no new source acquisition;
- no numerical boundary reconstruction;
- no numerical initial-state envelope;
- no hydraulic-parameter dataset;
- no model configuration;
- no SWAP execution;
- no readiness promotion by default, convenience value or inferred historical truth.

Verdict: `RECONCILED_P1_READINESS_DELTA_AFTER_ANTECEDENT_PACKAGE_NO_ROLE_PROMOTION`
