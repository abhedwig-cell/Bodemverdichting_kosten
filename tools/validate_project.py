from __future__ import annotations

from pathlib import Path

from validate_current_state_gate import validate as validate_current_state_gate
from validate_drainage_gate import validate as validate_drainage_gate
from validate_event_forcing_gate import validate as validate_event_forcing_gate
from validate_domain_schema import validate as validate_domain_schema
from validate_evidence import validate as validate_evidence
from validate_formal_traceability import validate as validate_formal_traceability
from validate_input_readiness import validate as validate_input_readiness
from validate_initial_state_gate import validate as validate_initial_state_gate
from validate_managed_boundary_gate import validate as validate_managed_boundary_gate
from validate_land_use_gate import validate as validate_land_use_gate
from validate_profile_baseline import validate as validate_profile_baseline
from validate_spatial_geometry import validate as validate_spatial_geometry

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "CONTRIBUTING.md",
    "docs/00_colleague_reader_guide.md",
    "docs/01_overview.md",
    "docs/02_theoretical_framework.md",
    "docs/03_conceptual_model.md",
    "docs/04_formal_model.md",
    "docs/05_data_model.md",
    "docs/06_implementation.md",
    "docs/07_evidence_and_qualification.md",
    "docs/14_documentation_status_a_light.md",
    "docs/17_formal_traceability_register_v0_1.md",
    "docs/18_status_a_light_checkpoint_v0_1.md",
    "docs/21_data_model_v0_3_contract.md",
    "docs/25_tollebeek_current_state_evidence_route_v0_1.md",
    "docs/26_tollebeek_drainage_evidence_route_v0_1.md",
    "docs/27_tollebeek_event_forcing_baseline_v0_1.md",
    "docs/28_tollebeek_initial_state_evidence_route_v0_1.md",
    "docs/29_tollebeek_managed_boundary_evidence_route_v0_1.md",
    "docs/30_tollebeek_land_use_evidence_route_v0_1.md",
    "docs/24_tollebeek_profile_baseline_v0_1.md",
    "schema/entities.yml",
    "schema/fields.yml",
    "schema/domain_fields_v0_3.yml",
    "schema/profile_fields_v0_1.yml",
    "schema/event_forcing_fields_v0_1.yml",
    "schema/data_request_fields.yml",
    "schema/datasets.yml",
    "schema/relationships.yml",
    "schema/workbook_contract.yml",
    "evidence/sources.csv",
    "evidence/evidence_register.csv",
    "evidence/claims.csv",
    "evidence/qualification_register.csv",
    "data_requests/data_request_register.csv",
    "data_requests/tollebeek_current_state_data_request_v0_1.md",
    "data_requests/tollebeek_drainage_data_request_v0_1.md",
    "data_requests/tollebeek_initial_state_data_request_v0_1.md",
    "data_requests/tollebeek_managed_boundary_data_request_v0_1.md",
    "data_requests/tollebeek_land_use_data_request_v0_1.md",
    "data/soil/tollebeek_soil_profiles.csv",
    "data/soil/tollebeek_soil_layers.csv",
    "data/soil/tollebeek_profile_screening_v0_1.json",
    "data/events/tollebeek_events.csv",
    "data/events/tollebeek_1998_marknesse_hourly.csv",
    "data/spatial/tollebeek_ot02_current.geojson",
    "model/equations.csv",
    "model/traceability.csv",
]


def validate_required_paths() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).exists():
            errors.append(f"missing required project path: {relative}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    errors.extend(f"evidence: {item}" for item in validate_evidence())
    errors.extend(f"formal-traceability: {item}" for item in validate_formal_traceability())
    errors.extend(f"current-state-gate: {item}" for item in validate_current_state_gate())
    errors.extend(f"drainage-gate: {item}" for item in validate_drainage_gate())
    errors.extend(f"event-forcing-gate: {item}" for item in validate_event_forcing_gate())
    errors.extend(f"domain-schema: {item}" for item in validate_domain_schema())
    errors.extend(f"input-readiness: {item}" for item in validate_input_readiness())
    errors.extend(f"initial-state-gate: {item}" for item in validate_initial_state_gate())
    errors.extend(f"managed-boundary-gate: {item}" for item in validate_managed_boundary_gate())
    errors.extend(f"land-use-gate: {item}" for item in validate_land_use_gate())
    errors.extend(f"profile-baseline: {item}" for item in validate_profile_baseline())
    errors.extend(f"spatial-geometry: {item}" for item in validate_spatial_geometry())
    errors.extend(f"project-structure: {item}" for item in validate_required_paths())
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Status-A-light project validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Status-A-light project validation passed.")
    print(
        "Validated evidence integrity, formal traceability, Data Model v0.3 domain-schema "
        "integrity, source-model input-readiness gates, admitted spatial geometry and profile-baseline integrity "
        "and required review structure."
    )
    print("This is an integrity verdict, not a scientific qualification of still data-gated capabilities.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
