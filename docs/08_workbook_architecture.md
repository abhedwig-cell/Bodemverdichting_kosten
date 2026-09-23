# 8. Workbook architecture

## Purpose

This document defines how Excel workbooks fit into the project architecture.

The workbook is a **user-facing artifact**, not the canonical data model. Scientific meaning, dataset definitions, field definitions, evidence status and model semantics live in the repository. Workbooks should expose that canonical meaning in a readable form.

The governing chain is:

**theory → conceptual model → formal model → data model → implementation → artifact**

Evidence and qualification connect to every layer.

## Core rule

**One table = one clearly defined dataset object.**

A table should not mix unrelated grains. If two sections have different row meaning, they are different datasets even when they happen to fit on one worksheet.

Every dataset needs:

- a stable `dataset_id`;
- a clear purpose;
- an owning entity or relationship;
- an explicit grain;
- a primary key or candidate key where applicable;
- canonical field definitions;
- provenance and qualification semantics;
- a declared artifact role.

## Workbook classes

The prototype lineage already contains more than one kind of workbook. These classes are now explicit:

- `FULL_FRAMEWORK_SNAPSHOT`: broad integrated workbook intended to expose many project domains.
- `BOUNDED_MODULE`: a focused workbook for one capability, case, pilot or evidence campaign.
- `REVIEW_ARTIFACT`: a workbook primarily intended for review/decision support.
- `GENERATED_REPORT`: a workbook generated from canonical project state.
- `LEGACY_PROTOTYPE`: historical workbook retained for traceability but not used as canonical state.

A higher version number does **not** imply that a workbook contains all earlier sheets or is a cumulative replacement.

## Required workbook front matter

Future generated workbooks should begin with:

### `00_METADATA`

Machine- and human-readable artifact metadata. Minimum fields:

- `project_id`
- `artifact_id`
- `artifact_class`
- `artifact_version`
- `framework_version`
- `schema_version`
- `generated_on`
- `git_commit`
- `purpose`
- `scope`
- `intended_audience`
- `canonical_status`
- `input_datasets`
- `evidence_snapshot`
- `known_limitations`
- `owner`
- `contact`

### `01_GUIDE`

A short reader guide explaining:

- what the workbook contains;
- which sheets are source data, model inputs, outputs, evidence, qualification or views;
- which cells are editable;
- which values are examples/scenarios;
- which outputs are blocked or not yet qualified;
- where to find the canonical definitions.

### `DATA_DICTIONARY`

A generated view of canonical field definitions used in the workbook.

Minimum columns:

- `field_id`
- `label`
- `description`
- `entity`
- `dataset_id`
- `datatype`
- `unit`
- `nullable`
- `vocabulary`
- `provenance_class`
- `qualification_rule`
- `guardrail`

## Dataset-level metadata

Each data-bearing sheet should expose a compact metadata block before or beside the table, or through a standard linked metadata sheet.

Minimum dataset metadata:

- `dataset_id`
- `entity`
- `role`
- `grain`
- `primary_key`
- `canonical_status`

Recommended contextual metadata includes `dataset_version`, purpose, source or derivation, qualification status and known limitations when those are separately defined. Do not invent those values to make the workbook look complete.

Here `canonical_status` uses the shared controlled vocabulary for canonicality/readiness of the exposed dataset instance. More detailed operational states such as `WAIT_DATA` or `PARTIAL_EVIDENCE` belong in explicit readiness/status views and must not be smuggled into `canonical_status`.

## Field-level help in Excel

Column labels must stay short enough to keep tables readable.

Long definitions belong in the canonical field dictionary. Workbooks should expose contextual help on the column header through a supported mechanism, for example:

1. cell note/comment, preferably generated from the canonical field description; or
2. data-validation input message when comments are not supported by the generator.

The help text should normally contain:

- human-readable definition;
- unit;
- row/grain context if needed;
- provenance/status cue;
- one important guardrail where relevant.

Example:

> **Extra generated surface runoff**  
> Difference in generated parcel runoff between matched current and reference states for the same event. Unit: mm/event. This is not field-edge, ditch or pump volume.

`DATA_DICTIONARY` remains authoritative when tooltip/help mechanisms differ between spreadsheet software.

## Sheet roles

A workbook may expose the following roles:

- `METADATA`
- `GUIDE`
- `DATASET`
- `MODEL_INPUT`
- `MODEL_OUTPUT`
- `EVIDENCE`
- `QUALIFICATION`
- `GOVERNANCE`
- `DATA_REQUEST`
- `VIEW`
- `DASHBOARD`
- `LEGACY_COMPATIBILITY`

Views and dashboards must not silently become source tables.

## Workbook generation rule

The preferred long-term direction is:

**canonical schema + canonical data/evidence + code → generated workbook**

rather than:

**hand-edited workbook → reverse-engineered application**

Manual workbook edits may remain useful during research, but any scientifically relevant change should ultimately be reconciled back into canonical project state.
