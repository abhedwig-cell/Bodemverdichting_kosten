# Tollebeek soil-state → hydraulic transformation protocol v0.1

Status: **DESIGN / QUALIFICATION CANDIDATE — no numerical parameterization**

## 1. Purpose

Define how an admitted or scenario soil state may be translated into the hydraulic properties required by the source-response model without collapsing measurement, inference and model input into one object.

This protocol closes an explicit gap in the Status-A-light theoretical/formal baseline: construction of CURRENT/REFERENCE hydraulic parameter sets.

It does **not** select a Tollebeek pedotransfer function, does not create hydraulic values and does not authorize a SWAP run.

## 2. Required separation

The canonical chain is:

```text
source observation / measurement
        ↓
SoilState
        ↓
HydraulicParameterization
        ↓
SWAP adapter / model input
        ↓
ModelRun
```

Keep the following distinct:

1. **profile context** — texture, organic matter, intrinsic/modal profile identity, layer geometry;
2. **state evidence** — measured or constructed bulk density, penetration resistance or other state indicators;
3. **hydraulic transformation** — the method that maps state + context to water-retention / conductivity functions;
4. **serialized model input** — the exact SWAP analytical parameters or hydraulic tables;
5. **model response** — outputs produced by a run.

A measured bulk density is not itself a measured Mualem–Van Genuchten parameter set.

## 3. SWAP target contract

For each soil-physical layer SWAP can use either:

### Analytical hydraulic functions

A Mualem–Van Genuchten representation with, depending on SWAP input version, fields including:

- residual water content `theta_r` / `ORES`;
- saturated water content `theta_s` / `OSAT`;
- `alpha`;
- `n`;
- saturated/fitting hydraulic conductivity `Ksat`;
- hydraulic-conductivity exponent `lambda` / `LEXP`;
- optional wetting/hysteresis and near-saturation parameters;
- measured saturated conductivity where separately supplied;
- dry bulk density as an explicit soil property.

### Tabulated hydraulic functions

A table describing the relation among water content, pressure head and hydraulic conductivity over the required range.

The project must record which representation is used. Analytical parameters derived by fitting a measured/predicted table are **derived values** and must retain their source table and fit diagnostics.

## 4. Transformation ladder

### H0 — DIRECT_HYDRAULIC_EVIDENCE

Highest authority for a local state.

Examples:

- measured water-retention curve from representative undisturbed samples;
- measured saturated and/or unsaturated hydraulic conductivity;
- a source-native hydraulic table;
- Mualem–Van Genuchten parameters fitted to those measurements with retained fit method and diagnostics.

Requirements:

- sample/location/depth and state linkage;
- measurement date or campaign context;
- laboratory/field method;
- replicate/QC semantics;
- fitted-versus-measured distinction;
- uncertainty / variability representation;
- representativeness decision for the modelled layer.

A fitted parameter set is not relabelled as direct measurement merely because its source curve was measured.

### H1 — QUALIFIED_PEDOTRANSFER_PARAMETERIZATION

Permitted when direct hydraulic measurements are unavailable or incomplete and the PTF is demonstrably appropriate for the intended soil/state domain.

Required metadata:

- exact PTF name, publication/code/version and checksum where executable code is used;
- output hydraulic representation;
- predictor list and units;
- training/calibration domain;
- valid texture/depth/state range;
- handling of bulk density and soil structure;
- prediction uncertainty / validation performance;
- treatment of predictors that are missing;
- whether the PTF predicts a full curve, curve points or analytical parameters;
- any subsequent fitting step and its diagnostics.

Bulk density may be a predictor but is not sufficient provenance for the complete hydraulic function.

The Dutch/Flemish compaction studies demonstrate that adding bulk density to PTFs can improve prediction of water-retention and conductivity behaviour, particularly in the wetter range, but that is a **method precedent**, not automatic authority for Tollebeek coefficients.

### H2 — EVIDENCE_BOUNDED_HYDRAULIC_SCENARIO

Allowed for sensitivity/mechanism analysis when the state evidence does not uniquely identify H0/H1 parameters.

Examples:

- an ensemble of hydraulic parameter sets sampled from a qualified prediction interval;
- a compacted/reference envelope based on experimentally observed hydraulic changes within a comparable soil domain;
- alternative admissible PTFs treated as method uncertainty.

Rules:

- every member is labelled `SCENARIO_ONLY` unless separately qualified;
- no member is selected because it yields a preferred hydrological result;
- the ensemble definition is identical in logic for CURRENT and REFERENCE;
- uncertainty remains visible in downstream response outputs.

### H3 — INADMISSIBLE_HYDRAULIC_DEFAULT

The following are prohibited as closure mechanisms:

- copy SoilPhys or BOFEK/Staring modal hydraulic functions and call them measured CURRENT state;
- set `theta_s = 1 - bulk_density / assumed_particle_density` without qualifying particle density, trapped air and the intended interpretation;
- apply one universal percentage reduction to `Ksat`, `alpha`, `theta_s` or another parameter because soil is labelled compacted;
- infer a full hydraulic function from penetration resistance alone;
- use a SWAP example profile or default parameter set because it runs;
- fit CURRENT and REFERENCE independently to obtain a desired runoff difference;
- replace a missing predictor/parameter by zero;
- use a PTF outside its documented domain without an explicit scenario/transferability qualification.

H3 cannot support source-response admission.

## 5. Bulk density semantics

Bulk density is an important physical state indicator because compaction changes pore volume and pore-size distribution. However:

