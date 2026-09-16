from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_spatial_geometry import validate  # noqa: E402


class SpatialGeometryTests(unittest.TestCase):
    def test_admitted_ot02_geometry_contract(self) -> None:
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
