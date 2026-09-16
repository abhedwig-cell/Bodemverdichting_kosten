# Tollebeek hydraulic transformation v0.1 — QUALIFY

Capability: `CAP_HYDRAULIC_TRANSFORMATION`

Phase: `QUALIFY`

## Canonical/source baseline

- base `main`: `45735b863a588db2b009a2908af6e324f717257c`
- clean pre-checkpoint PR head: `d867666942701d39f7a447c452a374a7a48f2bee`
- PR: `#44`

## Qualified architecture

The workunit introduces the explicit scientific chain:

`SoilState → HydraulicParameterization → ModelRun`

with formal relation:

`H_i,s,m = T_v(S_i,s, X_i, m)`

The transformation object retains method/version, representation, predictor/state linkage, uncertainty/member identity, qualification and SWAP serialization semantics.

Transformation classes:

- `H0_DIRECT_HYDRAULIC_EVIDENCE`
- `H1_QUALIFIED_PEDOTRANSFER`
- `H2_EVIDENCE_BOUNDED_SCENARIO`

Convenience/default closure routes described as H3 in the protocol remain prohibited.

## Evidence qualification boundary

Evidence supports the architecture and method hierarchy only:

- SWAP hydraulic input representation;
- Staringreeks as modal/context prior;
- bulk-density-responsive PTF method precedent;
- multi-predictor/domain-aware PTF semantics;
- direct treatment-specific hydraulic evidence route precedent;
- pore-structure/connectivity guardrail.

No literature coefficient, PTF parameter, modal Staring/BOFEK value or experimental treatment value is transferred to Tollebeek.

## Validation evidence

Temporary transaction finalizer:

- first wrapper run `35098053088`: failed before job start because the temporary workflow YAML was invalid; no scientific/schema postimage was committed;
- repaired finalizer run `35098409209`: SUCCESS;
- architecture patch applied;
- central Status-A-light integrity gate PASS;
- full unit/contract test suite PASS;
- validated permanent postimage committed as `30f3565c94526261497eaa4bc0857f644e760793`.

Repository hygiene after validation:

- temporary workflow removed;
- temporary patcher removed;
- existing `model/equations.csv` formatting restored so only `EQ_STATE_TO_HYDRAULICS` remains as semantic delta;
- resulting clean PR head: `d867666942701d39f7a447c452a374a7a48f2bee`.

Independent normal PR CI:

- run `35098700394`: SUCCESS;
- compile PASS;
- central Status-A-light integrity gate PASS;
- full unit/contract suite PASS.

## Numerical/state boundary

This qualification does **not**:

- admit a Tollebeek CURRENT soil state;
- admit a Tollebeek REFERENCE soil state;
- choose a numerical PTF;
- create a canonical hydraulic-parameter dataset/storage file;
- create Mualem–Van Genuchten values or hydraulic tables;
- change `DR_SM_CURRENT_STATE` readiness;
- authorize a SWAP model run.

`hydraulic_parameterization_register` deliberately has no `storage` path at this stage.

## Verdict

`QUALIFIED_HYDRAULIC_TRANSFORMATION_ARCHITECTURE_DATA_GATED`

## Merge authority

Only the exact head produced by this QUALIFY checkpoint may be merged after a new exact-head CI success.

## Next permitted action

Run exact-head CI on this checkpoint. If green, merge without further scientific changes and verify post-merge `main` CI.
