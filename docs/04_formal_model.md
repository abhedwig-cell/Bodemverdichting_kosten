# 4. Formal model

Status: **Status-A-light formal baseline**

This document is the home for canonical equations, state definitions, units and formal decision rules. It translates the theoretical and conceptual model into relations that can be implemented in code, tested and exposed through workbooks or the future application.

A formal relation is not the same thing as a numerical parameter. Numerical values become project inputs only after their evidence and intended use have been qualified.

## 4.1 Notation and state roles

For a spatial unit `i`, event `e`, response variable `Y` and state role `s`:

```text
s ∈ {CURRENT, REFERENCE, SCENARIO}
```

The primary attribution pair is:

```text
Y_current(i,e)   = M(S_current(i),   F_e, C_i,e, B_i,e, D_i,e, config)
Y_reference(i,e) = M(S_reference(i), F_e, C_i,e, B_i,e, D_i,e, config)
```

where, schematically:

- `S` = soil state/profile parameters;
- `F` = meteorological forcing;
- `C` = crop/land-use context;
- `B` = hydrological boundary conditions;
- `D` = drainage configuration;
- `config` = controlled model/numerical configuration.

The attributable difference is:

```text
delta_Y(i,e) = Y_current(i,e) - Y_reference(i,e)
```

### Pairing rule

For a clean soil-state attribution, all controlled dimensions except the admitted soil-state change must be identical or explicitly demonstrated equivalent between the pair.

This is a governance rule, not merely a modelling preference.

## 4.2 Sign conventions

Every implemented response variable must document its sign convention. Until a variable-specific convention is registered, `delta_Y` means algebraic current minus reference and should not automatically be relabelled `damage`.

For generated surface runoff:

```text
delta_R_mm = R_current_mm - R_reference_mm
```

A positive value means more generated runoff in the current state than the reference state for the same controlled event/context.

## 4.3 Depth-to-volume conversion

For an affected area `A_ha` and attributable water-depth difference `delta_R_mm`:

```text
V_generated_m3 = 10 * A_ha * delta_R_mm
```

because:

```text
1 ha × 1 mm = 10 m3
```

### Domain restrictions

- `A_ha >= 0`;
- `A_ha = null` or `delta_R_mm = null` implies `V_generated_m3 = null`;
- no system-area default is substituted for missing affected area;
- `V_generated_m3` is a source volume and does not imply transfer beyond the parcel.

The identity is implemented in `src/transfer/volume.py` and has software tests.

## 4.4 Event-conditioned transfer

Let `V_g` be generated parcel volume and `V_k` a downstream volume at transfer stage `k`.

The formal stages currently recognised in the Tollebeek vertical slice are:

```text
GENERATED_PARCEL
FIELD_EDGE
DITCH
NETWORK
PUMP_INTAKE
```

The project does not assume that all stages exist for every pathway or that they can be collapsed into one factor.

### Hurdle representation

For field-edge runoff, occurrence and magnitude are conceptually separated:

```text
p_e = P(V_edge,e > 0 | X_e)
```

and, conditional on a positive occurrence:

```text
V_edge,e | (V_edge,e > 0) = G(X_e)
```

where `X_e` may include source state, event forcing, initial wetness, process class and connectivity information.

This does not prescribe one statistical model. It defines the required semantic separation.

### Diagnostic delivery ratio

Where both generated and delivered volumes are defined and `V_g > 0`:

```text
f_delivery,e = V_edge,e / V_g,e
```

This ratio is event-specific and primarily diagnostic unless separately qualified as a predictive relation.

Rules:

- there is no universal project default for `f_delivery`;
- zero-runoff events remain part of occurrence evidence;
- an apparent ratio above one is a QA signal and must not be silently clipped;
- ponding alone does not define `V_edge`.

## 4.5 Network routing and conservation

A network transfer stage should preserve the volume identity appropriate to the selected control volume.

For a generic routed unit over event/window `e`:

```text
V_in + DeltaStorage_initial_sources
    = V_out + DeltaStorage + V_losses + residual
```

The exact terms depend on the water-system representation. The formal requirement is that storage and alternative exits are explicit enough to avoid treating all ditch-delivered water as immediate pump intake.

A routing model may be simple or detailed, but its mass-balance boundary must be stated.

## 4.6 Two-zone / two-pump dispatch

