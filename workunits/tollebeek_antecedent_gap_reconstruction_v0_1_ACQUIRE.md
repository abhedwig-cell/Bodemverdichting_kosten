# Tollebeek antecedent-gap reconstruction v0.1 — ACQUIRE checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Decision surface: trace-aware `SCENARIO_ONLY` precipitation-gap reconstruction package
Branch: `work/tollebeek-antecedent-gap-reconstruction-v0.1`
Canonical start: `41d5896dbf90dc33df1455467017ba8f2976f73b`

## Phase verdict

`ACQUIRED_SOURCE_NATIVE_NOT_YET_RECONSTRUCTED`

The exact official KNMI source responses required for the bounded 108-hour precipitation-gap reconstruction have been persisted as immutable evidence snapshots. They are source evidence, not a reconstructed forcing dataset and not model-ready input.

No SWAP run was executed.

## Persisted source snapshots

Directory:

`evidence/source_snapshots/tollebeek_antecedent_gap_v0_1/`

Files:

1. `knmi_hourly_prcp_273_267_269_270_279_19980902_19980908.txt`
   - official KNMI hourly climatology endpoint;
   - POST request: stations 273, 267, 269, 270 and 279; `PRCP`; 1998-09-02 01 through 1998-09-08 24 source notation;
   - source-native bytes retained, including source whitespace and blank fields;
   - size: 33,492 bytes;
   - SHA-256: `6076cfb910fa498daca93091e6fbbd361cbcd2a113b4518995ee817d2714c5bd`.

2. `knmi_manual_rd_317_19980903_19980908.txt`
   - official KNMI manual precipitation series endpoint;
   - POST request: station 317, report dates 1998-09-03 through 1998-09-08;
   - source-native bytes retained;
   - size: 715 bytes;
   - SHA-256: `eee4895db5f335a8ec7f82cf828a3d4adb965a26cbba0c111adc16029bbedc35`.

3. `source_receipt_manifest.json`
   - records exact URLs, POST bodies, source paths, response byte sizes, SHA-256 values, workflow head/run identity and source semantics;
   - classification: `ACQUIRED_SOURCE_NATIVE_NOT_YET_RECONSTRUCTED`;
   - repository role: immutable evidence snapshot, not model-ready forcing.

Persist commit created by the acquisition workflow:

`fb41bf0406c3ab781bab8c11be6243c824c78061`

Successful raw-only acquisition run:

`35108854803` at acquisition head `10857295c0d8a2e1c15aaea78ad5235e612e8590`.

## Reproducibility evidence

The same two response hashes were independently returned by three bounded acquisitions in this workstream:

- original package acquisition run `35107095125`;
- raw receipt attempt run `35108436960`;
- source-snapshot attempt run `35108603030`;
- final successful persistence run `35108854803`.

The final persisted snapshot uses the hashes above. Repeated equality is acquisition reproducibility evidence, not a claim that the external service can never change in the future.

## Source semantics retained

The source header/receipt semantics remain:

- hourly `RH` is reported in 0.1 mm;
- `RH=-1` means trace precipitation `<0.05 mm`, not zero and not missing;
- blank hourly `RH` is source missing;
- station-317 manual `RD` is a 24-hour precipitation total using the native 08:00 UTC previous day to 08:00 UTC report-date window.

No trace value has been converted to an observed numerical amount in the persisted source snapshot.

## Failed acquisition mechanics that do not affect science

Two persistence attempts failed for repository-mechanical reasons:

1. `data/raw/` is deliberately ignored by `.gitignore`; the project did not bypass that policy with `git add -f`.
2. `git diff --cached --check` rejected source-native KNMI trailing whitespace. The source text was not normalized to satisfy the Git check because doing so would change the acquired bytes.

The snapshots were therefore placed under the canonical evidence layer at `evidence/source_snapshots/`, and the raw-file diff whitespace check was removed for the source-native persistence step only.

These failures are not scientific evidence and no scientific conclusion was drawn from them.

## Temporary acquisition infrastructure

The temporary branch-only workflow has been removed after successful persistence. It must not appear in the canonical PR diff.

## Scientific boundary

This checkpoint does not:

- fill any station-273 missing hour;
- promote station 317 to station-273 observation status;
- select one trace realization as truth;
- select one timing station or ensemble as historical truth;
- admit a warm-up forcing dataset;
- alter `DR_SM_INITIAL_STATE = PARTIAL_EVIDENCE`;
- authorize SWAP execution.

## Next permitted action

Implement a deterministic trace-aware scenario reconstruction generator against these immutable snapshots and the already qualified method contract in `docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md`.

The generated result must remain explicitly `SCENARIO_ONLY`, retain per-hour origin/provenance and member identity, preserve observed station-273 hours, fail rather than invent a fallback, and be independently qualified before any repository admission for scenario use.
