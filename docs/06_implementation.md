# 6. Implementation

## Architectural layers

The intended implementation separates:

- domain/scientific model;
- data ingestion and adapters;
- calculations/model orchestration;
- evidence and qualification;
- persistence/export;
- user-facing artifacts.

## Excel

Excel is a documented interface and review artifact, not the canonical database.

Future workbooks should contain at least:

- `00_METADATA`
- `01_GUIDE`
- `DATA_DICTIONARY`
- clearly defined data/calculation/output sheets
- provenance/checks/change information where relevant

Column headers should remain compact. Detailed definitions should be accessible through a note/input-message mechanism where technically robust, and always through the data dictionary.

## Workbook metadata

Expected metadata include project, artifact type, artifact version, framework version, schema version, generation date, Git commit, purpose, scope, intended audience, canonical status, source/evidence snapshot, known limitations and change summary.

## Code

Scientific calculations should progressively move into testable code under `src/`. Workbooks and the future application should consume the same formal definitions rather than reproduce separate calculation logic where avoidable.

## Current state

Existing scripts and workbooks have not yet been fully migrated into this repository. Migration will follow schema and documentation bootstrap rather than precede it.
