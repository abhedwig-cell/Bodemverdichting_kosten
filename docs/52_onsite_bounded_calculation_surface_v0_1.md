# First bounded on-site calculation surface v0.1

Status: **BOUNDED WORKING SURFACE — NO DAMAGE RESULT ADMITTED**  
Parent methods: `49_project_effect_pathway_matrix_v0_1.md`, `50_evidence_ensemble_protocol_v0_1.md`  
Canonical response migration: `51_onsite_ensemble_source_migration_v0_1.md`

## 1. Purpose

This workunit creates the first calculation surface that a colleague can actually continue from without inventing missing values.

The target is deliberately modest:

```text
reporting area
  × crop share where needed
  × current compaction exposure
  × qualified response ensemble
  × explicit economic valuation
  = bounded on-site cost result
```

At v0.1, several terms are intentionally blank. The output is therefore a **bounded no-result surface**, not a Dutch damage estimate.

Machine-readable surface:

`evidence/onsite_bounded_calculation_surface_v0_1.csv`

## 2. Why a no-result surface is useful

A conventional spreadsheet often encourages missing cells to be filled so that a total can be produced.

This surface does the opposite. It makes the calculation executable only when every causal term has a qualified meaning.

For each row, it records:

- known reporting area;
- whether the crop occupies the whole reporting class or needs a crop crosswalk;
- current compaction exposure;
- required exposure dimension;
- response ensemble;
- response transfer status;
- economic-value readiness;
- current permitted output;
- blocker;
- next action.

This turns missing knowledge into a project plan rather than a hidden assumption.

## 3. Public CC-NL state checked on 18 September 2026

The current repeat CC-NL project is publicly listed by WUR as active for 2024–2026, ending 31 December 2026.

The bounded public review for this workunit did not identify a final published table supplying the required current exposure as:

```text
land use × soil × depth × severity
```

Therefore:

`CURRENT_COMPACTION_EXPOSURE = WAIT_DATA`

This is a dated public-route conclusion. It must be rechecked when the CC-NL project releases results or if direct project-holder data become available.

The published 2018 CC-NL report remains useful as a national structural/historical baseline, but it is not a 2026 exposure dataset.

## 4. Area basis

The earlier project workbook contained a 12-domain 2018 reporting basis derived from Van den Elsen et al. (2020).

This surface carries forward only four priority parent strata:

| Surface | Parent context | Inherited 2018 area |
|---|---|---:|
| grass / other sandy soils | NL_GR_ZAND | 331,592 ha |
| grass / sandy soils with thick plaggen layer | NL_GR_EERD | 124,495 ha |
| arable / other sandy soils | NL_AK_ZAND | 348,814 ha |
| arable / sandy soils with thick plaggen layer | NL_AK_EERD | 94,578 ha |

These exact area figures are marked:

`MIGRATION_BASELINE_REVERIFY_TABLE`

They may structure the calculation and review work, but table-level source provenance should be reverified before they are used in a published numeric result.

This distinction matters because the calculation is currently blocked elsewhere anyway; there is no benefit in pretending that an inherited workbook number is already a fully re-admitted production input.

## 5. Grass surfaces

For grassland, `crop_share = 1.0` is used only as a **land-use identity**:

```text
grassland reporting unit → grass response pathway
```

It does not mean:

- every hectare has the same species;
- every hectare has the same management;
- the grass/sand ensemble is universally transferable;
- the whole area is compacted.

For `NL_GR_ZAND`, the current response candidate is:

`ENS_O1_GRASS_SAND`

but this remains a `SCENARIO_ENSEMBLE`.

For `NL_GR_EERD`, an additional context-match gate is retained because the available evidence is not automatically transferable to soils with a thick plaggen layer.

No damage percentage is assigned.

## 6. Maize surfaces

The published parent class is **arable land on a soil class**, not silage maize.

Therefore:

```text
maize_share = blank
```

and:

`crop_share_status = WAIT_CROP_CROSSWALK`

The parent areas 348,814 ha and 94,578 ha must never be multiplied directly by a maize response coefficient.

