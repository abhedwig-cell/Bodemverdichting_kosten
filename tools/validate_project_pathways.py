from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"


def read_csv(name: str) -> list[dict[str, str]]:
    with (EVIDENCE / name).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate() -> list[str]:
    errors: list[str] = []
    pathways = read_csv("effect_pathway_matrix_v0_1.csv")
    ensembles = read_csv("evidence_ensemble_register_v0_1.csv")
    surfaces = read_csv("onsite_bounded_calculation_surface_v0_1.csv")
    evidence = read_csv("evidence_register.csv")

    pathway_ids = [row["pathway_id"] for row in pathways]
    if len(pathway_ids) != len(set(pathway_ids)):
        errors.append("duplicate pathway_id in effect pathway register")
    known_pathways = set(pathway_ids)
    if not {"O1", "O2", "O3", "O4", "O5", "F1", "F2", "F3", "F4", "F5", "F6"}.issubset(
        known_pathways
    ):
        errors.append("effect pathway register does not cover the current O1-O5/F1-F6 project baseline")

    evidence_ids = {row["evidence_id"] for row in evidence}
    ensemble_ids: set[str] = set()
    seen_members: set[tuple[str, str]] = set()
    for row in ensembles:
        ensemble_id = row["ensemble_id"]
        member_id = row["member_evidence_id"]
        ensemble_ids.add(ensemble_id)
        key = (ensemble_id, member_id)
        if key in seen_members:
            errors.append(f"duplicate ensemble member {ensemble_id} x {member_id}")
        seen_members.add(key)
        if row["pathway_id"] not in known_pathways:
            errors.append(f"{ensemble_id}: unknown pathway_id {row['pathway_id']}")
        migration_status = row["migration_status"]
        if migration_status == "CANONICAL_QUALIFIED" and member_id not in evidence_ids:
            errors.append(
                f"{ensemble_id}: canonical member {member_id} is missing from evidence_register.csv"
            )
        if member_id not in evidence_ids and migration_status != "LEGACY_WORKBOOK_NOT_YET_CANONICAL":
            errors.append(
                f"{ensemble_id}: unknown member {member_id} must remain explicitly legacy until migrated"
            )
        if row["central_value_allowed"].strip().lower() not in {"true", "false"}:
            errors.append(f"{ensemble_id}: central_value_allowed must be true/false")
        if not row["ensemble_next_action"].strip():
            errors.append(f"{ensemble_id}: ensemble_next_action is required")

    surface_ids = [row["surface_id"] for row in surfaces]
    if len(surface_ids) != len(set(surface_ids)):
        errors.append("duplicate surface_id in bounded calculation surface")
    for row in surfaces:
        sid = row["surface_id"]
        if row["pathway_id"] not in known_pathways:
            errors.append(f"{sid}: unknown pathway_id {row['pathway_id']}")
        if row["response_ensemble_id"] not in ensemble_ids:
            errors.append(
                f"{sid}: unknown response_ensemble_id {row['response_ensemble_id']}"
            )
        if not row["surface_next_action"].strip():
            errors.append(f"{sid}: surface_next_action is required")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Project pathway validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Project pathway validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
