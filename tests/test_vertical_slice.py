"""Software tests for the bounded source -> dispatch vertical slice.

All numerical fixtures are synthetic software QA unless the test says otherwise.
Passing these tests does not qualify Tollebeek hydrology or pump operation.
"""

import math
import unittest

from src.transfer.volume import generated_increment_m3
from src.water_system.dispatch import two_zone_two_pump_dispatch
from src.water_system.energy import pump_energy_kwh


class SourceVolumeTests(unittest.TestCase):
    def test_generated_volume_identity(self):
        self.assertEqual(generated_increment_m3(100.0, 10.0), 10000.0)

    def test_unknown_stays_unknown(self):
        self.assertIsNone(generated_increment_m3(None, 10.0))
        self.assertIsNone(generated_increment_m3(100.0, None))

    def test_negative_area_rejected(self):
        with self.assertRaises(ValueError):
            generated_increment_m3(-1.0, 1.0)


class DispatchTests(unittest.TestCase):
    def test_no_hidden_assist_default(self):
        r = two_zone_two_pump_dispatch(
            primary_zone_volume_m3=100000.0,
            assist_zone_volume_m3=20000.0,
            assist_fraction_to_primary=None,
            primary_installed_capacity_m3_min=540.0,
            secondary_installed_capacity_m3_min=60.0,
            primary_availability_fraction=1.0,
            secondary_availability_fraction=1.0,
            response_window_h=24.0,
        )
        self.assertEqual(r.status, "WAIT_ASSIST_OR_ROUTED_VOLUME")
        self.assertIsNone(r.primary_total_volume_m3)
        self.assertIsNone(r.primary_pump_hours)

    def test_explicit_assist_allocation(self):
        r = two_zone_two_pump_dispatch(
            primary_zone_volume_m3=100000.0,
            assist_zone_volume_m3=20000.0,
            assist_fraction_to_primary=0.5,
            primary_installed_capacity_m3_min=540.0,
            secondary_installed_capacity_m3_min=60.0,
            primary_availability_fraction=1.0,
            secondary_availability_fraction=1.0,
            response_window_h=24.0,
        )
        self.assertEqual(r.assist_zone_volume_to_primary_m3, 10000.0)
        self.assertEqual(r.assist_zone_volume_to_secondary_m3, 10000.0)
        self.assertEqual(r.primary_total_volume_m3, 110000.0)
        self.assertTrue(math.isclose(r.primary_pump_hours, 110000.0/(540.0*60.0)))
        self.assertTrue(math.isclose(r.secondary_pump_hours, 10000.0/(60.0*60.0)))

    def test_fraction_bounds(self):
        with self.assertRaises(ValueError):
            two_zone_two_pump_dispatch(
                primary_zone_volume_m3=1.0,
                assist_zone_volume_m3=1.0,
                assist_fraction_to_primary=1.1,
                primary_installed_capacity_m3_min=1.0,
                secondary_installed_capacity_m3_min=1.0,
            )


class EnergyTests(unittest.TestCase):
    def test_missing_operating_point_stays_unknown(self):
        self.assertIsNone(pump_energy_kwh(1000.0, None, 0.7))
        self.assertIsNone(pump_energy_kwh(1000.0, 1.4, None))

    def test_energy_identity(self):
        expected = 1000.0 * 9.80665 * 1.4 * 1000.0 / (0.7 * 3.6e6)
        self.assertTrue(math.isclose(
            pump_energy_kwh(1000.0, 1.4, 0.7),
            expected,
            rel_tol=1e-12,
        ))


if __name__ == "__main__":
    unittest.main()