For the current Tollebeek vertical slice, define:

- `V_P` = routed incremental volume from the primary/IJsvogel-core zone;
- `V_A` = routed incremental volume from the assist/Kievit zone;
- `a` = explicit fraction of `V_A` assigned to the primary/assist pump, with `0 <= a <= 1`.

Then:

```text
V_A_to_primary   = a * V_A
V_A_to_secondary = (1 - a) * V_A
V_primary_total  = V_P + V_A_to_primary
V_secondary      = V_A_to_secondary
```

### Null rule

If `a` is unknown, allocation-dependent pump volumes remain unknown. The implementation must not substitute `a = 0`, `a = 0.5` or any other convenience value.

### Direction rule

The current qualified Tollebeek evidence supports an assist path from Kievit-zone water to IJsvogel under extreme conditions. It does not currently support an automatic reverse assist path. The generic code is capable of other configurations only when a future project configuration explicitly defines them.

## 4.7 Available pump capacity

For pump `p` with installed/nominal capacity `Q_inst,p` and event-specific availability fraction `u_p`:

```text
Q_available,p = Q_inst,p * u_p
```

with:

```text
0 <= u_p <= 1
```

`u_p` has no hidden default.

If `Q_inst,p` is a historical or nominal benchmark rather than a qualified current operating capacity, the status of the resulting calculation must retain that limitation.

## 4.8 Pump hours and capacity pressure

For assigned incremental pumped volume `V_p` and available capacity `Q_available,p` in `m3/min`:

```text
pump_hours_p = V_p / (60 * Q_available,p)
```

where the expression is undefined/null when the required capacity information is missing or non-positive.

For an explicitly chosen response window `T_window_h`:

```text
capacity_pressure_p = pump_hours_p / T_window_h
```

Interpretation:

- `< 1`: the assigned incremental volume could theoretically be processed within the window at the assumed available capacity;
- `= 1`: theoretical full use of the assumed available capacity over the window;
- `> 1`: the assignment cannot be processed within the chosen window under the assumed capacity.

This is a **capacity diagnostic**, not automatically flood damage, failure probability or a statutory threshold.

## 4.9 Pump energy

For pumped volume `V_m3`, total dynamic head `H_m`, overall efficiency `eta` and water density `rho`:

```text
E_kWh = rho * g * H_m * V_m3 / (eta * 3.6e6)
```

with approximately:

```text
g = 9.80665 m/s2
rho ≈ 1000 kg/m3
```

unless a different value is explicitly required and documented.

Domain rules:

- `V_m3 >= 0`;
- `H_m >= 0`;
- `0 < eta <= 1`;
- missing `H_m` or `eta` means energy remains unknown;
- a nominal peil difference is not automatically `H_m`;
- efficiency must refer to the chosen energy boundary, for example pump hydraulic efficiency or wire-to-water efficiency, and that boundary must be stated.

The core identity is implemented in `src/water_system/energy.py`.

## 4.10 Direct pumping budget cost

When energy and a current tariff are qualified for the same scope:

```text
C_energy = E_kWh * p_electricity_EUR_per_kWh
```

A direct public-budget pumping estimate may be expressed as:

```text
C_pump_budget = C_energy + C_variable_OM_attributable
```

Fixed expenditure is not automatically attributable to one incremental event.

Historical `EUR/m3` benchmarks may be stored for comparison but are not substituted for this relation unless the project explicitly qualifies them for the relevant time, technology and accounting scope.

## 4.11 Potential water need versus actual delivery

For dry-side effects, the formal model must distinguish potential incremental requirement from actual delivered water.

A generic structure is:

```text
V_need_potential = 10 * A_ha * delta_I_mm
```

followed, where relevant, by explicit system factors or models for:

```text
V_requested
V_available
V_delivered
```

A potential irrigation/water requirement is not automatically a societal off-site water-supply cost. Availability, response, allocation and delivery must be represented.

## 4.12 Crop/private damage skeleton

A generic private output-loss relation may take the form:

```text
C_output_loss = delta_Yield * area * qualified_output_price
```

but private net damage should distinguish:

```text
private_damage
    = lost_output_value
      - genuinely_avoided_yield_dependent_costs
      + attributable_extra_operations
```

Area-dependent costs should not be subtracted automatically merely because yield is lower.

