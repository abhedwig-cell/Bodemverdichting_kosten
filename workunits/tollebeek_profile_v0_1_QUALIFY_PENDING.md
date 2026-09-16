# Tollebeek profile v0.1 — QUALIFY pending checkpoint

Current branch head before PR qualification: `4b62e2f530484f6d470e59a33f4489ed86b523f8`.

The proposed canonical diff contains only bounded profile-context data/schema/evidence/tests/documentation. Temporary acquisition/finalization workflows are absent.

Qualification requirements:

- evidence integrity PASS;
- formal/domain schema integrity PASS;
- source-model readiness integrity PASS;
- admitted spatial geometry integrity PASS;
- OT.02 profile-baseline validator PASS;
- full unit/contract test suite PASS.

No merge is permitted until an exact-head CI run satisfies these gates.
