# 5. Data model

## Purpose

The data model defines scientific meaning independently of Excel, Python or the future application.

Canonical machine-readable definitions live under [`../schema/`](../schema/).

## Required field metadata

Each canonical field should eventually define at least:

- `name`
- `label`
- `description`
- `entity`
- `datatype`
- `unit`
- `nullable`
- `allowed_values` or vocabulary where applicable
- `provenance_class`
- `status`
- `grain` / row meaning
- important guardrails

## Grain is mandatory

Every table/dataset should state what one row represents. Examples:

- one row per soil layer;
- one row per event × spatial unit × state;
- one row per evidence item;
- one row per pump asset;
- one row per cost estimate.

## Workbook mapping

A workbook sheet should map to a defined dataset object. The preferred principle is:

**one table = one clearly defined dataset object**.

Workbook headers/tooltips and the workbook `DATA_DICTIONARY` should be generated from or checked against the same canonical field definitions to prevent documentation drift.

## Status

The current schema is a bootstrap v0.1 and will be reconciled against the existing workbook line before being declared canonical v1.
