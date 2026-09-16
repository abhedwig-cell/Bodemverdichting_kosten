from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "model"
EVIDENCE_DIR = ROOT / "evidence"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(raw: str) -> list[str]:
    return [item.strip() for item in (raw or "").split(";") if item.strip()]


def duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicate: set[str] = set()
    for value in values:
        if value in seen:
            duplicate.add(value)
        seen.add(value)
    return duplicate


def repo_path_exists(reference: str) -> bool:
    if not reference:
        return True
    for item in split_ids(reference):
        path_part = item.split("::", 1)[0]
        if not (ROOT / path_part).exists():
            return False
    return True


def validate() -> list[str]:
    errors: list[str] = []

    vocab = yaml.safe_load(
        (ROOT / "schema" / "controlled_vocabularies.yml").read_text(encoding="utf-8")
    )["vocabularies"]
    allowed_capability_status = set(vocab["capability_status"])

    datasets = yaml.safe_load(
        (ROOT / "schema" / "datasets.yml").read_text(encoding="utf-8")
    )["datasets"]
    dataset_ids = set(datasets)

    equations = read_csv(MODEL_DIR / "equations.csv")
    traceability = read_csv(MODEL_DIR / "traceability.csv")
    claims = read_csv(EVIDENCE_DIR / "claims.csv")
    evidence = read_csv(EVIDENCE_DIR / "evidence_register.csv")

    equation_ids = [row["equation_id"] for row in equations]
    capability_ids = [row["capability_id"] for row in traceability]
    claim_ids = {row["claim_id"] for row in claims}
    evidence_ids = {row["evidence_id"] for row in evidence}

    for label, values in (
        ("equation_id", equation_ids),
        ("capability_id", capability_ids),
    ):
        dup = duplicates(values)
        if dup:
            errors.append(f"duplicate {label}: {sorted(dup)}")

    equation_set = set(equation_ids)

    for row in equations:
        if row["capability_status"] not in allowed_capability_status:
            errors.append(
                f"{row['equation_id']}: invalid capability_status {row['capability_status']}"
            )
        if row["code_location"] and not repo_path_exists(row["code_location"]):
            errors.append(
                f"{row['equation_id']}: missing code path {row['code_location']}"
            )
        if row["test_location"] and not repo_path_exists(row["test_location"]):
            errors.append(
                f"{row['equation_id']}: missing test path {row['test_location']}"
            )

    for row in traceability:
        capability_id = row["capability_id"]
        if row["capability_status"] not in allowed_capability_status:
            errors.append(
                f"{capability_id}: invalid capability_status {row['capability_status']}"
            )
        for equation_id in split_ids(row["formal_reference"]):
            if equation_id.startswith("EQ_") and equation_id not in equation_set:
                errors.append(f"{capability_id}: unknown equation {equation_id}")
        for dataset_id in split_ids(row["dataset_ids"]):
            if dataset_id not in dataset_ids:
                errors.append(f"{capability_id}: unknown dataset {dataset_id}")
        for reference in split_ids(row["evidence_or_claim_ids"]):
            if reference.startswith("CL_") and reference not in claim_ids:
                errors.append(f"{capability_id}: unknown claim {reference}")
            elif reference.startswith("EV_") and reference not in evidence_ids:
                errors.append(f"{capability_id}: unknown evidence {reference}")
        if row["implementation_paths"] and not repo_path_exists(row["implementation_paths"]):
            errors.append(
                f"{capability_id}: missing implementation path {row['implementation_paths']}"
            )
        if row["test_paths"] and not repo_path_exists(row["test_paths"]):
            errors.append(f"{capability_id}: missing test path {row['test_paths']}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Formal equation and traceability validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
