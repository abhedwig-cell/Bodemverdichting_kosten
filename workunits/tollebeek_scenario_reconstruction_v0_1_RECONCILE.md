# Tollebeek scenario/reconstruction admissibility v0.1 — RECONCILE checkpoint

Date: 2026-09-16
Capability surface: unresolved P1 source-model inputs after the current-canonical readiness baseline
Protocol phase: RECONCILE / CLASSIFY

## Canonical authority

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- canonical start: `main` @ `8ef90b123dbce0b9c855cd9a008405806ad6451b`
- branch: `work/tollebeek-scenario-reconstruction-v0.1`
- P1 baseline verdict inherited: `P1_ROUTE_COVERAGE_COMPLETE_INPUT_ADMISSION_INCOMPLETE`
- inherited readiness count: `ADMITTED=3`, `PARTIAL_EVIDENCE=7`, `MISSING=0`

No existing scenario/reconstruction branch was found before branch creation.

## Governing scientific rule

The canonical theoretical framework defines attribution as a matched comparison:

`Y_current = M(S_current, F, C, G, B)`

`Y_reference = M(S_reference, F, C, G, B)`

with `delta_Y = Y_current - Y_reference`.

The meaning of the result depends on matching forcing, crop/land use, geometry and boundary/system context. A modelled counterfactual is allowed in principle, but only when its construction is evidence-based and explicitly qualified. Missing observed inputs cannot be silently replaced by defaults and still support an observed-history attribution claim.

## Purpose of this workunit

Classify the seven `PARTIAL_EVIDENCE` roles by whether further progress can occur without new external records.

This workunit does **not**:

- admit any missing scientific input;
- create a runnable SWAP configuration;
- choose a representative crop;
- invent drainage or boundary values;
- create CURRENT or REFERENCE soil-state values;
- run SWAP5;
- change the 3/7/0 readiness counts.

## Classification vocabulary

- `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION`: an observed/history-specific claim requires new source-native external evidence; scenarios may exist separately but cannot close the historical gate.
- `RECONSTRUCTABLE_WITH_EXPLICIT_UNCERTAINTY`: direct telemetry/observations are preferred, but a bounded reconstruction may become admissible if historical constraints, uncertainty envelope, sensitivity and claim limits are explicitly qualified.
- `SCENARIO_ELIGIBLE_ONLY`: a scenario can support conditional/sensitivity questions, but not an observed 1998-state claim.
- `DEPENDENT_INTERNAL_DECISION`: no new external datum is intrinsically required for the decision itself, but it must wait for prerequisite states/configurations.

## Initial classification

| Readiness role | Classification | Reason |
| --- | --- | --- |
| `DR_SM_CURRENT_STATE` | `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION` | No auditable OT.02 raw measured compaction state is admitted. A synthetic state would change the question from measured Tollebeek attribution to sensitivity/scenario analysis. |
| `DR_SM_REFERENCE_STATE` | `DEPENDENT_INTERNAL_DECISION` | Reference construction is a scientific decision, but it must be matched to the finally admitted CURRENT state and profile/layer grain. |
| `DR_SM_DRAINAGE` | `HARD_EXTERNAL_FOR_HISTORICAL_ATTRIBUTION` | Existing owner inventory lacks usable spacing/depth/date values. A drainage scenario may be explored separately but cannot be relabelled as observed/current configuration. |
| `DR_SM_INITIAL_STATE` | `RECONSTRUCTABLE_WITH_EXPLICIT_UNCERTAINTY` | Direct shallow observations are preferred; a reproducible warm-up/restart route may become admissible after boundary, drainage, land-use and model configuration are sufficiently specified. |
| `DR_SM_MANAGED_BOUNDARY` | `RECONSTRUCTABLE_WITH_EXPLICIT_UNCERTAINTY` | Historical topology, target levels, nominal capacities and event context constrain the system, but an inferred event hydrograph/control sequence must carry explicit uncertainty and cannot be called observed telemetry. |
| `DR_SM_LAND_USE` | `SCENARIO_ELIGIBLE_ONLY` | Exact 1998 crop identity remains externally unresolved. Conditional crop scenarios or a demonstrably crop-independent design can be studied separately, but cannot be presented as observed 1998 land use. |
| `DR_SM_MODEL_CONFIG` | `DEPENDENT_INTERNAL_DECISION` | SWAP5 execution authority is pinned; the concrete configuration can only be closed after the scientific inputs and reconstruction/scenario choices it binds are resolved. |

## Two distinct future products

### Track H — historical attribution

Goal: estimate the compaction-attributable response for the actual/defensibly reconstructed 1998 Tollebeek event.

This track requires stronger event/state evidence. Scenario substitutions do not close historical data gaps unless an explicit reconstruction qualification demonstrates that the substituted quantity is a bounded historical reconstruction rather than a convenience assumption.

### Track S — bounded scenario analysis

Goal: answer conditional questions such as how the same admitted event forcing responds under explicitly defined soil-state, drainage, crop or boundary scenarios.

Track S may become runnable earlier, but its outputs must be labelled `SCENARIO_ONLY`/conditional. It cannot be used as evidence that those conditions occurred in Tollebeek in 1998.

## Next permitted action

Persist a scenario/reconstruction admissibility matrix that defines, for each open role:

1. whether historical closure requires external evidence;
2. whether reconstruction/scenario treatment is scientifically permissible;
3. minimum prerequisites and uncertainty requirements;
4. prohibited shortcuts;
5. allowable claim language.

No readiness status changes are permitted in this workunit.