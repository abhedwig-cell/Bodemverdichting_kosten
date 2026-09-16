from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUEST_FILE = ROOT / "data_requests" / "data_request_register.csv"
EVIDENCE_FILE = ROOT / "evidence" / "evidence_register.csv"
CLAIMS_FILE = ROOT / "evidence" / "claims.csv"
TRACEABILITY_FILE = ROOT / "model" / "traceability.csv"
DRAINAGE_CONFIG_FILE = ROOT / "data" / "water" / "tollebeek_drainage_configuration.csv"

REQUIRED_ROUTE_EVIDENCE = {
    "EV_TOL_DRAINAGE_OWNER_COVERAGE",
    "EV_TOL_DRAINAGE_LEGGER_TOPOLOGY",
}
REQUIRED_GATE_CLAIM = "CL_TOL_DRAINAGE_GATE"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


def validate() -> list[str]:
    errors: list[str] = []

    requests = {row["data_request_id"]: row for row in read_csv(REQUEST_FILE)}
    request = requests.get("DR_SM_DRAINAGE")
    if request is None:
        return ["missing DR_SM_DRAINAGE readiness item"]

    evidence_ids = {row["evidence_id"] for row in read_csv(EVIDENCE_FILE)}
    claim_ids = {row["claim_id"] for row in read_csv(CLAIMS_FILE)}

    missing_evidence = REQUIRED_ROUTE_EVIDENCE - evidence_ids
    if missing_evidence:
        errors.append(f"missing drainage route evidence: {sorted(missing_evidence)}")

    missing_links = REQUIRED_ROUTE_EVIDENCE - split_ids(request["current_evidence_ids"])
    if missing_links:
        errors.append(f"DR_SM_DRAINAGE missing required route evidence links: {sorted(missing_links)}")

    if REQUIRED_GATE_CLAIM not in claim_ids:
        errors.append(f"missing drainage gate claim: {REQUIRED_GATE_CLAIM}")
    if REQUIRED_GATE_CLAIM not in split_ids(request["current_claim_ids"]):
        errors.append("DR_SM_DRAINAGE is not linked to CL_TOL_DRAINAGE_GATE")

    status = request["input_readiness_status"]
    if status == "ADMITTED" and not DRAINAGE_CONFIG_FILE.exists():
        errors.append(
            "DR_SM_DRAINAGE cannot be ADMITTED without a canonical Tollebeek drainage configuration dataset"
        )
    if status != "ADMITTED" and DRAINAGE_CONFIG_FILE.exists():
        errors.append(
            "canonical Tollebeek drainage configuration exists while DR_SM_DRAINAGE is not ADMITTED"
        )

    if status == "PARTIAL_EVIDENCE":
        boundary = " ".join(
            [request["blocking_reason"], request["next_action"], request["request_notes"]]
        ).lower()
        for phrase in ("spacing", "depth", "resistance"):
            if phrase not in boundary:
                errors.append(
                    f"DR_SM_DRAINAGE partial-evidence boundary must retain {phrase!r} context"
                )
        if not any(marker in boundary for marker in ("spacing 0", "sentinel", "unavailable")):
            errors.append(
                "DR_SM_DRAINAGE partial-evidence boundary must preserve that owner spacing 0 is not a physical zero"
            )

    trace = {row["capability_id"]: row for row in read_csv(TRACEABILITY_FILE)}
    capability = trace.get("CAP_MULTI_DRAIN")
    if capability is None:
        errors.append("missing CAP_MULTI_DRAIN traceability row")
    else:
        if status != "ADMITTED" and capability["capability_status"] != "DATA_GATED":
            errors.append("CAP_MULTI_DRAIN must remain DATA_GATED while DR_SM_DRAINAGE is not ADMITTED")
        links = split_ids(capability["evidence_or_claim_ids"])
        for item in REQUIRED_ROUTE_EVIDENCE | {REQUIRED_GATE_CLAIM}:
            if item not in links:
                errors.append(f"CAP_MULTI_DRAIN traceability missing {item}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Tollebeek drainage gate validation FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Tollebeek drainage gate validation passed.")
    print(
        "Validated owner drainage-route evidence and the strict boundary between drainage inventory/topology "
        "and an admitted source-model drainage configuration."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
