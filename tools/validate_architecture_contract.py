from __future__ import annotations

import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schema"

FIELD_FILES = [
    "fields.yml",
    "evidence_fields.yml",
    "formal_traceability_fields.yml",
    "tollebeek_vertical_slice.yml",
    "domain_fields_v0_3.yml",
    "profile_fields_v0_1.yml",
    "event_forcing_fields_v0_1.yml",
    "hydraulic_parameterization_fields_v0_1.yml",
    "data_request_fields.yml",
    "project_pathway_fields_v0_1.yml",
]

REQUIRED_WORKBOOK_DATASET_METADATA = {
    "dataset_id",
    "entity",
    "role",
    "grain",
    "primary_key",
    "canonical_status",
    "source_or_derivation",
}

REQUIRED_WORKBOOK_ARTIFACT_METADATA = {
    "schema_version",
    "git_commit",
}


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def merged_fields() -> tuple[dict[str, dict], list[str]]:
    fields: dict[str, dict] = {}
    errors: list[str] = []
    for filename in FIELD_FILES:
        path = SCHEMA / filename
        if not path.exists():
            errors.append(f"missing field schema: schema/{filename}")
            continue
        for field_id, definition in load_yaml(path).get("fields", {}).items():
            if field_id in fields and fields[field_id] != definition:
                errors.append(
                    f"conflicting field definition for {field_id} in schema/{filename}"
                )
            else:
                fields[field_id] = definition
    return fields, errors


def validate() -> list[str]:
    errors: list[str] = []
    entities = load_yaml(SCHEMA / "entities.yml").get("entities", {})
    datasets_doc = load_yaml(SCHEMA / "datasets.yml")
    datasets = datasets_doc.get("datasets", {})
    allowed_roles = set(datasets_doc.get("dataset_roles", []))
    relationships = load_yaml(SCHEMA / "relationships.yml").get("relationships", {})
    fields, field_errors = merged_fields()
    errors.extend(field_errors)

    vocab = load_yaml(SCHEMA / "controlled_vocabularies.yml").get("vocabularies", {})
    allowed_canonical_status = set(vocab.get("canonical_status", []))
    artifact_spec = load_yaml(
        SCHEMA / "artifacts" / "tollebeek_vertical_slice_workbook.yml"
    )
    artifact_status = artifact_spec.get("artifact", {}).get("canonical_status")
    if artifact_status not in allowed_canonical_status:
        errors.append(
            f"workbook artifact canonical_status {artifact_status!r} is not controlled"
        )
    for item in artifact_spec.get("datasets", []):
        status = item.get("canonical_status")
        if status not in allowed_canonical_status:
            errors.append(
                f"workbook dataset {item.get('dataset_id')}: canonical_status "
                f"{status!r} is not controlled"
            )

    for dataset_id, dataset in datasets.items():
        entity = dataset.get("entity")
        if entity not in entities:
            errors.append(f"{dataset_id}: unknown entity {entity!r}")
        role = dataset.get("role")
        if role not in allowed_roles:
            errors.append(f"{dataset_id}: invalid dataset role {role!r}")
        if not str(dataset.get("grain") or "").strip():
            errors.append(f"{dataset_id}: grain is required")
        primary_key = dataset.get("primary_key")
        if not isinstance(primary_key, list) or not primary_key:
            errors.append(f"{dataset_id}: non-empty primary_key list is required")
            primary_key = []
        for field_id in primary_key:
            if field_id not in fields:
                errors.append(f"{dataset_id}: primary-key field {field_id} is not defined")

        storage = dataset.get("storage")
        if storage:
            path = ROOT / storage
            if not path.exists():
                errors.append(f"{dataset_id}: storage path does not exist: {storage}")
            elif path.suffix.lower() == ".csv":
                with path.open("r", encoding="utf-8", newline="") as handle:
                    headers = csv.DictReader(handle).fieldnames or []
                for field_id in headers:
                    if field_id not in fields:
                        errors.append(
                            f"{dataset_id}: stored CSV field {field_id} has no canonical definition"
                        )
                for field_id in primary_key:
                    if field_id not in headers:
                        errors.append(
                            f"{dataset_id}: primary-key field {field_id} missing from {storage}"
                        )

    for relationship_id, relation in relationships.items():
        if relation.get("from_entity") not in entities:
            errors.append(
                f"{relationship_id}: unknown from_entity {relation.get('from_entity')!r}"
            )
        if relation.get("to_entity") not in entities:
            errors.append(
                f"{relationship_id}: unknown to_entity {relation.get('to_entity')!r}"
            )
        foreign_key = relation.get("foreign_key")
        if foreign_key:
            field_id = foreign_key.split(".")[-1]
            if field_id not in fields:
                errors.append(
                    f"{relationship_id}: foreign-key field {field_id} is not defined"
                )

    workbook_contract = load_yaml(SCHEMA / "workbook_contract.yml")
    required_metadata = set(
        workbook_contract.get("workbook", {})
        .get("dataset_metadata", {})
        .get("required", [])
    )
    missing_metadata = REQUIRED_WORKBOOK_DATASET_METADATA - required_metadata
    if missing_metadata:
        errors.append(
            "workbook contract misses required dataset metadata: "
            + ", ".join(sorted(missing_metadata))
        )

    required_artifact_metadata = set(
        workbook_contract.get("workbook", {})
        .get("metadata_fields", {})
        .get("required", [])
    )
    missing_artifact_metadata = (
        REQUIRED_WORKBOOK_ARTIFACT_METADATA - required_artifact_metadata
    )
    if missing_artifact_metadata:
        errors.append(
            "workbook contract misses required artifact metadata: "
            + ", ".join(sorted(missing_artifact_metadata))
        )

    authority = ROOT / "docs" / "58_project_architecture_status_v0_1.md"
    if not authority.exists():
        errors.append("missing current project architecture authority page")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Project architecture contract validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Project architecture contract validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
