# 3. Conceptual model

## Core object groups

### Spatial and soil
- SpatialUnit
- SoilProfile
- SoilLayer
- SoilState
- LandUse / Crop
- DrainageConfiguration

### Event and model
- Event
- MeteorologicalForcing
- InitialHydrologicalState
- ModelRun
- HydrologicalResponse

### Transfer and managed water system
- TransferEvent
- WaterSystemUnit
- RoutingLink
- PumpAsset
- PumpDispatch
- CapacityPressure

### Valuation
- CostItem
- ValuationRelation
- CostEstimate

### Evidence and governance
- Source
- EvidenceItem
- Claim
- Qualification
- AdmissionDecision

## Core relationships

```text
SpatialUnit
  ├─ SoilProfile ─ SoilLayer ─ SoilState
  ├─ LandUse/Crop
  ├─ DrainageConfiguration
  └─ WaterSystemUnit

Event + SoilState + boundary conditions
  └─ ModelRun
       └─ HydrologicalResponse
            └─ TransferEvent
                 └─ WaterSystemResponse
                      └─ PumpDispatch / CapacityPressure
                           └─ CostEstimate

Source → EvidenceItem → Claim → Qualification → AdmissionDecision
```

## Design principle

Scientific entities are independent of their Excel representation. A workbook row or application widget should map to a defined entity and grain rather than create a new implicit data concept.
