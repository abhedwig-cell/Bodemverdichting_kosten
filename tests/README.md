# Tests and qualification

Tests distinguish at least:

- software/unit tests;
- data-quality checks;
- numerical/model qualification;
- scientific plausibility/benchmark checks;
- transfer validation;
- artifact/schema conformance.

A passing software test does not by itself qualify scientific meaning.

Current software-QA slice:

- `test_vertical_slice.py` verifies generated-volume, dispatch and energy semantics;
- all numerical fixtures in that file are synthetic unless explicitly documented otherwise.

Run locally from repository root with:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

Future tests should reference the evidence or contract they qualify where possible.
