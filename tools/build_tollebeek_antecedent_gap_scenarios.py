from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = ROOT / "evidence" / "source_snapshots" / "tollebeek_antecedent_gap_v0_1"
DEFAULT_OUTPUT = ROOT / "artifacts" / "scenarios" / "tollebeek_antecedent_gap_reconstruction_v0_1.json"

GAP_START = datetime(1998, 9, 3, 0, tzinfo=timezone.utc)
GAP_END = datetime(1998, 9, 7, 12, tzinfo=timezone.utc)
REPORT_DATES = ("19980903", "19980904", "19980905", "19980906", "19980907", "19980908")
TIMING_STATIONS = ("267", "269", "270", "279")
TRACE_POLICIES = {
    "TRACE_BOUND_LOWER": 0.0,
    "TRACE_MIDPOINT": 0.025,
    "TRACE_NEAR_UPPER": 0.049,
}
METHOD_ID = "ST317_MASS_CONSTRAINED_MULTI_STATION_TIMING_V0_1"
METHOD_AUTHORITY = "docs/47_tollebeek_antecedent_precip_gap_reconstruction_protocol_v0_1.md"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def iso_z(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def classify_tenths(raw: str) -> dict[str, Any]:
    raw = raw.strip()
    if raw == "":
        return {"kind": "missing", "raw": raw}
    value = int(raw)
    if value == -1:
        return {
            "kind": "trace",
            "raw": raw,
            "lower_mm_inclusive": 0.0,
            "upper_mm_exclusive": 0.05,
        }
    if value < -1:
        raise ValueError(f"unexpected negative precipitation code {value}")
    if value == 0:
        return {"kind": "zero", "raw": raw, "reported_mm": 0.0}
    return {"kind": "reported_positive", "raw": raw, "reported_mm": value / 10.0}


def numeric_precip(obs: dict[str, Any], trace_value_mm: float) -> float | None:
    kind = obs["kind"]
    if kind == "missing":
        return None
    if kind == "trace":
        return trace_value_mm
    return float(obs["reported_mm"])


def report_window(report_date: str) -> tuple[datetime, datetime]:
    end_date = datetime.strptime(report_date, "%Y%m%d").replace(tzinfo=timezone.utc)
    return end_date - timedelta(days=1) + timedelta(hours=8), end_date + timedelta(hours=8)


def hourly_range(start: datetime, end: datetime) -> list[datetime]:
    out: list[datetime] = []
    current = start
    while current < end:
        out.append(current)
        current += timedelta(hours=1)
    return out


def load_receipt(source_dir: Path) -> tuple[dict[str, Any], dict[str, bytes]]:
    receipt_path = source_dir / "source_receipt_manifest.json"
    receipt_bytes = receipt_path.read_bytes()
    receipt = json.loads(receipt_bytes.decode("utf-8"))
    if receipt.get("classification") != "ACQUIRED_SOURCE_NATIVE_NOT_YET_RECONSTRUCTED":
        raise ValueError("source receipt has unexpected classification")

    raw_by_name: dict[str, bytes] = {}
    for request in receipt["requests"]:
        name = request["name"]
        raw_path = ROOT / request["raw_path"] if not Path(request["raw_path"]).is_absolute() else Path(request["raw_path"])
        if source_dir != DEFAULT_SOURCE_DIR:
            raw_path = source_dir / Path(request["raw_path"]).name
        raw = raw_path.read_bytes()
        expected_size = int(request["response_bytes"])
        expected_sha = request["response_sha256"]
        if len(raw) != expected_size:
            raise ValueError(f"{name}: byte size mismatch: {len(raw)} != {expected_size}")
        actual_sha = sha256_bytes(raw)
        if actual_sha != expected_sha:
            raise ValueError(f"{name}: SHA-256 mismatch: {actual_sha} != {expected_sha}")
        raw_by_name[name] = raw

    if set(raw_by_name) != {"hourly", "manual317"}:
        raise ValueError(f"unexpected source set: {sorted(raw_by_name)}")
    return receipt, raw_by_name


def parse_hourly(raw: bytes) -> dict[str, dict[datetime, dict[str, Any]]]:
    text = raw.decode("utf-8-sig")
    hourly: dict[str, dict[datetime, dict[str, Any]]] = defaultdict(dict)
    for line_no, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split(",")]
        if len(fields) != 5:
            raise ValueError(f"hourly line {line_no}: expected 5 fields, got {len(fields)}")
        station, date, hour_raw, dr_raw, rh_raw = fields
        day = datetime.strptime(date, "%Y%m%d").replace(tzinfo=timezone.utc)
        hour = int(hour_raw)
        end = day + (timedelta(days=1) if hour == 24 else timedelta(hours=hour))
        start = end - timedelta(hours=1)
        if start in hourly[station]:
            raise ValueError(f"duplicate hourly row {station} {iso_z(start)}")
        hourly[station][start] = {
            "station": station,
            "source_date": date,
            "source_hour": hour,
            "timestamp_utc": iso_z(start),
            "DR_raw": dr_raw,
            "RH": classify_tenths(rh_raw),
        }
    return dict(hourly)


