# Colleague review package v0.1

**Status:** READY_FOR_REVIEW_USE  
**Purpose:** package the current Status-A-light project state into a bounded colleague review surface without turning the meeting into a legacy-workbook audit.

## 1. Package contents

The minimum package is:

1. `docs/00_colleague_reader_guide.md`;
2. `docs/18_status_a_light_checkpoint_v0_1.md`;
3. generated Tollebeek review workbook v0.2;
4. repository root link;
5. `review/review_record_v0_1.csv` for recording outcomes.

Role-specific additions are listed in `review/pre_read_manifest_v0_1.csv`.

## 2. Review boundary

The package is intended to answer whether the current architecture is a defensible basis for the next scientific stage. It is not a request to approve:

- a finished application;
- a complete Status-A report;
- current Tollebeek impact numbers;
- convenience defaults for missing soil, drainage, transfer or pump-operation inputs.

## 3. Review record semantics

The seeded record contains the six review questions R1–R6. Review comments may add extra rows when a substantive issue does not fit one question cleanly.

Each substantive item should end in one of:

- `ACCEPT`;
- `CHANGE`;
- `EVIDENCE_REQUIRED`;
- `OPEN_QUESTION`.

Blank means not yet reviewed. `OPEN` in the `status` column means the item is still active and must not be interpreted as accepted.

## 4. Why the record is not canonical yet

The review record is deliberately kept outside the canonical data model for the first cycle. We first want to learn whether the proposed fields, dispositions and workflow are useful in a real colleague review.

If the first review demonstrates that repeated structured review is valuable, a later bounded change may promote `review_item` to a canonical governance entity and add a `review_register` dataset.

## 5. Expected outputs from the meeting

The meeting should produce:

- explicit objections or confirmations on causal structure and counterfactual logic;
- changes or questions on entity/grain/null semantics;
- challenged claims or evidence gaps;
- confirmation or revision of current data gates;
- a small number of assigned next actions with owners;
- a clear statement whether the project is ready to proceed to the first spatial current/reference source model.

## 6. Post-review discipline

Do not rewrite scientific meaning directly in the review record. The record captures the decision surface. Accepted changes are implemented through normal repository changes so theory, schema, code, evidence and generated artifacts remain traceable.

`COLLEAGUE_REVIEW_PACKAGE_V0_1 = READY_FOR_USE`
