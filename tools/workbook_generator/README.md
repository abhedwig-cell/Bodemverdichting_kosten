# Workbook generator

This directory contains the first schema-driven workbook adapter for the project.

The design goal is:

**canonical schema + artifact specification + canonical project state → workbook**

not:

**hand-edited workbook → reverse-engineered project meaning**.

## Current adapter

`generate.py` uses `artifact_tool` to create an `.xlsx` workbook from:

- `schema/fields.yml`;
- `schema/tollebeek_vertical_slice.yml`;
- `schema/datasets.yml`;
- `schema/artifacts/tollebeek_vertical_slice_workbook.yml`.

The current adapter is provisional and environment-specific. Scientific semantics must not depend on the spreadsheet library. A future open-source/local adapter may replace or complement it without changing the canonical field or dataset definitions.

## Header help

Column-header help is generated from the canonical field definition and exposed through an Excel data-validation input message. The full `DATA_DICTIONARY` sheet remains authoritative because spreadsheet-client behaviour can differ.

## Important boundary

The generated v0.1 workbook is a review/interface artifact. It deliberately leaves unknown scientific data blank. It does not qualify Tollebeek hydrology, routing, pump operation or costs.

## Example

```bash
python tools/workbook_generator/generate.py \
  --root . \
  --output /tmp/tollebeek_vertical_slice.xlsx \
  --git-commit <commit-sha>
```
