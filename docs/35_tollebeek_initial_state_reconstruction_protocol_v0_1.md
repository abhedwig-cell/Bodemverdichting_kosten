# Tollebeek 1998 initial-state reconstruction protocol v0.1

Status: **QUALIFICATION CANDIDATE — protocol only**

Governing readiness item: `DR_SM_INITIAL_STATE`

Event: `EVT_TOL_1998_OCT`

This protocol defines when an initial hydrological state for the 1998 Tollebeek event may be treated as observed, historically reconstructed, scenario-only, or inadmissible. It does **not** create a numerical initial state, restart file, groundwater level, pressure-head profile or soil-water profile.

## 1. Scientific purpose

The first paired CURRENT/REFERENCE experiment requires an initial hydrological state that does not contaminate the intended soil-state attribution.

The canonical evidence currently provides:

- observed hourly meteorological forcing from KNMI station 273 for 1998-10-24 through 1998-10-30;
- qualitative owner evidence that the period preceding the event was very wet / described as fully saturated;
- two deep-screen historical piezometric series inside OT.02 with observations around the event period;
- a systematic public BRO search that found no qualifying shallow historical series inside OT.02;
- nearby shallow series outside the admitted OT.02 polygon, retained as context only;
- no admitted event-date root-zone pressure-head, soil-water or shallow phreatic profile inside OT.02.

The 144-hour admitted event-forcing context is **not** a hydrological warm-up by itself.

## 2. Core attribution rule

CURRENT and REFERENCE must receive **equivalent initialization semantics**.

Equivalent does not necessarily mean numerically identical state variables.

If CURRENT and REFERENCE use different hydraulic functions, then:

- identical volumetric water content can imply different pressure heads;
- identical pressure heads can imply different volumetric water contents;
- a common warm-up under identical forcing and boundary semantics can legitimately end in different water-content profiles because the soil states differ.

The initialization rule must therefore be tied to the causal design, not to superficial numerical equality.

For a simple soil-state attribution experiment, the preferred rule is:

> Apply the same reproducible initialization protocol, forcing history, managed-boundary semantics, drainage semantics, crop/land-use semantics and numerical convergence criteria to CURRENT and REFERENCE; allow the resulting hydrological state to differ only through the admitted soil-state contrast and its physical consequences.

Any deliberate difference in initialization semantics between CURRENT and REFERENCE requires a separate scientific justification and breaks the simple matched-pair interpretation.

## 3. Reconstruction ladder

### I0 — OBSERVED_INITIAL_STATE

Highest authority.

An I0 state requires direct or sufficiently local observations that constrain the variables used to initialize the selected model representation. Depending on the model configuration this may include:

- shallow/phreatic groundwater level;
- pressure head by depth;
- volumetric water content by depth;
- soil-water potential or an independently qualified transformation;
- an observed/model restart produced before the event under a separately qualified continuous simulation.

Required metadata include location, date/time, timezone, vertical datum, ground level, depth/screen interval, units, QC/status, source-native identifiers and provenance.

A single deep piezometric head is not sufficient to define an I0 root-zone state without a separately qualified hydrogeological relation.

### I1 — CONSTRAINED_HISTORICAL_RECONSTRUCTION

Permitted for Track H only when direct I0 observations are unavailable and a reproducible reconstruction can be constrained by historical evidence.

Allowed I1 mechanisms include:

1. **Warm-up/restart reconstruction**
   - simulate a period preceding `1998-10-24T00:00:00Z`;
   - use observed or independently qualified forcing for the warm-up period;
   - use the admitted or historically reconstructed boundary, drainage and land-use semantics appropriate to that period;
   - persist the exact warm-up start, forcing source, configuration, convergence criteria and restart checksum;
   - apply equivalent protocol semantics to CURRENT and REFERENCE.

2. **Hydrostatic or pressure-profile reconstruction**
   - only if a sufficiently representative shallow groundwater anchor or pressure-head observation is available;
   - preserve ground elevation and datum;
   - do not derive the anchor from target surface-water level, deep piezometric head or narrative wetness alone;
   - document the hydrostatic assumption and sensitivity to plausible deviations.

3. **Data-constrained ensemble reconstruction**
   - retain multiple admissible initial-state members when the evidence is non-identifying;
   - propagate member uncertainty into model outputs rather than selecting a single undocumented best guess.

I1 must expose the gap between observed evidence and reconstructed variables. Reconstructed values must never be relabelled as direct observations.

## 4. I1 minimum requirements

An I1 initial state may be considered for historical attribution only when all of the following hold:

1. the numerical variables required by the selected SWAP configuration are explicitly listed;
2. the reconstruction start and event start are explicit and timezone-safe;
3. forcing before the event is independently sourced and persisted;
4. historical boundary semantics are at least R1-qualified under the managed-boundary protocol;
5. drainage semantics are sufficiently specified for the chosen representation;
6. land-use/crop semantics are admitted or explicitly scenario-controlled for the warm-up period;
7. model executable/configuration authority is pinned;
8. CURRENT and REFERENCE use equivalent initialization protocol semantics;
9. convergence or spin-up adequacy criteria are explicit;
10. uncertainty from non-observed initial conditions is quantified by alternatives/sensitivity where material;
11. available shallow/deep observations and the qualitative very-wet antecedent evidence are used only as appropriate validation constraints, respecting their representativeness limits;
12. no missing variable is silently filled by a SWAP default.

Failure of one of these conditions keeps the reconstruction below I1.

## 5. Spin-up adequacy

A warm-up is not qualified merely because the model runs for a long time.

The protocol must define one or more adequacy diagnostics appropriate to the selected representation, for example:

