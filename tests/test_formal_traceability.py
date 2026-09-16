from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_formal_traceability import validate


class FormalTraceabilityTests(unittest.TestCase):
    def test_register_integrity(self):
        self.assertEqual(validate(), [])

    def test_equation_register_contains_core_identities(self):
        text = (ROOT / "model" / "equations.csv").read_text(encoding="utf-8")
        for equation_id in (
            "EQ_ATTRIBUTION_DELTA",
            "EQ_GENERATED_VOLUME",
            "EQ_ASSIST_ALLOCATION",
            "EQ_PUMP_ENERGY",
            "EQ_DIRECT_PUMP_COST",
        ):
            self.assertIn(equation_id, text)

    def test_no_mature_status_hides_key_tollebeek_data_gates(self):
        text = (ROOT / "model" / "traceability.csv").read_text(encoding="utf-8")
        self.assertIn("CAP_K_CAP", text)
        self.assertIn("Post-2020 current Q-H/operational capacity is missing", text)
        self.assertIn("CAP_ATTRIB", text)
        self.assertIn("Current depth-resolved Tollebeek current/reference states are not admitted", text)


if __name__ == "__main__":
    unittest.main()
