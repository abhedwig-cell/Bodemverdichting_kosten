from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_evidence import validate


def test_evidence_register_integrity():
    assert validate() == []
