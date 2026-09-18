from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLASS_DEFS = ROOT / "config" / "ccnl6_class_definition_v0_1.csv"
MAPPING = ROOT / "config" / "bro_sgm_to_ccnl6_mapping_v0_1.csv"
ACQUISITION = (
    ROOT / "artifacts" / "acquisition" / "onsite_maize_soil_crosswalk_sources_v0_1.json"
)
EXPECTED_CLASSES = {"ZE", "ZO", "K", "L", "M", "V"}
MAPPING_COLUMNS = {
    "soil_unit_code",
    "soil_classification",
    "main_soil_classification",
    "ccnl6_class",
    "mapping_basis",
    "mapping_status",
    "review_notes",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def validate() -> list[str]:
    errors: list[str] = []

    for path in (CLASS_DEFS, MAPPING, ACQUISITION):
        if not path.exists():
            errors.append(f"missing required maize-soil-crosswalk path: {path.relative_to(ROOT)}")
    if errors:
        return errors

    defs = read_csv(CLASS_DEFS)
    classes = [row.get("ccnl6_class", "").strip() for row in defs]
    if set(classes) != EXPECTED_CLASSES or len(classes) != len(EXPECTED_CLASSES):
        errors.append(
            f"CCNL6 class definition must contain exactly {sorted(EXPECTED_CLASSES)}; got {classes}"
        )
    for row in defs:
        cid = row.get("ccnl6_class", "").strip()
        if not row.get("definition", "").strip():
            errors.append(f"{cid}: class definition is blank")
        if not row.get("source_basis", "").strip():
            errors.append(f"{cid}: source_basis is blank")
        if row.get("mapping_status", "").strip() != "DEFINED":
            errors.append(f"{cid}: mapping_status must be DEFINED")

    with MAPPING.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if set(reader.fieldnames or []) != MAPPING_COLUMNS:
            errors.append(
                "BRO-to-CCNL6 mapping columns differ from contract: "
                f"{reader.fieldnames}"
            )
            mapping_rows: list[dict[str, str]] = []
        else:
            mapping_rows = list(reader)

    seen: set[str] = set()
    qualified_count = 0
    for row in mapping_rows:
        code = row.get("soil_unit_code", "").strip()
        klass = row.get("ccnl6_class", "").strip()
        status = row.get("mapping_status", "").strip()
        basis = row.get("mapping_basis", "").strip()
        if not code:
            errors.append("mapping row has blank soil_unit_code")
            continue
        if code in seen:
            errors.append(f"duplicate mapped soil_unit_code: {code}")
        seen.add(code)
        if klass not in EXPECTED_CLASSES:
            errors.append(f"{code}: invalid ccnl6_class {klass!r}")
        if status not in {"REVIEW_REQUIRED", "QUALIFIED", "REJECTED"}:
            errors.append(f"{code}: invalid mapping_status {status!r}")
        if status == "QUALIFIED":
            qualified_count += 1
            if not basis:
                errors.append(f"{code}: QUALIFIED mapping requires mapping_basis")

    acquisition = json.loads(ACQUISITION.read_text(encoding="utf-8"))
    if acquisition.get("run_authorized") is not False:
        errors.append("acquisition contract must remain run_authorized=false in v0.1")
    if acquisition.get("scientific_status") != (
        "ACQUISITION_ROUTES_QUALIFIED_RAW_DATA_NOT_MATERIALIZED"
    ):
        errors.append("unexpected acquisition scientific_status")
    if qualified_count == 0 and acquisition.get("run_authorized") is not False:
        errors.append("zero qualified soil mappings cannot authorize a run")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("On-site maize/soil crosswalk design validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