- change in root-zone storage between repeated forcing cycles below an explicit tolerance;
- stability of pressure head / groundwater trajectory over a defined terminal period;
- convergence of drainage/storage terms relevant to the event response;
- sensitivity of event outputs to extending the warm-up duration;
- consistency with available late-October groundwater context without calibrating to data that are not spatially representative.

The exact tolerances are part of the later numerical workunit and are not invented here.

## 6. I2 — ENVELOPE_INITIAL_STATE_SCENARIO

I2 is allowed for Track S mechanism/sensitivity analysis when historical reconstruction cannot be qualified.

Examples include explicitly bounded wetness scenarios such as multiple initial pressure-head or groundwater-depth members.

I2 rules:

- label every member `SCENARIO_ONLY`;
- document the physical meaning of each member;
- use the same member definition for CURRENT and REFERENCE;
- do not describe the ensemble median or preferred member as the observed 1998 initial state;
- do not use the owner statement `fully saturated` as authorization to set every profile node to saturation without a separate scenario definition;
- report sensitivity across the envelope rather than hiding it in one selected run.

I2 cannot support a claim about the actual magnitude of the 1998 Tollebeek compaction effect without additional historical qualification.

## 7. I3 — INADMISSIBLE_DEFAULT

The following are explicitly inadmissible as closure mechanisms:

- set initial groundwater equal to the NAP -6.20 m surface-water target;
- infer shallow groundwater directly from the two deep-screen piezometric heads;
- initialize the profile as fully saturated because the historical narrative uses the words `fully saturated`;
- treat the admitted 144-hour forcing window as sufficient spin-up by definition;
- start from field capacity, wilting point or another standard profile merely because SWAP accepts it;
- copy an arbitrary historical SWAP example/restart;
- set missing initial-state variables to zero;
- choose a single plausible-looking profile because it produces stable output;
- tune the initial state differently for CURRENT and REFERENCE to improve agreement.

Any of these routes is I3 and cannot move `DR_SM_INITIAL_STATE` beyond `PARTIAL_EVIDENCE`.

## 8. Role of current canonical observations

### Deep inside-OT.02 GLD series

The inside series at `GMW000000053815` remain hydrogeological context only. Their filters are far below the root zone and their historical observation status is `onbekend`.

They may constrain later hydrogeological plausibility only if a separate relationship between deep head and shallow system behaviour is qualified.

### Nearby shallow GLD series outside OT.02

These remain contextual validation evidence only. They must not be spatially interpolated into OT.02 and called an observed event initial state.

### Owner narrative of very wet / saturated antecedent conditions

This is a qualitative event-state constraint. It supports rejection of clearly dry reconstructions, but does not uniquely define groundwater depth, pressure head or water content.

### Antecedent meteorological forcing

Observed rainfall before the event can support an I1 warm-up only if a sufficiently long, independently acquired pre-event forcing history is persisted. Rainfall totals by themselves are not state variables.

## 9. Relationship to managed-boundary protocol

An I1 warm-up that depends on surface-water management cannot outrank the boundary information that drives it.

Therefore:

- R0 boundary evidence may support I1 initialization;
- R1 constrained historical boundary reconstruction may support I1 initialization if uncertainty is propagated consistently;
- R2 envelope-only boundary scenarios imply at most I2 initial-state status for historical claims unless separately justified;
- R3 boundary defaults cannot support any admissible historical initial-state reconstruction.

## 10. Relationship to drainage and land use

Warm-up can be sensitive to drainage and vegetation. Therefore:

- unresolved parcel-drain geometry/parameters cannot be silently replaced by historical 100 d / 30 d priors in an I1 reconstruction;
- unresolved October-1998 crop identity cannot be silently replaced by one representative crop or bare soil;
- if crop-independent or drainage-envelope experiments are used, the resulting initialization remains scenario-conditioned and must be labelled accordingly.

## 11. Relationship to CURRENT/REFERENCE soil state

REFERENCE-state construction follows CURRENT-state evidence; the initialization protocol must not be used to create the missing soil-state contrast.

The initialization process may produce different hydrological storage in CURRENT and REFERENCE because the admitted physical soil states differ. That difference is acceptable when it follows from the shared protocol and is part of the causal response to the soil-state contrast.

What is not acceptable is changing initial-condition rules, boundary forcing, warm-up length or tuning targets between the two pair members without explicitly changing the scientific question.

## 12. Future numerical admission contract

A future initial-state dataset/restart can only be admitted when it contains or references at minimum:

- `initial_state_id` / reconstruction member ID;
- event ID;
- CURRENT/REFERENCE pair semantics;
- reconstruction class I0/I1/I2;
- source/restart authority and checksum;
- warm-up start/end or observation timestamp;
- forcing authority;
- boundary member/reconstruction authority;
- drainage configuration authority;
- land-use/crop semantics;
- SWAP executable/configuration authority;
- exact state variables/units/depth convention;
- spin-up adequacy diagnostics;
- uncertainty/member identity;
- QC/verdict;
- explicit prohibition on relabelling reconstructed/scenario states as observations.

## 13. Current verdict

`DR_SM_INITIAL_STATE` remains `PARTIAL_EVIDENCE`.

Current route classification remains `RECONSTRUCTABLE_WITH_EXPLICIT_UNCERTAINTY`.

No I0 observation, I1 restart/warm-up, I2 numerical envelope or SWAP model input is admitted by this protocol.

The next numerical step is permitted only after dependencies required by the chosen route are sufficiently specified. For Track H this means, at minimum, a qualified boundary reconstruction/observation route plus sufficiently specified drainage, land-use and model configuration, or newly acquired direct initial-state observations that reduce those dependencies.
