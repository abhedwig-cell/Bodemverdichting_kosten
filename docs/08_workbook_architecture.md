# 8. Workbook architecture

## Purpose

This document defines how Excel workbooks fit into the project architecture.

The workbook is a **user-facing artifact**, not the canonical data model. Scientific meaning, dataset definitions, field definitions, evidence status and model semantics live in the repository. Workbooks expose that canonical meaning in a readable form.

The governing chain is:

**theory → conceptual model → formal model → data model → implementation → artifact**

Evidence and qualification connect to every layer.

## Core rule

**One table = one clearly defined dataset object.**

A table should not mix unrelated grains. If two sections have different row meaning, they are different datasets even when they happen to fit on one worksheet.

Dataset identity, role, grain, key and field meaning come from the canonical repository contracts. A workbook may add presentation metadata, but it must not create a competing scientific definition.

## Workbook classes

The prototype lineage contains more than one kind of workbook. These classes are explicit:

- `FULL_FRAMEWORK_SNAPSHOT`: broad integrated workbook intended to expose many project domains.
- `BOUNDED_MODULE`: focused workbook for one capability, case, pilot or evidence campaign.
- `REVIEW_ARTIFACT`: workbook primarily intended for review/decision support.
- `GENERATED_REPORT`: workbook generated from canonical project state.
- `LEGACY_PROTOTYPE`: historical workbook retained for traceability but not used as canonical state.

A higher artifact version does not imply that the workbook contains all earlier sheets or is a cumulative scientific replacement.

## Required workbook front matter

Generated workbooks begin with:

### `00_METADATA`

Required artifact metadata are:

- `project_id`
- `artifact_id`
- `artifact_class`
- `artifact_version`
- `schema_version`
- `generated_on`
- `git_commit`
- `purpose`
- `scope`
- `canonical_status`

Additional metadata such as framework version, intended audience, input datasets, evidence snapshot, known limitations, owner and contact can be included where useful.

A blank or missing Git commit is not a substitute for provenance. The generated artifact should identify the repository state from which it was produced.

### `01_GUIDE`

The guide explains:

- what the workbook contains;
- which sheets are source data, model inputs, outputs, evidence, qualification or views;
- which values are examples or scenarios;
- which outputs are blocked or not yet qualified;
- where the canonical definitions live.

### `DATA_DICTIONARY`

The current generator exposes the canonical field definitions used by the artifact. The baseline columns are:

- `field_id`
- `label`
- `description`
- `entity`
- `datatype`
- `unit`
- `nullable`
- `allowed_values`
- `guardrail`

Future adapters may add dataset context, provenance or qualification metadata, but they must derive those from canonical repository contracts rather than hand-maintained workbook text.

## Dataset-level metadata

Each data-bearing sheet exposes at least:

- `dataset_id`
- `entity`
- `role`
- `grain`
- `primary_key`
- `canonical_status`
- `source_or_derivation`

Dataset version, purpose, qualification status and known limitations may be added where they have independent meaning.

## Scenario and context

A workbook may show scenario-dependent results, but a scenario label must not hide the conditions that change interpretation.

When a result materially depends on compaction severity/depth, crop, weather or event, groundwater/drainage, water-system state, time horizon or valuation perspective, those conditions must remain explicit in canonical fields, linked datasets or artifact/view metadata.

The project does not require the workbook to enumerate every conceivable scenario in advance. It should expose only the context dimensions needed by the calculation or review surface at hand.

## Field-level help in Excel

Column labels should remain compact. Long definitions belong in the canonical field registry.

Workbooks expose contextual help on headers through a supported mechanism, for example a cell note/comment or a data-validation input message. `DATA_DICTIONARY` remains the fallback when spreadsheet clients differ.

## Sheet roles

A workbook may expose roles such as:

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

The preferred direction is:

**canonical schema + canonical data/evidence + code → generated workbook**

rather than:

**hand-edited workbook → reverse-engineered application**

The current generator is a bounded Tollebeek review adapter that demonstrates this contract. It is not the canonical project database and not the future application backend.

Manual workbook edits may remain useful during research, but any scientifically relevant change must ultimately be reconciled back into canonical project state.
