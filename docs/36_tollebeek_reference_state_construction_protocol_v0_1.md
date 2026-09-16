# Tollebeek reference-state construction protocol v0.1

Status: **QUALIFICATION CANDIDATE — protocol only**

Governing readiness item: `DR_SM_REFERENCE_STATE`

This protocol defines how a matched Tollebeek REFERENCE soil state may later be constructed for compaction attribution. It does **not** create a numerical reference state or admit any soil-state values.

## 1. Scientific purpose

The project estimates a soil-state contribution through a controlled comparison:

```text
Y_current   = M(S_current,   F, C, G, B)
Y_reference = M(S_reference, F, C, G, B)

delta_Y = Y_current - Y_reference
```

The causal meaning of `delta_Y` depends on what differs between `S_current` and `S_reference` and what is held fixed.

REFERENCE is therefore not a generic 'healthy soil' label. It is a counterfactual construction matched to a specific causal question.

## 2. Core matching rule

For a simple soil-compaction attribution pair, CURRENT and REFERENCE must share, unless explicitly included in another research question:

- spatial unit / profile identity;
- layer geometry and intrinsic soil context;
- meteorological forcing;
- land-use/crop semantics;
- drainage semantics;
- managed-boundary semantics;
- model executable and numerical configuration;
- initialization protocol semantics;
- output and accounting conventions.

The intended contrast is restricted to the admitted compaction-related soil-state variables and the model properties derived from them.

If crop, boundary, drainage or other system controls also change, the comparison is not a simple compaction attribution and must be labelled accordingly.

## 3. Temporal alignment rule

A reference state inherits the temporal meaning of the CURRENT state it is paired with.

Examples:

- a CURRENT state measured in 2020–2021 supports a reference for a **dated 2020–2021 state comparison** unless an explicit temporal-transfer argument is qualified;
- applying that 2020–2021 pair to the observed October-1998 meteorological event is a controlled historical-forcing stress test, not evidence that the same soil states existed in 1998;
- an actual 1998 historical attribution requires a CURRENT state and REFERENCE construction whose temporal semantics are defensible for 1998.

Historical forcing must not silently backdate modern soil measurements.

## 4. Reference-state ladder

### RF0 — OBSERVED_PAIRED_REFERENCE

Highest authority.

RF0 requires a directly observed comparison state that is sufficiently matched to the CURRENT observation, for example a paired field/control area with compatible:

- soil profile / intrinsic texture and organic-matter context;
- layer depths;
- measurement method and date window;
- management context relevant to the causal question;
- spatial scale and QC.

An experimental 'control' is not automatically pristine or uncompacted. It represents the actual control condition documented by the source.

### RF1 — EVIDENCE_DERIVED_COUNTERFACTUAL

RF1 is permitted when a direct local control is unavailable but the reference can be constructed from independently qualified evidence.

Possible RF1 routes include:

1. **Matched empirical relation**
   - derive a less-compacted/reference state from paired experiments or local/regional observations matched by soil type, depth and management context;
   - retain uncertainty and transfer limitations.

2. **Qualified physical state transformation**
   - transform admitted CURRENT state variables to a reference state using a documented, independently reviewable rule;
   - show which variables change and which remain invariant;
   - derive hydraulic properties only through separately qualified relations.

3. **Locally anchored agronomic/reference benchmark**
   - use a benchmark demonstrably relevant to the same soil/profile context;
   - document why it represents the intended counterfactual rather than an arbitrary optimum.

RF1 must preserve the distinction between observed values and constructed values.

### RF2 — REFERENCE_ENVELOPE_SCENARIO

RF2 is allowed for Track S sensitivity/mechanism analysis when an historical or observational reference cannot be qualified.

Examples may include multiple explicitly defined reference-state members spanning plausible compaction relief.

RF2 rules:

- every member is labelled `SCENARIO_ONLY`;
- the transformation from CURRENT is explicit;
- no member is described as the actual historical uncompacted state;
- uncertainty is reported across members;
- external dimensions remain matched to CURRENT.

RF2 can support mechanism/sensitivity statements but not a claim of the observed historical compaction effect.

### RF3 — INADMISSIBLE_REFERENCE_DEFAULT

The following are inadmissible as automatic reference construction:

- 'pristine soil' without a local definition;
- zero traffic;
- arbitrary percentage reduction in bulk density with no evidence basis;
- choosing the lowest plausible bulk density because it maximises the effect;
- SoilPhys `modal_bulk_density_g_cm3` copied directly into `soil_state.bulk_density_g_cm3`;
- BOFEK profile class treated as an observed uncompacted state;
- changing crop, drainage, boundary or initialization together with soil state;
- null values converted to zero;
- selecting a reference because model outputs look realistic.

