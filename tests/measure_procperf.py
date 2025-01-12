import os
import sys
import json
sys.path.append(os.path.dirname(__file__))
from command import *
sys.path.append(os.path.join(os.path.dirname(__file__), "../src/perfait/scripts/perfait_scripts"))
from measure_command import *

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

def versions(args):
  return capture_command(args).stdout.rstrip().split()

def proglang_version(proglang):
  match proglang:
    case "cpp":
      args = ["g++", "-dumpversion"]
      return " ".join([args[0], versions(args)[0]])
    case "python":
      args = ["python3", "-V"]
      return versions(args)[-1]
    case "csharp":
      args = ["mcs", "--version"]
      return " ".join([args[0], versions(args)[-1]])
    case "go":
      args = ["go", "version"]
      return versions(args)[2][2:]
    case "ruby":
      args = ["ruby", "--version"]
      return versions(args)[1]
    case "php":
      args = ["php", "--version"]
      return versions(args)[1]
    case "javascript":
      args = ["node", "-v"]
      return " ".join([args[0], versions(args)[0][1:]])
    case "java":
      args = ["java", "--version"]
      return " ".join(versions(args)[0:2])
    case _:
      return "?"

os.chdir(os.path.join(os.path.dirname(__file__), "procperf"))
perfait = {
  "Tick": {"Dtick": 200, "Format": "d"},
  "LayoutTitleText": "<b>[procperf]<br>Measurement of 100 million increments</b>",
  "XTitleText": "Elapsed time(ms)",
  "YTitleText": "Programming language",
  "Array": [],
}
for proglang in procperfConfig.keys():
  proglang_prepare(proglang)
  measure = measure_command(5, procperfConfig[proglang])
  if 0 < len(measure["stderr"]):
    sys.exit("""\033[40m\033[31m{}\033[0m""".format(measure["stderr"]))
  internalElapsedTime = int(measure["internalElapsedTime"] * 1000)
  externalElapsedTime = int(measure["externalElapsedTime"] * 1000)
  perfait["Array"].append(["""{}<br>({})""".format(proglang, proglang_version(proglang)), internalElapsedTime, externalElapsedTime, internalElapsedTime + externalElapsedTime])
perfait["Array"].sort(key = lambda value: value[1])
perfait["Array"].insert(0 , ["", "Internal", "External", "Total"])
filePath = "../../images/procperf.json"
os.makedirs(os.path.dirname(filePath), exist_ok = True)
with open(filePath, "w", encoding = "utf-8", newline = "\n") as file:
  json.dump(perfait, file, indent = 2)