def parse_manual(raw: bytes) -> dict[str, dict[str, Any]]:
    text = raw.decode("utf-8-sig")
    manual: dict[str, dict[str, Any]] = {}
    for line_no, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = [field.strip() for field in line.split(",")]
        if len(fields) < 3:
            raise ValueError(f"manual line {line_no}: expected at least 3 fields")
        station, report_date, rd_raw = fields[:3]
        if station != "317":
            raise ValueError(f"unexpected manual station {station}")
        if report_date in manual:
            raise ValueError(f"duplicate manual report date {report_date}")
        manual[report_date] = {
            "station": station,
            "report_date": report_date,
            "RD": classify_tenths(rd_raw),
        }
    return manual


def _retained_mass_enclosure(rows: list[dict[str, Any]]) -> dict[str, Any]:
    reported_positive = 0.0
    trace_count = 0
    for row in rows:
        obs = row["RH"]
        if obs["kind"] == "reported_positive":
            reported_positive += float(obs["reported_mm"])
        elif obs["kind"] == "trace":
            trace_count += 1
        elif obs["kind"] == "missing":
            raise ValueError(f"unexpected source-missing retained station-273 row {row['timestamp_utc']}")
    return {
        "reported_positive_mm": round(reported_positive, 9),
        "trace_count": trace_count,
        "lower_mm_inclusive": round(reported_positive, 9),
        "upper_mm_exclusive": round(reported_positive + trace_count * 0.05, 9),
    }


