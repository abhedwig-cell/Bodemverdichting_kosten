from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = ROOT / "evidence"


def read_csv(name: str) -> list[dict[str, str]]:
    with (EVIDENCE_DIR / name).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def duplicates(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    dup: set[str] = set()
    for value in values:
        if value in seen:
            dup.add(value)
        seen.add(value)
    return dup


def validate() -> list[str]:
    errors: list[str] = []
    vocab = yaml.safe_load(
        (ROOT / "schema" / "controlled_vocabularies.yml").read_text(encoding="utf-8")
    )["vocabularies"]
    allowed_evidence_status = set(vocab["evidence_status"])
    allowed_qualification_status = set(vocab["qualification_status"])
    allowed_provenance = set(vocab["provenance_class"])

    sources = read_csv("sources.csv")
    evidence = read_csv("evidence_register.csv")
    qualifications = read_csv("qualification_register.csv")
    claims = read_csv("claims.csv")

    source_ids = {r["source_id"] for r in sources}
    evidence_ids = {r["evidence_id"] for r in evidence}
    qualification_ids = [r["qualification_id"] for r in qualifications]
    claim_ids = [r["claim_id"] for r in claims]

    for name, values in (
        ("source_id", [r["source_id"] for r in sources]),
        ("evidence_id", [r["evidence_id"] for r in evidence]),
        ("qualification_id", qualification_ids),
        ("claim_id", claim_ids),
    ):
        dup = duplicates(values)
        if dup:
            errors.append(f"duplicate {name}: {sorted(dup)}")

    for row in evidence:
        if row["source_id"] not in source_ids:
            errors.append(f"{row['evidence_id']}: unknown source_id {row['source_id']}")
        if row["evidence_status"] not in allowed_evidence_status:
            errors.append(
                f"{row['evidence_id']}: invalid evidence status {row['evidence_status']}"
            )
        if row["provenance_class"] not in allowed_provenance:
            errors.append(
                f"{row['evidence_id']}: invalid provenance_class {row['provenance_class']}"
            )

    for row in qualifications:
        if row["evidence_id"] not in evidence_ids:
            errors.append(
                f"{row['qualification_id']}: unknown evidence_id {row['evidence_id']}"
            )
        if row["qualification_status"] not in allowed_qualification_status:
            errors.append(
                f"{row['qualification_id']}: invalid qualification verdict "
                f"{row['qualification_status']}"
            )

    for row in claims:
        if row["qualification_status"] not in allowed_qualification_status:
            errors.append(
                f"{row['claim_id']}: invalid claim qualification status "
                f"{row['qualification_status']}"
            )
        for evidence_id in [
            x.strip() for x in row["evidence_ids"].split(";") if x.strip()
        ]:
            if evidence_id not in evidence_ids:
                errors.append(f"{row['claim_id']}: unknown evidence_id {evidence_id}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Evidence register validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
