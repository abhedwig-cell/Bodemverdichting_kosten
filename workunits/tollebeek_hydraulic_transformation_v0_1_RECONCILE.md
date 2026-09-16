# Tollebeek hydraulic transformation v0.1 — RECONCILE

Capability: soil-state → hydraulic parameterization for SWAP source-response modelling

Phase: `RECONCILE → EVIDENCE REVIEW → DESIGN → QUALIFY → CLOSE`

Canonical start: `45735b863a588db2b009a2908af6e324f717257c`

## Why this is a distinct decision surface

The canonical project already distinguishes:

- intrinsic/modal `SoilProfile` / `SoilLayer` context;
- `SoilState` for CURRENT / REFERENCE / SCENARIO;
- `ModelConfiguration` for shared model/boundary/numerical choices;
- `ModelRun` for an execution.

However, no canonical object currently records how an observed or constructed soil state is transformed into the hydraulic functions actually consumed by SWAP.

The theoretical and formal baselines explicitly identify construction of current/reference hydraulic parameter sets as incomplete.

## Existing scientific boundary

- `bulk_density_g_cm3` is a nullable `soil_state` variable.
- SoilPhys `modal_bulk_density_g_cm3` remains profile context and is not CURRENT anthropogenic compaction.
- Texture / organic matter are layer/profile context unless the scientific question explicitly changes them.
- CURRENT and REFERENCE must remain matched on external controls for simple soil-state attribution.
- No current Tollebeek CURRENT state has been admitted.

## SWAP target semantics

SWAP supports per soil-physical layer either:

1. analytical Mualem–Van Genuchten hydraulic functions, with parameters including residual and saturated water content, alpha, n, saturated conductivity / fitting conductivity and conductivity exponent; or
2. tabulated soil hydraulic functions.

Dry bulk density is also an explicit SWAP soil input but does not by itself identify the complete hydraulic functions.

## Evidence reviewed

- SWAP version 4 theory/user guide, DOI `10.18174/416321`.
- Staringreeks update 2018, DOI `10.18174/512761`.
- Wösten et al. / HYPRES and Vereecken et al. 2010 review of pedotransfer functions, DOI `10.2136/vzj2010.0045`.
- Van der Bolt et al. 2016, *Bodemverdichting in Vlaanderen*, DOI `10.18174/387766`.
- Bakema et al. 2024, BoVer final report, DOI `10.18174/675719`.
- Mossadeghi-Björklund et al. 2019, DOI `10.1111/sum.12481`.
- Tian et al. 2019 / 2021 studies on bulk-density-responsive hydraulic conductivity and retention functions.

## Initial evidence synthesis

1. Hydraulic response to compaction is mediated by pore volume, pore-size distribution, structure and connectivity; bulk density is informative but not sufficient to uniquely determine a complete hydraulic function.
2. PTFs can estimate hydraulic functions from combinations of texture, bulk density, organic matter and related predictors, but method domain and prediction uncertainty matter.
3. Dutch/Flemish WUR work demonstrates a defensible workflow in which measured hydraulic data support PTFs responsive to bulk density, curves are predicted, Mualem–Van Genuchten functions are fitted and SWAP is used for response experiments.
4. Direct measured hydraulic curves or parameters are higher-authority than a generic PTF for a local state when representative measurements exist.
5. Staring/BOFEK provide strong modal hydraulic context but are not automatically the hydraulic expression of an observed anthropogenic CURRENT or constructed REFERENCE compaction state.

## Proposed object boundary

Introduce conceptually a `HydraulicParameterization` between `SoilState` and `ModelRun`.

Proposed grain:

`one row/object per soil_state × hydraulic method/version × uncertainty/member × representation`

It must retain:

- source soil-state identity;
- method family and exact method/version;
- predictor/input identities;
- output representation (`MVG_ANALYTICAL`, `HYDRAULIC_TABLE`, or future explicit representation);
- fitted/derived parameters or table authority;
- uncertainty/member identity;
- fit/validation diagnostics where applicable;
- evidence/qualification status;
- model adapter/version used to serialize to SWAP.

## Matching rule

For a simple CURRENT/REFERENCE soil-state attribution:

- use the same transformation family/version and equivalent predictor semantics where feasible;
- differences in resulting hydraulic functions may follow from the admitted soil-state contrast;
- do not use a direct-measured method for one pair member and an unrelated generic PTF for the other and then label the delta a clean soil-state effect without separate decomposition/qualification.

## Null/default rule

No missing hydraulic parameter is filled by:

- SoilPhys modal values;
- Staring/BOFEK class means;
- arbitrary compacted/uncompacted multipliers;
- default porosity from an assumed particle density;
- SWAP example values;
- null → zero.

Such values may only enter a separately labelled method prior or scenario after qualification.

## Current verdict

`DESIGN_REQUIRED — NUMERICAL_PARAMETERIZATION_NOT_AUTHORIZED`

No model run and no Tollebeek hydraulic parameter values are admitted by this checkpoint.

## Next permitted action

Persist the transformation protocol; then update conceptual/formal/schema contracts only if the object remains scientifically distinct after review.