def build_package(source_dir: Path = DEFAULT_SOURCE_DIR) -> dict[str, Any]:
    receipt, raw = load_receipt(source_dir)
    hourly = parse_hourly(raw["hourly"])
    manual = parse_manual(raw["manual317"])

    required_hourly_stations = {"273", *TIMING_STATIONS}
    if not required_hourly_stations.issubset(hourly):
        raise ValueError(f"missing hourly stations: {sorted(required_hourly_stations - set(hourly))}")

    gap_hours = hourly_range(GAP_START, GAP_END)
    if len(gap_hours) != 108:
        raise AssertionError("internal gap duration is not 108 hours")
    for timestamp in gap_hours:
        row = hourly["273"].get(timestamp)
        if row is None or row["RH"]["kind"] != "missing":
            raise ValueError(f"station 273 gap hour is not source-missing: {iso_z(timestamp)}")

    windows: list[dict[str, Any]] = []
    covered_gap_hours: list[datetime] = []

    for report_date in REPORT_DATES:
        if report_date not in manual:
            raise ValueError(f"missing manual station-317 report date {report_date}")
        rd = manual[report_date]["RD"]
        if rd["kind"] not in {"reported_positive", "zero"}:
            raise ValueError(f"station-317 RD is not point-reported for {report_date}: {rd}")
        mass317 = float(rd["reported_mm"])

        window_start, window_end = report_window(report_date)
        timestamps = hourly_range(window_start, window_end)
        missing = [t for t in timestamps if GAP_START <= t < GAP_END]
        retained = [t for t in timestamps if not (GAP_START <= t < GAP_END)]
        covered_gap_hours.extend(missing)

        retained_rows: list[dict[str, Any]] = []
        for timestamp in retained:
            row = hourly["273"].get(timestamp)
            if row is None:
                raise ValueError(f"missing station-273 retained timestamp {iso_z(timestamp)}")
            if row["RH"]["kind"] == "missing":
                raise ValueError(f"station-273 retained timestamp is source-missing {iso_z(timestamp)}")
            retained_rows.append(row)

        enclosure = _retained_mass_enclosure(retained_rows)
        residual_lower = max(0.0, mass317 - enclosure["upper_mm_exclusive"])
        residual_upper = max(0.0, mass317 - enclosure["lower_mm_inclusive"])
        if mass317 - enclosure["upper_mm_exclusive"] < -1e-12:
            raise ValueError(f"negative residual lower bound for {report_date}")

        policy_results: list[dict[str, Any]] = []
        for trace_policy, trace_value in TRACE_POLICIES.items():
            retained_numeric = sum(
                float(numeric_precip(row["RH"], trace_value)) for row in retained_rows
            )
            residual = mass317 - retained_numeric
            if residual < -1e-9:
                raise ValueError(
                    f"negative residual under {trace_policy} for {report_date}: {residual}"
                )
            residual = max(0.0, residual)

            station_members: list[dict[str, Any]] = []
            valid_fraction_sets: list[tuple[str, list[float]]] = []

            for station in TIMING_STATIONS:
                observations: list[dict[str, Any]] = []
                source_values: list[float] = []
                invalid_reason: str | None = None

                for timestamp in missing:
                    row = hourly[station].get(timestamp)
                    if row is None or row["RH"]["kind"] == "missing":
                        invalid_reason = "SOURCE_MISSING_TIMING_HOUR"
                        break
                    value = numeric_precip(row["RH"], trace_value)
                    if value is None:
                        invalid_reason = "SOURCE_MISSING_TIMING_HOUR"
                        break
                    observations.append(row)
                    source_values.append(float(value))

                if invalid_reason is not None:
                    station_members.append({
                        "timing_source_station": station,
                        "status": "INVALID",
                        "failure_reason": invalid_reason,
                    })
                    continue

                timing_mass = sum(source_values)
                if residual > 0.0 and timing_mass <= 0.0:
                    station_members.append({
                        "timing_source_station": station,
                        "status": "INVALID",
                        "failure_reason": "ZERO_TIMING_MASS_WITH_POSITIVE_RESIDUAL",
                        "source_trace_count": sum(
                            1 for row in observations if row["RH"]["kind"] == "trace"
                        ),
                        "source_reported_positive_count": sum(
                            1 for row in observations
                            if row["RH"]["kind"] == "reported_positive"
                        ),
                    })
                    continue

                fractions = (
                    [0.0 for _ in source_values]
                    if timing_mass == 0.0
                    else [value / timing_mass for value in source_values]
                )
                reconstructed = [
                    round(residual * fraction, 9) for fraction in fractions
                ]
                station_members.append({
                    "timing_source_station": station,
                    "status": "VALID_SCENARIO_MEMBER",
                    "provenance": {
                        "mass_anchor_station": "317",
                        "mass_anchor_report_date": report_date,
                        "trace_policy": trace_policy,
                        "method_id": METHOD_ID,
                        "value_origin": "reconstructed",
                        "hour_axis": "window.gap_timestamps_utc",
                    },
                    "source_timing_mass_mm_under_trace_policy": round(timing_mass, 9),
                    "source_trace_count": sum(
                        1 for row in observations if row["RH"]["kind"] == "trace"
                    ),
                    "source_reported_positive_count": sum(
                        1 for row in observations
                        if row["RH"]["kind"] == "reported_positive"
                    ),
                    "reconstructed_mm_by_gap_timestamp": reconstructed,
                })
                valid_fraction_sets.append((station, fractions))

            if residual > 0.0 and not valid_fraction_sets:
                raise ValueError(
                    f"no valid timing member for positive residual on {report_date} {trace_policy}"
                )

            ensemble_values: list[float] = []
            valid_stations = [station for station, _ in valid_fraction_sets]
            if missing:
                if valid_fraction_sets:
                    ensemble_fractions = [
                        sum(fractions[index] for _, fractions in valid_fraction_sets)
                        / len(valid_fraction_sets)
                        for index in range(len(missing))
                    ]
                    total_fraction = sum(ensemble_fractions)
                    if residual > 0.0 and total_fraction <= 0.0:
                        raise ValueError(
                            f"zero ensemble timing fraction for {report_date} {trace_policy}"
                        )
                    if total_fraction > 0.0:
                        ensemble_fractions = [
                            fraction / total_fraction for fraction in ensemble_fractions
                        ]
                else:
                    ensemble_fractions = [0.0 for _ in missing]

                ensemble_values = [
                    round(residual * fraction, 9) for fraction in ensemble_fractions
                ]

            policy_results.append({
                "trace_policy": trace_policy,
                "numeric_trace_mm_for_scenario_calculation": trace_value,
                "source_trace_semantics_unchanged": "0 <= trace < 0.05 mm",
                "station273_retained_mass_mm_under_trace_policy": round(retained_numeric, 9),
                "residual_mass_mm_under_trace_policy": round(residual, 9),
                "station_members": station_members,
                "ensemble": {
                    "status": "DIAGNOSTIC_AGGREGATE_NOT_HISTORICAL_TRUTH",
                    "provenance": {
                        "mass_anchor_station": "317",
                        "mass_anchor_report_date": report_date,
                        "timing_source_stations": valid_stations,
                        "trace_policy": trace_policy,
                        "method_id": METHOD_ID,
                        "aggregate_role": "DIAGNOSTIC_EQUAL_VALID_MEMBER_ENSEMBLE",
                    },
                    "valid_timing_stations": valid_stations,
                    "reconstructed_mm_by_gap_timestamp": ensemble_values,
                },
            })

        windows.append({
            "report_date": report_date,
            "window_start_utc": iso_z(window_start),
            "window_end_utc_exclusive": iso_z(window_end),
            "gap_hour_count": len(missing),
            "gap_timestamps_utc": [iso_z(t) for t in missing],
            "station317_reported_total_mm": mass317,
            "station273_retained_mass_enclosure": enclosure,
            "residual_mass_enclosure": {
                "lower_mm_conservative": round(residual_lower, 9),
                "lower_is_open_when_retained_trace_count_positive": enclosure["trace_count"] > 0,
                "upper_mm_inclusive": round(residual_upper, 9),
            },
            "trace_policy_results": policy_results,
        })

    if sorted(covered_gap_hours) != gap_hours:
        raise ValueError("08:00-08:00 report windows do not partition the 108-hour gap exactly")

    receipt_bytes = (source_dir / "source_receipt_manifest.json").read_bytes()
    return {
        "schema_version": "tollebeek_antecedent_gap_reconstruction_package_v0.1",
        "classification": "SCENARIO_ONLY_CANDIDATE_NOT_RUN_READY",
        "method_id": METHOD_ID,
        "method_authority": METHOD_AUTHORITY,
        "gap_start_utc": iso_z(GAP_START),
        "gap_end_utc_exclusive": iso_z(GAP_END),
        "gap_hour_count": 108,
        "source_snapshot": {
            "receipt_path": "evidence/source_snapshots/tollebeek_antecedent_gap_v0_1/source_receipt_manifest.json",
            "receipt_sha256": sha256_bytes(receipt_bytes),
            "hourly_response_sha256": next(
                request["response_sha256"]
                for request in receipt["requests"]
                if request["name"] == "hourly"
            ),
            "manual317_response_sha256": next(
                request["response_sha256"]
                for request in receipt["requests"]
                if request["name"] == "manual317"
            ),
        },
        "trace_policy_notice": (
            "Numeric trace values are explicit scenario realizations only. "
            "KNMI source semantics remain 0 <= trace < 0.05 mm."
        ),
        "observed_station273_rule": (
            "This package contains reconstruction candidates only for the 108 source-missing "
            "station-273 hours. Observed station-273 hours remain authoritative and are not overwritten."
        ),
        "uncertainty_rule": (
            "Valid station-specific timing reconstructions are retained as uncertainty members. "
            "The equal-valid-member ensemble is diagnostic and is not historical truth."
        ),
        "run_authorized": False,
        "dr_sm_initial_state_status_change": None,
        "windows": windows,
    }


def write_package(package: dict[str, Any], output_path: Path = DEFAULT_OUTPUT) -> bytes:
    data = (json.dumps(package, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)
    return data


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build the trace-aware Tollebeek antecedent precipitation-gap SCENARIO_ONLY candidate package."
    )
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    package = build_package(args.source_dir)
    data = write_package(package, args.output)
    print(f"Wrote {args.output} ({len(data)} bytes, sha256={sha256_bytes(data)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
