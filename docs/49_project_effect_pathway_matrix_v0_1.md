# Project effect-pathway matrix v0.1

Status: **WORKING CANONICAL DECISION MATRIX**  
Parent document: `00_project_handover_and_continuation.md`  
Purpose: give a colleague a practical surface for continuing the project without collapsing the causal chain or defaulting immediately to detailed modelling.

## 1. How to use this matrix

This matrix answers one question per effect route:

> **What is the lightest scientifically defensible way to move from soil compaction to a physical and, where possible, monetary consequence?**

For every route we keep separate:

1. the full causal chain;
2. evidence already available;
3. uncertainty within and between sources;
4. whether an empirical shortcut is defensible;
5. what can already be monetised;
6. the smallest useful next action;
7. what is explicitly not allowed.

The matrix is deliberately not a table of "best coefficients". A source may be useful as:

- direct evidence;
- proxy;
- bound;
- benchmark;
- mechanism-only evidence;
- scenario evidence.

Those roles should not be silently mixed.

## 2. Common trunk

All on-site and off-site routes start from a common description of exposure/state:

```text
where is compaction present?
        ↓
what state/severity/depth/profile context does it represent?
        ↓
what comparison/reference is relevant?
        ↓
which response pathway is being asked about?
```

The same exposure dataset may feed multiple pathways, but **one universal damage coefficient is not assumed**.

National reporting should generally retain at least:

- land use;
- soil type / soilscape;
- depth or restrictive-layer context where material;
- severity/exposure definition;
- relevant crop refinement where valuation depends strongly on crop.

## 3. On-site pathways

### O1 — Crop yield / production quantity

**Full chain**

```text
compaction/state
 → rooting + aeration + water availability + mechanical resistance
 → crop stress / growth
 → physical yield
 → attributable yield loss
 → economic valuation
```

**Evidence already available**

The earlier evidence library contains several distinct classes rather than one transferable coefficient:

- Dutch maize field evidence / historical estimates;
- grassland evidence with both negative and sign-changing responses;
- soil-improvement model studies for grass and maize;
- long-term international field-experiment bounds around persistent subsoil compaction;
- context-specific heavy-clay cereal evidence.

The earlier response bridge correctly concluded that no central CC-NL-severity-to-yield coefficient was yet admitted.

**Uncertainty**

Keep at least four components visible:

- study-internal uncertainty/range;
- crop and soil context;
- weather dependence;
- comparator/reference-state definition.

**Evidence-ensemble option**

Yes. For a matched soil/crop context, multiple studies may form a bounded ensemble, but treatment-based experiments, inverse soil-improvement studies and severity-class data should remain distinguishable ensemble members rather than being blindly pooled.

**Possible shortcut**

A direct empirical yield relation is the preferred low-computation route **when context matching is defensible**.

**Monetisation**

Use crop-specific economic data. Keep separate:

- gross revenue loss;
- marginal farmer-private loss;
- lost production value;
- societal welfare loss.

**Current verdict**

`EVIDENCE_AVAILABLE_BUT_NO_UNIVERSAL_COEFFICIENT`

**Smallest next action**

For the first 1–3 priority soil × crop combinations, construct an evidence ensemble with explicit applicability and low/base/high or source-member outcomes before considering a process model.

**Do not**

- assign one 5–30% workplan range nationally;
- map axle load directly to a modern severity class;
- treat inverse soil-improvement benefits automatically as equal compaction damage;
- multiply all arable land by one generic yield-loss percentage.

---

### O2 — Crop quality

**Full chain**

```text
compaction/state
 → crop physiological response
 → quality/grade/marketability
 → price or rejected product
 → private/economic consequence
```

**Evidence already available**

The present canonical and recovered evidence set is much thinner here than for physical yield.

**Uncertainty**

Potentially crop-specific and market-specific.

**Evidence-ensemble option**

Not yet justified.

**Possible shortcut**

Only if crop-specific literature directly reports quality/grade effects under a relevant compaction treatment/state.

**Monetisation**

Potentially price differential, rejected volume or quality-class shift.

**Current verdict**

