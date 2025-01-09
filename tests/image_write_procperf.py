import os
import sys
import json
import time
import gc
sys.path.append(os.path.dirname(__file__))
from command import *

if "PERFAIT_PATH" not in os.environ:
  os.environ["PERFAIT_PATH"] = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/perfait/scripts/perfait_scripts/perfait"))

procperfConfig = dict(
  cpp = ["./procperf_cpp"],
  python = ["python3", "./procperf.py"],
  csharp = ["mono", "./procperf_cs"],
  go = ["go", "run", "./procperf.go"],
  ruby = ["ruby", "-I", os.environ["PERFAIT_PATH"], "./procperf.rb"],
  php = ["php", "-c", ".", "./procperf.php"],
  javascript = ["node", "./procperf.js"],
  java = ["java", "perfait.Procperf"],
)

def proglang_prepare(proglang):
  perfaitPath = os.environ["PERFAIT_PATH"]
  match proglang:
    case "cpp":
      command(["g++", "-o", "procperf_cpp", "-I", perfaitPath, "procperf.cpp"])
    case "csharp":
      command(["mcs", "-out:procperf_cs", "./procperf.cs", os.path.join(perfaitPath, "perfait.cs")])
    case "java":
      command(["javac", os.path.join(perfaitPath, "perfait.java"), "./procperf.java", "-d", "."])
      command(["javac", "./procperf.java", "-d", "."])
    case "python":
      os.environ["PYTHONPATH"] = perfaitPath
    case "javascript":
      os.environ["NODE_PATH"] = perfaitPath

def proglang_version(proglang):
  match proglang:
    case "cpp":
      args = ["g++", "-dumpversion"]
      return " ".join([args[0], capture_command(args).stdout.rstrip().split()[0]])
    case "python":
      args = ["python3", "-V"]
      return capture_command(args).stdout.rstrip().split()[-1]
    case "csharp":
      args = ["mcs", "--version"]
      return " ".join([args[0], capture_command(args).stdout.rstrip().split()[-1]])
    case "go":
      args = ["go", "version"]
      return capture_command(args).stdout.rstrip().split()[2][2:]
    case "ruby":
      args = ["ruby", "--version"]
      return capture_command(args).stdout.rstrip().split()[1]
    case "php":
      args = ["php", "--version"]
      return capture_command(args).stdout.rstrip().split()[1]
    case "javascript":
      args = ["node", "-v"]
      return " ".join([args[0], capture_command(args).stdout.rstrip()[1:]])
    case "java":
      args = ["java", "--version"]
      versions = capture_command(args).stdout.rstrip().split()
      return " ".join([versions[0], versions[1]])
    case _:
      return "?"

def proglang_elapsed_times(args):
  elapsedTimes = []
  for _ in range(5):
    gc.collect()
    gc.disable()
    startTime = time.perf_counter()
    result = capture_command(args)
    stdout = result.stdout
    stderr = result.stderr
    elapsedTime = time.perf_counter() - startTime
    if 0 < len(stderr):
      sys.exit("""\033[40m\033[31m{}\033[0m""".format(stderr))
    print(stdout, end = "")
    internalElapsedTime = float(stdout)
    elapsedTimes.append([internalElapsedTime, elapsedTime - internalElapsedTime, elapsedTime])
    gc.enable()
  elapsedTimes.sort()
  return list(map(lambda elapsedTime: int(elapsedTime * 1000), elapsedTimes[int(len(elapsedTimes) / 2)]))

os.chdir(os.path.join(os.path.dirname(__file__), "procperf"))
for proglang in procperfConfig.keys():
  proglang_prepare(proglang)
pivotTableArray = []
for proglang in procperfConfig.keys():
  pivotTable = proglang_elapsed_times(procperfConfig[proglang])
  pivotTable.insert(0, """{}<br>({})""".format(proglang, proglang_version(proglang)))
  pivotTableArray.append(pivotTable)
pivotTableArray.sort(key = lambda performance: performance[1])
pivotTableArray.insert(0 , ["", "Internal", "External", "Total"])
filePath = "../../images/procperf.json"
os.makedirs(os.path.dirname(filePath), exist_ok = True)
with open(filePath, "w", encoding = "utf-8", newline = "\n") as file:
  json.dump(pivotTableArray, file, indent = 2)
