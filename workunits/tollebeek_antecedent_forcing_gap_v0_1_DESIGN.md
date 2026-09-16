# Tollebeek antecedent-forcing precipitation-gap v0.1: DESIGN checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Phase: `DESIGN`
Branch: `work/tollebeek-antecedent-forcing-gap-v0.1`
Design commit before this checkpoint: `44f0637539d1611cd3375bbf0194b005355a3faa`

## Design artifact

Canonical candidate protocol: `docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md`.

## Method disposition

- `G0` native gap preservation remains the source-authority baseline but is not run-ready.
- `G1` direct station-269 substitution is not qualified.
- `G2` a single nearby-station timing shape may only be a scenario member under explicit local-mass constraints and fail-fast semantics.
- `G3` a station-317 mass-constrained, multi-station timing family is the only treatment class advanced to qualification as `SCENARIO_ONLY` reconstruction methodology.
- `G4` other manual precipitation stations remain regional plausibility context, not a pooled local mass estimator.
- `G5` moving the warm-up window merely to avoid the gap is not qualified.

## Evidence basis

Reused immutable diagnostics:

- run `35100300817`, artifact digest `sha256:a98f851b5305ec2a2ab6b48f2b2f8301f65c4f37c2626cafa0fead03340ca4f0`;
- run `35094939299`, artifact digest `sha256:a23415c0c413664fb97bb267f68f5087aab39d4fe8ae87dc5b6d2ef45f1a60f3`.

The timing cross-validation covered 80 complete validation windows. The equal multi-station timing diagnostic was defined on 78 windows and returned hourly correlation `0.8145`, MAE `0.1093 mm/h`, RMSE `0.3537 mm/h`, wet-hour precision `0.6792` and wet-hour recall `0.8275`.

These metrics support a multi-member reconstruction family. They do not prove historical hourly truth and do not establish hydrological warm-up adequacy.

## Scientific safeguards retained

- no source-missing value becomes zero by default;
- observed station-273 hours are immutable under reconstruction;
- manual daily mass is not relabelled as hourly station-273 observation;
- regional station observations retain their own source identity;
- trace handling remains explicit and is not silently inherited from the diagnostic numeric convention;
- no deterministic method is selected from model output;
- no SWAP run is permitted in this workunit.

## Remaining qualification boundary

The protocol can be qualified as a reconstruction-method family only. It cannot admit an actual filled forcing series because no production reconstruction artifact with row-level provenance has been created and hydrological state sensitivity cannot yet be evaluated under the unresolved P1 run dependencies.

Next permitted action: open a clean PR against current `main`, run repository CI, then persist an exact-head QUALIFY checkpoint if CI and scientific review of this bounded diff both pass.
