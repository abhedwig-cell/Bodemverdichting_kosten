from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_architecture_contract import validate


class ArchitectureContractTests(unittest.TestCase):
    def test_architecture_contract_integrity(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
