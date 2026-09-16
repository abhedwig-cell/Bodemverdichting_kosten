from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "build_tollebeek_antecedent_gap_scenarios.py"
SPEC = importlib.util.spec_from_file_location("gap_scenarios", TOOL_PATH)
assert SPEC is not None and SPEC.loader is not None
gap_scenarios = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gap_scenarios)

SOURCE_DIR = ROOT / "evidence" / "source_snapshots" / "tollebeek_antecedent_gap_v0_1"
MANIFEST = ROOT / "artifacts" / "scenarios" / "tollebeek_antecedent_gap_reconstruction_v0_1_manifest.json"


class AntecedentGapScenarioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.package = gap_scenarios.build_package(SOURCE_DIR)
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_source_receipt_and_gap_contract(self) -> None:
        receipt, raw = gap_scenarios.load_receipt(SOURCE_DIR)
        self.assertEqual(
            receipt["classification"],
            "ACQUIRED_SOURCE_NATIVE_NOT_YET_RECONSTRUCTED",
        )
        self.assertEqual(
            hashlib.sha256(raw["hourly"]).hexdigest(),
            "6076cfb910fa498daca93091e6fbbd361cbcd2a113b4518995ee817d2714c5bd",
        )
        self.assertEqual(
            hashlib.sha256(raw["manual317"]).hexdigest(),
            "eee4895db5f335a8ec7f82cf828a3d4adb965a26cbba0c111adc16029bbedc35",
        )
        self.assertEqual(self.package["gap_hour_count"], 108)
        self.assertFalse(self.package["run_authorized"])
        self.assertIsNone(self.package["dr_sm_initial_state_status_change"])

    def test_package_only_reconstructs_source_missing_gap_hours(self) -> None:
        all_timestamps: set[str] = set()
        expected = {
            gap_scenarios.iso_z(t)
            for t in gap_scenarios.hourly_range(
                gap_scenarios.GAP_START, gap_scenarios.GAP_END
            )
        }
        for window in self.package["windows"]:
            all_timestamps.update(window["gap_timestamps_utc"])
            for policy in window["trace_policy_results"]:
                for member in policy["station_members"]:
                    if member["status"] != "VALID_SCENARIO_MEMBER":
                        continue
                    values = member["reconstructed_mm_by_gap_timestamp"]
                    self.assertEqual(len(values), len(window["gap_timestamps_utc"]))
                    self.assertEqual(member["provenance"]["value_origin"], "reconstructed")
                    self.assertEqual(member["provenance"]["hour_axis"], "window.gap_timestamps_utc")
                    self.assertTrue(all(value >= 0.0 for value in values))
        self.assertEqual(all_timestamps, expected)

    def test_mass_closure_and_no_hidden_fallback(self) -> None:
        invalid_pairs: set[tuple[str, str, str]] = set()
        for window in self.package["windows"]:
            for policy in window["trace_policy_results"]:
                residual = policy["residual_mass_mm_under_trace_policy"]
                for member in policy["station_members"]:
                    if member["status"] == "INVALID":
                        invalid_pairs.add(
                            (
                                window["report_date"],
                                policy["trace_policy"],
                                member["timing_source_station"],
                            )
                        )
                        self.assertIn("failure_reason", member)
                        self.assertNotIn("reconstructed_mm_by_gap_timestamp", member)
                        continue
                    total = sum(member["reconstructed_mm_by_gap_timestamp"])
                    self.assertAlmostEqual(total, residual, places=6)

                ensemble_values = policy["ensemble"]["reconstructed_mm_by_gap_timestamp"]
                total = sum(ensemble_values)
                self.assertAlmostEqual(total, residual, places=6)

        self.assertIn(("19980907", "TRACE_BOUND_LOWER", "279"), invalid_pairs)
        self.assertIn(("19980908", "TRACE_BOUND_LOWER", "267"), invalid_pairs)
        self.assertIn(("19980908", "TRACE_BOUND_LOWER", "269"), invalid_pairs)

    def test_trace_uncertainty_is_explicit(self) -> None:
        policies = {
            result["trace_policy"]
            for window in self.package["windows"]
            for result in window["trace_policy_results"]
        }
        self.assertEqual(policies, set(gap_scenarios.TRACE_POLICIES))
        self.assertIn("scenario realizations", self.package["trace_policy_notice"])
        trace_windows = [
            window
            for window in self.package["windows"]
            if window["station273_retained_mass_enclosure"]["trace_count"] > 0
        ]
        self.assertTrue(trace_windows)
        self.assertTrue(
            all(
                window["residual_mass_enclosure"][
                    "lower_is_open_when_retained_trace_count_positive"
                ]
                for window in trace_windows
            )
        )

    def test_generated_package_matches_manifest_hash(self) -> None:
        expected_bytes = (
            json.dumps(
                self.package,
                indent=2,
                sort_keys=True,
                ensure_ascii=False,
            )
            + "\n"
        ).encode("utf-8")
        generated = self.manifest["generated_package"]
        self.assertEqual(len(expected_bytes), generated["bytes"])
        self.assertEqual(hashlib.sha256(expected_bytes).hexdigest(), generated["sha256"])
        self.assertFalse(generated["committed"])
        self.assertEqual(self.manifest["classification"], self.package["classification"])


if __name__ == "__main__":
    unittest.main()
