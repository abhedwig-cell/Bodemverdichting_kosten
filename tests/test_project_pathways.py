from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_project_pathways import validate


class ProjectPathwayTests(unittest.TestCase):
    def test_project_pathway_integrity(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
