# 5. Data model

## Purpose

The data model defines scientific meaning independently of Excel, Python, databases or the future application.

Canonical machine-readable definitions live under [`../schema/`](../schema/).

## Current schema level

Data Model **v0.2** is a migration baseline derived from the actual prototype workbook lineage.

It is not yet canonical v1.

v0.2 adds:

- explicit artifact and dataset objects;
- a dataset registry;
- expanded physical/model/evidence entities;
- explicit claim, governance and data-request entities;
- a provisional workbook contract;
- machine-generated workbook sheet/field inventories.

See:

- [`09_workbook_inventory_v0_2.md`](09_workbook_inventory_v0_2.md)
- [`10_data_model_v0_2_migration.md`](10_data_model_v0_2_migration.md)
- [`../schema/datasets.yml`](../schema/datasets.yml)
- [`../schema/workbook_contract.yml`](../schema/workbook_contract.yml)

## Required field metadata

Each canonical field should eventually define at least:

- `field_id`
- `label`
- `description`
- `entity`
- `datatype`
- `unit`
- `nullable`
- vocabulary/allowed values where applicable
- provenance semantics
- qualification semantics
- important guardrails

## Grain is mandatory

Every table/dataset must state what one row represents.

Examples:

- one row per soil layer;
- one row per event × spatial unit × state;
- one row per evidence item;
- one row per pump asset configuration;
- one row per source zone × event × pump dispatch;
- one row per cost estimate.

## Dataset identity is distinct from workbook sheet name

Legacy sheet names are lineage locators.

A canonical `dataset_id` describes stable scientific meaning and should survive:

- workbook redesign;
- renaming of display tabs;
- migration to a database;
- migration to an application.

## Workbook mapping

A workbook sheet should map to one or more explicitly registered dataset objects. The preferred principle is:

**one table = one clearly defined dataset object**.

Workbook headers/tooltips and `DATA_DICTIONARY` should be generated from or checked against `schema/fields.yml` to prevent documentation drift.

## Null semantics

Unknown is not zero.

Missing, blocked, not-ingested and not-applicable states must remain explicit and must not be silently converted into numeric zero.

## Status

The migration baseline is ready for a first vertical implementation slice.

Recommended next slice:

**Tollebeek source response → transfer → water-system zone → pump dispatch**

with evidence and qualification links carried end-to-end.
