# Evidence ensemble protocol v0.1

Status: **WORKING METHOD BASELINE**  
Parent: `49_project_effect_pathway_matrix_v0_1.md`  
Purpose: define how multiple literature/data sources can jointly inform one effect pathway without creating a false single coefficient.

## 1. Why an ensemble is needed

Several project pathways have more than one potentially relevant source. Their estimates may differ because they do not measure exactly the same thing.

Differences can arise from:

- soil;
- crop;
- weather;
- compaction treatment/state;
- depth;
- comparator/reference;
- time horizon;
- measurement/model method;
- geographic context.

The project therefore treats source plurality as information, not as noise that must immediately be averaged away.

## 2. Ensemble object

An ensemble is defined for one explicit target question.

Example:

```text
What yield response can be defended for silage maize on sandy mineral soils
under a specified compaction/reference contrast?
```

Each member retains its own metadata.

Minimum member fields:

- source/evidence ID;
- effect definition;
- soil context;
- crop/land use;
- compaction metric/treatment;
- comparator;
- time/weather context;
- low/base/high or source-reported interval;
- unit;
- directness;
- transferability;
- allowed use;
- prohibited use.

## 3. Member roles

### DIRECT_CANDIDATE
Close enough to the target question to be considered for direct quantitative transfer after qualification.

### PROXY
Mechanistically or empirically relevant, but one or more material dimensions do not match.

### BOUND
Useful for an upper/lower or magnitude constraint, not as a central coefficient.

### SCENARIO
Represents a specific state such as a dry year, extreme event or alternative reference.

### BENCHMARK
Useful for comparison only.

### GUARDRAIL
Evidence whose main value is to show why a simple monotonic or universal relation is unsafe.

## 4. Ensemble verdicts

### COMPARABLE_ENSEMBLE
Members are similar enough that a combined range or, later, formal synthesis may be defensible.

### BOUND_ENSEMBLE
Members jointly constrain plausible magnitude but do not support a central estimate.

### SCENARIO_ENSEMBLE
Members represent materially different contexts; report them separately as scenarios.

### INCOMPATIBLE_SET
Sources are informative but should not be numerically combined.

### SINGLE_SOURCE_ONLY
Only one usable quantitative source exists; retain its own uncertainty and do not manufacture between-source uncertainty.

## 5. Default combination rule

**Do not average by default.**

The first output should be one of:

- source-member table;
- source envelope;
- scenario set;
- bounded range;
- explicit incompatibility statement.

A weighted or statistical pooled estimate requires a separate method justification.

## 6. Two levels of uncertainty

The ensemble must preserve:

### Within-source uncertainty
The range, confidence interval, scenario range or sensitivity reported by the study itself.

### Between-source uncertainty
The spread caused by different studies, designs and contexts.

These should not be conflated.

## 7. Direction and sign

Some recovered evidence is reported as:

- damage after compaction;
- benefit after soil improvement;
- difference from a lower-load treatment;
- historical national attribution.

These are not automatically algebraic inverses.

The register therefore keeps `effect_direction` and `comparator` explicit. Reverse-direction evidence remains `PROXY` unless equivalence is separately justified.

## 8. Weather and time

Long-term average, dry-year, event and persistent multi-year evidence belong to different scenario/time strata.

A dry-year effect should not be averaged into a long-term annual estimate unless the frequency weighting is explicitly modelled.

## 9. Transfer to Dutch national estimates

Before an ensemble can feed a national calculation, it needs a transfer decision for:

- Dutch soil/context;
- crop/land use;
- exposure definition;
- depth/severity;
- weather/time basis;
- reference state.

A national estimate may use different ensembles for different soil × crop or hydrological-system strata.

## 10. Initial seed ensembles

The first seed register is stored in:

`evidence/evidence_ensemble_register_v0_1.csv`

It is intentionally conservative. Existing legacy-workbook evidence is grouped to show how the method works; no new national coefficient is admitted.

## 11. Escalation to new modelling

A model should be considered when:

- ensemble members remain too context-dependent to answer the target question;
- the unresolved mechanism materially dominates the final cost range;
- a model can use observed/qualified state data to reduce that uncertainty.

A model should not be added merely because multiple sources disagree.

## 12. Admission boundary

This protocol admits the **ensemble method**, not the numerical transfer of any ensemble to a current Dutch policy estimate.

Each future ensemble-to-result use still requires its own applicability and valuation qualification.
