# Tollebeek antecedent-forcing precipitation-gap v0.1: QUALIFY checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Phase: `QUALIFY`
Branch: `work/tollebeek-antecedent-forcing-gap-v0.1`

## Qualified decision

Verdict:

`EVIDENCE_BOUNDED_ANTECEDENT_PRECIP_GAP_RECONSTRUCTION_FAMILY_SCENARIO_ONLY`

The method family in `docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md` is qualified for future scenario-only reconstruction design.

This is a method qualification, not admission of a filled historical forcing series.

## Scientific disposition

Qualified:

- preserve observed station-273 precipitation wherever source observations exist;
- use station-317 native 08:00 to 08:00 UTC precipitation mass as the local mass constraint in the qualified reconstruction family;
- use nearby automatic-station hourly timing only as explicitly identified reconstruction members;
- preserve member uncertainty and row-level reconstruction provenance;
- fail if constrained residual mass or timing support is not defined under the protocol;
- retain trace handling as an explicit production decision rather than silently treating traces as exact zero.

Not qualified:

- direct station-269 copying as a deterministic station-273 fill;
- null-to-zero or linear interpolation;
- a single nearby timing station as canonical historical truth;
- distance weighting or bias correction without separate validation;
- pooling regional manual gauges into a local mass estimate;
- changing the warm-up window merely to avoid the gap;
- selecting reconstruction members from model-output preference.

## Evidence used

Canonical source qualification reused unchanged:

- `docs/45_tollebeek_antecedent_forcing_review_v0_1.md`;
- one-year station-273 raw SHA-256 `aac1c6082105e685d594aae518e2dcfe080513e4485b546e177499005b74f52b`;
- normalized source candidate SHA-256 `5ed2c604f6cce2c09c7379eeb3f745fed6b4f46a4778bb6c0fbb20098ada0272`;
- exact 108-hour `DR`/`RH` gap retained.

Gap diagnostic evidence:

- run `35100300817`, head `7ef520c9e6272c82033047349eb5246e3362b00f`, artifact digest `sha256:a98f851b5305ec2a2ab6b48f2b2f8301f65c4f37c2626cafa0fead03340ca4f0`;
- run `35094939299`, head `9b08b7f4f09d1792587f0f82dca7e6f4214bae23`, artifact digest `sha256:a23415c0c413664fb97bb267f68f5087aab39d4fe8ae87dc5b6d2ef45f1a60f3`.

Cross-validation diagnostic summary:

- 80 complete validation windows available;
- equal multi-station timing diagnostic defined on 78 windows;
- hourly correlation `0.8145`;
- MAE `0.1093 mm/h`;
- RMSE `0.3537 mm/h`;
- wet-hour precision `0.6792`;
- wet-hour recall `0.8275`.

These metrics support reconstruction-family feasibility only. They do not demonstrate exact historical hourly precipitation or hydrological state convergence.

## Repository qualification before scientific status update

Pre-qualification PR head: `ef531637c33a7695389f40c57daa9287141cbe90`.

CI run `35105957449`: `SUCCESS`.

Passed on that exact head:

- project validation and workbook-tool compilation;
- Status-A-light integrity gate;
- unit and contract tests.

The protocol status was then advanced from design candidate to qualified method family in commit `0e87c3bc0997d33a3ffd60a7b7a7828e6dcf297e`.

## State retained

No change to:

- `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE`;
- `DR_SM_EVENT_FORCING` and its admitted 144-hour event forcing;
- `DR_SM_CURRENT_STATE` or `DR_SM_REFERENCE_STATE`;
- drainage, managed boundary, land use or model configuration;
- hydraulic parameterization admission;
- model inputs or outputs.

No reconstructed hourly forcing file is created by this workunit.

## Hydrological sensitivity boundary

The required next scientific test is not currently executable under project rules. Before reconstructed antecedent forcing can be used for an I1 state qualification, managed boundary, drainage, land use, model configuration and state/hydraulic semantics must first be admitted or explicitly qualified as `SCENARIO_ONLY` for that test.

Only then may reconstruction members be propagated to event-start model state, using a sensitivity design fixed before output inspection.

## Next permitted action

Run CI again on the exact branch head containing this QUALIFY checkpoint. Merge is permitted only if that exact head is green and the branch remains clean against the same canonical base.
