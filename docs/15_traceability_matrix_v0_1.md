# Traceability matrix v0.1

Status: **historical early baseline; current project-wide authority is `../PROJECT_ARCHITECTURE_STATUS.md` plus `../model/traceability.csv`**

Purpose: show the first major project capabilities connected across theory, conceptual model, formal model, data model, implementation and evidence/qualification.

This file predates the later project-wide on-site evidence ensembles, bounded calculation surface and BRP × BRO crosswalk. It is retained for review history and should not be read as a complete list of current priorities.

This is a lightweight review surface, not a duplicate database of all project information.

| Capability | Theoretical / conceptual meaning | Formal rule | Canonical data objects | Implementation | Evidence / qualification | Current status |
|---|---|---|---|---|---|---|
| Current versus reference attribution | Damage/effect must be attributed by comparing matched soil states while other controlled context is held equal | `delta_Y = Y_current - Y_reference` | `soil_state`, `event`, `model_run`, `hydrological_response` | model-run orchestration still to be integrated with SWAP input/output adapters | reference-state logic documented; Tollebeek current/reference physical states not yet admitted | `DATA_GATED` |
| Generated runoff volume | Extra runoff depth is first a parcel/source response, not yet a delivered system volume | `V_generated = 10 * A_ha * delta_R_mm` | `hydrological_response`; fields `affected_area_ha`, `delta_runoff_mm`, `generated_increment_m3` | `src/transfer/volume.py` | equation semantics implemented and software-tested; physical `delta_R` remains unqualified for Tollebeek | `ARCHITECTURE_READY` |
| Event-conditioned field-edge transfer | Runoff occurrence and positive magnitude depend on event/process/connectivity; no universal static delivery factor | occurrence hurdle + positive-volume model; diagnostic `f_delivery_event = V_edge/V_generated` where defined | `transfer_event`; `transfer_stage`, `delivered_volume_m3`, `event_delivery_factor` | canonical semantics defined; empirical transfer implementation still open | SURFLAT/Twente/Appels evidence routes identified; raw empirical event qualification still incomplete | `EVIDENCE_GATED` |
| Managed Tollebeek boundary | Tollebeek is a managed polder system; free drainage is not the default conceptual boundary | boundary must represent managed groundwater/surface-water context explicitly | `spatial_unit`, `water_system_unit`, future boundary/model configuration | formal SWAP adapter/configuration not yet completed | target-level and coupled-system evidence qualified with limitations | `PARTIAL_METHOD_READY` |
| Multi-system drainage | Parcel/system response may involve primary, secondary, tertiary, tile and surface drainage rather than one resistance | multiple drainage pathways/parameters, no single universal resistance | `drainage_configuration` | not yet implemented as current OT.02 configuration | historical NOP SWAP drainage values retained as method priors; current drainage remains missing | `DATA_GATED` |
| IJsvogel installed capacity | Installed asset capacity is distinct from event-specific available capacity and effective system capacity | capacity enters dispatch only after explicit availability/operation state | `pump_asset`; `installed_capacity_m3_min` | generic dispatch accepts capacity/availability explicitly | 540 m3/min owner-backed benchmark qualified; no default availability | `QUALIFIED_FOR_DEFINED_USE` |
| Kievit capacity semantics | nominal hardware, historical calculated capacity and current operational capacity are distinct quantities | no collapse to one min/max parameter | `pump_asset` plus evidence/claims/qualification | dispatch accepts an explicit capacity input; no Kievit constant hard-coded in scientific core | 60 m3/min nominal hardware and 1.44 m3/s historical calculated value retained separately; current Q-H curve missing | `DATA_GATED` |
| Kievit-zone assist to IJsvogel | extreme operation may allocate some Kievit-zone water to IJsvogel | `V_K_to_IJ = f_assist * V_K`; `0<=f_assist<=1`; no default | `pump_dispatch`; `source_zone_id`, `assist_fraction`, `pumped_volume_m3` | `src/water_system/dispatch.py` | directional assist qualified; magnitude/control rule not qualified; reverse route not evidenced | `SEMANTICS_READY_DATA_GATED` |
| Pump energy | energy depends on pumped volume, total dynamic head and efficiency at the defined operating state | `E_kWh = rho*g*H*V/(eta*3.6e6)` | `pump_dispatch`; `pumped_volume_m3`, `total_dynamic_head_m`, `pump_efficiency`, `energy_kwh` | `src/water_system/energy.py` | equation qualified as physical identity; current pump-specific head/efficiency missing | `ARCHITECTURE_READY_DATA_GATED` |
| Direct pumping cost | direct budget cost may combine attributable energy and variable O&M; it is not automatically societal welfare loss | `C_pump = E_kWh * p_electricity + attributable_variable_OM` | future `valuation_relation`, `cost_estimate` | not yet promoted to full production module | historical FutureWater cost values are benchmark/context only; current tariff/O&M missing | `DATA_GATED` |
| Evidence chain | source facts, project claims and intended-use qualifications must remain separate | `Source -> EvidenceItem -> Claim -> Qualification` | `source_register`, `evidence_register`, `claim_register`, `qualification_register` | CSV registers + validator + workbook population | first Tollebeek baseline populated and validation tests added | `WORKING_BASELINE` |
| Workbook as generated interface | Excel must expose canonical meaning without becoming the source of truth | schema/spec + canonical records -> generated workbook | `artifact`, `artifact_dataset`, `field_definition` | schema-driven workbook generator with metadata, guide, data dictionary and header help | contract and generator tests in repository | `WORKING_BASELINE` |

## Broken-link review

The matrix highlights three current weak links that matter more than further workbook expansion:

1. **physical source attribution** — current depth-resolved Tollebeek soil state and matched reference are not yet available;
2. **source-to-system transfer** — empirical event-conditioned transfer remains insufficiently qualified for production use;
3. **current operations** — Kievit/IJsvogel routing, availability, head, efficiency and energy telemetry are not yet available at the required level.

Until those links are strengthened, additional UI sophistication should not be interpreted as increased scientific maturity.

## Update rule

Update this matrix when a material capability changes state, when an implementation moves from template to executable production path, or when new evidence changes what a relation may be used for.
