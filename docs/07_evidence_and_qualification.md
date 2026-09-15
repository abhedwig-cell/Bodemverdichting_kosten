# 7. Evidence and qualification

Status: **Status-A-light evidence baseline**

## 7.1 Principle

A source citation, an observed value, a project claim, a model input and a qualified/admitted use are different states.

The evidence system exists to prevent a common failure mode in modelling projects: a number is found in a report, copied into a workbook and gradually becomes an unquestioned model parameter even though its original scope or definition was different.

The project therefore records the chain:

```text
Source
  ↓
EvidenceItem
  ↓
Claim
  ↓
Qualification for an intended use
  ↓
Model/data/application use
```

The current implementation does not require a separate `AdmissionDecision` record for every value; admission semantics can be carried by the evidence/qualification status and the consuming configuration. A distinct admission object can be introduced later where governance requires it.

## 7.2 Source

A `Source` identifies a document, dataset, service or system/version.

Examples include:

- peer-reviewed literature;
- official administrative documents;
- water-board asset/operations information;
- WUR datasets/services;
- model reports;
- measured datasets;
- internal project data where governance allows registration.

A source-level status describes the source record, not every fact within it.

A reliable source can contain a value that is still inappropriate for a particular project use because the scale, definition or time differs.

## 7.3 Evidence item

An `EvidenceItem` is one atomic extractable fact, measurement, relation or historical model setting.

Good evidence items are deliberately narrow. For example:

> IJsvogel has three large screw pumps with combined installed capacity 540 m3/min.

is preferable to:

> The Tollebeek pump system has enough capacity.

The second sentence is already an interpretation and depends on event load, availability, routing and other assumptions.

Evidence items should state, where relevant:

- source ID;
- statement;
- spatial scope;
- time scope;
- value and unit;
- provenance class;
- intended use;
- guardrail;
- evidence status.

## 7.4 Claim

A `Claim` records the project's interpretation of one or more evidence items.

Claims are necessary because modelling often requires reconciliation rather than direct copying.

Example pattern:

```text
Evidence A: nominal Kievit hardware description = 60 m3/min
Evidence B: historical calculated capacity = 1.44 m3/s
Evidence C: installation renovated in 2020
        ↓
Claim: current effective operational capacity is unknown;
       the existing figures represent different definitions/states.
```

Keeping the claim separate from the source facts means a future post-2020 pump curve can change the project interpretation without rewriting the historical evidence.

## 7.5 Qualification

Qualification answers:

> does this evidence support this specific intended project use?

A useful qualification record states:

- evidence or claim being assessed;
- intended use;
- relevant dependencies;
- test, reconciliation or review performed;
- verdict;
- review date;
- limitations/notes.

The same evidence can therefore be:

- qualified for use as a historical benchmark;
- rejected as a current model parameter;
- retained as context for a data request.

There is no contradiction because the intended uses differ.

## 7.6 Evidence status versus qualification status

These are related but not identical.

### Evidence status

Describes the role/standing of the evidence item itself. The current controlled vocabulary includes statuses such as:

- `ADMITTED`;
- `QUALIFIED`;
- `BENCHMARK_ONLY`;
- `METHOD_PRIOR`;
- `SCENARIO_ONLY`;
- `CONTEXT_ONLY`;
- `SOFTWARE_QA_ONLY`;
- `WAIT_DATA`;
- `BLOCKED`;
- `REJECTED_FOR_PROJECT_USE`.

### Qualification status

Describes the verdict for a defined intended use, for example:

- `NOT_REVIEWED`;
- `REVIEWED`;
- `QUALIFIED`;
- `QUALIFIED_WITH_LIMITATIONS`;
- `REJECTED`;
- `BLOCKED_DATA`.

A `BENCHMARK_ONLY` evidence item can therefore have a `QUALIFIED_WITH_LIMITATIONS` qualification for the intended use `historical plausibility benchmark`.

## 7.7 Provenance classes

Current provenance classes include:

- `DIRECT_MEASUREMENT`;
- `DERIVED_MEASUREMENT`;
- `OFFICIAL_METADATA`;
- `PEER_REVIEWED_RELATION`;
- `MODEL_OUTPUT`;
- `HISTORICAL_BENCHMARK`;
- `SCENARIO_ASSUMPTION`;
- `SOFTWARE_QA`.

Provenance class is descriptive, not a universal quality ranking.

For example, official administrative metadata can be authoritative for a peil-area identifier but unsuitable for a soil hydraulic response coefficient.

## 7.8 Qualification questions

For important evidence, reviewers should be able to answer:

1. **What exactly is the quantity or relation?**
2. **What are its units and sign/definition?**
3. **Which spatial domain does it represent?**
4. **Which time/state does it represent?**
5. **Was it measured, derived, modelled or administratively defined?**
6. **Which model quantity may it support?**
7. **Which dependencies must remain unchanged?**
8. **Is the intended transfer of scale/context defensible?**
9. **What independent check or reconciliation was performed?**
10. **What use is explicitly prohibited?**

If these cannot be answered, the project should normally retain the evidence but block the intended use rather than fill the gap with assumption.

## 7.9 Guardrails

A guardrail is a concise statement of a likely misinterpretation that is forbidden or conditional.

Examples from the current project include:

