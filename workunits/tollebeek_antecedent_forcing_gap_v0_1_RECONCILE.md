# Tollebeek antecedent-forcing precipitation-gap v0.1: RECONCILE checkpoint

Date: 2026-09-16
Capability dependency: `DR_SM_INITIAL_STATE`
Phase: `RECONCILE`
Branch: `work/tollebeek-antecedent-forcing-gap-v0.1`

## Canonical state

Canonical `main` at reconciliation: `32442fdbf14926c2bc05aedaedf90af277e9b67e`.

Post-merge CI authority: run `35102809757`, `SUCCESS`, on that exact main SHA.

Open pull requests at reconciliation: none.

The branch was deliberately reset to the canonical main SHA before this checkpoint. Earlier temporary probe commits are therefore not part of the proposed canonical diff.

## Reused qualified dependency

The controlling canonical decision remains `docs/45_tollebeek_antecedent_forcing_review_v0_1.md` and `workunits/tollebeek_antecedent_forcing_v0_1_QUALIFY.md`:

- station 273 Marknesse provides a reproducible one-year source interval from `1997-10-24T00:00:00Z` to `1998-10-24T00:00:00Z` exclusive;
- all 8760 timestamps exist;
- `DR` and `RH` are source-missing for exactly 108 contiguous hours from `1998-09-03T00:00:00Z` through `1998-09-07T12:00:00Z` exclusive;
- classification remains `QUALIFIED_ANTECEDENT_FORCING_SOURCE_WITH_PRECIPITATION_GAP`;
- `DR_SM_INITIAL_STATE` remains `PARTIAL_EVIDENCE`;
- no station-269 substitution, null-to-zero fill, interpolation, warm-up adequacy claim, initial-state admission or SWAP run is authorized.

No relevant dependency of that qualified decision changed after its admission.

## Reused immutable diagnostic evidence

Two earlier branch-only GitHub Actions probes are retained as immutable diagnostic evidence by run/head/artifact identity. Their temporary workflows are not carried forward.

### Gap source and regional constraint probe

- source branch head: `7ef520c9e6272c82033047349eb5246e3362b00f`;
- Actions run: `35100300817`, `SUCCESS`;
- artifact: `10448120861`, `tollebeek-antecedent-gap-probe`;
- artifact digest: `sha256:a98f851b5305ec2a2ab6b48f2b2f8301f65c4f37c2626cafa0fead03340ca4f0`.

Official KNMI requests in that probe show:

- validated daily station-273 precipitation fields are also source-missing on the core affected dates, so they do not restore the lost hourly observations;
- manual precipitation station 317 provides 08:00 to 08:00 UTC daily precipitation totals through the gap;
- manual stations 344, 348, 352 and 356 provide independent regional context;
- nearby automatic stations provide observed hourly timing information but are not station-273 observations.

Source-response SHA-256 values recorded by the probe include:

- daily station 273: `cd3f3184cf105c1788818d98cab015ee2b1204ea9f82df981405cf58adb39190`;
- hourly station 273: `20f15fc9820bb2718debc1c0e43758a96d6fe1a8ebceb2b08f122a06651edbb0`;
- hourly station 267: `2a4f6a9e877985865d95dd01399c2f434510d3dea0aea5da945cce1892ec04bb`;
- hourly station 269: `1874ee0561f38d03dc057eb4157067d4423fb1335ca812e179a0c4f05a1c45d9`;
- hourly station 278: `ce5b5344c312d0e71fcd6b338faf7504cdb905da7fc2bc7365c43af89e25837d`;
- hourly station 279: `b5559c1bbcd3bde2a2916ae4ab962f7fb40dbc08557f8e6926a013b3750f6478`;
- manual station 317: `95462f186ff7d9c103be44d6ea4b81e87e1ceefc3261308614b86addc6ac684a`;
- manual station 344: `77be07dfa5c8d4b24ca4bceec03b490c9f2cab281ab92a4c23e520212c28470e`;
- manual station 348: `dfc28f77c18dd2f63eb11eda738bf4e3df2aa0f2b942c355a25239eb1415b138`;
- manual station 352: `e0c3b9271e72f85b6f6d49e2564496dc5f72ceaf6a2e417faf89850643943949`;
- manual station 356: `a11dad6020bf5855fef3ed653ca66869d4f916c41f6455a39d18e8f0a7779a3d`.

### Temporal-disaggregation cross-validation

- source branch head: `9b08b7f4f09d1792587f0f82dca7e6f4214bae23`;
- Actions run: `35094939299`, `SUCCESS`;
- artifact: `10445817743`, `tollebeek-antecedent-gap-disaggregation-cv`;
- artifact digest: `sha256:a23415c0c413664fb97bb267f68f5087aab39d4fe8ae87dc5b6d2ef45f1a60f3`.

The diagnostic tested station 317 daily mass with hourly timing shapes from stations 269, 267, 270 and 279 against complete station-273 hours outside the gap. It is method evidence only. It does not relabel reconstructed precipitation as observation.

## Relevant state delta

Since canonical main `32442fdb...`, no new external WER3382 current-state dataset or source-holder response is present in the repository and no new canonical P1 input was admitted.

The only relevant reusable delta is the already generated precipitation-gap diagnostic evidence above.

## Reconcile verdict

`RECONCILED_TO_CANONICAL_MAIN_GAP_METHOD_DECISION_SURFACE_OPEN`

The next permitted action is to qualify the precipitation-gap treatment classes against the immutable diagnostics. This workunit may qualify a reconstruction protocol, but must not create an admitted historical forcing series or claim hydrological warm-up adequacy without a separate state-sensitivity qualification.

## Exclusions

Out of scope here:

- renewed CURRENT-state proxy or dataset search;
- changing `DR_SM_CURRENT_STATE`, `DR_SM_REFERENCE_STATE`, drainage, managed boundary, land use or model configuration;
- modifying the admitted 144-hour event forcing;
- treating manual daily precipitation as observed hourly station-273 data;
- selecting a method because it produces preferable model output;
- SWAP execution.
