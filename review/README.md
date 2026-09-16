# Colleague review workspace

This directory contains non-canonical review artifacts for the first Status-A-light colleague review.

The purpose is to collect comments and decisions without changing scientific meaning during the meeting itself.

## Files

- `pre_read_manifest_v0_1.csv` — compact role-aware pre-read package.
- `review_record_v0_1.csv` — seeded review record with the six review questions from `docs/19_colleague_review_session_v0_1.md`.

## Governance

The review record is a **review artifact**, not yet a canonical governance dataset. The first review should test whether the proposed fields and dispositions are actually useful before the project promotes this structure into `schema/`.

Allowed dispositions:

- `ACCEPT`
- `CHANGE`
- `EVIDENCE_REQUIRED`
- `OPEN_QUESTION`

Blank disposition means not yet reviewed. Do not convert blanks to `ACCEPT` by default.

A substantive review outcome should be implemented later through normal repository changes, with the affected theory, schema, code, evidence or documentation updated explicitly.