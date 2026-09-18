# Documentation map

The documentation is organised from scientific meaning to implementation and evidence. The first documents form the **core colleague reader path**; later documents record migration, implementation and governance milestones.

## Start here

If you are new to the project or taking the work over from someone else, begin with [`00_project_handover_and_continuation.md`](00_project_handover_and_continuation.md). It restores the broad project philosophy: minimum necessary computation, parallel on-site/off-site chains, literature/evidence shortcuts, uncertainty and source ensembles, and the role of Tollebeek/SWAP as optional deepening rather than the project definition.

Then read [`00_colleague_reader_guide.md`](00_colleague_reader_guide.md). It explains the more detailed scientific/evidence architecture, current/reference attribution, the Tollebeek pilot, the role of GitHub and Excel, and the main current data gates.

For documentation governance and Status-A-light expectations, see [`14_documentation_status_a_light.md`](14_documentation_status_a_light.md).

For a compact cross-layer review of the current architecture, see [`15_traceability_matrix_v0_1.md`](15_traceability_matrix_v0_1.md). The machine-readable equation and capability traceability baseline is documented in [`17_formal_traceability_register_v0_1.md`](17_formal_traceability_register_v0_1.md).

For the current transfer/review moment, use [`18_status_a_light_checkpoint_v0_1.md`](18_status_a_light_checkpoint_v0_1.md). It summarises maturity per layer, current Tollebeek data gates, what the tests do and do not prove, and the next scientific milestone.

For the actual first colleague review, use [`19_colleague_review_session_v0_1.md`](19_colleague_review_session_v0_1.md) together with [`20_colleague_review_package_v0_1.md`](20_colleague_review_package_v0_1.md) and the templates under [`../review/`](../review/).

The first explicit evidence baseline for the general theoretical framework is [`16_theory_evidence_baseline_v0_1.md`](16_theory_evidence_baseline_v0_1.md).

For the project-wide continuation surface, see [`49_project_effect_pathway_matrix_v0_1.md`](49_project_effect_pathway_matrix_v0_1.md). The companion source-ensemble rules are in [`50_evidence_ensemble_protocol_v0_1.md`](50_evidence_ensemble_protocol_v0_1.md). The first concrete on-site source migration is documented in [`51_onsite_ensemble_source_migration_v0_1.md`](51_onsite_ensemble_source_migration_v0_1.md).

For the bounded Data Model v0.3 architecture step, use [`21_data_model_v0_3_contract.md`](21_data_model_v0_3_contract.md) and [`22_domain_traceability_v0_3.md`](22_domain_traceability_v0_3.md). These documents do not add new science; they make already documented domain and run-control semantics machine-readable.

## Core reader path

1. [`01_overview.md`](01_overview.md) — project purpose, scope, maturity and how the calculation is decomposed
2. [`02_theoretical_framework.md`](02_theoretical_framework.md) — state, response, counterfactual attribution, transfer, aggregation and valuation theory
3. [`03_conceptual_model.md`](03_conceptual_model.md) — scientific/project objects, grains and relationships
4. [`04_formal_model.md`](04_formal_model.md) — equations, variables, units, null semantics and formal decision rules
5. [`05_data_model.md`](05_data_model.md) — canonical entities, datasets, fields, keys and migration principles
6. [`06_implementation.md`](06_implementation.md) — mapping to code, evidence registers, workbooks, CI and the future application
7. [`07_evidence_and_qualification.md`](07_evidence_and_qualification.md) — source → evidence → claim → qualification architecture and review expectations

A colleague who wants to understand **what we are doing and why** should normally read `00` and then these seven documents in order. They are deliberately written at a higher level than the historical Excel workbook lineage.

## Architecture and migration records

8. [`08_workbook_architecture.md`](08_workbook_architecture.md) — workbook contract, metadata and field help
9. [`09_workbook_inventory_v0_2.md`](09_workbook_inventory_v0_2.md) — inspected prototype lineage and migration baseline
10. [`10_data_model_v0_2_migration.md`](10_data_model_v0_2_migration.md) — migration layers and first vertical-slice strategy

## Concrete implementation milestones

11. [`11_tollebeek_vertical_slice_v0_2.md`](11_tollebeek_vertical_slice_v0_2.md) — first theory/data/code/test vertical slice
12. [`12_workbook_generator_v0_1.md`](12_workbook_generator_v0_1.md) — first schema-driven workbook artifact generator
13. [`13_tollebeek_evidence_baseline_v0_1.md`](13_tollebeek_evidence_baseline_v0_1.md) — first canonical Tollebeek source/evidence/claim/qualification baseline

The generated workbook has since advanced to an evidence-aware v0.2 artifact: canonical evidence registers are populated into the workbook while scientifically blocked model-result datasets remain explicit blank templates. The repository remains canonical; the workbook remains a generated review interface.

## Status-A-light governance, traceability and theory evidence

14. [`14_documentation_status_a_light.md`](14_documentation_status_a_light.md) — documentation layers, maturity states, minimum metadata, scientific-claim discipline and review triggers
15. [`15_traceability_matrix_v0_1.md`](15_traceability_matrix_v0_1.md) — colleague-facing theory-to-code/evidence traceability for the main current capabilities and broken-link review
16. [`16_theory_evidence_baseline_v0_1.md`](16_theory_evidence_baseline_v0_1.md) — first source/evidence/claim/qualification baseline for the general theoretical framework
17. [`17_formal_traceability_register_v0_1.md`](17_formal_traceability_register_v0_1.md) — machine-readable equation register and capability traceability with integrity validation
18. [`18_status_a_light_checkpoint_v0_1.md`](18_status_a_light_checkpoint_v0_1.md) — current review checkpoint, maturity matrix, data gates and next science/transfer milestones
19. [`19_colleague_review_session_v0_1.md`](19_colleague_review_session_v0_1.md) — review questions, 90-minute agenda, dispositions and review boundary
20. [`20_colleague_review_package_v0_1.md`](20_colleague_review_package_v0_1.md) — bounded pre-read/review package and review-record semantics
21. [`21_data_model_v0_3_contract.md`](21_data_model_v0_3_contract.md) — bounded v0.3 domain/run-control contract and scientific exclusions
22. [`22_domain_traceability_v0_3.md`](22_domain_traceability_v0_3.md) — cross-layer mapping from theory and conceptual objects to formal controls and canonical datasets

The corresponding machine-readable formal registers live under [`model/`](../model/).

## Suggested reading paths

**Scientific colleague / reviewer:** `00 → 01 → 02 → 16 → 03 → 04 → 07 → 15 → 17 → 18 → 19 → 21 → 22`

**Data/software colleague:** `00 → 05 → 06 → 08 → 11 → 12 → 15 → 17 → 18 → 21 → 22`

**Tollebeek/domain reviewer:** `00 → 11 → 13 → evidence/ → 15 → 17 → 18 → 19`

**Contributor:** `00 → 14 → 18 → ../CONTRIBUTING.md`

## Status-A-light principle

These documents are intentionally living documentation while the project is in Status-A-light development. The objective is not to make every section look complete. The objective is to make the current scientific state reconstructable:

```text
theory
  ↓
conceptual model
  ↓
formal model
  ↓
data model
  ↓
implementation
  ↓
evidence / qualification
  ↓
generated artifacts and application views
```

Unknowns, legacy mappings, contested definitions and blocked items should remain visible rather than being silently normalised or filled with convenient assumptions.
