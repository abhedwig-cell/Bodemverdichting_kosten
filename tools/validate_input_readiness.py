from __future__ import annotations

import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "data_requests" / "data_request_register.csv"

REQUIRED_COLUMNS = {
    "data_request_id",
    "requirement_kind",
    "capability_id",
    "input_role",
    "requirement_statement",
    "request_spatial_scope",
    "request_time_scope",
    "priority",
    "input_readiness_status",
    "current_evidence_ids",
    "current_claim_ids",
    "acceptance_criteria",
    "blocking_reason",
    "next_action",
    "request_notes",
}

FIRST_SOURCE_MODEL_ROLES = {
    "SPATIAL_GEOMETRY",
    "SOIL_PROFILE_CONTEXT",
    "CURRENT_SOIL_STATE",
    "REFERENCE_SOIL_STATE",
    "DRAINAGE_CONFIGURATION",
    "EVENT_FORCING",
    "INITIAL_HYDROLOGICAL_STATE",
    "MANAGED_BOUNDARY",
    "LAND_USE_CROP_CONTEXT",
    "MODEL_CONFIGURATION",
}


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate() -> list[str]:
    errors: list[str] = []
    if not REGISTER.exists():
        return ["missing canonical data-request register"]

    with REGISTER.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        rows = list(reader)

    missing_columns = REQUIRED_COLUMNS - columns
    if missing_columns:
        errors.append(f"data-request register missing columns: {sorted(missing_columns)}")
        return errors

    vocab = yaml.safe_load(
        (ROOT / "schema" / "controlled_vocabularies.yml").read_text(encoding="utf-8")
    )["vocabularies"]
    allowed_kind = set(vocab["input_requirement_kind"])
    allowed_status = set(vocab["input_readiness_status"])
    allowed_priority = set(vocab["priority"])

    evidence_ids = {row["evidence_id"] for row in read_csv(ROOT / "evidence" / "evidence_register.csv")}
    claim_ids = {row["claim_id"] for row in read_csv(ROOT / "evidence" / "claims.csv")}
    capability_ids = {row["capability_id"] for row in read_csv(ROOT / "model" / "traceability.csv")}

    request_ids: set[str] = set()
    input_roles: set[str] = set()
    for row in rows:
        request_id = row["data_request_id"].strip()
        if not request_id:
            errors.append("blank data_request_id")
            continue
        if request_id in request_ids:
            errors.append(f"duplicate data_request_id: {request_id}")
        request_ids.add(request_id)

        role = row["input_role"].strip()
        if role in input_roles:
            errors.append(f"duplicate input_role in first source-model baseline: {role}")
        input_roles.add(role)

        if row["requirement_kind"] not in allowed_kind:
            errors.append(f"{request_id}: invalid requirement_kind {row['requirement_kind']}")
        if row["input_readiness_status"] not in allowed_status:
            errors.append(f"{request_id}: invalid input_readiness_status {row['input_readiness_status']}")
        if row["priority"] not in allowed_priority:
            errors.append(f"{request_id}: invalid priority {row['priority']}")
        if row["capability_id"] not in capability_ids:
            errors.append(f"{request_id}: unknown capability_id {row['capability_id']}")

        for field in ("requirement_statement", "acceptance_criteria", "blocking_reason", "next_action"):
            if not row[field].strip():
                errors.append(f"{request_id}: blank required field {field}")

        for evidence_id in split_ids(row["current_evidence_ids"]):
            if evidence_id not in evidence_ids:
                errors.append(f"{request_id}: unknown evidence_id {evidence_id}")
        for claim_id in split_ids(row["current_claim_ids"]):
            if claim_id not in claim_ids:
                errors.append(f"{request_id}: unknown claim_id {claim_id}")

    missing_roles = FIRST_SOURCE_MODEL_ROLES - input_roles
    extra_roles = input_roles - FIRST_SOURCE_MODEL_ROLES
    if missing_roles:
        errors.append(f"first source-model baseline missing input roles: {sorted(missing_roles)}")
    if extra_roles:
        errors.append(f"unexpected input roles in bounded first source-model baseline: {sorted(extra_roles)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Source-model input-readiness validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Source-model input-readiness validation passed.")
    print("This validates register integrity and gate coverage, not the missing scientific inputs themselves.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
