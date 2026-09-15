# Tests and qualification

Tests distinguish at least:

- software/unit tests;
- data-quality checks;
- numerical/model qualification;
- scientific plausibility/benchmark checks;
- transfer validation;
- artifact/schema conformance.

A passing software test does not by itself qualify scientific meaning.

Current software-QA slices:

- `test_vertical_slice.py` verifies generated-volume, dispatch and energy semantics;
- `test_workbook_generator_contract.py` verifies that the workbook artifact specification resolves against the schema and that canonical guardrails survive into generated header help;
- all numerical fixtures are synthetic unless explicitly documented otherwise.

Run locally from repository root with:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

The spreadsheet adapter itself is environment-specific; schema/contract tests are kept separate so scientific semantics do not depend on a particular workbook library.

Future tests should reference the evidence or contract they qualify where possible.
