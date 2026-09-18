# Colleague review workspace

This directory contains non-canonical review artifacts for the first Status-A-light colleague review.

The purpose is to collect comments and decisions without changing scientific meaning during the meeting itself.

## Files

- `review_baseline_v0_1.yml` — pinned repository commit, successful CI run, review-workbook checksum and scientific review boundary for the first review cycle.
- `pre_read_manifest_v0_1.csv` — compact role-aware pre-read package.
- `review_record_v0_1.csv` — seeded review record with the six review questions from `docs/19_colleague_review_session_v0_1.md`.

## Why the baseline is pinned

`main` will continue to evolve. A review must therefore refer to a fixed scientific/technical state rather than to whatever happens to be current later. The baseline manifest records the exact commit and CI result that define review cycle v0.1 and identifies the generated workbook by SHA-256.

The generated workbook remains a derived review artifact. Canonical scientific meaning lives in the repository schema, documentation, evidence, formal model, code and tests at the pinned commit.

## Governance

The review record is a **review artifact**, not yet a canonical governance dataset. The first review should test whether the proposed fields and dispositions are actually useful before the project promotes this structure into `schema/`.

Allowed dispositions:

- `ACCEPT`
- `CHANGE`
- `EVIDENCE_REQUIRED`
- `OPEN_QUESTION`

Blank disposition means not yet reviewed. Do not convert blanks to `ACCEPT` by default.

A substantive review outcome should be implemented later through normal repository changes, with the affected theory, schema, code, evidence or documentation updated explicitly.
## Current colleague review v0.2

For a colleague who knows the initial project discussion but has not followed the subsequent development, the current review entry point is:

- `../docs/57_colleague_review_package_v0_2.md` — self-contained project story, theory, on-site/off-site chains, uncertainty, dashboard design logic, current state and review focus;
- `pre_read_manifest_v0_2.csv` — deliberately small pre-read sequence rather than a repository dump;
- `colleague_review_questions_v0_2.csv` — ten structured questions covering project frame, causality, on-site/off-site completeness, evidence shortcuts, uncertainty, valuation, dashboard and priorities.

The v0.2 review is intended to test the **scientific and conceptual reasoning**, not to approve a finished model. Dashboard prototype screens are treated as interface designs; their older counts/statuses are not the current canonical scientific state.

Suggested dispositions are simple: confirm, adjust, investigate further, or defer/out of scope. Review feedback should subsequently be implemented through normal repository changes rather than edited directly into evidence during the meeting.

