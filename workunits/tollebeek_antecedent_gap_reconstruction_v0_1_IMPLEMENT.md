# Tollebeek antecedent-gap reconstruction v0.1 — IMPLEMENT checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Branch: `work/tollebeek-antecedent-gap-reconstruction-v0.1`
Canonical start: `41d5896dbf90dc33df1455467017ba8f2976f73b`
Source ACQUIRE checkpoint: `workunits/tollebeek_antecedent_gap_reconstruction_v0_1_ACQUIRE.md`

## Phase verdict

`IMPLEMENTED_SCENARIO_ONLY_CANDIDATE_PENDING_QUALIFICATION`

A deterministic generator has been implemented for the already qualified antecedent precipitation-gap reconstruction method. The implementation does not select a historical truth series and does not authorize a SWAP run.

## Implementation

Generator:

`tools/build_tollebeek_antecedent_gap_scenarios.py`

Default generated package path:

`artifacts/scenarios/tollebeek_antecedent_gap_reconstruction_v0_1.json`

Canonical compact manifest:

`artifacts/scenarios/tollebeek_antecedent_gap_reconstruction_v0_1_manifest.json`

The expanded scenario matrix is intentionally generated on demand rather than committed. The manifest pins its expected deterministic size and SHA-256.

## Method contract encoded

The generator implements `ST317_MASS_CONSTRAINED_MULTI_STATION_TIMING_V0_1` under the authority of `docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md`.

It:

- verifies the persisted source response byte sizes and SHA-256 values before parsing;
- requires all 108 station-273 gap hours to remain source-missing in the source snapshot;
- partitions the gap by the six native station-317 08:00–08:00 UTC reporting windows;
- preserves station-273 observed hours outside the gap as authoritative and never writes replacements for them;
- carries KNMI trace semantics as the interval `0 <= trace < 0.05 mm`;
- evaluates exactly three explicit scenario trace realizations: `0.0`, `0.025`, and `0.049 mm`;
- constrains each reconstructed reporting window to station-317 precipitation mass after retained station-273 mass under that trace realization;
- retains station-specific timing reconstructions from stations 267, 269, 270 and 279 as uncertainty members when defined;
- marks an undefined timing member invalid when its timing mass is zero while the constrained residual is positive;
- never falls back to zero, uniform spreading or silent station switching;
- computes an equal-valid-member ensemble only as a diagnostic aggregate, explicitly not historical truth;
- sets `run_authorized = false` and makes no `DR_SM_INITIAL_STATE` status change.

## Deterministic candidate package

Local qualification-preparation execution against the exact persisted source snapshot produced:

- classification: `SCENARIO_ONLY_CANDIDATE_NOT_RUN_READY`;
- gap hours: 108;
- expanded package bytes: `117484`;
- expanded package SHA-256: `85dbb685dd888bdad7078f243ca01adb134b343f1d382d578f53cdce1c879932`.

The canonical manifest also records source hashes:

- hourly source: `6076cfb910fa498daca93091e6fbbd361cbcd2a113b4518995ee817d2714c5bd`;
- station-317 manual source: `eee4895db5f335a8ec7f82cf828a3d4adb965a26cbba0c111adc16029bbedc35`;
- source receipt: `51a35da9dbf8ccc913ae6dde207b199bee0911bbc4b95b8ac5701f31d9ea6b19`.

## Explicit fail-fast cases retained

Under `TRACE_BOUND_LOWER`:

- station 279 is invalid for report window `19980907` because the timing realization has zero mass while the local constrained residual is positive;
- stations 267 and 269 are invalid for report window `19980908` for the same reason.

They are retained as explicit invalid members with failure reason `ZERO_TIMING_MASS_WITH_POSITIVE_RESIDUAL`; they are not silently replaced.

## Tests added

`tests/test_tollebeek_antecedent_gap_scenarios.py`

The bounded test contract checks:

1. exact source SHA-256 values and source-receipt classification;
2. exactly 108 gap hours and `run_authorized = false`;
3. reconstruction support is restricted to the source-missing gap timestamps;
4. non-negative reconstructed values and per-window mass closure;
5. explicit invalid-member handling without hidden fallback;
6. trace uncertainty remains explicit;
7. the on-demand expanded package reproduces the SHA-256 and byte size pinned by the canonical manifest.

Local pre-commit execution: 5 tests, all PASS.

This local execution is implementation evidence only. Repository CI on the committed exact head remains required before QUALIFY.

## Scientific boundary

No reconstructed package is yet qualified or admitted. No single trace realization, station member or ensemble is selected as the historical series. The compact manifest is a candidate configuration/evidence artifact, not an observed dataset.

`DR_SM_INITIAL_STATE` remains `PARTIAL_EVIDENCE`.

No SWAP run is permitted from this checkpoint.

## Next permitted action

Commit this implementation atomically, run the repository CI and direct generator/tests on the exact branch head, inspect the resulting scenario manifest against the qualified method contract, and only then persist a QUALIFY checkpoint. If qualified, the permissible admission is `SCENARIO_ONLY` method/configuration use, not historical forcing admission and not warm-up adequacy.
