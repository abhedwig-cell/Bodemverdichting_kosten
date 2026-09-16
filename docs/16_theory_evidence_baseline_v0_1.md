# Theory evidence baseline v0.1

Status: **WORKING_BASELINE**  
Scope: core theory used by the project across state, response, counterfactual attribution, transfer, aggregation and valuation  
Purpose: connect the narrative theoretical framework to explicit sources, atomic evidence items, project claims and intended-use qualifications

## 1. Why this baseline exists

`02_theoretical_framework.md` defines the scientific logic the project wants to preserve. This document answers a different question:

> Which parts of that logic are currently supported by explicit project evidence, and what does that evidence *not* permit us to conclude?

The canonical records are in:

- `evidence/sources.csv`;
- `evidence/evidence_register.csv`;
- `evidence/claims.csv`;
- `evidence/qualification_register.csv`.

This document is a readable index over those records. It is not a replacement for them.

## 2. Core source set

The first theory baseline uses five sources that serve different purposes.

### Keller et al. 2019

`SRC_KELLER2019`

Peer-reviewed synthesis/mechanistic paper on machinery loading, soil stress, soil physical functioning, root accessibility, crop response and hydrological consequences.

Project use:

- physical mechanisms linking compaction to root/resource accessibility;
- reduced infiltration, hydraulic conductivity and storage as plausible runoff mechanisms;
- explicit caveat that field-experiment controls are often *normally compacted* rather than truly uncompacted;
- scale-up problem from soil/profile studies to catchment and societal effects.

Not admitted:

- a universal yield-loss percentage;
- a universal runoff coefficient;
- direct attribution of observed flood trends to soil compaction.

### Graves et al. 2015

`SRC_GRAVES2015`

Peer-reviewed national economic/ecosystem-services framework for England and Wales.

Project use:

- explicit counterfactual reasoning;
- soil × land-use `soilscape` architecture as national aggregation precedent;
- distinction between on-site/private and off-site/external effects;
- boundary between high-level national assessment and local process modelling.

Not admitted:

- UK soilscape probabilities as Dutch exposure probabilities;
- UK cost shares or unit values as current Dutch coefficients;
- the high-level soilscape model as a substitute for event/process hydrology.

### Groenendijk et al. 2017

`SRC_GROENENDIJK2017`

Dutch WUR/STOWA report combining measurements, synthesis and SWAP-based model studies.

Project use:

- explicit compacted-layer depth/thickness in hydrological modelling;
- thin numerical discretisation around strong hydraulic contrasts;
- hourly rainfall as a defensible baseline for source-runoff studies;
- evidence that model response changes with lower-boundary choice;
- case-specific runoff and evapotranspiration results as external magnitude/context checks.

Not admitted:

- a generic Netherlands `delta runoff` factor;
- direct transfer of local/podzol results to Tollebeek light zavel;
- treatment of all reported `soil improvement` yield gains as the inverse of compaction damage.

### Kuhlman et al. 2010

`SRC_KUHLMAN2010`

Exploratory Dutch economic study of several soil-degradation processes including subsoil compaction.

Project use:

- historical Dutch context for agricultural and external effects;
- evidence that rooting, infiltration/aeration and runoff-related external pathways were already identified as relevant;
- historical cost estimates as comparison benchmarks.

Not admitted:

- the 2010 EUR/ha figures as current unit costs;
- simple inflation of those figures to create a 2026 cost parameter;
- a national current estimate of affected area.

### Romero-Ruiz et al. 2026

`SRC_ROMERO2026`

Peer-reviewed European future-climate modelling study coupling soil-compaction and agroecosystem modelling across multiple soil services.

Project use:

- comparison with a multi-service architecture;
- reminder that crop, nitrogen, carbon and runoff consequences can arise from a shared soil-state problem while remaining different response pathways;
- external benchmark/scenario context.

Not admitted:

- direct use of European future-climate monetary estimates as current Netherlands costs;
- transfer of winter-wheat/SSP585/4–8 Mg wheel-load scenario results to another crop, climate or current Dutch soilscape without separate qualification.

## 3. Qualified theoretical principles

### 3.1 State does not map to one universal damage coefficient

Canonical claim: `CL_THEORY_STATE_RESPONSE_CONTEXT`.

Keller supports multiple interacting mechanisms and explicitly states that the limiting process depends on soil and weather conditions. Groenendijk shows that lower-boundary conditions and profile configuration materially change simulated response.

Therefore the framework keeps:

```text
soil state + forcing + crop + geometry + boundary
    → response
```

rather than:

```text
severity class → fixed damage %
```

This is a structural conclusion. It does not supply the missing pathway-specific response functions.

### 3.2 Reference state must be contextual

Canonical claim: `CL_THEORY_REFERENCE_CAUTION`.

Keller shows why `no additional experimental compaction` is not identical to an uncompacted soil. Graves independently uses a counterfactual defined within the context of each managed soilscape.

For this project that supports:

```text
Y_current   = M(S_current,   F, C, G, B)
Y_reference = M(S_reference, F, C, G, B)

delta_Y = Y_current - Y_reference
```

where the scientific meaning of `S_reference` must be explicitly justified.

### 3.3 Vertical profile geometry is part of the state

Canonical claim: `CL_THEORY_PROFILE_DEPTH`.

Groenendijk identifies compacted-layer thickness and overlying-layer thickness as strong controls on hydrological response and recommends fine discretisation around the restrictive layer.

The consequence for the data model is that layer depth and thickness cannot be discarded in favour of a single soil-wide compaction scalar where the response depends on depth.

