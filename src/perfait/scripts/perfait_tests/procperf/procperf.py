import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../perfait_scripts/perfait"))
import perfait

def on_process():
  for _ in range(100000000): pass

perfait.Perfait.measure(on_process)
