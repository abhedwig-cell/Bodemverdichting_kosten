# Tollebeek P1 source-model readiness baseline v0.1

Date: 2026-09-16
Canonical start: `1e9844e6aade92f840d5539d552cdd2b6b065665`
Event: `EVT_TOL_1998_OCT`

## Verdict

`P1_ROUTE_COVERAGE_COMPLETE_INPUT_ADMISSION_INCOMPLETE`

All ten P1 source-model input roles now have an explicit evidence/acquisition/decision route. None remains `MISSING`. This is **not** a run-readiness verdict: only three roles are scientifically admitted, while seven remain `PARTIAL_EVIDENCE`.

## Current status matrix

| Data request | Role | Status | Current boundary |
|---|---|---|---|
| `DR_SM_GEOMETRY` | spatial geometry | `ADMITTED` | Current definitive OT.02 owner polygon admitted as spatial identity/sampling domain. |
| `DR_SM_PROFILE` | soil profile context | `ADMITTED` | Eight SoilPhys/BOFEK profile classes and modal layers admitted; no current compaction implied. |
| `DR_SM_CURRENT_STATE` | current soil/compaction state | `PARTIAL_EVIDENCE` | Qualified 2020–2021 Flevoland field-measurement route; raw georeferenced point records still required for OT.02. |
| `DR_SM_REFERENCE_STATE` | matched reference soil state | `PARTIAL_EVIDENCE` | Concept qualified; construction must wait for an admitted CURRENT state and explicit causal contrast. |
| `DR_SM_DRAINAGE` | drainage configuration | `PARTIAL_EVIDENCE` | Owner inventory/topology route qualified; parcel-drain spacing/depth/outlet and model mapping unresolved. |
| `DR_SM_EVENT_FORCING` | event forcing | `ADMITTED` | 144-hour October 1998 KNMI station-273 forcing admitted for bounded experiment context. |
| `DR_SM_INITIAL_STATE` | initial hydrological state | `PARTIAL_EVIDENCE` | Deep/nearby BRO context qualified; no shallow event-date OT.02 state admitted. Warm-up route remains dependent on other inputs. |
| `DR_SM_MANAGED_BOUNDARY` | managed boundary | `PARTIAL_EVIDENCE` | Historical pre-IJsvogel system constrained; 1998 dynamic levels/operations absent. |
| `DR_SM_LAND_USE` | land-use/crop context | `PARTIAL_EVIDENCE` | Near-period/LGN routes qualified; no parcel/profile-level October 1998 crop/vegetation state admitted. |
| `DR_SM_MODEL_CONFIG` | source-model configuration | `PARTIAL_EVIDENCE` | SWAP5 scientific/Status-A authority chain pinned; no complete runnable Tollebeek configuration admitted. |

Counts: `ADMITTED=3`, `PARTIAL_EVIDENCE=7`, `MISSING=0`.

## Blocker classes

### A — Primary external-data blockers

These can be advanced independently through acquisition from data holders:

1. **CURRENT soil state** — acquire raw georeferenced Flevo-land-in-beweging / WER 3382 observations with dates, depths, replicates and QC.
2. **Drainage configuration** — acquire source-native parcel-drain spacing/density, depth/elevation, outlet relation, status and reference date for selected OT.02 units.
3. **1998 managed boundary** — acquire local and Urkervaart water levels, historical pump runtime/realized discharge, stuw/inlaat operations and emergency-pump records for 24–30 October 1998.
4. **1998 land use/crop** — seek dated parcel/field records spatially linkable to the historical Tollebeek control areas; if unavailable, any scenario/crop-independent design must be separately qualified and labelled non-observational.
5. **Initial hydrological state** — continue archival shallow groundwater/soil-water acquisition near the 24 October 1998 start. Existing deep heads and nearby shallow records are context only.

### B — Dependent scientific decisions

These should not be forced before their prerequisites are resolved:

1. **REFERENCE state** depends on the admitted CURRENT state and the explicit attribution question.
2. **Warm-up/restart initialization**, if used instead of direct initial observations, depends on a sufficiently complete configuration, drainage, managed boundary and land-use treatment.
3. **Concrete model configuration** depends on the unresolved scientific inputs or separately qualified scenario/reconstruction semantics. The SWAP5 execution authority is already pinned; defaults are not an admission mechanism.

## Dependency order

Recommended dependency order, not a claim of equal effort:

`CURRENT acquisition → REFERENCE construction`

in parallel with:

`DRAINAGE acquisition + MANAGED BOUNDARY acquisition + LAND USE acquisition + INITIAL observation search`

then:

`MODEL CONFIGURATION → (if needed) qualified WARM-UP/RESTART → paired CURRENT/REFERENCE source-model runs`

The event forcing, geometry and profile basis can be inherited throughout unless their relevant source authority changes.

## Scientific guardrails

- `MISSING=0` means route coverage is complete, **not** that the model is ready to run.
- `PARTIAL_EVIDENCE` may not be converted to `ADMITTED` using convenience defaults.
- SoilPhys modal density remains profile context, not CURRENT compaction state.
- Historical drainage resistance values remain priors, not current configuration.
- NAP -6.20 m remains target-level context, not a 1998 hydrograph or initial groundwater head.
- Current IJsvogel/current merged OT.02 controls may not be backcast to 1998.
- LGN3/LGN4 do not establish exact October 1998 crop state.
- SWAP5 scientific executable authority is pinned, but no runnable project configuration exists yet.

## Next state boundary

The project has reached the end of what can be closed from public-route qualification alone without either new external records or an explicitly reviewed scenario/reconstruction design. The next material progress should be evidence acquisition, not additional parameter invention.