- soils with equal bulk density may have different pore connectivity, aggregation and macropore systems;
- hydraulic conductivity, especially near saturation, is highly sensitive to structure and connected large pores;
- water-retention curve shape can change with density and structure rather than only through a change in total porosity;
- predictor relations are soil-domain dependent.

Therefore `bulk_density_g_cm3` remains a soil-state field. It is an **input to** a hydraulic transformation when a qualified method uses it, not a synonym for the resulting hydraulic parameter set.

## 6. Penetration-resistance semantics

Penetration resistance is useful evidence for mechanical state but is strongly affected by moisture, texture, instrument/protocol and depth.

It may:

- corroborate a compacted layer;
- stratify state severity;
- enter a specifically validated multi-predictor transformation.

It must not be directly converted to `Ksat`, `theta_s`, `alpha`, `n` or another hydraulic parameter through an undocumented rule.

## 7. Staringreeks / BOFEK / SoilPhys role

The Staringreeks and BOFEK provide high-value Dutch modal soil-hydraulic context and are appropriate as:

- profile-context prior;
- benchmark;
- candidate non-state baseline for sensitivity;
- source of layer/class hydraulic information where the research question is about the modal class itself.

They do **not** automatically define:

- measured CURRENT anthropogenic compaction state;
- locally uncompacted REFERENCE state;
- the hydraulic effect of a measured change in bulk density.

SoilPhys modal bulk density remains subject to the same boundary.

## 8. Proposed `HydraulicParameterization` object

The transformation has distinct scientific identity and grain and should not be hidden inside `ModelConfiguration` or `SoilState`.

Proposed grain:

```text
one hydraulic parameterization
per soil_state × layer × method/version × uncertainty/member × representation
```

Minimum identity/metadata:

- `hydraulic_parameterization_id`;
- `soil_state_id`;
- `soil_layer_id` where not already unambiguous from state;
- `hydraulic_method_class` (`H0`, `H1`, `H2` class or future controlled vocabulary);
- `hydraulic_method_id` and `hydraulic_method_version`;
- `representation` (`MVG_ANALYTICAL`, `HYDRAULIC_TABLE`, etc.);
- exact input predictor references and source identities;
- direct/derived/scenario provenance;
- uncertainty/member ID;
- validation/fit diagnostics;
- qualification status;
- SWAP serialization adapter/version.

### Analytical outputs when applicable

Do not require every field for every representation. For Mualem–Van Genuchten, candidate outputs include:

- `theta_r`;
- `theta_s`;
- `alpha_cm_inv`;
- `n`;
- `ksat_cm_d`;
- `lambda` / conductivity exponent;
- optional hysteresis / near-saturation parameters required by the selected SWAP configuration.

Tabular representations instead reference the complete qualified hydraulic table and checksum.

## 9. Relationship to `ModelConfiguration`

`ModelConfiguration` controls the shared modelling semantics, e.g.:

- SWAP authority/version;
- analytical versus tabular hydraulic representation policy;
- hysteresis option;
- numerical configuration;
- boundary/drainage representation contract.

State-specific hydraulic values do **not** belong in the shared pair configuration if they differ between CURRENT and REFERENCE.

`ModelRun` should therefore reference both:

- the shared `model_configuration_id`;
- the state-specific `hydraulic_parameterization_id`.

## 10. CURRENT/REFERENCE matching rule

For a simple soil-state attribution:

1. CURRENT and REFERENCE use the same hydraulic transformation family/version where scientifically possible;
2. they use equivalent predictor definitions, units and depth conventions;
3. intrinsic context such as texture is kept fixed unless the causal question explicitly changes it;
4. state-dependent predictors may differ only because of the admitted CURRENT/REFERENCE state contrast;
5. transformation uncertainty is propagated symmetrically;
6. no member-specific tuning is performed against the desired response.

### Asymmetric evidence

If CURRENT has direct measured hydraulics but REFERENCE is PTF-derived, or vice versa, the pair combines soil-state contrast with transformation-method contrast.

Such a pair may still be useful but must be labelled accordingly and cannot automatically support the clean simple-attribution interpretation.

## 11. Uncertainty contract

Hydraulic uncertainty is a separate uncertainty layer from state-sampling uncertainty.

Retain, where available:

- measurement replicate variability;
- fitted-parameter uncertainty;
- PTF prediction error / prediction interval;
- model-form uncertainty among PTFs or hydraulic representations;
- spatial representativeness uncertainty;
- state-to-hydraulic transferability uncertainty.

Do not collapse all uncertainty into a single confidence score.

If one unique hydraulic parameterization is not identified, retain an ensemble/member set rather than a hidden best guess.

## 12. Admission criteria for a future Tollebeek parameterization

A numerical Tollebeek hydraulic parameterization may move toward admission only when:

1. its source `SoilState` is itself admitted or explicitly scenario-qualified;
2. layer/depth identity is explicit;
3. all required predictors have source/provenance and null semantics;
4. method/version is immutable and reproducible;
5. method applicability to the soil/state domain is reviewed;
6. output units/representation match the selected SWAP adapter;
7. fit/prediction uncertainty is retained where applicable;
8. CURRENT/REFERENCE matching semantics are documented;
9. no modal/profile-context value has been silently reclassified as state evidence;
10. validation catches missing required SWAP hydraulic inputs before execution.

## 13. Current verdict

`HYDRAULIC_TRANSFORMATION_ARCHITECTURE_DESIGNED — NUMERICAL_PARAMETERIZATION_DATA_GATED`

This protocol authorizes schema/formal modelling of the transformation object. It does not authorize a Tollebeek numerical hydraulic parameter set or model run.