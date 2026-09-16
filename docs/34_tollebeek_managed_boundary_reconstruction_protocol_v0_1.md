# Tollebeek 1998 managed-boundary reconstruction protocol v0.1

Status: **PROTOCOL QUALIFIED FOR FUTURE USE; NO BOUNDARY ADMISSION**

Canonical basis: `main` @ `a8b62c423391bf13ff8e638a749d70f4c9ab6944`.

## 1. Purpose

This protocol defines when a managed-boundary reconstruction for `EVT_TOL_1998_OCT` could be scientifically admissible if direct 1998 telemetry remains incomplete or unavailable.

It does not reconstruct the boundary now.

The governing distinction is:

- **observed boundary** — source-native measurements/logs;
- **historically constrained reconstruction** — inferred but bounded by qualified historical evidence;
- **scenario envelope** — conditional exploration where historical identification is insufficient;
- **convenience default** — prohibited.

## 2. Historical system authority

Any reconstruction must preserve the qualified pre-redesign system context:

- separate OT02 De Rietgors, OT03 De Fuut and OT04 De Kievit;
- all three directly connected by pumping to the Urkervaart;
- near-period target level NAP -6.20 m;
- near-period official nominal capacities listed as 2.600, 0.670 and 1.000 m3/s respectively;
- actual surface-water level documented as fluctuating around target and potentially rising by more than 0.20 m during heavy persistent rainfall;
- emergency pumping formed part of the 27-28 October 1998 crisis response.

Post-1998 stuwen, the 2010 connecting watercourse, 2011-2012 hydraulic works, IJsvogel and the current merged OT.02 control system are excluded unless a separate historical-equivalence proof exists.

The listed near-period capacities are **not** automatically accepted as exact 1998 realized capacity or discharge.

## 3. Reconstruction ladder

### R0 — OBSERVED_EVENT_BOUNDARY

Use when event-specific source-native records are recovered.

Minimum examples:

- surface-water level series;
- pump on/off or runtime logs;
- realized discharge or capacity-state records;
- stuw/inlaat operation logs;
- emergency-pump deployment records.

R0 may support an `OBSERVED` boundary claim after normal QC, temporal and spatial qualification.

### R1 — CONSTRAINED_HISTORICAL_RECONSTRUCTION

Use only when direct telemetry is incomplete but the historical state is sufficiently constrained to infer bounded alternatives.

An R1 reconstruction must contain all of the following:

1. fixed historical topology;
2. explicit target/control rules supported by source evidence;
3. explicit distinction between nominal pump capacity and realized operation;
4. documented emergency-intervention treatment;
5. time-varying or interval-wise uncertainty rather than one unsupported deterministic series;
6. at least one alternative admissible reconstruction where the evidence does not identify a unique sequence;
7. sensitivity of project-relevant outputs to those alternatives;
8. an identifiability statement listing quantities that remain unobserved.

R1 may support the claim label `HISTORICALLY_CONSTRAINED_RECONSTRUCTION`. It may not be labelled observed telemetry.

### R2 — ENVELOPE_ONLY_SCENARIO

Use when historical evidence constrains only broad behaviour, not a defensible event sequence.

Examples include:

- water-level response envelopes around a target regime;
- bounded pump-capacity availability scenarios;
- emergency-intervention presence/absence or timing-window scenarios;
- alternative receiving-water constraints.

R2 is `SCENARIO_ONLY`. It can support mechanism/sensitivity work, acquisition prioritization and robustness analysis, but not historical attribution of a unique 1998 managed-boundary trajectory.

### R3 — INADMISSIBLE_DEFAULT

Any of the following remains inadmissible:

- flat NAP -6.20 m imposed as the actual event hydrograph solely because it is the target level;
- pumps assumed to run continuously at nameplate capacity;
- 2006 listed capacity treated as exact 1998 realized discharge without temporal/equipment qualification;
- current IJsvogel or merged OT.02 operation backcast into 1998;
- emergency pumping omitted because exact records are unavailable;
- one arbitrary hydrograph selected from a broad plausible range without alternatives/sensitivity;
- missing control data replaced by zero.

R3 cannot enter Track H or Track S as qualified evidence.

## 4. Reconstruction state vector

A future managed-boundary reconstruction record should distinguish at least:

