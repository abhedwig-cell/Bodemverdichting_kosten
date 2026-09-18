from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Iterable


CCNL6_CLASSES = {"ZE", "ZO", "K", "L", "M", "V"}
QUALIFIED_MAPPING_STATUS = "QUALIFIED"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_mapping_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def validate_mapping_rows(rows: Iterable[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()

    for i, row in enumerate(rows, start=2):
        code = (row.get("soil_unit_code") or "").strip()
        klass = (row.get("ccnl6_class") or "").strip()
        status = (row.get("mapping_status") or "").strip()
        basis = (row.get("mapping_basis") or "").strip()

        if not code:
            errors.append(f"row {i}: soil_unit_code is blank")
            continue
        if code in seen:
            errors.append(f"row {i}: duplicate soil_unit_code {code}")
        seen.add(code)

        if klass not in CCNL6_CLASSES:
            errors.append(f"row {i}: invalid ccnl6_class {klass!r} for {code}")
        if status not in {"REVIEW_REQUIRED", "QUALIFIED", "REJECTED"}:
            errors.append(f"row {i}: invalid mapping_status {status!r} for {code}")
        if status == QUALIFIED_MAPPING_STATUS and not basis:
            errors.append(f"row {i}: QUALIFIED mapping {code} requires mapping_basis")

    return errors


def mapping_coverage(
    soil_unit_codes: Iterable[str],
    rows: Iterable[dict[str, str]],
) -> tuple[list[str], list[str]]:
    mapping = {
        (row.get("soil_unit_code") or "").strip(): row
        for row in rows
        if (row.get("soil_unit_code") or "").strip()
    }
    missing: list[str] = []
    unqualified: list[str] = []

    for code in sorted({str(x).strip() for x in soil_unit_codes if str(x).strip()}):
        row = mapping.get(code)
        if row is None:
            missing.append(code)
        elif (row.get("mapping_status") or "").strip() != QUALIFIED_MAPPING_STATUS:
            unqualified.append(code)

    return missing, unqualified


def is_target_brp_record(row: dict[str, object]) -> bool:
    return (
        str(row.get("gewascode", "")).strip() == "259"
        and str(row.get("jaar", "")).strip() == "2025"
        and str(row.get("status", "")).strip().casefold() == "definitief"
    )


def require_columns(columns: Iterable[str], required: set[str], label: str) -> None:
    available = set(columns)
    missing = sorted(required - available)
    if missing:
        raise ValueError(f"{label}: missing required columns {missing}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Build a fail-closed 2025 silage-maize by CC-NL6 soil-class crosswalk "
            "from a local BRP file and local BRO SGM soil-map file."
        )
    )
    p.add_argument("--brp", required=True, type=Path)
    p.add_argument("--soil", required=True, type=Path)
    p.add_argument("--soil-layer", default=None)
    p.add_argument(
        "--mapping",
        type=Path,
        default=Path("config/bro_sgm_to_ccnl6_mapping_v0_1.csv"),
    )
    p.add_argument(
        "--output",
        type=Path,
        default=Path("data/derived/onsite_maize_soil_crosswalk_2025.csv"),
    )
    p.add_argument(
        "--manifest",
        type=Path,
        default=Path("data/derived/onsite_maize_soil_crosswalk_2025_manifest.json"),
    )
    p.add_argument(
        "--unmapped-report",
        type=Path,
        default=Path("data/derived/onsite_maize_soil_unmapped_codes_2025.csv"),
        help=(
            "Diagnostic CSV written when intersecting BRO soil codes are missing "
            "or not yet QUALIFIED."
        ),
    )
    p.add_argument(
        "--closure-tolerance",
        type=float,
        default=0.005,
        help="Maximum relative area closure error; default 0.005 = 0.5%%.",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()

    mapping_rows = read_mapping_rows(args.mapping)
    mapping_errors = validate_mapping_rows(mapping_rows)
    if mapping_errors:
        for error in mapping_errors:
            print(f"ERROR: mapping: {error}")
        return 2

    try:
        import geopandas as gpd
        import pandas as pd
    except ImportError:
        print(
            "ERROR: geospatial execution requires geopandas and pandas. "
            "The repository integrity tests do not require those packages."
        )
        return 2

    read_soil_kwargs = {}
    if args.soil_layer:
        read_soil_kwargs["layer"] = args.soil_layer

    brp = gpd.read_file(args.brp)
    soil = gpd.read_file(args.soil, **read_soil_kwargs)

    require_columns(
        brp.columns,
        {"gewascode", "jaar", "status", "geometry"},
        "BRP",
    )
    require_columns(
        soil.columns,
        {
            "soil_unit_code",
            "soil_classification",
            "main_soil_classification",
            "geometry",
        },
        "BRO SGM",
    )

    if brp.crs is None:
        print("ERROR: BRP input has no CRS")
        return 2
    if soil.crs is None:
        print("ERROR: BRO SGM input has no CRS")
        return 2

    brp = brp.to_crs(28992)
    soil = soil.to_crs(28992)

    target_mask = (
        brp["gewascode"].astype(str).str.strip().eq("259")
        & brp["jaar"].astype(str).str.strip().eq("2025")
        & brp["status"].astype(str).str.strip().str.casefold().eq("definitief")
    )
    maize = brp.loc[target_mask, ["gewascode", "jaar", "status", "geometry"]].copy()
    if maize.empty:
        print("ERROR: no definitive 2025 silage-maize parcels (gewascode 259) found")
        return 2

    maize = maize.reset_index(drop=False).rename(columns={"index": "source_parcel_index"})
    maize["parcel_area_m2"] = maize.geometry.area
    maize_area_m2 = float(maize["parcel_area_m2"].sum())
    if maize_area_m2 <= 0:
        print("ERROR: target BRP maize area is zero")
        return 2

    # First identify only soil units that actually intersect target maize geometry.
    joined = gpd.sjoin(
        maize[["source_parcel_index", "geometry"]],
        soil[["soil_unit_code", "geometry"]],
        how="left",
        predicate="intersects",
    )
    candidate_codes = [
        str(x).strip()
        for x in joined["soil_unit_code"].dropna().tolist()
        if str(x).strip()
    ]
    if not candidate_codes:
        print("ERROR: no BRO SGM soil units intersect target maize geometry")
        return 2

    missing, unqualified = mapping_coverage(candidate_codes, mapping_rows)
    if missing or unqualified:
        problem_codes = set(missing) | set(unqualified)
        report = soil.loc[
            soil["soil_unit_code"].astype(str).str.strip().isin(problem_codes),
            [
                "soil_unit_code",
                "soil_classification",
                "main_soil_classification",
            ],
        ].copy()
        report["soil_unit_code"] = report["soil_unit_code"].astype(str).str.strip()
        report = report.drop_duplicates(subset=["soil_unit_code"]).sort_values(
            "soil_unit_code"
        )
        report["mapping_state"] = report["soil_unit_code"].map(
            lambda code: "MISSING" if code in set(missing) else "UNQUALIFIED"
        )
        args.unmapped_report.parent.mkdir(parents=True, exist_ok=True)
        report.to_csv(args.unmapped_report, index=False)

        if missing:
            print("ERROR: unmapped intersecting BRO soil_unit_code values:")
            for code in missing:
                print(f"  - {code}")
        if unqualified:
            print("ERROR: intersecting BRO soil_unit_code values not QUALIFIED:")
            for code in unqualified:
                print(f"  - {code}")
        print(f"Wrote review diagnostic: {args.unmapped_report}")
        print(
            "Crosswalk aborted. Add/review explicit mappings in "
            "config/bro_sgm_to_ccnl6_mapping_v0_1.csv; no fallback class is allowed."
        )
        return 3

    mapping_lookup = {
        row["soil_unit_code"].strip(): row["ccnl6_class"].strip()
        for row in mapping_rows
        if row["mapping_status"].strip() == QUALIFIED_MAPPING_STATUS
    }

    candidate_soil = soil.loc[
        soil["soil_unit_code"].astype(str).str.strip().isin(set(candidate_codes)),
        [
            "soil_unit_code",
            "soil_classification",
            "main_soil_classification",
            "geometry",
        ],
    ].copy()
    candidate_soil["soil_unit_code"] = (
        candidate_soil["soil_unit_code"].astype(str).str.strip()
    )
    candidate_soil["ccnl6_class"] = candidate_soil["soil_unit_code"].map(mapping_lookup)

    intersections = gpd.overlay(
        maize[["source_parcel_index", "geometry"]],
        candidate_soil[
            [
                "soil_unit_code",
                "soil_classification",
                "main_soil_classification",
                "ccnl6_class",
                "geometry",
            ]
        ],
        how="intersection",
        keep_geom_type=False,
    )
    if intersections.empty:
        print("ERROR: overlay produced no intersections")
        return 2

    intersections["intersection_area_m2"] = intersections.geometry.area
    mapped_area_m2 = float(intersections["intersection_area_m2"].sum())
    closure_error = abs(mapped_area_m2 - maize_area_m2) / maize_area_m2
    if closure_error > args.closure_tolerance:
        print(
            "ERROR: maize/soil overlay area closure failed: "
            f"maize={maize_area_m2 / 10000:.3f} ha, "
            f"mapped={mapped_area_m2 / 10000:.3f} ha, "
            f"relative_error={closure_error:.6f}, "
            f"tolerance={args.closure_tolerance:.6f}"
        )
        return 4

    summary = (
        intersections.groupby("ccnl6_class", as_index=False)["intersection_area_m2"]
        .sum()
        .rename(columns={"intersection_area_m2": "maize_area_m2"})
    )
    summary["maize_area_ha"] = summary["maize_area_m2"] / 10000.0
    summary["share_of_total_maize"] = summary["maize_area_m2"] / maize_area_m2
    summary["mapping_status"] = "QUALIFIED_MAPPING_USED"
    summary = summary[
        [
            "ccnl6_class",
            "maize_area_ha",
            "share_of_total_maize",
            "mapping_status",
        ]
    ].sort_values("ccnl6_class")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output, index=False)

    manifest = {
        "artifact_id": "ONSITE_MAIZE_SOIL_CROSSWALK_2025",
        "status": "GENERATED_NOT_SCIENTIFICALLY_ADMITTED",
        "brp_file": str(args.brp),
        "brp_sha256": sha256_file(args.brp),
        "soil_file": str(args.soil),
        "soil_sha256": sha256_file(args.soil),
        "mapping_file": str(args.mapping),
        "mapping_sha256": sha256_file(args.mapping),
        "target": {
            "gewascode": 259,
            "jaar": 2025,
            "status": "Definitief",
        },
        "target_crs": "EPSG:28992",
        "maize_parcel_count": int(len(maize)),
        "maize_area_ha": maize_area_m2 / 10000.0,
        "mapped_area_ha": mapped_area_m2 / 10000.0,
        "relative_area_closure_error": closure_error,
        "closure_tolerance": args.closure_tolerance,
        "ccnl6_classes_present": summary["ccnl6_class"].tolist(),
        "guardrails": [
            "No unmapped or unqualified intersecting BRO soil_unit_code is allowed.",
            "No residual unknown soil unit is assigned automatically to ZO or another class.",
            "The BRO SGM spatial crosswalk is not identical to historical LSK domain membership.",
            "This artifact does not provide compaction exposure or crop-damage response.",
        ],
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Wrote {args.output}")
    print(f"Wrote {args.manifest}")
    print(
        f"Area closure passed: {maize_area_m2 / 10000:.3f} ha target, "
        f"{mapped_area_m2 / 10000:.3f} ha mapped, "
        f"relative error {closure_error:.6f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
