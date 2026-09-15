# 2. Theoretical framework

Status: **Status-A-light theoretical baseline**

This document defines the scientific logic that the conceptual model, equations, data model and implementation must preserve. It is not a complete literature review. Source-specific facts and numerical relations belong in the evidence registers and are only used for a project purpose after qualification.

## 2.1 Object of study

Soil compaction changes the physical arrangement and functioning of the soil. Depending on texture, structure, organic matter, water status, depth and loading history, this can affect mechanical root impedance, porosity, water retention, hydraulic conductivity, infiltration, aeration, drainage and surface runoff.

The consequence is not determined by compaction alone. It emerges from the interaction between:

- soil profile and current physical state;
- depth and thickness of restrictive layers;
- land use, crop and rooting;
- meteorological forcing and antecedent conditions;
- groundwater and surface-water boundary conditions;
- artificial drainage and local topography;
- water-system connectivity and management;
- the economic receptor and valuation concept.

The theoretical framework therefore treats soil compaction as a **state-dependent causal driver inside a system**, not as a fixed percentage loss or a universal runoff coefficient.

## 2.2 Five scientific questions

The project separates five questions that can otherwise be accidentally collapsed.

### A. What soil state exists?

This is the **state/exposure question**.

Relevant observations may include bulk density, texture, clay/lutum content, organic matter, profile layering, compacted-layer depth and thickness, penetration resistance, hydraulic measurements and land use.

A severity class can summarise observations, but it does not by itself define a hydrological or crop response.

### B. What response follows from that state?

This is the **response question**.

Response depends on a forcing and boundary context. The same soil state may behave differently in a dry year, a wet winter, a short intense event or under another groundwater regime.

Responses of interest include, among others:

- crop production and transpiration;
- root-zone water stress;
- drainage;
- groundwater response;
- generated surface runoff;
- timing and magnitude of water fluxes.

### C. What part of the response is attributable to compaction?

This is the **counterfactual/attribution question**.

Observed runoff, yield loss or pump operation cannot automatically be attributed to compaction. Attribution requires a comparison with a relevant reference state under otherwise controlled conditions.

### D. Does the effect reach another actor or system?

This is the **transfer question**.

Parcel-generated water may be stored locally, infiltrate later, leave via drainage, cross the field edge, enter a ditch, be delayed in the network, reach a pump or be discharged elsewhere. The transfer pathway is therefore a scientific layer in its own right.

### E. What is the value or cost of the qualified effect?

This is the **valuation question**.

Money enters only after a physical effect and its receptor are defined. Different economic concepts answer different questions, so private cost, public-budget expenditure and societal-welfare effect cannot be mixed without an explicit relation.

## 2.3 Counterfactual framework

Let `S_current` denote the soil state for which the project wants to estimate consequences, and `S_reference` a matched reference state.

For an outcome `Y` under forcing `F`, crop/land use `C`, geometry `G` and boundary/system context `B`:

```text
Y_current   = M(S_current,   F, C, G, B)
Y_reference = M(S_reference, F, C, G, B)
```

The attributable difference is:

```text
delta_Y = Y_current - Y_reference
```

The scientific meaning comes from the **matching**. If crop, weather, drainage or boundary conditions also change, the result is no longer a clean estimate of the soil-state contribution unless those changes are explicitly part of the research question.

### Reference state is contextual

`REFERENCE` does not automatically mean:

- pristine soil;
- forest soil;
- zero traffic;
- zero bulk density increase;
- a universal national optimum.

A defensible reference should match the intended causal question and the profile context. Possible reference concepts may include a paired measured control, a locally lower-compaction state, a qualified agronomic reference or a modelled counterfactual constructed from evidence.

Reference choice is therefore part of the evidence and qualification record.

## 2.4 State, exposure and anthropogenic attribution are separate

A physically compacted state is not the same thing as proof of anthropogenic cause.

The project should keep at least the following distinctions visible:

```text
measured physical state
        ≠
response to that state
        ≠
anthropogenic attribution of that state
        ≠
transfer of the response
        ≠
economic valuation
```

This is especially important for national monitoring data. A bulk-density threshold may identify a restrictive state, but additional reasoning or evidence is needed before assigning that state to a specific management cause or converting it to damage.

## 2.5 Profile geometry matters

Compaction is vertically structured. A mean over a broad interval can hide the restrictive layer that controls infiltration, rooting or water storage.

The project therefore prefers a representation of the form:

```text
profile
  ├─ layer depth
  ├─ texture / organic matter
  ├─ hydraulic properties
  └─ state variables by depth
```

rather than one soil-wide compaction scalar where the physical process depends on depth.

For hydrology, the geometry above and within a compacted layer can influence how quickly storage is exhausted and when surface runoff begins. This is one reason the source-response model should preserve profile layers rather than only reporting a severity category.

## 2.6 Response is conditional on process and event state