```text
1497 ha system area != affected compaction area
installed pump capacity != event-specific available capacity
managed target level != total dynamic pump head
generated runoff != ditch or pump volume
historical drainage resistance != current OT.02 calibrated resistance
modal soil profile != direct parcel measurement
```

Guardrails are intentionally duplicated into the data dictionary/workbook interface where they help prevent user error.

## 7.10 Evidence inheritance and dependency change

Evidence should not be re-qualified merely because a new workbook or application version was created.

A qualification can be reused while its relevant dependencies remain unchanged.

Examples:

- a source document does not become invalid because the workbook layout changes;
- an IJsvogel installed-capacity qualification can survive a new dashboard version;
- a reference-state response qualification may need review if the reference-state construction changes;
- a pump-energy result must be re-evaluated if the operating head or efficiency definition changes.

This is the project equivalent of immutable evidence inheritance.

## 7.11 Evidence for measurements versus evidence for models

The project distinguishes at least four uses of evidence.

### State evidence

Supports what exists physically or administratively, such as bulk density, soil type, geometry or pump metadata.

### Relation/method evidence

Supports a process relation or modelling method, such as a pedotransfer approach or historical drainage representation.

### Validation evidence

Provides an independent outcome against which a model result can be compared.

### Operational evidence

Supports how a managed system actually functions, such as telemetry, control rules, availability or energy use.

One dataset can sometimes support multiple uses, but each use should be stated separately.

## 7.12 Software evidence is not scientific evidence

Synthetic fixtures and unit tests are essential for implementation quality, but their scientific role is limited.

A test such as:

```text
100 ha × 10 mm = 10,000 m3
```

qualifies the implementation of the conversion identity. It does not show that 10 mm extra runoff occurs in Tollebeek.

Similarly, a synthetic 50% pump-assist test can verify dispatch arithmetic without providing any evidence that the real system uses a 50% assist fraction.

The project therefore labels such evidence `SOFTWARE_QA` or documents it explicitly as software-only.

## 7.13 Model-output qualification

A model output should move through several questions before it becomes an application result.

A possible progression is:

```text
run completed
    ↓
software/numerical checks pass
    ↓
input state and configuration qualified
    ↓
mass balance / numerical behaviour acceptable
    ↓
response plausible against independent evidence
    ↓
transfer applicability established
    ↓
result admitted for stated reporting scope
```

A model can run successfully while the result remains scientifically blocked.

## 7.14 Current Tollebeek example

The Tollebeek evidence baseline demonstrates the architecture.

### Qualified with appropriate scope

Current examples include:

- 1,497 ha as an administrative area benchmark, with explicit distinction from affected area;
- NAP -6.20 m as managed-level context, not dynamic pump head;
- 540 m3/min as IJsvogel installed capacity, with availability separate;
- coupled Kievit/IJsvogel topology;
- directional Kievit-zone → IJsvogel assist semantics;
- historical NOP drainage settings as method priors only.

### Still data-gated

Examples include:

- reviewed current OT.02 geometry;
- current spatial drainage configuration;
- current/reference depth-resolved soil state;
- event field-edge/network transfer;
- post-2020 current Kievit pump curve;
- event-specific assist/control rule;
- current total dynamic head and efficiency;
- attributable event/annual pump energy and cost.

This split is captured in the canonical registers rather than being left only in narrative notes.

## 7.15 Canonical registers

The current canonical evidence layer is:

- [`../evidence/sources.csv`](../evidence/sources.csv)
- [`../evidence/evidence_register.csv`](../evidence/evidence_register.csv)
- [`../evidence/claims.csv`](../evidence/claims.csv)
- [`../evidence/qualification_register.csv`](../evidence/qualification_register.csv)

The registers are validated by `tools/validate_evidence.py` and repository CI checks identifiers, foreign keys and controlled-vocabulary values.

The workbook generator reads these registers into the review artifact rather than maintaining an independent evidence copy.

## 7.16 Relationship to literature synthesis

Narrative literature review and machine-readable evidence serve different functions.

The theoretical documentation should explain the broader state of knowledge and competing mechanisms. The evidence register should capture specific extractable project-relevant facts or relations with explicit intended use.

A literature statement should therefore not be omitted from prose merely because it has an evidence ID, and a citation in prose should not replace the evidence record for a value used in the model.

## 7.17 Review levels

Not every evidence item needs the same review burden.

A practical risk-based approach is:

- **low risk**: labels, navigation metadata, non-critical display information;
- **medium risk**: scenario bounds, contextual priors, secondary benchmarks;
- **high risk**: causal response relations, current/reference definitions, transfer coefficients, operational capacity, cost parameters that materially affect reported conclusions.

Higher-risk evidence should receive more independent review and stronger traceability.

The project should avoid turning this principle into unnecessary bureaucracy for low-risk metadata.

## 7.18 Status-A-light expectation

For an important reported result, Status-A-light documentation should make it possible to trace:

```text
reported result
  ↓
model/output record
  ↓
formal relation / code version
  ↓
input/configuration records
  ↓
evidence/claims/qualifications
  ↓
source
```

Not every link is complete today. The purpose of the current architecture is to make missing links explicit and progressively close them, rather than hide them behind a finished-looking spreadsheet.
