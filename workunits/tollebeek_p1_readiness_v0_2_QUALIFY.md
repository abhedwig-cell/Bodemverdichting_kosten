# Tollebeek P1 readiness v0.2 — QUALIFY checkpoint

Capability: `CAP_TOLLEBEEK_P1_READINESS_V0_2`

Phase: `QUALIFY`

Date: 2026-09-16

## Authority

- canonical base: `main` @ `cac711c05ef340a2f6369717892805445c11af1a`
- implementation head: `0e5ea7989cae4873a6e7c867fd4ef4ffc234049d`
- precheck head: `32265a53bdf02578bd3deeec6effc12b44410e51`
- pull request: `#50`

## Qualified delta

The v0.2 delta records the scientific consequence of the already qualified antecedent precipitation-gap reconstruction package without promoting any P1 input role.

The package advances one forcing subdependency for future hydrological reconstruction/sensitivity work. It does not provide an observed historical precipitation series, a qualified warm-up, a numerical initial state, a managed-boundary realization, drainage configuration, land-use realization, hydraulic parameterization or runnable Tollebeek model configuration.

Role counts remain exactly:

- `ADMITTED=3`
- `PARTIAL_EVIDENCE=7`
- `MISSING=0`

`DR_SM_INITIAL_STATE` remains `PARTIAL_EVIDENCE`.

## Qualification evidence

Normal PR CI on exact precheck head `32265a53bdf02578bd3deeec6effc12b44410e51`:

- run `35114583824`: `SUCCESS`
- compile project validation and workbook tools: PASS
- Status-A-light integrity gate: PASS
- full unit and contract tests: PASS

Precheck diff remained documentation/governance only. No production/model/schema/evidence-register semantics were modified.

## Scientific guardrails retained

- `SCENARIO_ONLY` antecedent precipitation is not historical truth.
- The precipitation package does not demonstrate warm-up adequacy.
- No I0/I1/I2 numerical initial state is admitted here.
- CURRENT and REFERENCE remain unresolved as numerical paired soil states.
- REFERENCE construction remains downstream of CURRENT admission.
- Managed-boundary, drainage and land-use uncertainties remain explicit blockers.
- No missing value may be replaced by zero, a default, an average or a representative value to obtain run-readiness.
- No SWAP run is authorized by this workunit.

## Verdict

`QUALIFIED_P1_READINESS_V0_2_NO_ROLE_PROMOTION_EXTERNAL_BLOCKERS_PRESERVED`

## Merge authority

Only the exact head containing this QUALIFY checkpoint may be merged after a new exact-head CI success and a final diff review confirming that the workunit remains documentation/governance only.

## Next permitted action

Run normal PR CI on this exact QUALIFY head. If green, re-check live `main`, competing PR state and final diff; then SHA-lock squash merge without further scientific changes and verify post-merge push CI before CLOSE.