`KNOWLEDGE_GAP`

**Smallest next action**

Do not launch broad modelling. First perform a focused literature check for high-value crops where quality loss could materially change total costs.

**Do not**

infer quality loss from yield loss without evidence.

---

### O3 — Potential irrigation need / drought sensitivity

**Full chain**

```text
compaction/state
 → root-zone water availability / ET / drought stress
 → potential irrigation requirement
 → actual irrigation decision
 → supplied water and energy/cost
```

**Evidence already available**

Dutch model/case evidence contains:

- ET reductions for grass and maize;
- strong profile dependence;
- dry-year irrigation-sensitivity examples;
- large weather dependence.

The earlier work correctly separated **ET reduction**, **potential irrigation need**, and **actual water supplied**.

**Uncertainty**

- weather/year type;
- soil profile and groundwater;
- irrigation rule;
- water availability;
- farmer adoption/response.

**Evidence-ensemble option**

Yes, but as scenario/conditional evidence rather than one annual coefficient.

**Possible shortcut**

Use literature-derived dry-year or long-term potential-demand ranges where the soil/crop context matches.

**Monetisation**

Only after a separate supply/adoption step. Candidate values can come from current agricultural water-cost/value sources, but physical need is not automatically actual supply.

**Current verdict**

`PHYSICAL_BOUNDS_AVAILABLE_SUPPLY_LINK_MISSING`

**Smallest next action**

Build a three-stage calculation:

```text
potential deficit → irrigation/adoption fraction → actual supplied water
```

with each stage separately uncertain.

**Do not**

convert 50–90 mm potential irrigation response directly into water-board cost or supplied volume.

---

### O4 — Extra field operations / workability

**Full chain**

```text
compaction/state
 → wetness / bearing capacity / trafficability / tillage resistance
 → delayed or extra field operation
 → machinery, labour, fuel, crop-timing consequence
 → private cost
```

**Evidence already available**

The current recovered project evidence is not yet sufficiently populated for a robust numerical route.

**Uncertainty**

Operation, soil, crop, weather and management dependent.

**Evidence-ensemble option**

Potentially, once farm-management evidence is gathered.

**Possible shortcut**

Business/farm-accountancy evidence may be more efficient than physical modelling.

**Monetisation**

Additional operation cost, labour, fuel or timeliness loss.

**Current verdict**

`PROMISING_ONSITE_GAP`

**Smallest next action**

Use WSER/business expertise and targeted literature to determine whether this pathway is material enough to retain in the first national estimate.

**Do not**

create machinery-cost coefficients from engineering intuition alone.

---

### O5 — Private farm cost consolidation

This is not a physical pathway but a valuation node.

Preferred hierarchy:

1. marginal farmer-private damage where data support it;
2. gross revenue loss as transparent accounting/sensitivity measure;
3. proportional margin only as sensitivity;
4. societal production value reported separately.

**Key guardrail**

Private farm loss and societal lost production value are not automatically additive.

**Current verdict**

`METHOD_READY_INPUT_GATED`

---

## 4. Off-site pathways

### F1 — Additional surface runoff / altered drainage response

**Full chain**

```text
compaction/state
 → hydraulic/storage/root-zone change
 → runoff/drainage response at parcel
 → field-edge/source hydrograph
```

**Evidence already available**

The recovered evidence includes:

- Dutch/Vlaamse process-model examples of additional annual runoff;
- event peak sensitivity to compacted-layer depth;
- measured/profile-based hydrological model cases;
- mechanistic evidence for reduced conductivity/infiltration.

The evidence strongly supports context sensitivity and the importance of layer depth, but not one national runoff factor.

**Uncertainty**

- profile geometry;
- antecedent wetness;
- groundwater;
- rainfall regime/event;
- hydraulic mapping;
- surface storage.

**Evidence-ensemble option**

Yes, as local/process bounds or matched-source ensembles.

**Possible shortcut**

For a sufficiently similar soilscape/event, a published local response range can be used as a bounded physical shortcut.

**Monetisation**

Not yet. Parcel runoff is only a source effect.

**Current verdict**