## 5. SoilPhys modal density boundary

`modal_bulk_density_g_cm3` is canonical profile context only.

It is **not** CURRENT state and it is **not** automatically REFERENCE state.

A future RF1 workunit may review whether a modal profile property can contribute evidence to a reference construction, but only through an explicit argument addressing:

- what population/modal condition it represents;
- whether it is compatible with the local profile ID and depth;
- whether anthropogenic compaction is included in that modal source;
- temporal meaning;
- uncertainty and transferability;
- mapping from modal property to the state variables required by the model.

Without such qualification, modal density remains excluded from the counterfactual.

## 6. State versus hydraulic parameterization

REFERENCE construction must distinguish:

```text
physical state evidence
        ->
reference state variables
        ->
qualified hydraulic-property transformation
        ->
model parameters
```

A reference bulk density value alone does not define a complete SWAP hydraulic profile.

Any change to retention or conductivity parameters must have an explicit relation to the reference-state construction. Parameters must not be manually tuned independently for CURRENT and REFERENCE to obtain a desired response.

## 7. Layer and profile matching

REFERENCE must be constructed at a compatible grain with CURRENT.

For the admitted eight-profile OT.02 context:

- preserve source profile identity;
- preserve layer boundaries unless the causal hypothesis explicitly includes structural layer change;
- do not average sparse state observations into an exact area-weighted profile without an admitted weighting scheme;
- allow missing reference variables to remain missing;
- if only a subset of profiles can be paired, record the subset explicitly rather than extrapolating to all eight.

## 8. Anthropogenic attribution boundary

A less dense or less resistant reference state is not automatically proof of an anthropogenic cause.

The project must keep separate:

1. measured/constructed physical state difference;
2. hydrological/crop response difference;
3. attribution of the physical state difference to traffic/management;
4. transfer to water-system receptors;
5. economic valuation.

A valid CURRENT/REFERENCE response comparison may quantify the effect of a state contrast even when the management cause of that contrast remains uncertain.

## 9. Initialization interaction

REFERENCE construction must use the canonical initial-state reconstruction protocol.

For simple attribution:

- CURRENT and REFERENCE use equivalent initialization semantics;
- a shared warm-up may yield different hydrological storage because the soil states differ;
- that difference is acceptable when it emerges from the admitted state contrast;
- separate tuning of initial state to compensate for the reference construction is inadmissible.

## 10. Historical versus scenario tracks

### Track H — historical attribution

Requires:

- temporally defensible CURRENT state;
- RF0 or qualified RF1 reference;
- sufficiently historical forcing/boundary/drainage/land-use semantics;
- no silent use of modern state as 1998 state.

### Track S — controlled scenario/stress test

May combine, for example, a dated modern CURRENT/REFERENCE pair with the admitted 1998 extreme meteorological forcing, provided the result is explicitly labelled as a scenario such as:

> response of the dated modern soil-state pair under the observed 1998 meteorological event forcing

This must not be described as the actual soil-compaction effect that occurred in 1998.

## 11. Future reference-state dataset contract

A future admitted reference record should include or reference at minimum:

- `reference_state_id`;
- paired `current_state_id`;
- spatial/profile/layer IDs;
- reference class RF0/RF1/RF2;
- causal question / intended contrast;
- source/evidence IDs;
- construction rule and version;
- observation/construction date semantics;
- state variables, units and depths;
- direct versus derived provenance per variable;
- uncertainty/QC;
- hydraulic-parameter mapping authority where used;
- dimensions intentionally held fixed;
- dimensions intentionally changed;
- temporal applicability;
- scenario/historical label;
- qualification verdict.

The pair must be reconstructable from stable IDs; no hidden spreadsheet-only pairing is allowed.

## 12. Admission criteria

`DR_SM_REFERENCE_STATE` may move beyond `PARTIAL_EVIDENCE` only after:

1. an admitted or qualified CURRENT state exists for the same intended analysis;
2. the reference construction route is explicitly RF0 or RF1 for Track H, or RF2 for Track S;
3. the state contrast is defined at compatible profile/layer grain;
4. changed and fixed dimensions are enumerated;
5. temporal semantics are explicit;
6. missing values remain missing;
7. any hydraulic transformation is separately traceable;
8. CURRENT/REFERENCE initialization and external forcing/control semantics are matched;
9. uncertainty is preserved;
10. the result is independently reviewable.

## 13. Current verdict

`DR_SM_REFERENCE_STATE` remains `PARTIAL_EVIDENCE`.

Its route classification remains `DEPENDENT_INTERNAL_DECISION` because a Tollebeek-specific reference cannot be selected before CURRENT-state evidence and the intended historical/scenario track are fixed.

No RF0/RF1/RF2 state, model parameters or model run are admitted by this protocol.
