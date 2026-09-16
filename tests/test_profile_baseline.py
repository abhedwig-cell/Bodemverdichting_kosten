from __future__ import annotations

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_profile_baseline import validate


class ProfileBaselineContractTests(unittest.TestCase):
    def test_profile_baseline_has_no_integrity_errors(self) -> None:
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
