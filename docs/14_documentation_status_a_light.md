# Status-A-light documentation contract

Status: **project documentation governance v0.1**

## 1. Purpose

The repository does not claim a complete Status A dossier. It adopts a Status-A-like discipline early so that scientific meaning, implementation and evidence can be reviewed without reconstructing the project from spreadsheets or chat history.

The required traceability chain is:

**theory → conceptual model → formal model → data model → implementation → evidence/qualification → artifact/application**

A material change should be traceable through every layer that it affects.

## 2. Documentation layers

### Layer T — theory

Describes why a relation is scientifically expected and under which physical, biological or economic conditions it applies.

Canonical home: `02_theoretical_framework.md` plus source/evidence registers.

### Layer C — conceptual model

Defines the objects and processes that the project distinguishes before implementation details are introduced.

Canonical home: `03_conceptual_model.md` and `schema/entities.yml` / `schema/relationships.yml`.

### Layer F — formal model

Defines equations, variables, states, units, allowed transitions and decision rules.

Canonical home: `04_formal_model.md`, model-equation datasets and testable code contracts.

### Layer D — data model

Defines stable entities, dataset identity, row grain, field meaning, null semantics and controlled vocabularies.

Canonical home: `05_data_model.md` and `schema/`.

### Layer I — implementation

Defines how formal concepts are realised in code, adapters, generated workbooks and eventually the application.

Canonical home: `06_implementation.md`, `src/`, `tools/` and `tests/`.

### Layer E — evidence and qualification

Separates source, atomic evidence, project interpretation and intended-use qualification.

Canonical home: `07_evidence_and_qualification.md` and `evidence/`.

### Layer A — artifact/application

Defines how users see or interact with canonical state without making the artifact itself authoritative.

Canonical home: `08_workbook_architecture.md`, artifact specifications and future application documentation.

## 3. Minimum metadata for substantive documents

Substantive project documents should make the following clear either in a short header or in the opening section:

- purpose;
- scope;
- intended audience;
- maturity/status;
- canonical or supporting role;
- important dependencies;
- known limitations;
- what would cause the document to require review.

The project does not require formal Status A cover sheets at this stage. The purpose is traceability, not paperwork for its own sake.

## 4. Maturity states

Recommended documentation states are:

- `SKELETON`: structure exists but substantive content is incomplete;
- `WORKING_BASELINE`: sufficiently coherent to support project work and review, but not fully qualified;
- `QUALIFIED_FOR_DEFINED_USE`: reviewed and supported for an explicitly defined use;
- `DATA_GATED`: structure is ready but substantive completion depends on unavailable data;
- `SUPERSEDED`: retained for history but no longer current;
- `REFERENCE_ONLY`: useful background that is not normative for current project state.

No document should be called simply `FINAL` unless the project later defines a formal release process.

## 5. Scientific claims in prose

Narrative documentation may explain project reasoning, but it must not become an untracked substitute for evidence registers.

For material scientific or administrative statements:

1. the source should be identifiable;
2. the atomic fact should be representable as an evidence item where practical;
3. project interpretation should be distinguishable from source wording;
4. the intended use should be qualified where it drives calculation or model structure;
5. important prohibited uses should be recorded as guardrails.

A prose sentence is therefore not automatically a canonical parameter definition.

## 6. Equations and formal rules

Every equation that affects project results should eventually have:

- stable identifier;
- variables and units;
- domain of validity;
- null/missing-data behaviour;
- evidence or theoretical basis;
- code implementation location;
- tests or qualification evidence;
- known exclusions.

The formal model may initially document equations before all of these fields are populated, but missing elements must remain visible.

## 7. Data-model documentation

Every canonical dataset should state:

- `dataset_id`;
- entity or entity relation represented;
- role such as reference, input, output, evidence or governance;
- row grain;
- primary key;
- canonical fields;
- controlled vocabularies where applicable;
- provenance expectations;
- qualification expectations;
- legacy mappings if data originated in prototype workbooks.

Every canonical field should state at least label, description, datatype, unit where applicable, nullability and critical guardrails.

## 8. Workbook documentation

Generated workbooks are review/user artifacts.

Each generated workbook should expose:

- `00_METADATA`;
- `01_GUIDE`;
- `DATA_DICTIONARY`;
- dataset-level metadata including grain and key;
- short header help derived from the canonical field schema;
- a visible distinction between source/data tables and views;
- artifact version, schema version and repository commit where available.

Unknown scientific values remain blank/null. The workbook must not improve visual completeness by manufacturing numeric defaults.

## 9. Code documentation and tests

Code that implements a scientific equation or semantic rule should identify the corresponding formal concept in its module/function documentation or nearby project documentation.

Tests are classified conceptually as at least one of:

- software/contract test;
- numerical identity test;
- evidence/register integrity test;
- model qualification test;
- empirical validation test.

Passing software tests does not qualify a physical model result.

## 10. Traceability matrix

The project maintains a lightweight traceability matrix linking major scientific capabilities across documentation, schema, implementation and evidence.

The machine-readable capability register in `model/traceability.csv` is the integrity-controlled traceability baseline. `15_traceability_matrix_v0_1.md` remains a readable Tollebeek-first capability snapshot. Current project-wide maturity and authority are summarised in `58_project_architecture_status_v0_1.md`.

These surfaces are not intended to duplicate all information from the repository. Their purpose is to reveal broken links and direct reviewers to the canonical layer.

## 11. Review triggers

A document or qualification should be revisited when a relevant dependency changes, for example:

- a new source overturns an admitted asset value;
- a model equation changes;
- dataset grain or field meaning changes;
- current geometry or drainage evidence replaces a prior;
- a historical benchmark is replaced by current measurement;
- the application starts consuming a field differently;
- a scientific pathway is extended from pilot to national use.

A new Excel export by itself is not a scientific review trigger.

## 12. Documentation work priority

Documentation effort should follow scientific risk rather than file count.

Priority order:

1. definitions that affect attribution or interpretation;
2. formal relations that affect calculations;
3. fields/datasets that cross module boundaries;
4. evidence that determines parameter admission;
5. user-facing interpretation of outputs;
6. lower-risk descriptive or UI detail.

This prevents the project from spending disproportionate effort documenting legacy workbook layout while more important scientific dependencies remain unclear.
