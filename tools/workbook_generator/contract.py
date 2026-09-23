from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


DATASET_METADATA_FIELDS = (
    "dataset_id",
    "entity",
    "role",
    "grain",
    "primary_key",
    "canonical_status",
    "source_or_derivation",
)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def merged_fields(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    """Merge canonical fields with a bounded vertical-slice overlay.

    A conflicting redefinition fails fast; the workbook generator must never
    silently replace canonical field meaning.
    """
    fields = dict(base.get("fields", {}))
    for key, value in overlay.get("fields", {}).items():
        if key in fields and fields[key] != value:
            raise ValueError(
                f"Field {key!r} is defined incompatibly in base and overlay schemas."
            )
        fields[key] = value
    return fields


def dataset_metadata_rows(
    dataset_id: str,
    dataset: dict[str, Any],
    dataset_spec: dict[str, Any],
) -> list[list[str]]:
    data_file = dataset_spec.get("data_file")
    values = {
        "dataset_id": dataset_id,
        "entity": dataset.get("entity", ""),
        "role": dataset.get("role", ""),
        "grain": dataset.get("grain", ""),
        "primary_key": ", ".join(dataset.get("primary_key", [])),
        "canonical_status": dataset_spec.get("canonical_status", "PROVISIONAL"),
        "source_or_derivation": (
            data_file
            or dataset.get("storage")
            or "generated template / not yet populated"
        ),
    }
    return [[field, values[field]] for field in DATASET_METADATA_FIELDS]


def field_help(field_id: str, definition: dict[str, Any]) -> str:
    """Build compact header help from canonical field metadata."""
    parts = [definition.get("description", "").strip()]
    unit = definition.get("unit")
    if unit:
        parts.append(f"Unit: {unit}.")
    if "allowed_values" in definition:
        parts.append(
            "Allowed: " + ", ".join(map(str, definition["allowed_values"])) + "."
        )
    guardrail = definition.get("guardrail")
    if guardrail:
        parts.append("Guardrail: " + guardrail)
    text = " ".join(part for part in parts if part)
    # Keep the input message compact across spreadsheet clients.
    return text[:255]


def validate_spec(
    spec: dict[str, Any],
    fields: dict[str, Any],
    datasets: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    artifact = spec.get("artifact", {})
    for key in (
        "project_id",
        "artifact_id",
        "artifact_class",
        "artifact_version",
        "schema_version",
        "purpose",
        "scope",
        "canonical_status",
    ):
        if not artifact.get(key):
            errors.append(f"artifact.{key} is required")

    seen_sheets: set[str] = set()
    seen_datasets: set[str] = set()
    for item in spec.get("datasets", []):
        dataset_id = item.get("dataset_id")
        sheet_name = item.get("sheet_name")
        if dataset_id not in datasets:
            errors.append(f"Unknown dataset_id: {dataset_id}")
        if dataset_id in seen_datasets:
            errors.append(f"Duplicate dataset_id: {dataset_id}")
        seen_datasets.add(dataset_id)
        if not item.get("canonical_status"):
            errors.append(f"dataset {dataset_id}: canonical_status is required")
        if not sheet_name:
            errors.append(f"dataset {dataset_id}: sheet_name is required")
        elif sheet_name in seen_sheets:
            errors.append(f"Duplicate sheet_name: {sheet_name}")
        seen_sheets.add(sheet_name)
        for field_id in item.get("fields", []):
            if field_id not in fields:
                errors.append(f"dataset {dataset_id}: unknown field {field_id}")
    return errors
