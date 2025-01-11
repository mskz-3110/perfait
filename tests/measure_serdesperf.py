import os
import sys
sys.path.append(os.path.dirname(__file__))
from command import *

os.chdir(os.path.join(os.path.dirname(__file__), "serdesperf"))
command(["protoc", "--csharp_out=.", "-I.", "SerdesProtobuf.proto"])
filePath = "../../images/serdesperf.json"
os.makedirs(os.path.dirname(filePath), exist_ok = True)
with open(filePath, "w", encoding = "utf-8", newline = "\n") as file:
  command(["dotnet", "dev-certs", "https", "--trust"])
  file.write(capture_command(["dotnet", "run", "-c", "Release"]).stdout)
