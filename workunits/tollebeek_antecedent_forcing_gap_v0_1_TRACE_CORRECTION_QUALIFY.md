# Tollebeek antecedent-forcing precipitation-gap v0.1: TRACE CORRECTION QUALIFY checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Phase: `QUALIFY_CORRECTION`
Branch: `work/tollebeek-antecedent-forcing-gap-v0.1`

## Qualified correction

The trace-aware correction recorded in `workunits/tollebeek_antecedent_forcing_gap_v0_1_TRACE_CORRECTION.md` and implemented in `docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md` is scientifically accepted.

Correction verdict:

`QUALIFIED_TRACE_UNCERTAINTY_CORRECTION_CLASSIFICATION_UNCHANGED`

The controlling classification remains:

`EVIDENCE_BOUNDED_ANTECEDENT_PRECIP_GAP_RECONSTRUCTION_FAMILY_SCENARIO_ONLY`

## Pre-QUALIFY repository gate

Correction PR head before this checkpoint: `fe730fac16a6e0854dc76541e77df9d42a9d3a1e`.

CI run `35106582108`: `SUCCESS`.

The correction is documentation and scientific-semantics only. No forcing data, schema, production model code or run configuration changes are included.

## Scientific effect

The correction narrows uncertainty claims rather than changing the method family:

- `RH=-1` remains a trace amount below `0.05 mm`, not exact zero;
- residual precipitation in partially observed mass windows is propagated as an interval/enclosure;
- timing traces require interval propagation or pre-registered trace-realization members;
- direct station-269 copying remains not qualified because its trace-scale mass cannot satisfy the local station-317 residual constraint in the 1998-09-08 affected segment;
- the earlier cross-validation metrics remain diagnostic under their explicitly declared trace-as-zero screening convention only.

## State retained

- `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE`;
- no reconstructed forcing series admitted;
- no change to admitted event forcing;
- no warm-up adequacy claim;
- no SWAP run.

## Next permitted action

Run CI on the exact head containing this QUALIFY correction checkpoint. Merge is permitted only if that exact head is green and the correction diff remains bounded to the trace-aware protocol change and its checkpoints.
