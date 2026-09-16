from __future__ import annotations

from pathlib import Path

from validate_domain_schema import validate as validate_domain_schema
from validate_evidence import validate as validate_evidence
from validate_formal_traceability import validate as validate_formal_traceability
from validate_input_readiness import validate as validate_input_readiness
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
    "schema/entities.yml",
    "schema/fields.yml",
    "schema/domain_fields_v0_3.yml",
    "schema/profile_fields_v0_1.yml",
    "schema/data_request_fields.yml",
    "schema/datasets.yml",
    "schema/relationships.yml",
    "schema/workbook_contract.yml",
    "evidence/sources.csv",
    "evidence/evidence_register.csv",
    "evidence/claims.csv",
    "evidence/qualification_register.csv",
    "data_requests/data_request_register.csv",
    "data/soil/tollebeek_soil_profiles.csv",
    "data/soil/tollebeek_soil_layers.csv",
    "data/soil/tollebeek_profile_screening_v0_1.json",
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
    errors.extend(f"domain-schema: {item}" for item in validate_domain_schema())
    errors.extend(f"input-readiness: {item}" for item in validate_input_readiness())
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
        "integrity, source-model input-readiness gates, admitted spatial geometry integrity "
        "and required review structure."
    )
    print("This is an integrity verdict, not a scientific qualification of still data-gated capabilities.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
