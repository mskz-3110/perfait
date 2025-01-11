from pyemon import *

def test_procperf():
  Command(["docker", "compose", "run", "--rm", "debian", "python3", "/home/perfait/tests/measure_procperf.py"]).run()
  Command(["pipenv", "run", "python", "-m", "src.perfait.cli", "image.write", "images/procperf.json", "images/procperf.png"]).run()
