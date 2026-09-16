from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEOMETRY = ROOT / "data" / "spatial" / "tollebeek_ot02_current.geojson"
REQUESTS = ROOT / "data_requests" / "data_request_register.csv"

EXPECTED_SPATIAL_UNIT_ID = "TOLLEBEEK_OT02_CURRENT"
EXPECTED_GLOBALID = "c07f3d9b-c063-42c3-ba0a-1ff65a1b9c6a"
EXPECTED_GEOMETRY_SHA256 = "6a1bf94807ead57bbc347154664c003610dad4694c150ef3b1f1ad40b1b73414"


def validate() -> list[str]:
    errors: list[str] = []
    if not GEOMETRY.exists():
        return [f"missing admitted geometry: {GEOMETRY.relative_to(ROOT)}"]

    try:
        document = json.loads(GEOMETRY.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"cannot parse admitted geometry: {exc}"]

    if document.get("type") != "FeatureCollection":
        errors.append("admitted geometry must be a FeatureCollection")

    crs_name = ((document.get("crs") or {}).get("properties") or {}).get("name")
    if crs_name != "EPSG:28992":
        errors.append(f"unexpected geometry CRS: {crs_name!r}")

    metadata = document.get("project_metadata") or {}
    if metadata.get("spatial_unit_id") != EXPECTED_SPATIAL_UNIT_ID:
        errors.append("unexpected or missing project spatial_unit_id")
    if metadata.get("source_status_code") != 4:
        errors.append("admitted owner feature must retain status code 4")
    if metadata.get("source_status_label") != "vigerend definitief":
        errors.append("admitted owner feature must retain status label vigerend definitief")

    features = document.get("features") or []
    if len(features) != 1:
        errors.append(f"admitted geometry must contain exactly one feature, found {len(features)}")
        return errors

    feature = features[0]
    props = feature.get("properties") or {}
    if props.get("GPGIDENT") != "OT.02":
        errors.append("admitted feature GPGIDENT must be OT.02")
    if props.get("IWS_GPGSTATU") != 4:
        errors.append("admitted feature IWS_GPGSTATU must be 4")
    if props.get("GLOBALID") != EXPECTED_GLOBALID:
        errors.append("admitted feature GLOBALID changed")
    if props.get("OBJECTID") != metadata.get("source_objectid"):
        errors.append("source OBJECTID mismatch between metadata and feature")
    if props.get("GLOBALID") != metadata.get("source_globalid"):
        errors.append("source GLOBALID mismatch between metadata and feature")

    geometry = feature.get("geometry")
    if not geometry or geometry.get("type") != "Polygon":
        errors.append("admitted feature must contain polygon geometry")
    else:
        digest = hashlib.sha256(
            json.dumps(geometry, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        if digest != EXPECTED_GEOMETRY_SHA256:
            errors.append(f"geometry hash changed: {digest}")
        if metadata.get("geometry_sha256") != digest:
            errors.append("project metadata geometry_sha256 does not match geometry")

    shape_area = props.get("Shape__Area")
    if not isinstance(shape_area, (int, float)) or shape_area <= 0:
        errors.append("Shape__Area must be a positive numeric source attribute")
    else:
        if abs(metadata.get("shape_area_m2", 0) - shape_area) > 1e-6:
            errors.append("metadata shape_area_m2 does not equal source Shape__Area")
        if abs(metadata.get("shape_area_ha", 0) - shape_area / 10000.0) > 1e-9:
            errors.append("metadata shape_area_ha does not equal source geometry area conversion")

    with REQUESTS.open(newline="", encoding="utf-8") as handle:
        rows = {row["data_request_id"]: row for row in csv.DictReader(handle)}
    request = rows.get("DR_SM_GEOMETRY")
    if not request:
        errors.append("DR_SM_GEOMETRY is missing")
    else:
        if request.get("input_readiness_status") != "ADMITTED":
            errors.append("DR_SM_GEOMETRY must be ADMITTED when canonical geometry is present")
        links = set(filter(None, request.get("current_evidence_ids", "").split(";")))
        required = {"EV_TOL_OT02_CURRENT_GEOMETRY", "EV_TOL_OT02_PEILBESLUIT_CROSSCHECK"}
        missing = required - links
        if missing:
            errors.append(f"DR_SM_GEOMETRY missing admitted evidence links: {sorted(missing)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Spatial geometry validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Spatial geometry validation passed.")
    print("Validated admitted OT.02 owner feature identity, geometry hash, CRS and readiness binding.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
