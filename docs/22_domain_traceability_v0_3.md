# Domain traceability v0.3

Status: **Status-A-light architecture baseline candidate**

This document makes the existing theory → conceptual model → formal model → data model chain explicit for the core physical domains. It does not add scientific relations; it records where the current relation is defined and what remains evidence-gated.

| Domain capability | Theory | Conceptual object | Formal control | Canonical data object | Implementation/evidence status |
|---|---|---|---|---|---|
| soil profile context | profile geometry and state dependence | `SoilProfile`, `SoilLayer` | profile/layer context held fixed where required by the causal question | `soil_profile_register`, `soil_layer_register` | schema-level contract; current OT.02 profile data still gated |
| soil physical state | state/exposure question | `SoilState` | explicit current/reference/scenario state | `soil_state_register` with `soil_state_id` | schema-level contract; current compaction state still gated |
| crop/land-use context | response conditional on crop/land use | `LandUseCrop` | controlled run dimension where relevant | `land_use_crop_register` | new stable v0.3 register; no new crop-response function admitted |
| event/forcing context | response conditional on event state | `Event` | same controlled event for simple current/reference attribution | `event_register` | existing contract; event-specific pilot inputs remain evidence-gated |
| drainage context | drainage is a separate system condition | `DrainageConfiguration` | controlled run dimension | `drainage_configuration_register` | existing dataset; current Tollebeek configuration still data-gated |
| model/boundary configuration | response depends on boundary/system context | `ModelConfiguration` | same controlled configuration for simple attribution | `model_configuration_register` | new stable v0.3 register; configuration presence is not qualification |
| controlled execution | state/response separation | `ModelRun` | run identity tied to explicit control dimensions | `model_run_register` | schema relation strengthened; no current/reference Tollebeek run admitted |
| hydrological response | response question | `HydrologicalResponse` | response belongs to a run | `hydrological_response_register` | existing contract; current attribution still blocked |
| current/reference attribution | counterfactual question | matched run pair, not yet separate entity | controlled dimensions equal except admitted state change | reconstructable through run relations | no pair table introduced; qualification still required before labelling delta attributable |
| transfer | transfer question | `TransferEvent`, `WaterSystemUnit` | stage explicit; no universal delivery default | `transfer_event_register`, `water_system_unit_register` | existing vertical-slice semantics; downstream values may remain null |
| pump operation | managed-system response | `PumpAsset`, `PumpDispatch` | availability, assist, head and efficiency explicit | `pump_asset_register`, `pump_dispatch_register` | software identities exist; current operation remains unknown/data-gated |
| valuation | valuation question | `ValuationRelation`, `CostEstimate` | physical effect and valuation category explicit | `valuation_relation_register`, `cost_estimate_register` | architecture only; no new economic coefficient admitted |
| evidence admission | theory/evidence separation | `Source`, `EvidenceItem`, `Claim`, `Qualification` | use-specific qualification with dependencies | canonical evidence registers | inherited current baseline |

## Current/reference reconstructability

Data Model v0.3 deliberately avoids a convenience `attribution_pair` entity. For the current maturity level, the scientifically relevant pairing can be reconstructed only when the two runs expose the same controlled context and distinct admitted soil states.

Minimum control dimensions are:

```text
spatial_unit_id
event_id
soil_state_id
model_configuration_id
```

and, where part of the scientific question:

```text
drainage_configuration_id
land_use_crop_id
```

The formal pairing rule remains stronger than simple key equality. A pair still requires scientific review that the controlled dimensions are identical or demonstrably equivalent and that the state change represents the intended causal contrast.

## Why this is not a new scientific model

This v0.3 layer does not decide:

- how current soil hydraulic parameters are derived;
- which reference state is scientifically admissible;
- which meteorological event should be simulated;
- what downstream delivery relation applies;
- what current pump operating point applies;
- what economic coefficient applies.

It only ensures those decisions have separate identities and cannot be silently hidden in workbook layout or run names.
