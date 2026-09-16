from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_domain_schema import validate


class DomainSchemaV03Tests(unittest.TestCase):
    def test_domain_schema_integrity(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
