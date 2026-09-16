# Tollebeek P1 readiness delta v0.2

Date: 2026-09-16

Canonical basis before this workunit: `main` @ `cac711c05ef340a2f6369717892805445c11af1a`

Predecessor baseline: `docs/32_tollebeek_p1_readiness_baseline_v0_1.md`

Relevant new qualified package: `Q_TOL_ANTECEDENT_GAP_RECONSTRUCTION_V0_1`

## Verdict

`P1_READINESS_UNCHANGED_ANTECEDENT_FORCING_SUBDEPENDENCY_ADVANCED_SCENARIO_ONLY`

The trace-aware antecedent precipitation-gap package merged in PR #49 advances one supporting dependency for future hydrological reconstruction and sensitivity work. It does **not** promote any of the ten P1 input roles and does not authorize a model run.

The canonical role counts remain:

- `ADMITTED=3`
- `PARTIAL_EVIDENCE=7`
- `MISSING=0`

## Qualified delta since v0.1

The repository now contains a reproducible `SCENARIO_ONLY` package for the 108 source-missing station-273 antecedent precipitation hours.

Qualification authority:

- qualification: `artifacts/scenarios/tollebeek_antecedent_gap_reconstruction_v0_1_qualification.json`
- manifest: `artifacts/scenarios/tollebeek_antecedent_gap_reconstruction_v0_1_manifest.json`
- generator: `tools/build_tollebeek_antecedent_gap_scenarios.py`
- method: `ST317_MASS_CONSTRAINED_MULTI_STATION_TIMING_V0_1`
- method authority: `docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md`
- expanded package SHA-256: `85dbb685dd888bdad7078f243ca01adb134b343f1d382d578f53cdce1c879932`
- classification: `QUALIFIED_FOR_SCENARIO_ONLY_USE_NOT_RUN_READY`
- `run_authorized=false`

The package is admissible only as an uncertainty-preserving precipitation reconstruction input to a future scenario/sensitivity design after the remaining dependencies have themselves been admitted or explicitly scenario-qualified.

It is not an observed station-273 series and no timing member, trace realization or ensemble may be promoted to historical truth without separate qualification.

## Updated role matrix

| Data request | Role | Status | v0.2 readiness boundary |
|---|---|---|---|
| `DR_SM_GEOMETRY` | spatial geometry | `ADMITTED` | Unchanged. Current definitive OT.02 geometry remains admitted. |
| `DR_SM_PROFILE` | soil profile context | `ADMITTED` | Unchanged. SoilPhys/BOFEK modal profiles remain context, not current compaction. |
| `DR_SM_CURRENT_STATE` | current soil/compaction state | `PARTIAL_EVIDENCE` | Unchanged. Raw georeferenced WER3382/Flevo 2020–2021 point observations are still required for OT.02 admission. |
| `DR_SM_REFERENCE_STATE` | matched reference soil state | `PARTIAL_EVIDENCE` | Unchanged. Construction remains dependent on an admitted CURRENT state and explicit causal contrast. |
| `DR_SM_DRAINAGE` | drainage configuration | `PARTIAL_EVIDENCE` | Unchanged. Parcel spacing/depth/outlet/status/date and SWAP mapping remain unresolved. |
| `DR_SM_EVENT_FORCING` | event forcing | `ADMITTED` | Unchanged. The 144-hour 24–30 Oct 1998 station-273 event forcing remains admitted. The new antecedent package is separate `SCENARIO_ONLY` supporting material, not an extension of observed event forcing. |
| `DR_SM_INITIAL_STATE` | initial hydrological state | `PARTIAL_EVIDENCE` | One forcing subdependency is advanced, but no I0/I1/I2 numerical state is admitted. Managed boundary, drainage, land use, configuration and adequacy dependencies still block historical warm-up admission. |
| `DR_SM_MANAGED_BOUNDARY` | managed boundary | `PARTIAL_EVIDENCE` | Unchanged. Pre-IJsvogel topology is constrained, but 1998 dynamic levels/operations and emergency pumping magnitude/timing remain unidentified. |
| `DR_SM_LAND_USE` | land-use/crop context | `PARTIAL_EVIDENCE` | Unchanged. Near-period LGN context does not identify parcel/profile-level October 1998 crop state. |
| `DR_SM_MODEL_CONFIG` | source-model configuration | `PARTIAL_EVIDENCE` | Unchanged. SWAP5 authority is pinned, but no complete runnable Tollebeek configuration is admitted. |

