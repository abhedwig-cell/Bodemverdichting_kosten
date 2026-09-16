# Tollebeek antecedent precipitation-gap reconstruction protocol v0.1

Status: **QUALIFIED - reconstruction method family only, SCENARIO_ONLY**

Capability dependency: `DR_SM_INITIAL_STATE`
Controlling source qualification: `QUALIFIED_ANTECEDENT_FORCING_SOURCE_WITH_PRECIPITATION_GAP`

## Purpose

This protocol defines which treatment classes are scientifically admissible for the 108 source-missing station-273 precipitation hours from `1998-09-03T00:00:00Z` through `1998-09-07T12:00:00Z` exclusive.

It does not create a filled forcing dataset, does not admit an initial state and does not establish that a one-year warm-up is adequate.

## Evidence boundary

The qualified station-273 source record remains authoritative outside the gap. Existing observed station-273 hours must never be overwritten by a reconstruction.

Two branch-only diagnostics are reusable for method qualification:

1. run `35100300817`, head `7ef520c9e6272c82033047349eb5246e3362b00f`, artifact `10448120861`, digest `sha256:a98f851b5305ec2a2ab6b48f2b2f8301f65c4f37c2626cafa0fead03340ca4f0`;
2. run `35094939299`, head `9b08b7f4f09d1792587f0f82dca7e6f4214bae23`, artifact `10445817743`, digest `sha256:a23415c0c413664fb97bb267f68f5087aab39d4fe8ae87dc5b6d2ef45f1a60f3`.

These diagnostics are not admitted forcing data. They are evidence about reconstruction feasibility and method behaviour.

## What the diagnostics establish

Validated daily station-273 precipitation is also missing across the core affected dates. There is therefore no direct station-273 daily source that can restore the missing station-273 hourly precipitation.

Manual station 317 supplies precipitation totals using an 08:00 to 08:00 UTC reporting window through the affected period. Nearby automatic stations supply hourly timing information but represent other locations.

KNMI hourly `RH=-1` denotes trace precipitation below `0.05 mm`. A trace is not missing, not negative and not an exact zero. Therefore residual mass in a reporting window is an interval whenever retained station-273 observations in that window contain traces.

Using the source-native reported station-317 daily total and preserving all non-missing station-273 hours gives the following conservative residual-mass enclosures. Closed interval notation is used as an enclosure; where a trace contributes an open upper bound, the true mathematical bound is correspondingly open.

| report date | missing hours | station-317 reported total (mm) | retained station-273 positive mass (mm) | retained station-273 trace count | residual-mass enclosure for missing hours (mm) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1998-09-03 | 8 | 4.9 | 1.5 | 2 | [3.30, 3.40] |
| 1998-09-04 | 24 | 13.6 | 0.0 | 0 | [13.60, 13.60] |
| 1998-09-05 | 24 | 5.0 | 0.0 | 0 | [5.00, 5.00] |
| 1998-09-06 | 24 | 5.5 | 0.0 | 0 | [5.50, 5.50] |
| 1998-09-07 | 24 | 0.7 | 0.0 | 0 | [0.70, 0.70] |
| 1998-09-08 | 4 | 1.2 | 0.9 | 1 | [0.25, 0.30] |

For 1998-09-03 the exact trace-aware residual is greater than `3.30 mm` and at most `3.40 mm`. For 1998-09-08 it is greater than `0.25 mm` and at most `0.30 mm`. The closed intervals above deliberately preserve a conservative enclosure rather than pretending the trace amount is known.

The temporal-disaggregation diagnostic evaluated hourly timing shapes from stations 269, 267, 270 and 279 against complete station-273 periods outside the gap. In that diagnostic only, `RH=-1` was represented numerically as `0.0 mm`. This is a declared lower-bound trace convention for method screening and is not production trace semantics.

| timing method | defined validation days | hourly correlation | MAE (mm/h) | RMSE (mm/h) | wet-hour precision | wet-hour recall |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| station 269 | 73 | 0.7398 | 0.1381 | 0.4962 | 0.7004 | 0.6475 |
| station 267 | 75 | 0.6237 | 0.1562 | 0.6243 | 0.7013 | 0.5870 |
| station 270 | 71 | 0.6175 | 0.1630 | 0.5839 | 0.7281 | 0.6264 |
| station 279 | 77 | 0.5660 | 0.1547 | 0.5988 | 0.7232 | 0.6975 |
| equal multi-station timing ensemble | 78 | 0.8145 | 0.1093 | 0.3537 | 0.6792 | 0.8275 |

Under that diagnostic convention, the ensemble is more stable across the validation period than any tested single timing station. This is not evidence that one deterministic ensemble-mean series is the historical truth, and the numeric scores must not be interpreted as trace-aware production validation.

Single-station direct copying is also inconsistent with the local mass constraint in an actual affected window. For the four missing hours contributing to the 1998-09-08 reporting window, station 269 contains no precipitation report of `>=0.1 mm` and one trace, so its source-consistent mass is below `0.05 mm`. The local station-317 constraint combined with retained station-273 observations requires more than `0.25 mm` and at most `0.30 mm` in those missing hours. Direct station-269 copying therefore cannot satisfy the local reported mass constraint even when the station-269 trace is preserved correctly.

## Treatment classes

### G0 - preserve native missingness

Status: **ADMISSIBLE SOURCE BASELINE, NOT RUN-READY**.

