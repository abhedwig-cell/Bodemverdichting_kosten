# Documentation map

The documentation is organised from scientific meaning to implementation.

## Start here

If you are new to the project, begin with [`00_colleague_reader_guide.md`](00_colleague_reader_guide.md). It explains the scientific chain, the current/reference logic, the Tollebeek pilot, evidence qualification, the role of GitHub and Excel, and the main current data gates.

For documentation governance and Status-A-light expectations, see [`14_documentation_status_a_light.md`](14_documentation_status_a_light.md).

For a compact cross-layer review of the current architecture, see [`15_traceability_matrix_v0_1.md`](15_traceability_matrix_v0_1.md).

## Core scientific documentation

1. [`01_overview.md`](01_overview.md) — project purpose and scope
2. [`02_theoretical_framework.md`](02_theoretical_framework.md) — causal and theoretical basis
3. [`03_conceptual_model.md`](03_conceptual_model.md) — project objects and relationships
4. [`04_formal_model.md`](04_formal_model.md) — equations, variables, states and rules
5. [`05_data_model.md`](05_data_model.md) — canonical entities, datasets, fields and provenance
6. [`06_implementation.md`](06_implementation.md) — mapping to code, workbooks and application
7. [`07_evidence_and_qualification.md`](07_evidence_and_qualification.md) — evidence, qualification and admission

## Workbook and migration documentation

8. [`08_workbook_architecture.md`](08_workbook_architecture.md) — workbook contract and field help
9. [`09_workbook_inventory_v0_2.md`](09_workbook_inventory_v0_2.md) — inspected prototype lineage and migration baseline
10. [`10_data_model_v0_2_migration.md`](10_data_model_v0_2_migration.md) — migration layers and vertical-slice route
11. [`11_tollebeek_vertical_slice_v0_2.md`](11_tollebeek_vertical_slice_v0_2.md) — first theory/data/code/test vertical slice
12. [`12_workbook_generator_v0_1.md`](12_workbook_generator_v0_1.md) — first schema-driven workbook artifact generator
13. [`13_tollebeek_evidence_baseline_v0_1.md`](13_tollebeek_evidence_baseline_v0_1.md) — first canonical Tollebeek source/evidence/claim/qualification baseline

## Status-A-light documentation governance

14. [`14_documentation_status_a_light.md`](14_documentation_status_a_light.md) — documentation layers, maturity states, minimum metadata and review triggers
15. [`15_traceability_matrix_v0_1.md`](15_traceability_matrix_v0_1.md) — theory-to-code/evidence traceability for the main current capabilities

## Suggested reading paths

**Scientific colleague / reviewer:** `00 → 01 → 02 → 03 → 04 → 07 → 15`

**Data/software colleague:** `00 → 05 → 06 → 08 → 11 → 12 → 15`

**Tollebeek/domain reviewer:** `00 → 11 → 13 → evidence/ → 15`

The documents are intentionally incomplete while the repository is in Status-A-light development. Unknowns, legacy mappings and blocked items should remain visible rather than being silently normalised.
