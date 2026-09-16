# Source-model input baseline v0.1 — RECONCILE checkpoint

Protocol: RECONCILE → IMPLEMENT → QUALIFY → ADMIT → CLOSE

## Canonical start

- repository: `abhedwig-cell/Bodemverdichting_kosten`
- base branch: `main`
- base head: `f6e605b9cbf2d8c0dfa8f8df2b3ebc7a31644a0b`
- work branch: `work/source-model-input-baseline-v0.1`
- open PRs at start: none
- materially equivalent source-model-input workunit found: no

## Reconciled existing authority

The project already defines the next scientific milestone as a first spatial source model with matched CURRENT/REFERENCE input and explicitly lists data gates for current geometry, drainage, depth-resolved soil state, matched reference, event forcing/initial state and managed boundary representation.

Existing evidence already provides:

- administrative OT.02 area context, but not affected/model geometry;
- a PDOK/IMWA acquisition route for a candidate current peilgebied geometry, not an admitted feature;
- a SoilPhys acquisition/screening route for derived/modal profile attributes, not a measured current compaction state;
- historical Noordoostpolder drainage parameters as method priors only;
- managed-system/target-level context, but not event-specific boundary/control behaviour;
- theory/method evidence for contextual reference states, profile depth and sub-daily forcing.

## Classification

This workunit will establish a canonical input-readiness/data-request baseline for the first source-model pair. It will not acquire external datasets, select numerical values, run SWAP, calculate attribution, or extend downstream transfer/pump/cost semantics.

The source-model gate ends at qualified hydrological response. Event-scale transfer/routing and current pump operation remain later gates and are not prerequisites for the first paired source response.

## Next permitted action

IMPLEMENT a bounded machine-readable `data_request_register` with explicit requirement kind, readiness status, current evidence/claim links, acceptance criteria and next action; add validation and traceability. Missing values remain missing.

## Exclusions

- no invented OT.02 geometry;
- no invented current/reference soil state;
- no drainage calibration by analogy;
- no synthetic event forcing presented as current data;
- no hidden SWAP defaults;
- no transfer, pump or cost admission;
- no workbook expansion merely because a new register exists.
