"""Synthetic static scenario comparison for bounded transfer dispatch.

SOFTWARE_QA_ONLY. These numbers are invented test fixtures, not Tollebeek
observations or qualified compaction-related runoff.
"""
import math
import unittest

from src.water_system.dispatch import two_zone_two_pump_dispatch
from src.water_system.energy import pump_energy_kwh


def scenario(primary, secondary, availability=1.0):
    return two_zone_two_pump_dispatch(
        primary_zone_volume_m3=primary,
        assist_zone_volume_m3=secondary,
        assist_fraction_to_primary=0.25,
        primary_installed_capacity_m3_min=100.0,
        secondary_installed_capacity_m3_min=40.0,
        primary_availability_fraction=availability,
        secondary_availability_fraction=availability,
        response_window_h=12.0,
    )


class SyntheticIncrementTests(unittest.TestCase):
    def test_no_increment_means_no_dispatch_difference(self):
        baseline = scenario(6000.0, 2400.0)
        repeat = scenario(6000.0, 2400.0)
        self.assertEqual(baseline, repeat)
        self.assertEqual(repeat.primary_total_volume_m3 - baseline.primary_total_volume_m3, 0)
        self.assertEqual(repeat.assist_zone_volume_to_secondary_m3 - baseline.assist_zone_volume_to_secondary_m3, 0)

    def test_increment_preserves_routed_mass(self):
        baseline = scenario(6000.0, 2400.0)
        increased = scenario(6600.0, 2700.0)
        for case, p, s in ((baseline, 6000, 2400), (increased, 6600, 2700)):
            self.assertAlmostEqual(
                case.primary_total_volume_m3 + case.assist_zone_volume_to_secondary_m3,
                p + s,
            )
        self.assertAlmostEqual(
            increased.primary_total_volume_m3 - baseline.primary_total_volume_m3
            + increased.assist_zone_volume_to_secondary_m3
            - baseline.assist_zone_volume_to_secondary_m3,
            900.0,
        )

    def test_availability_changes_hours_not_volume(self):
        full = scenario(6600.0, 2700.0, 1.0)
        half = scenario(6600.0, 2700.0, 0.5)
        self.assertEqual(full.primary_total_volume_m3, half.primary_total_volume_m3)
        self.assertEqual(full.assist_zone_volume_to_secondary_m3, half.assist_zone_volume_to_secondary_m3)
        self.assertAlmostEqual(half.primary_pump_hours, 2 * full.primary_pump_hours)
        self.assertAlmostEqual(half.secondary_pump_hours, 2 * full.secondary_pump_hours)

    def test_energy_difference_only_under_explicit_assumptions(self):
        baseline = scenario(6000.0, 2400.0)
        increased = scenario(6600.0, 2700.0)
        delta_primary = increased.primary_total_volume_m3 - baseline.primary_total_volume_m3
        delta_secondary = increased.assist_zone_volume_to_secondary_m3 - baseline.assist_zone_volume_to_secondary_m3
        energy = pump_energy_kwh(delta_primary, 1.5, 0.75) + pump_energy_kwh(delta_secondary, 1.2, 0.70)
        expected = (1000 * 9.80665 / 3.6e6) * (
            delta_primary * 1.5 / 0.75 + delta_secondary * 1.2 / 0.70
        )
        self.assertTrue(math.isclose(energy, expected, rel_tol=1e-12))
        self.assertGreater(energy, 0)


if __name__ == "__main__":
    unittest.main()