## Initial-state consequence

The antecedent precipitation package partially satisfies only the requirement for independently sourced pre-event forcing in the I1 reconstruction protocol.

It does **not** by itself satisfy the I1 minimum contract because the following remain unresolved or unadmitted:

1. historical managed-boundary semantics of sufficient authority;
2. drainage semantics for the selected representation;
3. land-use/crop semantics for the warm-up period;
4. a complete runnable SWAP configuration;
5. equivalent CURRENT/REFERENCE numerical state semantics, which also depend on the not-yet-admitted soil-state contrast and hydraulic parameterization;
6. explicit spin-up/convergence diagnostics and adequacy evidence.

Therefore:

- no I1 restart may be created yet;
- no I2 numerical initial-state envelope is created by this workunit;
- the owner narrative of very wet/saturated antecedent conditions remains qualitative only;
- the reconstructed precipitation hours must not be treated as evidence of a unique historical hydrological state.

## What is now genuinely reusable

The following can be inherited without reacquisition while their dependencies remain unchanged:

- source-native KNMI response snapshots and receipt for the antecedent gap;
- the deterministic reconstruction generator;
- explicit trace-policy uncertainty;
- station-specific timing-member uncertainty;
- mass-constrained station-317 daily precipitation anchoring;
- exact package hash and qualification receipt.

This reduces future forcing-reconstruction work. It does not reduce the scientific need to qualify the state, boundary, drainage, crop and configuration dimensions that determine hydrological memory.

## Remaining primary external blockers

The external acquisition priorities remain materially the same as in v0.1:

1. **CURRENT state**: raw georeferenced Flevo-land-in-beweging / WER3382 observations with dates, depths, replicates and QC;
2. **drainage**: source-native parcel-drain spacing/density, depth/elevation, outlet relation, status and reference date;
3. **1998 managed boundary**: event-period local/Urkervaart levels, pump runtime/realized discharge and emergency-pumping records;
4. **1998 land use/crop**: dated parcel/field records linkable to the historical control areas;
5. **initial-state observations**: shallow groundwater or soil-water observations close enough in space and time to the event to constrain I0/I1.

## Dependent scientific decisions

These remain downstream of the blockers above:

- REFERENCE-state construction after CURRENT-state admission;
- numerical hydraulic parameterization after CURRENT/REFERENCE state definition;
- concrete model configuration after unresolved inputs are either admitted or explicitly scenario-qualified;
- warm-up/restart qualification only after the relevant boundary, drainage, land-use, configuration and adequacy contracts are satisfied;
- paired CURRENT/REFERENCE source-model runs only after all run-critical dimensions have explicit admission semantics.

## Guardrails

- `SCENARIO_ONLY` is not a synonym for `ADMITTED` historical truth.
- A qualified precipitation reconstruction does not constitute a qualified warm-up.
- `DR_SM_INITIAL_STATE` remains `PARTIAL_EVIDENCE`.
- No null scientific field may become zero, a default, an average or a representative value merely to obtain a runnable configuration.
- No post-1998 IJsvogel/current merged-system operation may be backcast into 1998 without separate qualification.
- No SWAP run is authorized by this readiness delta.

## Next natural state boundary

There is no further scientifically material internal promotion available from the antecedent precipitation package alone.

The next substantive progress requires either:

- new external source records for one of the primary blockers; or
- a separately bounded and reviewed `SCENARIO_ONLY` construction for another unresolved dimension, with explicit uncertainty and no historical-truth claim.

Until then, P1 remains route-complete but input-admission incomplete.
