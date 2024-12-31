import os
import sys
import json
sys.path.append(os.path.dirname(__file__))
from command import *

def proglang_build(proglang):
  match proglang:
    case "cpp":
      command(["g++", "-o", "procperf_cpp", "-I", "../../perfait_scripts/perfait", "procperf.cpp"])
    case "csharp":
      command(["mcs", "-out:procperf_cs", "./procperf.cs", "../../perfait_scripts/perfait/perfait.cs"])
    case "java":
      command(["javac", "../../perfait_scripts/perfait/perfait.java", "./procperf.java", "-d", "."])
      command(["javac", "./procperf.java", "-d", "."])

def proglang_elapsed_time(args, maxTimes):
  elapsedTimes = []
  for _ in range(maxTimes):
    stdout = capture_command(args).stdout
    print(stdout, end = "")
    elapsedTimes.append(float(stdout))
  elapsedTimes.sort()
  return int(elapsedTimes[int(len(elapsedTimes) / 2)] * 1000)

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

maxTimes = 5
procperfConfig = dict(
  cpp = ["./procperf_cpp"],
  python = ["python3", "./procperf.py"],
  csharp = ["mono", "./procperf_cs"],
  go = ["go", "run", "./procperf.go"],
  ruby = ["ruby", "./procperf.rb"],
  php = ["php", "./procperf.php"],
  javascript = ["node", "./procperf.js"],
  java = ["java", "perfait.Procperf"],
)
os.chdir(os.path.join(os.path.dirname(__file__), "../src/perfait/scripts/perfait_tests/procperf"))
for proglang in procperfConfig.keys():
  proglang_build(proglang)
pivotTableArray = []
for proglang in procperfConfig.keys():
  pivotTableArray.append(["""{}<br>({})""".format(proglang, proglang_version(proglang)), proglang_elapsed_time(procperfConfig[proglang], maxTimes)])
pivotTableArray.sort(key = lambda performance: performance[1])
pivotTableArray.insert(0 , ["", "Elapsed time(ms)"])
filePath = "../../../../../images/procperf.json"
os.makedirs(os.path.dirname(filePath), exist_ok = True)
with open(filePath, "w", encoding = "utf-8", newline = "\n") as file:
  json.dump(pivotTableArray, file, indent = 2)
