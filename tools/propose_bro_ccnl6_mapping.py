from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable


RULE_COLUMNS = {
    "priority",
    "family_token",
    "candidate_ccnl6_class",
    "proposal_status",
    "rule_basis",
    "notes",
}
VALID_CLASSES = {"ZE", "ZO", "K", "L", "M", "V"}
VALID_STATUSES = {"AUTO_PROPOSAL", "REVIEW_REQUIRED"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def validate_rules(rows: Iterable[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for i, row in enumerate(rows, start=2):
        token = (row.get("family_token") or "").strip()
        klass = (row.get("candidate_ccnl6_class") or "").strip()
        status = (row.get("proposal_status") or "").strip()
        basis = (row.get("rule_basis") or "").strip()
        try:
            int((row.get("priority") or "").strip())
        except ValueError:
            errors.append(f"row {i}: invalid priority")
        if not token:
            errors.append(f"row {i}: blank family_token")
        if token in seen:
            errors.append(f"row {i}: duplicate family_token {token}")
        seen.add(token)
        if status not in VALID_STATUSES:
            errors.append(f"row {i}: invalid proposal_status {status!r}")
        if klass and klass not in VALID_CLASSES:
            errors.append(f"row {i}: invalid candidate class {klass!r}")
        if status == "AUTO_PROPOSAL" and not klass:
            errors.append(f"row {i}: AUTO_PROPOSAL requires candidate class")
        if not basis:
            errors.append(f"row {i}: rule_basis is blank")
    if "UNKNOWN" not in seen:
        errors.append("rules must include UNKNOWN fallback")
    return errors


def strip_leading_modifiers(code: str) -> str:
    code = code.strip()
    i = 0
    while i < len(code) and code[i].islower():
        i += 1
    return code[i:]


def select_rule(code: str, rules: list[dict[str, str]]) -> dict[str, str]:
    core = strip_leading_modifiers(code)
    ordered = sorted(
        [row for row in rules if row["family_token"].strip() != "UNKNOWN"],
        key=lambda row: (
            int(row["priority"]),
            -len(row["family_token"].strip()),
        ),
    )
    # Priority is authoritative. Tokens are written so more-specific families
    # have a lower priority number than their generic parents.
    for row in ordered:
        token = row["family_token"].strip()
        if core.startswith(token):
            return row
    return next(row for row in rules if row["family_token"].strip() == "UNKNOWN")


def propose_record(
    record: dict[str, str],
    rules: list[dict[str, str]],
) -> dict[str, str]:
    code = (record.get("soil_unit_code") or "").strip()
    rule = select_rule(code, rules)
    return {
        "soil_unit_code": code,
        "soil_classification": (record.get("soil_classification") or "").strip(),
        "main_soil_classification": (
            record.get("main_soil_classification") or ""
        ).strip(),
        "candidate_ccnl6_class": (
            rule.get("candidate_ccnl6_class") or ""
        ).strip(),
        "proposal_rule": (rule.get("family_token") or "").strip(),
        "proposal_status": (rule.get("proposal_status") or "").strip(),
        "proposal_basis": (rule.get("rule_basis") or "").strip(),
        "review_notes": (rule.get("notes") or "").strip(),
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Generate review proposals for BRO soil_unit_code -> CC-NL6 mappings. "
            "Proposals never qualify mappings automatically."
        )
    )
    p.add_argument("--input", required=True, type=Path)
    p.add_argument(
        "--rules",
        type=Path,
        default=Path("config/bro_ccnl6_family_rules_v0_1.csv"),
    )
    p.add_argument("--output", required=True, type=Path)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    rules = read_csv(args.rules)
    errors = validate_rules(rules)
    if errors:
        for error in errors:
            print(f"ERROR: rule contract: {error}")
        return 2

    records = read_csv(args.input)
    required = {
        "soil_unit_code",
        "soil_classification",
        "main_soil_classification",
    }
    if records:
        missing = required - set(records[0])
        if missing:
            print(f"ERROR: input missing required columns {sorted(missing)}")
            return 2

    proposals = [propose_record(row, rules) for row in records]
    proposals.sort(key=lambda row: row["soil_unit_code"])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "soil_unit_code",
        "soil_classification",
        "main_soil_classification",
        "candidate_ccnl6_class",
        "proposal_rule",
        "proposal_status",
        "proposal_basis",
        "review_notes",
    ]
    with args.output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(proposals)

    auto = sum(1 for row in proposals if row["proposal_status"] == "AUTO_PROPOSAL")
    review = len(proposals) - auto
    print(f"Wrote {args.output}: {auto} auto proposals, {review} review-required")
    print("No proposal is scientifically qualified by this command.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