A reproducible crop × soil crosswalk is required first.

Candidate data routes include BRP/CBS/LGN or another qualified crop-area source, but the chosen route must preserve year and spatial semantics.

## 7. Current-exposure contract

The exposure term must eventually describe the share of the relevant surface to which a stated compaction condition applies.

At minimum the intended dimension is:

```text
soil / land use
  × depth interval
  × severity/state class
```

A headline prevalence percentage without these semantics is insufficient.

In particular, this surface explicitly rejects:

- using a historical national prevalence figure as current exposure;
- using the old workbook demo values;
- using 32% or 37% headline fractions directly as a yield-damage multiplier;
- treating "any compaction somewhere in profile" as equivalent to a crop-specific damaging state.

## 8. Response contract

The response term is not one global coefficient.

For every calculation member:

```text
response =
  qualified ensemble member
  + explicit comparator/reference
  + matching soil/crop/weather context
```

### Grass

The existing ensemble contains:

- non-monotonic field evidence;
- sign-changing field evidence;
- long-term inverse soil-improvement scenarios;
- dry-year inverse scenarios.

This structure currently supports scenarios/guardrails, not a central damage coefficient.

### Maize

The existing ensemble contains:

- Dutch axle-load field-response evidence;
- a historical national benchmark;
- long-term inverse soil-improvement scenarios;
- dry-year inverse scenarios.

No axle-load-to-CC-NL severity mapping is admitted.

## 9. Valuation contract

A physical yield response can be converted to money only after the economic perspective is chosen.

At least the following remain distinct:

### Gross revenue/accounting

```text
C_gross = A_affected × response_fraction × gross_money_yield_per_ha
```

Useful as a transparent accounting measure or upper-bound style result.

### Farmer-private marginal damage

```text
C_private =
  lost output revenue
  - genuinely avoided yield-dependent costs
  + extra compaction-related operating costs
```

Preferred when the question is "what does this cost the farmer?"

### Societal production/welfare

Must be reported separately. Lost production value is not automatically societal welfare loss and must not be added blindly to private damage.

At v0.1:

`economic_value_status = WAIT_ECONOMIC_VALUE`

## 10. Calculation states

A row can move through these states:

```text
AREA_CONTEXT_ONLY
 → EXPOSURE_BOUND
 → RESPONSE_SCENARIO_BOUND
 → ECONOMIC_INPUT_BOUND
 → BOUNDED_RESULT
```

The current four rows are:

`BOUNDED_NO_DAMAGE_RESULT`

because no current exposure is admitted and maize also lacks crop share.

## 11. What is already calculable

Even without a cost result, the project can already report:

- which national reporting strata are priority targets;
- which response evidence applies or may apply;
- which response evidence is non-transferable;
- which exact data fields block the next step;
- why a national number would currently be premature;
- which additional evidence has the highest information value.

This is a valid project output.

## 12. Immediate next data priorities

### P1 — current compaction exposure

Acquire or wait for CC-NL output that preserves depth and severity.

### P1 — maize crop × soil crosswalk

Determine how much silage maize occurs within the relevant sandy arable soil strata.

### P1 — economic values

Qualify crop-specific current economic data and decide which valuation perspective is being reported.

### P2 — table-level area re-verification

Reverify the inherited 2018 parent-area values directly against the published source/table before using them in a final numeric publication.

## 13. Escalation rule

Do **not** add a process model merely because the surface has empty cells.

First ask whether the missing term can be supplied by:

1. existing data;
2. direct source-holder data;
3. literature evidence;
4. a transparent scenario.

Only if the remaining response uncertainty is both important and model-reducible should SWAP/WOFOST or another process model be considered.

## 14. Verdict

The first onsite calculation surface is structurally ready but intentionally not numerically closed.

The correct present state is:

`AREA/ENSEMBLE ARCHITECTURE READY — CURRENT EXPOSURE DATA GATED — NO DAMAGE RESULT`

This is progress: the next work can now target the specific missing causal terms instead of building a larger model by default.