### 3.4 Runoff is an event-scale response

Canonical claim: `CL_THEORY_TEMPORAL_FORCING`.

Groenendijk specifically recommends hourly rainfall for the studied SWAP runoff problem. The project therefore treats annual rainfall/runoff totals as insufficient by themselves for event occurrence, timing or peak qualification.

Hourly forcing is currently a defensible baseline, not a claim that sub-hourly intensity can never matter.

### 3.5 Source response and off-site consequence require a transfer layer

Canonical claim: `CL_THEORY_SCALE_TRANSFER`.

Keller identifies the unresolved scale gap between profile-scale compaction knowledge and catchment/regional impacts. Graves states explicitly that its national soilscape method is not intended to represent local degradation probabilities or intensity gradients.

This supports the project decomposition:

```text
source response
    → transfer / connectivity / routing
    → receptor or managed-system response
    → valuation
```

A local runoff result therefore cannot be multiplied directly by national area and labelled societal damage without a qualified transfer/aggregation argument.

### 3.6 Soil × land use is useful for national exposure, not a universal response function

Canonical claim: `CL_THEORY_SOILSCAPE`.

Graves provides a clear precedent for combining land cover and soil type into national assessment units while treating climate/topography as modifying state factors.

For this project, that supports a Dutch soil × land-use exposure/aggregation layer. It does **not** support importing the UK categories, probabilities or costs.

### 3.7 Economic categories must remain explicit

Canonical claim: `CL_THEORY_ECONOMIC_CATEGORIES`.

Graves distinguishes on-site/private and off-site/external costs and notes that external effects can require market and non-market valuation. Kuhlman provides Dutch historical cost context but also emphasises the exploratory nature and incomplete quantification.

The project therefore keeps at least:

- private/farm cost;
- public-budget expenditure;
- societal-welfare effect.

These may overlap physically but are not the same accounting concept.

### 3.8 A benchmark is not automatically a parameter

Canonical claim: `CL_THEORY_BENCHMARK_NOT_PARAMETER`.

Three useful examples make this rule concrete:

- Groenendijk case-specific runoff results demonstrate plausible response magnitudes but are not Tollebeek coefficients;
- Kuhlman 2010 EUR/ha estimates are historical exploratory benchmarks, not current prices or damage functions;
- Romero-Ruiz European future-climate outputs belong to a different crop/scenario/population than the current Dutch pilot.

The project records benchmark evidence because comparison is valuable, while preventing silent parameter transfer.

### 3.9 One soil-state framework may feed multiple services

Canonical claim: `CL_THEORY_MULTI_SERVICE`.

Romero-Ruiz demonstrates a modelling architecture in which one compaction problem is evaluated for yield, nitrogen, carbon and runoff. Keller likewise documents multiple physical/biological mechanisms.

The project can therefore reuse a common description of soil state, but each response pathway still requires its own model, evidence, transfer and valuation qualification.

## 4. Evidence that remains intentionally local or bounded

Some numerically strong-looking evidence is *not* promoted to general theory.

### Groenendijk local runoff example

`EV_GROEN_LOCAL_RUNOFF` records a reported model comparison with 14 mm/year surface runoff under compaction versus 4 mm/year without compaction for one setup using 2008 hourly rainfall.

Project role: `BENCHMARK_ONLY`.

Reason: the magnitude is conditional on profile, hydraulic parameters, weather and boundary configuration.

### Kuhlman historical Dutch cost range

`EV_KUHLMAN_EXPLORATORY_COST` records the exploratory 2010 agricultural cost range of roughly EUR 80 to 300 per ha per year for selected Dutch farming/soil contexts.

Project role: `BENCHMARK_ONLY`.

Reason: historical price level, simplified assumptions and incomplete national exposure knowledge.

### Romero-Ruiz European future scenarios

The source contains large European economic estimates, but v0.1 deliberately does not register those values as project cost evidence because the current need is theoretical architecture, not a continental future-climate cost benchmark.

If they are later used in comparison figures, they should be added as explicit evidence items with scenario metadata rather than copied into the valuation model.

## 5. What this baseline changes in the project

Before this work, the repository had a strong theory narrative and a detailed Tollebeek evidence baseline, but the two were unevenly connected.

This v0.1 baseline makes several high-risk theoretical choices directly traceable:

```text
reference-state caution
profile depth / layer geometry
conditional response
sub-daily runoff forcing
plot-to-system transfer separation
soilscape aggregation boundary
economic-category separation
benchmark-versus-parameter rule
multi-service architecture
```

These principles can now be reviewed independently of the Tollebeek asset details.

## 6. What this baseline does not solve

It does not yet constitute a complete literature review.

Important next evidence work remains for:

- construction of current/reference hydraulic states from measured Dutch soil-state data;
- pedotransfer functions and hydraulic-property transformation under compaction;
- crop-specific production response beyond the current synthesis sources;
- direct event-scale field-edge runoff and connectivity evidence;
- national exposure weighting from CC-NL;
- current Dutch valuation relations;
- nutrients/pesticides and other future off-site pathways.

These should be added as bounded evidence campaigns rather than by expanding prose first.

## 7. Review rule

A theoretical claim should be revisited when:

- a primary source contradicts the present synthesis;
- the intended population or scale changes materially;
- a benchmark is promoted toward a model parameter;
- a new implementation uses the claim in a stronger way than currently qualified;
- new Dutch measurements allow a previously generic principle to become pathway-specific.

That review should update the evidence/claim/qualification registers first, and the narrative documents second.
