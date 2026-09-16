# Tollebeek antecedent-gap reconstruction v0.1 — QUALIFY checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Branch: `work/tollebeek-antecedent-gap-reconstruction-v0.1`
PR: #49
Canonical start: `41d5896dbf90dc33df1455467017ba8f2976f73b`

## Qualified decision

Verdict:

`QUALIFIED_ANTECEDENT_GAP_RECONSTRUCTION_PACKAGE_SCENARIO_ONLY_NOT_RUN_READY`

The immutable candidate manifest and its deterministic generator are qualified for one narrow purpose: representing uncertainty in the 108 source-missing station-273 antecedent precipitation hours as explicit `SCENARIO_ONLY` reconstruction members.

The candidate manifest itself remains labelled `SCENARIO_ONLY_CANDIDATE_NOT_RUN_READY`. Qualification is recorded separately in:

`artifacts/scenarios/tollebeek_antecedent_gap_reconstruction_v0_1_qualification.json`

This deliberately separates the generated scientific object from the decision about its permissible use.

## Immutable subject

Manifest:

`artifacts/scenarios/tollebeek_antecedent_gap_reconstruction_v0_1_manifest.json`

Git blob SHA:

`00e2863a6a6971661df24cbc3cced2fae1df4956`

Expanded on-demand package:

- bytes: `117484`;
- SHA-256: `85dbb685dd888bdad7078f243ca01adb134b343f1d382d578f53cdce1c879932`.

Generator:

`tools/build_tollebeek_antecedent_gap_scenarios.py`

Method:

`ST317_MASS_CONSTRAINED_MULTI_STATION_TIMING_V0_1`

Method authority:

`docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md`

## Source evidence retained

The source snapshot remains immutable and source-native:

- station-273/267/269/270/279 hourly response SHA-256 `6076cfb910fa498daca93091e6fbbd361cbcd2a113b4518995ee817d2714c5bd`;
- station-317 manual response SHA-256 `eee4895db5f335a8ec7f82cf828a3d4adb965a26cbba0c111adc16029bbedc35`;
- source receipt SHA-256 `51a35da9dbf8ccc913ae6dde207b199bee0911bbc4b95b8ac5701f31d9ea6b19`.

No source trace was converted into an observed exact precipitation amount. Numeric trace realizations remain scenario semantics only.

## Qualification evidence

Implementation commit:

`6154d6fded391edbf568c0455bfdd68f5e52b956`

Precheck head:

`a7db72166a8ffe2d6082571d4a3cf5a427d5617e`

Initial exact-head PR CI:

- run `35110265726`;
- conclusion `SUCCESS`;
- compilation PASS;
- Status-A-light integrity gate PASS;
- unit/contract suite PASS;
- the five antecedent-gap scenario tests were included in unittest discovery and PASS.

The tests verify:

1. exact source hashes before parsing;
2. exactly 108 source-missing station-273 gap hours;
3. gap-only reconstruction support and preservation of observed station-273 authority;
4. non-negative values and mass closure in each native station-317 reporting window;
5. explicit invalid members instead of fallback;
6. explicit trace-policy uncertainty;
7. deterministic reproduction of the expanded package size and SHA-256.

## Qualified use

The package may be used to generate explicit uncertainty members for a future hydrological sensitivity design, once the other required model dependencies are admitted or explicitly qualified as `SCENARIO_ONLY`.

The uncertainty dimensions that must remain visible include:

- trace realization;
- timing-source station;
- validity/failure state;
- mass-anchor report window;
- diagnostic ensemble identity where calculated.

The member spread must be propagated into later state-sensitivity analysis rather than collapsed into one preferred series because it produces a convenient model result.

## Prohibited interpretation

This qualification does not:

- turn reconstructed hours into station-273 observations;
- identify one trace realization as truth;
- identify one timing station or the ensemble as the historical truth;
- establish that the one-year antecedent period is a sufficient warm-up;
- admit an initial soil-water or groundwater state;
- change `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE`;
- authorize a SWAP production run;
- change event forcing `DR_SM_EVENT_FORCING`.

## Evidence-register boundary

No reconstructed scenario hour is added to the canonical observation evidence register. The project evidence chain already distinguishes observed KNMI event forcing from derived interpretation. For this derived scenario configuration, traceability is preserved as:

`source snapshot -> protocol 47 -> generator + manifest -> qualification receipt -> this QUALIFY checkpoint`

This avoids promoting scenario values to observation status merely because they are repository-persisted and tested.

## Remaining dependencies

Hydrological sensitivity remains execution-gated by the unresolved or only partially evidenced dimensions already recorded for:

- managed boundary;
- drainage;
- land use/crop;
- concrete model configuration;
- CURRENT/REFERENCE soil state and hydraulic parameterization;
- initial-state construction itself.

## Next permitted action

Run repository CI again on the exact head containing this QUALIFY checkpoint and qualification receipt. If that exact head passes, confirm a clean diff, merge only with an exact expected-head SHA, then require post-merge main CI before CLOSE.

No SWAP run is permitted as part of this workunit.
