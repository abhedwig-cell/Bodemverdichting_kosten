# Tollebeek antecedent-gap reconstruction v0.1: RECONCILE checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Phase: `RECONCILE`
Branch: `work/tollebeek-antecedent-gap-reconstruction-v0.1`

## Canonical state

Canonical `main` at branch creation: `41d5896dbf90dc33df1455467017ba8f2976f73b`.

Post-merge main CI authority: run `35106723512`, `SUCCESS`.

Open pull requests at reconciliation: none.

This branch starts from that exact main SHA.

## Controlling qualified method

`docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md` controls this workunit.

Qualified method family:

`EVIDENCE_BOUNDED_ANTECEDENT_PRECIP_GAP_RECONSTRUCTION_FAMILY_SCENARIO_ONLY`

Required semantics include:

- station-273 observations remain authoritative wherever present;
- `RH=-1` is trace precipitation below `0.05 mm`, not exact zero;
- station-317 source-reported 08:00 to 08:00 UTC totals provide the local mass constraint;
- nearby automatic stations may provide alternative hourly timing members;
- residual mass and timing traces retain uncertainty;
- row-level provenance, source checksums, method version and member identity are mandatory;
- no direct station-269 copy is admissible as canonical fill;
- no reconstructed forcing may be called historical observation.

## Scope

Create and qualify a **source-native receipt plus derived SCENARIO_ONLY reconstruction package** for the 108 missing station-273 precipitation hours.

This workunit may acquire the minimum official KNMI source records needed for the affected windows and may derive uncertainty-preserving reconstruction members under protocol 47.

It must not:

- modify the already admitted 144-hour event forcing;
- admit a hydrological initial state;
- assert one-year warm-up adequacy;
- alter managed boundary, drainage, land use, model configuration or hydraulic semantics;
- run SWAP;
- collapse trace uncertainty or member uncertainty to an undocumented single value.

## Acquisition discipline

The first mutation after this checkpoint may be a temporary branch-only GitHub Actions acquisition workflow.

Requirements:

- official KNMI source endpoints only;
- exact request parameters persisted;
- raw response bytes retained in the temporary artifact before transformation;
- SHA-256 for every raw response;
- parser output separate from raw bytes;
- trace flags retained source-native;
- no scientific conclusion from a failed request or parser;
- temporary workflow removed before canonical PR.

## Next permitted action

Acquire the bounded source-native records required to reconstruct the affected reporting windows. If official source acquisition or source semantics cannot be reproduced unambiguously, fail fast and close this workunit without a derived forcing artifact.
