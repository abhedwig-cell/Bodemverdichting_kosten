# Workbook generator

This directory contains the schema-driven workbook adapter for the project.

The design goal is:

**canonical schema + canonical evidence/data registers + artifact specification → workbook**

not:

**hand-edited workbook → reverse-engineered project meaning**.

## Current adapter

`generate.py` uses `artifact_tool` to create an `.xlsx` workbook from:

- `schema/fields.yml`;
- `schema/tollebeek_vertical_slice.yml`;
- `schema/evidence_fields.yml`;
- `schema/datasets.yml`;
- `schema/artifacts/tollebeek_vertical_slice_workbook.yml`;
- canonical CSV registers explicitly referenced by the artifact specification.

The v0.2 Tollebeek workbook therefore contains two different kinds of sheets:

1. **populated canonical registers**, currently SOURCE, EVIDENCE, CLAIMS and QUALIFICATION;
2. **explicit blank templates** for model datasets that remain scientifically data-gated.

This distinction is deliberate. A blank hydrological result is not a missing spreadsheet calculation; it means the canonical project state does not yet support that result.

The adapter remains provisional and environment-specific. Scientific semantics must not depend on the spreadsheet library. A future open-source/local adapter may replace or complement it without changing canonical field or dataset definitions.

## Front matter

Generated workbooks start with:

- `00_METADATA` — artifact identity, versions, scope, Git commit and limitations;
- `01_GUIDE` — how colleagues should interpret the artifact;
- `DATA_DICTIONARY` — canonical field definitions used by this artifact.

Every dataset sheet includes dataset ID, entity, role, grain, primary key, canonical status and source file before the actual table.

## Header help

Column-header help is generated from the canonical field definition and exposed through an Excel data-validation input message. The full `DATA_DICTIONARY` sheet remains authoritative because spreadsheet-client behaviour can differ.

## Important boundary

The generated workbook is a review/interface artifact. It does not become canonical merely because it contains canonical data. The repository schemas, registers, documentation and code remain the project source of truth.

## Example

```bash
python tools/workbook_generator/generate.py \
  --root . \
  --output /tmp/tollebeek_vertical_slice.xlsx \
  --git-commit <commit-sha>
```
