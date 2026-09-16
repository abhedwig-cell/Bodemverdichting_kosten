from __future__ import annotations

import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUEST_FILE = ROOT / "data_requests" / "data_request_register.csv"
EVIDENCE_FILE = ROOT / "evidence" / "evidence_register.csv"
CLAIMS_FILE = ROOT / "evidence" / "claims.csv"
PROFILE_SCHEMA = ROOT / "schema" / "profile_fields_v0_1.yml"
CORE_SCHEMA = ROOT / "schema" / "fields.yml"
CURRENT_STATE_FILE = ROOT / "data" / "soil" / "tollebeek_current_soil_states.csv"

REQUIRED_ROUTE_EVIDENCE = {
    "EV_FLEVO_COMPACTION_FIELD_PROTOCOL",
    "EV_FLEVO_COMPACTION_MAP_LIMIT",
    "EV_FLEVO_COMPACTION_DATASET_ROUTE",
}
REQUIRED_GATE_CLAIM = "CL_TOL_CURRENT_STATE_GATE"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


def validate() -> list[str]:
    errors: list[str] = []

    requests = {row["data_request_id"]: row for row in read_csv(REQUEST_FILE)}
    request = requests.get("DR_SM_CURRENT_STATE")
    if request is None:
        return ["missing DR_SM_CURRENT_STATE readiness item"]

    evidence_ids = {row["evidence_id"] for row in read_csv(EVIDENCE_FILE)}
    claim_ids = {row["claim_id"] for row in read_csv(CLAIMS_FILE)}

    missing_evidence = REQUIRED_ROUTE_EVIDENCE - evidence_ids
    if missing_evidence:
        errors.append(f"missing current-state route evidence: {sorted(missing_evidence)}")

    linked_evidence = split_ids(request["current_evidence_ids"])
    missing_links = REQUIRED_ROUTE_EVIDENCE - linked_evidence
    if missing_links:
        errors.append(
            f"DR_SM_CURRENT_STATE missing required route evidence links: {sorted(missing_links)}"
        )

    if REQUIRED_GATE_CLAIM not in claim_ids:
        errors.append(f"missing current-state gate claim: {REQUIRED_GATE_CLAIM}")
    if REQUIRED_GATE_CLAIM not in split_ids(request["current_claim_ids"]):
        errors.append("DR_SM_CURRENT_STATE is not linked to CL_TOL_CURRENT_STATE_GATE")

    profile_fields = yaml.safe_load(PROFILE_SCHEMA.read_text(encoding="utf-8"))["fields"]
    core_fields = yaml.safe_load(CORE_SCHEMA.read_text(encoding="utf-8"))["fields"]
    if profile_fields["modal_bulk_density_g_cm3"].get("entity") != "soil_layer":
        errors.append("modal_bulk_density_g_cm3 must remain soil-layer profile context")
    if core_fields["bulk_density_g_cm3"].get("entity") != "soil_state":
        errors.append("bulk_density_g_cm3 must remain a soil_state variable")

    status = request["input_readiness_status"]
    if status == "ADMITTED" and not CURRENT_STATE_FILE.exists():
        errors.append(
            "DR_SM_CURRENT_STATE cannot be ADMITTED without a canonical current-state dataset"
        )
    if status != "ADMITTED" and CURRENT_STATE_FILE.exists():
        errors.append(
            "canonical Tollebeek current-state data exist while DR_SM_CURRENT_STATE is not ADMITTED"
        )

    if status == "PARTIAL_EVIDENCE":
        notes = " ".join(
            [request["blocking_reason"], request["next_action"], request["request_notes"]]
        ).lower()
        for phrase in ("raw", "coordinate", "2020", "modal"):
            if phrase not in notes:
                errors.append(
                    f"DR_SM_CURRENT_STATE partial-evidence boundary must retain {phrase!r} context"
                )

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Tollebeek current-state gate validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Tollebeek current-state gate validation passed.")
    print(
        "Validated the measured-data acquisition route, evidence links and the strict boundary "
        "between modal profile context and an admitted CURRENT soil state."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