Surface runoff is a useful example of why event context matters.

A parcel may have zero field-edge runoff in one event and positive runoff in another despite an apparently similar annual water balance. Antecedent wetness, groundwater position, rainfall intensity, infiltration capacity, surface storage and connectivity can change occurrence and magnitude.

The project therefore separates conceptually:

1. **occurrence**: does a positive transfer/runoff response occur?
2. **conditional magnitude**: how large is it when it occurs?

and, where needed, a separate peak/timing response.

No universal event-delivery probability or fixed fraction is assumed by default.

## 2.7 Parcel response and water-system response are different state spaces

A parcel model describes source processes. A water-system model describes routing, storage, control and operation.

The water route is therefore:

```mermaid
flowchart LR
    R[Generated parcel response] --> O[Field-edge occurrence / volume]
    O --> D[Ditch / local drainage system]
    D --> N[Network routing and storage]
    N --> P[Pump or other managed receptor]
    P --> C[Capacity / energy / operational effect]
```

Each arrow may have different data, time scale and uncertainty.

For managed polders this distinction is essential. Installed pump capacity tells us little about extra compaction-related pump operation until we know how the incremental water reaches that asset, when it arrives and which capacity is available at that moment.

## 2.8 On-site and off-site are coupled, not independent

The same hydrological change can affect the farmer and the water system in different ways.

For example, a change in infiltration and root-zone storage may influence:

- crop water stress and yield;
- irrigation requirement;
- drainage flux;
- runoff generation;
- timing of water leaving the parcel.

The framework should therefore calculate the physical water balance once under a controlled state definition and expose the relevant outputs to multiple consequence pathways. This reduces the risk that separate on-site and off-site models imply incompatible physics.

## 2.9 Aggregation principles

National relevance requires aggregation, but the theoretical framework imposes limits on how aggregation is performed.

### Additive quantities

Some quantities may be summed across independent areas or events when their units and scopes are compatible, for example annual water volumes after the transfer stage is defined.

### Non-additive quantities

The following generally cannot be aggregated by simple summation or averaging without additional structure:

- event occurrence probabilities;
- peak flows;
- capacity pressure;
- coincident demand;
- damage thresholds;
- nonlinear yield response;
- system dispatch.

The correct aggregation level therefore follows the physical mechanism, not the convenience of a spreadsheet total.

## 2.10 Economic theory boundary

A physical effect becomes an economic quantity only through an explicit valuation relation.

Three categories are kept separate:

### Private cost

Effects on the farm or business, such as output loss, attributable extra operations or purchased inputs.

Where output is lost, costs that are genuinely avoided because production did not occur may need to be separated from area-dependent costs that remain.

### Public-budget cost

Direct expenditure by a public actor, such as attributable electricity or variable maintenance cost for pumping.

A public expenditure is not automatically a societal loss; some expenditures are transfers or pay for resources that have their own opportunity cost.

### Societal-welfare effect

The broader change in welfare or resource use. This may overlap with but is conceptually distinct from accounting expenditure.

The application must identify which category it reports rather than combine them into one unlabeled `cost` field.

## 2.11 Uncertainty architecture

Uncertainty should remain attached to the layer where it originates.

Examples:

- **state uncertainty**: sampling coverage, measurement error, interval averaging;
- **response uncertainty**: hydraulic functions, model structure, crop response;
- **counterfactual uncertainty**: choice of reference state;
- **transfer uncertainty**: connectivity, routing, storage and timing;
- **operation uncertainty**: asset availability, control rules, pump curves;
- **valuation uncertainty**: prices, cost attribution, welfare relation.

The project does not reduce these automatically to one generic confidence score. A result may have strong evidence for the source state and weak evidence for transfer, or vice versa. That distinction is scientifically useful and should remain visible.

## 2.12 Evidence and theory

The theory defines **what kind of relation is required**. The evidence layer defines **whether a specific relation or value is sufficiently supported for a project use**.

Examples:

- theory requires a current/reference comparison;
- evidence decides which reference state is admissible;
- theory requires pump head and efficiency for energy;
- evidence decides whether a specific head/efficiency pair represents the event;
- theory allows historical model settings as possible sensitivity priors;
- qualification decides whether they may be transferred to the current pilot.

This separation prevents convenient numbers from becoming theory merely because they are available.

## 2.13 Current theoretical boundary

The current theoretical baseline is sufficient to structure the first water vertical slice, but several areas still need dedicated synthesis as the project matures:

- crop/yield response and how it should be aggregated back to land-use × soil reporting;
- construction of defensible current/reference soil hydraulic states from monitoring data;
- event-scale field-edge runoff occurrence and magnitude;
- water-system transfer beyond pilots;
- nutrient and pesticide pathways;
- welfare valuation beyond direct accounting costs.

These additions should extend this framework without bypassing the state → response → attribution → transfer → valuation separation.
