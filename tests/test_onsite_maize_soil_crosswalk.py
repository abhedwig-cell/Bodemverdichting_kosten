from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from build_onsite_maize_soil_crosswalk import (
    is_target_brp_record,
    mapping_coverage,
    validate_mapping_rows,
)
from validate_onsite_maize_crosswalk import validate


class OnsiteMaizeSoilCrosswalkTests(unittest.TestCase):
    def test_design_contract_integrity(self):
        self.assertEqual(validate(), [])

    def test_target_brp_semantics(self):
        self.assertTrue(
            is_target_brp_record(
                {
                    "gewascode": 259,
                    "jaar": 2025,
                    "status": "Definitief",
                }
            )
        )
        self.assertFalse(
            is_target_brp_record(
                {
                    "gewascode": 259,
                    "jaar": 2024,
                    "status": "Definitief",
                }
            )
        )

    def test_mapping_is_fail_closed(self):
        rows = [
            {
                "soil_unit_code": "EXAMPLE_A",
                "ccnl6_class": "ZO",
                "mapping_basis": "reviewed example",
                "mapping_status": "QUALIFIED",
            },
            {
                "soil_unit_code": "EXAMPLE_B",
                "ccnl6_class": "ZE",
                "mapping_basis": "",
                "mapping_status": "REVIEW_REQUIRED",
            },
        ]
        self.assertEqual(validate_mapping_rows(rows), [])
        missing, unqualified = mapping_coverage(
            ["EXAMPLE_A", "EXAMPLE_B", "EXAMPLE_C"],
            rows,
        )
        self.assertEqual(missing, ["EXAMPLE_C"])
        self.assertEqual(unqualified, ["EXAMPLE_B"])

    def test_review_required_mapping_may_remain_unclassified(self):
        rows = [
            {
                "soil_unit_code": "AMBIGUOUS",
                "ccnl6_class": "",
                "mapping_basis": "",
                "mapping_status": "REVIEW_REQUIRED",
            }
        ]
        self.assertEqual(validate_mapping_rows(rows), [])
        missing, unqualified = mapping_coverage(["AMBIGUOUS"], rows)
        self.assertEqual(missing, [])
        self.assertEqual(unqualified, ["AMBIGUOUS"])

    def test_invalid_qualified_mapping_requires_basis(self):
        errors = validate_mapping_rows(
            [
                {
                    "soil_unit_code": "EXAMPLE",
                    "ccnl6_class": "ZO",
                    "mapping_basis": "",
                    "mapping_status": "QUALIFIED",
                }
            ]
        )
        self.assertTrue(any("requires mapping_basis" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
