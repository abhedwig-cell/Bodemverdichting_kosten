from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SURFACE_PATH = ROOT / "evidence" / "onsite_bounded_calculation_surface_v0_1.csv"
ENSEMBLE_PATH = ROOT / "evidence" / "evidence_ensemble_register_v0_1.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def validate() -> list[str]:
    errors: list[str] = []

    if not SURFACE_PATH.exists():
        return [f"missing bounded calculation surface: {SURFACE_PATH.relative_to(ROOT)}"]
    if not ENSEMBLE_PATH.exists():
        return [f"missing evidence ensemble register: {ENSEMBLE_PATH.relative_to(ROOT)}"]

    rows = read_csv(SURFACE_PATH)
    ensemble_rows = read_csv(ENSEMBLE_PATH)
    ensemble_ids = {row["ensemble_id"] for row in ensemble_rows}

    surface_ids = [row["surface_id"] for row in rows]
    if len(surface_ids) != len(set(surface_ids)):
        errors.append("duplicate surface_id in onsite bounded calculation surface")

    required_columns = {
        "surface_id",
        "pathway_id",
        "parent_reporting_unit",
        "parent_area_ha",
        "area_basis_status",
        "crop_share",
        "crop_share_status",
        "compaction_exposure_low",
        "compaction_exposure_base",
        "compaction_exposure_high",
        "exposure_status",
        "response_ensemble_id",
        "response_status",
        "economic_value_status",
        "formula_contract",
        "current_output_status",
        "primary_blocker",
        "surface_next_action",
    }
    if rows:
        missing = required_columns - set(rows[0])
        if missing:
            errors.append(f"missing required surface columns: {sorted(missing)}")
            return errors

    exposure_fields = (
        "compaction_exposure_low",
        "compaction_exposure_base",
        "compaction_exposure_high",
    )

    for row in rows:
        sid = row["surface_id"]

        if row["pathway_id"] != "O1":
            errors.append(f"{sid}: only O1 yield pathway is allowed in v0.1")

        if row["response_ensemble_id"] not in ensemble_ids:
            errors.append(
                f"{sid}: unknown response ensemble {row['response_ensemble_id']}"
            )

        try:
            area = float(row["parent_area_ha"])
            if area <= 0:
                errors.append(f"{sid}: parent_area_ha must be positive")
        except ValueError:
            errors.append(f"{sid}: parent_area_ha is not numeric")

        if row["exposure_status"] == "WAIT_DATA":
            populated = [field for field in exposure_fields if row[field].strip()]
            if populated:
                errors.append(
                    f"{sid}: WAIT_DATA exposure must remain blank; populated {populated}"
                )

        if row["crop_share_status"] == "WAIT_CROP_CROSSWALK":
            if row["crop_share"].strip():
                errors.append(
                    f"{sid}: WAIT_CROP_CROSSWALK requires blank crop_share"
                )

        if row["crop_share_status"] == "LANDUSE_IDENTITY_ONLY":
            try:
                share = float(row["crop_share"])
                if share != 1.0:
                    errors.append(
                        f"{sid}: LANDUSE_IDENTITY_ONLY crop_share must equal 1.0"
                    )
            except ValueError:
                errors.append(
                    f"{sid}: LANDUSE_IDENTITY_ONLY requires numeric crop_share 1.0"
                )

        if row["current_output_status"] != "BOUNDED_NO_DAMAGE_RESULT":
            errors.append(
                f"{sid}: v0.1 must remain BOUNDED_NO_DAMAGE_RESULT"
            )

        if row["economic_value_status"] != "WAIT_ECONOMIC_VALUE":
            errors.append(
                f"{sid}: v0.1 must keep economic_value_status WAIT_ECONOMIC_VALUE"
            )

        if not row["formula_contract"].strip():
            errors.append(f"{sid}: formula_contract must be explicit")
        if not row["primary_blocker"].strip():
            errors.append(f"{sid}: primary_blocker must be explicit")
        if not row["surface_next_action"].strip():
            errors.append(f"{sid}: surface_next_action must be explicit")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("On-site bounded calculation surface validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
