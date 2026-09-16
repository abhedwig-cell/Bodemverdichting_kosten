from __future__ import annotations
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; TOOLS=ROOT/'tools'
if str(TOOLS) not in sys.path: sys.path.insert(0,str(TOOLS))
from validate_initial_state_gate import validate
class InitialStateGateTests(unittest.TestCase):
    def test_initial_state_gate_integrity(self): self.assertEqual([],validate())
if __name__=='__main__': unittest.main()
