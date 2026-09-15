# Artifacts

Artifacts are user-facing or review outputs such as Excel workbooks, dashboards and reports.

## Rule

An artifact is not automatically canonical. The canonical scientific meaning should live in documentation, schemas, evidence registers and code.

## Current prototype lineage

A substantial workbook lineage was developed before repository bootstrap. The latest reviewed prototype at bootstrap is in the v4.x Tollebeek/framework line. Binary migration will be done deliberately after the workbook specification and data model have stabilised.

## Future workbook contract

Each workbook should eventually expose:

- `00_METADATA`
- `01_GUIDE`
- `DATA_DICTIONARY`
- dataset/table-level purpose and grain
- field-level descriptions linked to the canonical schema
- provenance and qualification status
- checks and known limitations
- artifact version and Git commit

Generated artifacts should be reproducible from canonical project state where practical.