Keep the 108 station-273 values null and preserve the qualified source record unchanged. This is the authority baseline against which any reconstruction must be compared.

### G1 - direct station-269 substitution

Status: **NOT QUALIFIED**.

Copying station-269 hourly precipitation into station-273 missing hours is not an admissible deterministic reconstruction. It mixes locations without a local mass constraint and can conflict materially with the station-317 mass evidence even when KNMI traces are handled correctly.

Station 269 may remain a timing-information source inside an explicitly reconstructed scenario family.

### G2 - single-station mass-scaled timing

Status: **SCENARIO MEMBER ONLY, NOT CANONICAL FILL**.

A nearby station's hourly precipitation timing may be used as one reconstruction member only when:

- the local mass anchor for that reporting window is separately admissible;
- the timing source has complete hourly coverage for the missing portion;
- exact-zero and trace observations remain distinguishable;
- any trace contribution to the timing shape is represented through an explicit trace-aware rule or member family;
- observed station-273 hours are retained unchanged;
- every reconstructed hour is explicitly flagged as reconstructed.

If the timing source has exact zero throughout the missing portion while the constrained local residual is positive, the member is undefined and must fail. Trace-only support must not be silently converted to exact zero or to an arbitrary fixed amount.

### G3 - locally mass-constrained multi-station timing ensemble

Status: **QUALIFIED FOR SCENARIO-ONLY RECONSTRUCTION METHOD**.

This is the strongest currently supported reconstruction family. It combines distinct evidence roles rather than pretending all sources measure the same object:

- station 317 constrains source-reported precipitation mass in its native 08:00 to 08:00 UTC reporting window;
- nearby automatic stations provide alternative observed hourly timing information;
- existing station-273 observations remain authoritative wherever present.

For each affected reporting window `d`, derive a trace-aware residual-mass interval from:

`M_residual(d) = M_317_reported(d) - M_273_retained(d)`.

`M_273_retained(d)` is itself an interval when retained station-273 hours contain `RH=-1` traces. A residual interval that is incompatible with non-negative precipitation fails qualification for that window. It must not be repaired by clipping to zero.

For each timing station `s`, construct a non-negative hourly timing family over only the source-missing station-273 hours in that reporting window. Reported positive amounts retain their source magnitude. Trace observations retain the source constraint `0 <= RH < 0.05 mm` and require either interval propagation or pre-registered trace-realization members. Exact zero remains exact zero.

Each valid timing member is normalized and scaled only within the qualified residual-mass member for that reporting window. The resulting station-specific and trace-specific reconstructions form an uncertainty family. A multi-station aggregate may be calculated for diagnostics, but member spread must be retained for later hydrological sensitivity assessment. The method must not collapse the family to a single historical truth claim.

No distance weighting or bias correction is currently qualified. Such weighting would require independent validation showing that the weighting rule improves transfer to station 273 rather than merely adding complexity.

### G4 - regional manual-station mass envelope

Status: **DIAGNOSTIC CONTEXT ONLY**.

Manual stations 344, 348, 352 and 356 demonstrate spatial variability and can bound regional plausibility. Their totals are not interchangeable with station 317 and must not be pooled into a local mass estimate without separate spatial-transfer qualification.

### G5 - move or shorten the warm-up window to avoid the gap

Status: **NOT QUALIFIED**.

Changing the warm-up window solely to avoid missing precipitation is a convenience adjustment, not a scientific reconstruction. A different window could only be considered after an independently defined spin-up/convergence analysis shows that the alternative initialization semantics are adequate.

## Required production semantics for any future reconstructed series

Any future implementation must preserve, at minimum, for every precipitation value:

- timestamp and source station-273 authority where observed;
- `value_origin = observed | reconstructed | source_missing`;
- source observation IDs or exact source query identity;
- mass-anchor station and native reporting window where reconstruction is used;
- timing-source member or ensemble-member identity;
- reconstruction method name and version;
- source-response checksums;
- source trace flag and trace handling rule;
- residual-mass member or interval identity;
- timing trace-realization member where applicable;
- uncertainty/member identifier;
- QC outcome and failure reason where no reconstruction is defined.

`null` remains `null` until a row has passed the reconstruction rule. No default, zero, mean or representative value is allowed as an implicit fallback.

KNMI trace precipitation must retain its source meaning as an amount below the reporting threshold. The cross-validation's trace-as-zero screening convention is diagnostic only and must not silently become production semantics.

## Hydrological sensitivity gate

Meteorological reconstruction skill is not equivalent to warm-up adequacy. Before any reconstructed precipitation series can be admitted for I1 initialization, a separate qualification must quantify how reconstruction members affect the model state at the event-start boundary.

That sensitivity step is currently blocked from execution because the project does not yet have the required admitted or explicitly `SCENARIO_ONLY` managed-boundary, drainage, land-use, model-configuration and hydraulic/state inputs for such a run.

When those dependencies are available, the sensitivity design must be fixed before model outputs are inspected. It must compare the same CURRENT/REFERENCE initialization semantics across admissible precipitation members and report state spread rather than selecting the member that produces the most convenient result.

## Decision boundary

This protocol qualifies a **reconstruction family** without admitting a reconstructed forcing dataset.

The qualified classification is:

`EVIDENCE_BOUNDED_ANTECEDENT_PRECIP_GAP_RECONSTRUCTION_FAMILY_SCENARIO_ONLY`

This classification does not change `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE`, does not alter the admitted event forcing and does not authorize SWAP execution.
