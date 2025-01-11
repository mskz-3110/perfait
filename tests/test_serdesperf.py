from pyemon import *

def test_serdesperf():
  Command(["docker", "compose", "run", "--rm", "debian", "python3", "/home/perfait/tests/measure_serdesperf.py"]).run()
  Command(["pipenv", "run", "python", "-m", "src.perfait.cli", "image.write", "images/serdesperf.json", "images/serdesperf.png"]).run()
