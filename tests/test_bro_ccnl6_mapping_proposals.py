from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from propose_bro_ccnl6_mapping import (
    propose_record,
    read_csv,
    select_rule,
    validate_rules,
)


class BroCcnl6ProposalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = read_csv(ROOT / "config" / "bro_ccnl6_family_rules_v0_1.csv")

    def test_rule_contract(self):
        self.assertEqual(validate_rules(self.rules), [])

    def proposal(self, code):
        return propose_record(
            {
                "soil_unit_code": code,
                "soil_classification": "example",
                "main_soil_classification": "example",
            },
            self.rules,
        )

    def test_unambiguous_family_proposals(self):
        expected = {
            "bEZ21": "ZE",
            "EL5": "L",
            "EK19": "K",
            "Hn23": "ZO",
            "cY21": "ZO",
            "pZn21": "ZO",
            "Zn50A": "ZO",
            "hVb": "V",
            "vWp": "M",
            "MOo02": "K",
            "ROb15": "K",
            "BLn6": "L",
            "BKn25": "K",
            "BZd23": "ZO",
            "pMn55A": "K",
            "Rn95C": "K",
            "Ldd6": "L",
        }
        for code, klass in expected.items():
            with self.subTest(code=code):
                row = self.proposal(code)
                self.assertEqual(row["candidate_ccnl6_class"], klass)
                self.assertEqual(row["proposal_status"], "AUTO_PROPOSAL")

    def test_ambiguous_families_require_review(self):
        for code in ["Snl3A", "MZ1", "FK2", "KM3", "BXX", "XYZ"]:
            with self.subTest(code=code):
                row = self.proposal(code)
                self.assertEqual(row["proposal_status"], "REVIEW_REQUIRED")


if __name__ == "__main__":
    unittest.main()
