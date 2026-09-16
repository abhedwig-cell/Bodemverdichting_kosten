from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from validate_event_forcing_gate import validate  # noqa: E402


class EventForcingGateTests(unittest.TestCase):
    def test_event_forcing_gate_integrity(self) -> None:
        self.assertEqual([], validate())


if __name__ == "__main__":
    unittest.main()