This section defines accounting structure only. Crop-specific response and economic coefficients require separate evidence.

## 4.13 Aggregation

For an additive quantity `X` with compatible scopes:

```text
X_total = sum_i X_i
```

Only after checking:

- units are identical or converted explicitly;
- spatial units do not overlap unintentionally;
- event/time windows are compatible;
- values represent the same transfer stage and valuation category.

For non-additive quantities such as peak flow, occurrence probability, capacity pressure or coincident water demand, no generic sum/mean operator is canonical. The aggregation relation must be pathway-specific.

## 4.14 Null, zero and not-applicable

The implementation distinguishes conceptually:

- `0`: a known numerical zero;
- `null`: unknown, unavailable or not yet calculated;
- `not applicable`: quantity does not apply to this object/context;
- `blocked`: calculation is intentionally not permitted because a prerequisite is missing.

The current CSV/workbook implementation often represents unknown numerical values as blank/null. Future database or API representations may encode richer status explicitly, but they must preserve this distinction.

## 4.15 Formal decision rules

The following rules are part of the model contract:

```text
IF required scientific input is unknown
THEN do not silently replace it with zero or a convenient default.

IF current/reference runs differ in uncontrolled dimensions
THEN the simple delta cannot be labelled a soil-state attribution without further decomposition.

IF a water volume changes transfer stage
THEN the stage must be explicit.

IF installed pump capacity is used
THEN availability remains a distinct event/operation variable.

IF pump energy is calculated
THEN total dynamic head and efficiency must be explicit.

IF a physical effect is converted to money
THEN the valuation relation and valuation category must be explicit.
```

## 4.16 Equation registry and code mapping

Formal equations should progressively be registered in the canonical model/equation schema and linked to their implementation and tests.

Current implemented examples are:

| Relation | Code | Test type |
|---|---|---|
| generated runoff volume | `src/transfer/volume.py` | software/unit QA |
| two-zone/two-pump dispatch | `src/water_system/dispatch.py` | software/unit QA |
| pump energy | `src/water_system/energy.py` | software/unit QA |

Passing those tests demonstrates implementation semantics, not the scientific correctness of a Tollebeek input dataset or event result.

## 4.17 Soil-state to hydraulic-parameterization contract

Let `S_i,s` be the admitted or explicitly scenario-qualified soil state for layer/profile unit `i` and state role `s`, and `X_i` the retained intrinsic/profile context used by a qualified transformation method `T_v`:

```text
H_i,s,m = T_v(S_i,s, X_i, m)
```

where `m` is an explicit uncertainty/scenario member when one unique hydraulic state is not identified, and `H` is the hydraulic representation consumed by SWAP (analytical parameters or a qualified hydraulic table).

Rules:

- `T_v` has an immutable method/version and explicit predictor contract;
- missing predictors remain missing and do not receive convenience defaults;
- measured state variables are not relabelled as measured hydraulic parameters;
- a fitted or pedotransfer-derived hydraulic function retains derived provenance and diagnostics/uncertainty;
- Staring/BOFEK/SoilPhys modal values are context/method priors unless separately qualified for the intended state;
- CURRENT and REFERENCE use the same transformation family/version and equivalent predictor semantics for simple matched attribution where scientifically possible;
- asymmetric transformation methods become an explicit additional source of contrast and require separate qualification;
- no single ensemble member may be selected because it yields a preferred hydrological response.

For an analytical Mualem–Van Genuchten representation, `H` may contain `theta_r`, `theta_s`, `alpha`, `n`, `Ksat` and the conductivity exponent plus configuration-dependent optional terms. For tabular input, `H` references the complete qualified retention/conductivity table.

This relation defines architecture and provenance. It does not supply numerical Tollebeek parameters.

## 4.18 Formal status

This formal baseline is sufficient for the current Tollebeek source → transfer → dispatch vertical slice. It remains incomplete for full project scope, especially:

- crop/yield response functions;
- numerical qualification/admission of current/reference hydraulic parameter sets under the explicit hydraulic-transformation contract;
- event occurrence/magnitude transfer models;
- nutrient and pesticide pathways;
- national scaling and nonlinear aggregation;
- full societal-welfare valuation.

New formal relations should be added only when their variables, grain, units, evidence requirements and test strategy are also made explicit.
