from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUEST_FILE = ROOT / "data_requests" / "data_request_register.csv"
EVENT_FILE = ROOT / "data" / "events" / "tollebeek_events.csv"
FORCING_FILE = ROOT / "data" / "events" / "tollebeek_1998_marknesse_hourly.csv"
DATASETS_FILE = ROOT / "schema" / "datasets.yml"
RELATIONSHIPS_FILE = ROOT / "schema" / "relationships.yml"
EVIDENCE_FILE = ROOT / "evidence" / "evidence_register.csv"
CLAIMS_FILE = ROOT / "evidence" / "claims.csv"
EXPECTED_SHA = "6c4ca1277523af73f26f6340ec8ebce5d52f42b6040085f7d50ecc78c5ca3c8a"
EVENT_ID = "EVT_TOL_1998_OCT"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


def precip_mm(native: str) -> float:
    if native == "":
        raise ValueError("missing precipitation amount")
    value = int(native)
    return 0.0 if value == -1 else value / 10.0


def validate() -> list[str]:
    errors: list[str] = []
    requests = {row["data_request_id"]: row for row in read_csv(REQUEST_FILE)}
    request = requests.get("DR_SM_EVENT_FORCING")
    if request is None:
        return ["missing DR_SM_EVENT_FORCING"]
    if request["input_readiness_status"] != "ADMITTED":
        errors.append("DR_SM_EVENT_FORCING must be ADMITTED for the persisted 1998 baseline")
    for required in ("EV_TOL_1998_KNMI_FORCING", "EV_TOL_1998_OWNER_EVENT"):
        if required not in split_ids(request["current_evidence_ids"]):
            errors.append(f"event forcing readiness missing evidence {required}")
    if "CL_TOL_1998_EVENT_FORCING" not in split_ids(request["current_claim_ids"]):
        errors.append("event forcing readiness missing CL_TOL_1998_EVENT_FORCING")

    if not EVENT_FILE.exists() or not FORCING_FILE.exists():
        return errors + ["canonical event or forcing file is missing"]
    events = read_csv(EVENT_FILE)
    if len(events) != 1 or events[0].get("event_id") != EVENT_ID:
        errors.append("event register must contain exactly EVT_TOL_1998_OCT")
    else:
        event = events[0]
        expected = {
            "context_start_utc": "1998-10-24T00:00:00Z",
            "context_end_utc": "1998-10-30T00:00:00Z",
            "core_start_utc": "1998-10-27T06:00:00Z",
            "core_end_utc": "1998-10-28T06:00:00Z",
            "source_station_id": "273",
            "timezone": "UTC",
            "temporal_resolution_minutes": "60",
            "forcing_dataset_sha256": EXPECTED_SHA,
        }
        for key, value in expected.items():
            if event.get(key) != value:
                errors.append(f"event {key}={event.get(key)!r} != {value!r}")

    digest = hashlib.sha256(FORCING_FILE.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA:
        errors.append(f"forcing file SHA-256 {digest} != {EXPECTED_SHA}")
    rows = read_csv(FORCING_FILE)
    if len(rows) != 144:
        errors.append(f"forcing context has {len(rows)} rows, expected 144")
    ids = [row.get("forcing_observation_id", "") for row in rows]
    if len(ids) != len(set(ids)) or "" in ids:
        errors.append("forcing observation IDs must be nonblank and unique")
    if {row.get("event_id") for row in rows} != {EVENT_ID}:
        errors.append("forcing rows must all reference EVT_TOL_1998_OCT")
    if {row.get("source_station_id") for row in rows} != {"273"}:
        errors.append("forcing rows must all retain source station 273")
    if rows:
        if rows[0].get("interval_start_utc") != "1998-10-24T00:00:00Z":
            errors.append("forcing context start timestamp changed")
        if rows[-1].get("interval_end_utc") != "1998-10-30T00:00:00Z":
            errors.append("forcing context end timestamp changed")
        for left, right in zip(rows, rows[1:]):
            if left.get("interval_end_utc") != right.get("interval_start_utc"):
                errors.append("forcing intervals are not contiguous")
                break

    required_fields = [
        "wind_direction_deg", "wind_hourly_mean_0_1_ms", "wind_mean_0_1_ms", "wind_gust_0_1_ms",
        "air_temperature_0_1_c", "dewpoint_temperature_0_1_c", "sunshine_duration_0_1_h",
        "global_radiation_j_cm2", "precipitation_duration_0_1_h", "precipitation_amount_0_1_mm",
        "visibility_code", "relative_humidity_pct",
    ]
    for field in required_fields:
        if any(row.get(field, "") == "" for row in rows):
            errors.append(f"admitted forcing field has missing values: {field}")

    core = [
        row for row in rows
        if row.get("interval_start_utc", "") >= "1998-10-27T06:00:00Z"
        and row.get("interval_end_utc", "") <= "1998-10-28T06:00:00Z"
    ]
    if len(core) != 24:
        errors.append(f"event core has {len(core)} hourly rows, expected 24")
    else:
        amount = sum(precip_mm(row["precipitation_amount_0_1_mm"]) for row in core)
        if abs(amount - 88.4) > 1e-9:
            errors.append(f"event-core rainfall {amount} mm != 88.4 mm")

    if any(row.get("sea_level_pressure_0_1_hpa", "") != "" for row in rows):
        errors.append("station pressure was source-missing and must remain blank in this baseline")

    datasets = DATASETS_FILE.read_text(encoding="utf-8")
    relationships = RELATIONSHIPS_FILE.read_text(encoding="utf-8")
    if "meteorological_forcing_register:" not in datasets or "data/events/tollebeek_1998_marknesse_hourly.csv" not in datasets:
        errors.append("meteorological forcing dataset contract/storage is missing")
    if "event_forcing:" not in relationships or "meteorological_forcing_observation.event_id" not in relationships:
        errors.append("event-to-forcing relationship is missing")

    evidence = {row["evidence_id"] for row in read_csv(EVIDENCE_FILE)}
    claims = {row["claim_id"] for row in read_csv(CLAIMS_FILE)}
    if "EV_TOL_1998_KNMI_FORCING" not in evidence:
        errors.append("missing EV_TOL_1998_KNMI_FORCING")
    if "CL_TOL_1998_EVENT_FORCING" not in claims:
        errors.append("missing CL_TOL_1998_EVENT_FORCING")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Tollebeek event forcing gate validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Tollebeek event forcing gate validation passed.")
    print("Validated the admitted 1998 Marknesse hourly forcing context, event core, native missing/trace semantics and event-to-forcing data-model contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
