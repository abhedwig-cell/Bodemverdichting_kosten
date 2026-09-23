from __future__ import annotations

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
    "project_pathway_fields_v0_1.yml",
]

REQUIRED_V03_DATASETS = {
    "land_use_crop_register": {
        "entity": "land_use_crop",
        "primary_key": ["land_use_crop_id"],
    },
    "model_configuration_register": {
        "entity": "model_configuration",
        "primary_key": ["model_configuration_id"],
    },
    "meteorological_forcing_register": {
        "entity": "meteorological_forcing_observation",
        "primary_key": ["forcing_observation_id"],
    },
}

REQUIRED_HYDRAULIC_DATASETS = {
    "hydraulic_parameterization_register": {
        "entity": "hydraulic_parameterization",
        "primary_key": ["hydraulic_parameterization_id"],
    },
}

REQUIRED_RUN_CONTROL_RELATIONSHIPS = {
    "spatial_run": ("spatial_unit", "model_run", "spatial_unit_id"),
    "event_run": ("event", "model_run", "event_id"),
    "event_forcing": ("event", "meteorological_forcing_observation", "event_id"),
    "soil_state_run": ("soil_state", "model_run", "soil_state_id"),
    "model_configuration_run": (
        "model_configuration",
        "model_run",
        "model_configuration_id",
    ),
    "drainage_configuration_run": (
        "drainage_configuration",
        "model_run",
        "drainage_configuration_id",
    ),
    "land_use_crop_run": ("land_use_crop", "model_run", "land_use_crop_id"),
}

REQUIRED_HYDRAULIC_RELATIONSHIPS = {
    "state_hydraulic_parameterization": (
        "soil_state", "hydraulic_parameterization", "soil_state_id"
    ),
    "hydraulic_parameterization_run": (
        "hydraulic_parameterization", "model_run", "hydraulic_parameterization_id"
    ),
}

REQUIRED_PROFILE_RELATIONSHIPS = {
    "spatial_profile": ("spatial_unit", "soil_profile", "spatial_unit_id"),
    "profile_layer": ("soil_profile", "soil_layer", "soil_profile_id"),
    "layer_state": ("soil_layer", "soil_state", "soil_layer_id"),
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
        current = load_yaml(path).get("fields", {})
        for field_id, definition in current.items():
            if field_id in fields and fields[field_id] != definition:
                errors.append(
                    f"conflicting field definition for {field_id} in schema/{filename}"
                )
            else:
                fields[field_id] = definition
    return fields, errors


def validate_relationship(
    name: str,
    expected: tuple[str, str, str],
    relationships: dict[str, dict],
    entities: set[str],
    fields: set[str],
) -> list[str]:
    errors: list[str] = []
    if name not in relationships:
        return [f"missing required relationship: {name}"]

    relation = relationships[name]
    from_entity, to_entity, field_id = expected
    if relation.get("from_entity") != from_entity:
        errors.append(
            f"{name}: from_entity {relation.get('from_entity')} != {from_entity}"
        )
    if relation.get("to_entity") != to_entity:
        errors.append(f"{name}: to_entity {relation.get('to_entity')} != {to_entity}")

    if from_entity not in entities:
        errors.append(f"{name}: unknown from_entity {from_entity}")
    if to_entity not in entities:
        errors.append(f"{name}: unknown to_entity {to_entity}")
    if field_id not in fields:
        errors.append(f"{name}: foreign-key field {field_id} is not defined")

    foreign_key = relation.get("foreign_key")
    if not foreign_key or foreign_key.split(".")[-1] != field_id:
        errors.append(
            f"{name}: foreign_key {foreign_key!r} does not end in canonical field {field_id}"
        )
    return errors


def validate() -> list[str]:
    errors: list[str] = []

    entities_doc = load_yaml(SCHEMA / "entities.yml")
    datasets_doc = load_yaml(SCHEMA / "datasets.yml")
    relationships_doc = load_yaml(SCHEMA / "relationships.yml")

    entities = set(entities_doc.get("entities", {}))
    datasets = datasets_doc.get("datasets", {})
    relationships = relationships_doc.get("relationships", {})
    fields, field_errors = merged_fields()
    errors.extend(field_errors)

    for field_id, definition in fields.items():
        entity = definition.get("entity")
        if entity and entity not in entities:
            errors.append(f"{field_id}: field refers to unknown entity {entity}")

    for dataset_id, expected in {**REQUIRED_V03_DATASETS, **REQUIRED_HYDRAULIC_DATASETS}.items():
        dataset = datasets.get(dataset_id)
        if dataset is None:
            errors.append(f"missing required v0.3 dataset: {dataset_id}")
            continue
        if dataset.get("entity") != expected["entity"]:
            errors.append(
                f"{dataset_id}: entity {dataset.get('entity')} != {expected['entity']}"
            )
        if dataset.get("primary_key") != expected["primary_key"]:
            errors.append(
                f"{dataset_id}: primary_key {dataset.get('primary_key')} != {expected['primary_key']}"
            )
        for field_id in expected["primary_key"]:
            if field_id not in fields:
                errors.append(f"{dataset_id}: primary-key field {field_id} is not defined")

    for name, expected in {
        **REQUIRED_PROFILE_RELATIONSHIPS,
        **REQUIRED_HYDRAULIC_RELATIONSHIPS,
        **REQUIRED_RUN_CONTROL_RELATIONSHIPS,
    }.items():
        errors.extend(
            validate_relationship(name, expected, relationships, entities, set(fields))
        )

    # Data Model v0.3 deliberately keeps current/reference pairing reconstructable
    # from controlled run dimensions rather than inventing a pair entity.
    if "attribution_pair" in entities or "attribution_pair_register" in datasets:
        errors.append(
            "v0.3 must not introduce an attribution_pair entity/register without a separate decision surface"
        )

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Data Model v0.3 domain-schema validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Composite Data Model v0.3.x domain-schema validation passed.")
    print(
        "Validated documented domain datasets, profile/hydraulic/run-control relationships, "
        "field identity and the no-premature-attribution-pair boundary."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
