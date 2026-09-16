from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PROFILE_FILE = ROOT / "data" / "soil" / "tollebeek_soil_profiles.csv"
LAYER_FILE = ROOT / "data" / "soil" / "tollebeek_soil_layers.csv"
METHOD_FILE = ROOT / "data" / "soil" / "tollebeek_profile_screening_v0_1.json"
REQUEST_FILE = ROOT / "data_requests" / "data_request_register.csv"

EXPECTED_PROFILES = {
    "90115240": ("Mn15A", 4019),
    "15100": ("Mv51A", 4006),
    "15250": ("Mn15Av", 4004),
    "90115270": ("Mn25A", 4018),
    "11020": ("Zn10A", 3005),
    "12010": ("Sn13A", 3004),
    "11021": ("Zn10Av", 3001),
    "90111050": ("Zn50A", 3015),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate() -> list[str]:
    errors: list[str] = []
    for path in (PROFILE_FILE, LAYER_FILE, METHOD_FILE):
        if not path.exists():
            errors.append(f"missing profile baseline file: {path.relative_to(ROOT)}")
    if errors:
        return errors

    profiles = read_csv(PROFILE_FILE)
    layers = read_csv(LAYER_FILE)
    method = json.loads(METHOD_FILE.read_text(encoding="utf-8"))

    if len(profiles) != 8:
        errors.append(f"expected 8 admitted profile-context records, found {len(profiles)}")

    source_ids: set[str] = set()
    canonical_profile_ids: set[str] = set()
    fraction_valid_sum = 0.0
    for row in profiles:
        source_id = row["source_profile_id"]
        source_ids.add(source_id)
        canonical_profile_ids.add(row["soil_profile_id"])
        expected = EXPECTED_PROFILES.get(source_id)
        if expected is None:
            errors.append(f"unexpected SoilPhys profile id: {source_id}")
            continue
        expected_smu, expected_bofek = expected
        if row["soil_profile_id"] != f"SOILPHYS_{source_id}":
            errors.append(f"{source_id}: unstable canonical soil_profile_id")
        if row["spatial_unit_id"] != "TOLLEBEEK_OT02_CURRENT":
            errors.append(f"{source_id}: wrong spatial unit")
        if row["source_id"] != "SRC_WUR_SOILPHYSICS":
            errors.append(f"{source_id}: wrong source_id")
        if row["soil_mapping_unit_code"] != expected_smu:
            errors.append(f"{source_id}: SMU {row['soil_mapping_unit_code']} != {expected_smu}")
        if int(row["bofek2020_unit"]) != expected_bofek:
            errors.append(f"{source_id}: BOFEK {row['bofek2020_unit']} != {expected_bofek}")
        if row["profile_provenance_class"] != "DERIVED_MODAL_PROFILE":
            errors.append(f"{source_id}: profile provenance must remain DERIVED_MODAL_PROFILE")
        if "not exact area weighting" not in row["profile_admission_scope"]:
            errors.append(f"{source_id}: admission scope lost exact-area guardrail")
        if "not current compaction state" not in row["profile_admission_scope"]:
            errors.append(f"{source_id}: admission scope lost current-state guardrail")
        fraction_valid_sum += float(row["screening_fraction_valid_points"])

    if source_ids != set(EXPECTED_PROFILES):
        errors.append(f"profile source ids differ from admitted screening set: {sorted(source_ids)}")
    if abs(fraction_valid_sum - 1.0) > 1e-9:
        errors.append(f"valid-profile screening fractions sum to {fraction_valid_sum}, expected 1")

    by_profile: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen_layers: set[str] = set()
    for row in layers:
        layer_id = row["soil_layer_id"]
        if layer_id in seen_layers:
            errors.append(f"duplicate soil_layer_id: {layer_id}")
        seen_layers.add(layer_id)
        profile_id = row["soil_profile_id"]
        by_profile[profile_id].append(row)
        if profile_id not in canonical_profile_ids:
            errors.append(f"{layer_id}: unknown profile {profile_id}")
        if row["property_provenance_class"] != "DERIVED_MODAL_PROFILE_PROPERTY":
            errors.append(f"{layer_id}: modal layer provenance changed")
        if "do not use as CURRENT or REFERENCE soil_state" not in row["state_guardrail"]:
            errors.append(f"{layer_id}: state guardrail missing")
        texture_sum = sum(float(row[k]) for k in ("clay_pct", "silt_pct", "sand_pct"))
        if abs(texture_sum - 100.0) > 1e-6:
            errors.append(f"{layer_id}: texture fractions sum to {texture_sum}")
        if not row["staring_series_spu"].strip():
            errors.append(f"{layer_id}: blank Staring-series SPU")

    for profile_id in canonical_profile_ids:
        rows = sorted(by_profile.get(profile_id, []), key=lambda r: float(r["layer_top_cm"]))
        if not rows:
            errors.append(f"{profile_id}: no layer records")
            continue
        if float(rows[0]["layer_top_cm"]) != 0.0:
            errors.append(f"{profile_id}: profile does not start at 0 cm")
        previous_bottom = None
        for row in rows:
            top = float(row["layer_top_cm"])
            bottom = float(row["layer_bottom_cm"])
            if bottom <= top:
                errors.append(f"{row['soil_layer_id']}: invalid depth interval")
            if previous_bottom is not None and abs(top - previous_bottom) > 1e-9:
                errors.append(f"{profile_id}: non-contiguous layers at {previous_bottom}/{top} cm")
            previous_bottom = bottom
        if abs((previous_bottom or 0.0) - 120.0) > 1e-9:
            errors.append(f"{profile_id}: retained SoilPhys profile does not end at 120 cm")

    coverage = method.get("coverage", {})
    if coverage.get("n_points") != 117 or coverage.get("n_profile") != 113 or coverage.get("n_no_data") != 4:
        errors.append("screening coverage counts changed from qualified 117/113/4 baseline")
    if coverage.get("detected_profile_count") != 8:
        errors.append("screening method no longer reports 8 detected profiles")
    if method.get("interpretation", {}).get("screening_fractions_are") != "diagnostic sampling fractions only":
        errors.append("screening fractions lost diagnostic-only interpretation")

    profile_schema = yaml.safe_load((ROOT / "schema" / "profile_fields_v0_1.yml").read_text(encoding="utf-8"))["fields"]
    core_schema = yaml.safe_load((ROOT / "schema" / "fields.yml").read_text(encoding="utf-8"))["fields"]
    if profile_schema["modal_bulk_density_g_cm3"].get("entity") != "soil_layer":
        errors.append("modal_bulk_density_g_cm3 must remain a soil_layer/profile-context property")
    if core_schema["bulk_density_g_cm3"].get("entity") != "soil_state":
        errors.append("bulk_density_g_cm3 must remain a soil_state property")

    requests = {row["data_request_id"]: row for row in read_csv(REQUEST_FILE)}
    profile_request = requests.get("DR_SM_PROFILE")
    if not profile_request:
        errors.append("missing DR_SM_PROFILE readiness item")
    elif profile_request["input_readiness_status"] != "ADMITTED":
        errors.append(f"DR_SM_PROFILE must be ADMITTED for this bounded profile-context baseline, found {profile_request['input_readiness_status']}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Tollebeek profile baseline validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Tollebeek profile baseline validation passed.")
    print("Validated eight modal SoilPhys profile identities, BOFEK crosswalk, contiguous 0-120 cm layers, screening coverage and the strict profile-context versus soil-state boundary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
