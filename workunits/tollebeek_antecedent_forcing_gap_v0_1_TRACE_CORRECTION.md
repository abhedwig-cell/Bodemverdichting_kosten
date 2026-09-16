# Tollebeek antecedent-forcing precipitation-gap v0.1: TRACE CORRECTION checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Phase: `RECONCILE / QUALIFY CORRECTION`
Branch: `work/tollebeek-antecedent-forcing-gap-v0.1`

## Canonical start

PR #47 merged as main `b008fbb189f0639816e35ff3f5a342809a6bde55`.

Post-merge CI run `35106207408`: `SUCCESS`.

Open pull requests before this correction: none.

The existing work branch was reset to that exact canonical main before the correction. No new branch was created because this is a correction within the same scientific decision surface.

## Finding

Final inspection of the immutable gap-probe artifact exposed an over-precise interpretation in the first qualified wording.

KNMI hourly `RH=-1` represents trace precipitation below `0.05 mm`. It is neither missing nor exact zero.

In the affected station-317 08:00 to 08:00 UTC windows:

- report date `1998-09-03` retains two station-273 trace hours outside the source gap, so the missing-hour residual is not exactly `3.4 mm`; its trace-aware enclosure is `[3.30, 3.40] mm`, with the exact lower bound open;
- report date `1998-09-08` retains one station-273 trace hour outside the source gap, so the missing-hour residual is not exactly `0.3 mm`; its trace-aware enclosure is `[0.25, 0.30] mm`, with the exact lower bound open;
- station 269 over the four missing hours contributing to `1998-09-08` has one trace and no reported amount `>=0.1 mm`, so describing it as exact zero was too strong.

The station-269 source-consistent mass in those four hours is below `0.05 mm`, while the local residual required by station 317 plus retained station-273 observations is greater than `0.25 mm` and at most `0.30 mm`. Direct station-269 copying therefore still fails the local mass constraint.

## Diagnostic cross-validation boundary

The earlier temporal-disaggregation screening converted `RH=-1` to numeric `0.0 mm`. That convention is acceptable only as an explicitly labelled lower-bound screening convention.

It is not production trace semantics and cannot be inherited by a reconstructed forcing dataset.

The published screening metrics remain useful for method comparison under that declared convention, but they do not constitute trace-aware production validation.

## Correction applied

Commit `9aa5cd868e2430b8aeca172e662baa8e315b6932` corrects `docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md` to:

- replace exact residual values by trace-aware residual-mass enclosures;
- correct the station-269 wording from exact zero to trace-scale precipitation;
- require interval propagation or pre-registered trace-realization members for reconstruction timing;
- keep exact zero distinct from trace;
- forbid clipping a negative/incompatible residual to zero;
- preserve trace/member identity in future row-level provenance.

## Scientific verdict

The correction does **not** change the workunit classification:

`EVIDENCE_BOUNDED_ANTECEDENT_PRECIP_GAP_RECONSTRUCTION_FAMILY_SCENARIO_ONLY`

It strengthens the uncertainty semantics supporting that classification.

Still unchanged:

- no reconstructed forcing series is admitted;
- `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE`;
- no event-forcing mutation;
- no warm-up adequacy claim;
- no SWAP run.

## Next permitted action

Open a bounded correction PR, run CI on the exact head, persist no further scientific mutation unless CI or review exposes a defect, merge only from the exact green SHA, then verify post-merge main CI and record the correction CLOSE verdict in the PR body.
