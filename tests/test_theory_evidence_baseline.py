from __future__ import annotations

import csv
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"


def rows(name: str, key: str) -> dict[str, dict[str, str]]:
    with (EVIDENCE / name).open("r", encoding="utf-8", newline="") as f:
        return {row[key]: row for row in csv.DictReader(f)}


class TheoryEvidenceBaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = rows("sources.csv", "source_id")
        cls.evidence = rows("evidence_register.csv", "evidence_id")
        cls.claims = rows("claims.csv", "claim_id")
        cls.qualifications = rows("qualification_register.csv", "qualification_id")

    def test_core_theory_sources_are_registered(self):
        expected = {
            "SRC_KELLER2019",
            "SRC_GRAVES2015",
            "SRC_GROENENDIJK2017",
            "SRC_KUHLMAN2010",
            "SRC_ROMERO2026",
        }
        self.assertTrue(expected.issubset(self.sources))

    def test_reference_state_claim_keeps_contextual_guardrail(self):
        claim = self.claims["CL_THEORY_REFERENCE_CAUTION"]
        self.assertEqual(claim["qualification_status"], "QUALIFIED")
        self.assertIn("context", claim["guardrail"].lower())
        self.assertIn("EV_KELLER_REFERENCE_CONTROL", claim["evidence_ids"])
        self.assertIn("EV_GRAVES_COUNTERFACTUAL", claim["evidence_ids"])

    def test_case_runoff_remains_benchmark_only(self):
        evidence = self.evidence["EV_GROEN_LOCAL_RUNOFF"]
        self.assertEqual(evidence["evidence_status"], "BENCHMARK_ONLY")
        self.assertIn("not a universal", evidence["guardrail"].lower())
        self.assertIn("Tollebeek", evidence["guardrail"])

    def test_historical_cost_is_not_current_unit_cost(self):
        evidence = self.evidence["EV_KUHLMAN_EXPLORATORY_COST"]
        self.assertEqual(evidence["evidence_status"], "BENCHMARK_ONLY")
        self.assertIn("not a current unit cost", evidence["guardrail"].lower())

    def test_scale_transfer_claim_has_no_generic_factor(self):
        claim = self.claims["CL_THEORY_SCALE_TRANSFER"]
        self.assertIn("No generic", claim["guardrail"])
        self.assertEqual(claim["qualification_status"], "QUALIFIED")

    def test_romero_scenario_scope_is_limited(self):
        evidence = self.evidence["EV_ROMERO_SCENARIO_SPECIFIC"]
        self.assertEqual(evidence["evidence_status"], "QUALIFIED")
        self.assertIn("current Dutch", evidence["guardrail"])


if __name__ == "__main__":
    unittest.main()
