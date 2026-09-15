# 12. Workbook generator v0.1

## Objective

Implement the workbook architecture as code rather than as another manually evolving Excel prototype.

The first generated artifact is deliberately small and bounded around the Tollebeek source → transfer → pump-dispatch vertical slice.

## Contract demonstrated

The generated workbook contains:

- `00_METADATA`;
- `01_GUIDE`;
- `DATA_DICTIONARY`;
- one sheet per selected canonical dataset object;
- `VIEW_STATUS` as an explicitly non-source view.

Every data-bearing sheet exposes before the table:

- `dataset_id`;
- entity;
- role;
- grain;
- primary key;
- canonical status.

This makes row meaning visible to a colleague before they start interpreting values.

## Field help

Column labels stay compact. Selecting a header exposes a generated Excel input message based on the canonical field definition in `schema/fields.yml` or the bounded Tollebeek overlay.

The message can include:

- definition;
- unit;
- allowed values;
- important guardrail.

The `DATA_DICTIONARY` sheet is the authoritative workbook-level fallback and exposes the longer definitions.

## Null semantics

The workbook generator creates blank template rows rather than example zeros.

This is deliberate:

**unknown / not supplied ≠ 0**.

No scientific Tollebeek values are invented merely to make the artifact look complete.

## Artifact specification

The workbook composition is declared in:

`schema/artifacts/tollebeek_vertical_slice_workbook.yml`

The specification selects canonical dataset IDs, sheet names and fields. The generator fails if a requested dataset or field is not defined.

This creates a testable boundary between schema evolution and workbook layout.

## Generator structure

- `tools/workbook_generator/contract.py` contains schema loading, field-help generation and artifact-spec validation without a spreadsheet-library dependency.
- `tools/workbook_generator/generate.py` is the current spreadsheet adapter.
- `tests/test_workbook_generator_contract.py` checks that the artifact specification resolves against the canonical schema and that guardrail text survives into field help.

## Current adapter limitation

The current `.xlsx` adapter uses `artifact_tool`. That dependency is implementation-specific and should not become part of the scientific model contract.

If colleagues later need a fully local/open-source generator, a second adapter can implement the same artifact specification while preserving dataset and field semantics.

## Scientific admission level

The generated workbook qualifies only the **artifact/interface architecture**.

It does not qualify:

- current OT.02 geometry;
- current/reference soil state;
- SWAP response;
- source-to-ditch delivery;
- pump availability or assist operation;
- total dynamic head or efficiency;
- current costs.

Those remain governed by their own evidence and qualification gates.

## Next useful step

Use this generator pattern for one populated, evidence-backed slice rather than migrating the 109-sheet prototype wholesale. A good next slice is the canonical evidence/source register plus the admitted pump-asset benchmarks, followed by current spatial and hydrological data when available.