`LOCAL_EVIDENCE_AVAILABLE_TRANSFER_REQUIRED`

**Smallest next action**

For each priority hydrological system type, choose either:
- a matched empirical/local response bound, or
- a simple/process calculation only if the bound is insufficient.

**Do not**

multiply a local +9 or +10 mm/year result by national affected area and call it system damage.

---

### F2 — Field-edge / ditch / network delivery

**Full chain**

```text
generated parcel response
 → field edge
 → drainage/ditch
 → local storage/routing
 → receiving network
```

**Evidence already available**

Conceptual structure is strong; generic numerical delivery evidence is weak. Tollebeek work has made the need for connectivity/routing explicit.

**Uncertainty**

- microrelief;
- drainage connectivity;
- local storage;
- ditch density;
- event timing;
- system class.

**Evidence-ensemble option**

Potentially by hydrological system type, not as a single national factor.

**Possible shortcut**

A bounded delivery factor may be used only after it is qualified for a system class or pilot.

**Monetisation**

No direct monetisation at this step.

**Current verdict**

`FRAMEWORK_READY_DATA_GAP`

**Smallest next action**

Develop a small hydrological-system typology and identify which classes can be supported by existing literature/data before any regional modelling.

**Do not**

assume generated runoff equals delivered runoff.

---

### F3 — Managed water-system operation: pumping, energy and capacity

**Full chain**

```text
delivered water / hydrograph
 → managed-system routing
 → pump/control response
 → additional volume/hours/energy/capacity pressure
 → public-budget or resource cost
```

**Evidence already available**

This is the most technically developed off-site subroute because of the Tollebeek pilot. The project already distinguishes:

- installed capacity from available capacity;
- target level from dynamic head;
- delivery from pump volume;
- directional assist/routing;
- pump volume from energy and economic cost.

**Uncertainty**

- actual delivered hydrograph;
- control rules;
- asset availability;
- head and efficiency;
- coincidence with baseline load;
- tariffs/O&M.

**Evidence-ensemble option**

More naturally a system-scenario ensemble than a literature ensemble.

**Possible shortcut**

For simple systems, observed energy/intensity or owner operational records could bypass detailed hydraulic simulation if attribution is defensible.

**Monetisation**

Variable energy, operation/maintenance, or other public-budget expenditure. Societal resource cost remains a separate concept.

**Current verdict**

`PILOT_ARCHITECTURE_ADVANCED_GENERAL_SCALING_OPEN`

**Smallest next action**

Do not extend Tollebeek detail everywhere. First determine whether a few representative managed-system classes plus observed operating cost/intensity can bound the national off-site contribution.

**Do not**

use installed pump capacity as actual incremental operation or treat one pilot as national transfer coefficient.

---

### F4 — Flood / waterlogging / peak-risk consequence

**Full chain**

```text
incremental hydrograph
 → network/storage/capacity interaction
 → change in exceedance or inundation
 → exposed assets/crops
 → damage/risk-management cost
```

**Evidence already available**

Graves supplies a high-level 3–10% attribution benchmark in an England/Wales national framework. The project has correctly retained this as benchmark-only rather than a Dutch damage factor.

**Uncertainty**

Very high because timing, buffering, threshold behaviour and spatial exposure dominate.

**Evidence-ensemble option**

Not yet for a Dutch national coefficient.

**Possible shortcut**

Benchmarking is useful; direct Dutch monetisation requires a system-risk link.

**Monetisation**

Expected damage / avoided damage / risk-management cost, depending on economic question.

**Current verdict**

`BENCHMARK_ONLY`

**Smallest next action**

Keep as an off-site endpoint in the cost tree. Quantify only when a Dutch hydrological-system response and exposure relation is available.

**Do not**

apply 3–10% of Dutch flood damage as a current soil-compaction cost.

---

### F5 — Regional water-supply pressure / actual additional water delivery

This pathway shares the physical drought-response trunk with O3 but the receptor is outside the farm.

```text
potential crop-water deficit
 → farmer demand
 → actual source/supply
 → regional water allocation / conveyance
 → resource or scarcity consequence
```