- `boundary_reconstruction_id` and version;
- historical control-area identity (`OT02`, `OT03`, `OT04` where applicable);
- receiving-water identity (`Urkervaart` or source-supported alternative);
- interval/timestamp;
- target level where source-supported;
- reconstructed/observed actual surface-water level;
- level provenance class (`OBSERVED`, `RECONSTRUCTED`, `SCENARIO`);
- pump availability state;
- pump operation state;
- realized discharge if observed/reconstructed;
- nominal capacity context kept separately from realized discharge;
- emergency-intervention state and source;
- stuw/inlaat state where material;
- lower/upper uncertainty bound or reconstruction-member ID;
- source/evidence IDs;
- free-assumption flags;
- QC/identifiability notes.

No field should overload target level, actual level and groundwater head into one value.

## 5. Constraint classes

Every reconstructed quantity must be tagged with one of these constraint types:

- `DIRECT_OBSERVATION` — source-native event measurement/log;
- `HARD_HISTORICAL_CONSTRAINT` — topology or documented system fact with direct applicability;
- `TEMPORALLY_TRANSFERRED_CONSTRAINT` — near-period value whose use in 1998 requires an explicit transfer argument;
- `EVENT_NARRATIVE_CONSTRAINT` — qualitative/categorical event fact such as emergency intervention occurring;
- `FREE_RECONSTRUCTION_PARAMETER` — not identified by evidence and therefore varied explicitly;
- `SCENARIO_PARAMETER` — deliberately chosen for conditional analysis, not historical inference.

A reconstruction with material `FREE_RECONSTRUCTION_PARAMETER` values must not collapse them to one hidden best guess.

## 6. Minimum R1 qualification tests

A candidate R1 reconstruction may only be reviewed for admission when it passes all of the following.

### T1 — topology fidelity

No post-1998 infrastructure is silently present.

### T2 — target/actual separation

NAP -6.20 m, or another target value, remains a control target unless an actual level observation supports equality at a given time.

### T3 — capacity/operation separation

Nominal capacity is never treated as realized discharge without an operation model and evidence-supported availability/operation assumptions.

### T4 — emergency-response representation

The documented emergency intervention is represented or the omission is shown immaterial to the selected event window and outcome. Silence is not acceptable.

### T5 — non-uniqueness exposure

Where multiple historical trajectories satisfy the evidence, at least two materially different admissible members are retained or the full uncertainty range is otherwise represented.

### T6 — sensitivity

The downstream hydrological attribution quantity must be tested across admissible reconstruction members. If the result changes materially, the boundary remains a dominant uncertainty and the historical claim must report that dependence.

### T7 — pair consistency

Exactly the same managed-boundary reconstruction/member must be applied to CURRENT and REFERENCE runs for simple soil-state attribution.

### T8 — provenance closure

Every bound, rule and transferred near-period value is linked to evidence and its temporal-applicability decision.

## 7. Temporal-transfer rule for near-period capacities

The 2006 official system evidence is useful because it documents the pre-merger topology and nominal capacities. It is still later than the 1998 event.

Before any listed capacity is used numerically in an R1 reconstruction, a future workunit must establish one of:

1. source evidence that the same pump/installed capacity applied in October 1998; or
2. an explicitly bounded transfer range that covers plausible 1998 capacity and is propagated through the reconstruction.

Without one of these, the capacities remain contextual constraints and cannot be fixed numerical 1998 inputs.

## 8. Emergency pumping rule

Current evidence proves emergency pumping occurred but does not identify enough numerical detail to construct its discharge series.

Therefore a future reconstruction must either:

- acquire deployment timing/location/capacity records; or
- represent emergency pumping through explicitly bounded alternative members whose timing/capacity are free reconstruction parameters constrained by the event narrative and any later archival evidence.

A reconstruction that omits emergency pumping and still claims to represent the actual crisis period requires an explicit immateriality demonstration.

## 9. Relationship to initial state

Managed-boundary reconstruction and initial-state reconstruction are coupled but not identical.

A reconstructed boundary cannot by itself define the root-zone/phreatic initial state. A later warm-up/restart protocol may use the qualified boundary reconstruction as one prerequisite, but must separately qualify forcing, drainage, crop/land use, soil-state semantics and convergence/equivalence across CURRENT and REFERENCE.

## 10. Current verdict

`MANAGED_BOUNDARY_RECONSTRUCTION_PROTOCOL_QUALIFIED_NO_EVENT_BOUNDARY_ADMISSION`

`DR_SM_MANAGED_BOUNDARY` remains `PARTIAL_EVIDENCE`.

The next scientific mutation requires either:

- new 1998 owner/archive evidence; or
- a separately reviewed candidate R1/R2 reconstruction dataset built according to this protocol.

No numerical boundary and no model run are authorized here.