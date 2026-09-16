from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_project import REQUIRED_PATHS, validate


class ProjectIntegrityTests(unittest.TestCase):
    def test_project_integrity_gate(self):
        self.assertEqual(validate(), [])

    def test_required_paths_are_unique(self):
        self.assertEqual(len(REQUIRED_PATHS), len(set(REQUIRED_PATHS)))


if __name__ == "__main__":
    unittest.main()