**Evidence already available**

Potential water-demand bounds exist; economic water-value/cost information exists in the recovered workbook, but the conversion from potential need to actual delivered supply remains a knowledge gap.

**Current verdict**

`VALUATION_CANDIDATE_PHYSICAL_TRANSFER_MISSING`

**Smallest next action**

Separate:
- groundwater abstraction;
- surface-water delivery;
- unsupplied deficit.

Only monetise actual resource use or welfare effect that can be attributed.

---

### F6 — Water quality: nutrients / pesticides / other substances

**Full chain**

```text
compaction
 → altered runoff/drainage/erosion
 → substance mobilisation/concentration
 → transfer/retention
 → receiving-water effect
 → treatment/ecological/welfare consequence
```

**Evidence already available**

The pathway is recognised but not quantitatively mature in the current project. Earlier scope governance deliberately kept nutrients as a linked-later route.

**Uncertainty**

Mechanism, concentration, route, retention, timing and receptor response.

**Evidence-ensemble option**

Potentially later.

**Possible shortcut**

Only where a directly relevant empirical concentration/load response exists.

**Monetisation**

Not active until physical load/receptor effect is defensible.

**Current verdict**

`LINKED_LATER`

**Smallest next action**

Maintain the causal node and collect candidate evidence opportunistically; do not let it delay the first water/yield estimates.

---

## 5. Cross-path uncertainty framework

For each active pathway, the preferred uncertainty record is:

| Uncertainty layer | Minimum representation |
|---|---|
| Exposure/state | range, class uncertainty or alternative state scenario |
| Response within study | reported CI/range/scenario if available |
| Between studies | separate ensemble members or source range |
| Transferability | applicability class / scenario, not a hidden weight |
| Transfer/system | system-class scenarios or measured bounds |
| Economic | price/cost period and low/base/high where material |
| Structural route | alternative causal/shortcut routes reported separately |

Do not automatically collapse this to a single confidence score.

## 6. Evidence ensemble protocol v0.1

An evidence ensemble should be created only when the members answer sufficiently similar questions.

Each member must carry:

- source ID;
- population/context;
- soil and crop;
- compaction definition;
- comparator/reference;
- time/weather context;
- effect estimate/range;
- uncertainty reported by the source;
- directness;
- transferability;
- allowed use;
- prohibited use.

### Ensemble outcomes

Three valid outcomes are possible:

1. **Comparable ensemble** — members can support a combined or envelope range.
2. **Scenario ensemble** — members represent different contexts and remain separate scenarios.
3. **Incompatible set** — sources are informative but should not be numerically pooled.

The default is **not** to average.

## 7. Priority order for the next substantive analysis

### Priority A — first on-site estimates

Start with soil × crop combinations for which Dutch or near-Dutch evidence already exists and economic valuation can be supplied with limited new work.

Candidate order from the existing work:

- grassland on sandy soils;
- silage maize on sandy soils;
- cereals / light-zavel or clay refinement only with explicit evidence bounds.

Target output:

```text
exposure × evidence ensemble × crop value
 → private/accounting range
```

with no need for a process model unless the literature ensemble remains too broad for the intended decision.

### Priority B — first off-site physical estimates

Keep two hydrological receptor classes in view:

- free/drained agricultural settings;
- managed/polder settings.

Target output first:

```text
source physical effect → delivery/system bound
```

before monetary aggregation.

Tollebeek remains useful for the managed-system class but should not define all off-site scaling.

### Priority C — information-value decision

For each remaining large uncertainty ask:

> Would a new dataset, a targeted literature extraction, or a detailed model reduce the final cost uncertainty most?

This should determine where 2027 modelling effort goes.

## 8. Working verdict

The project is already far enough to begin **bounded, source-ensemble-based estimates** for selected on-site pathways and **bounded physical estimates** for selected off-site pathways.

The present bottleneck is no longer the absence of a calculation framework. It is the disciplined matching of:

```text
exposure
× applicable response evidence
× transfer where required
× correct valuation
```

Detailed process modelling is therefore a targeted uncertainty-reduction instrument, not the default next step.
