import subprocess
import datetime
import os

def command(*args, **kwargs):
  commandString = args
  if type(args) is not str:
    commandString = " ".join(args[0])
  print("""\033[40m\033[32m[{}] {} $ {}\033[0m""".format(datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S"), os.getcwd(), commandString))
  return subprocess.run(*args, **kwargs)

def capture_command(*args, **kwargs):
  return command(*args, **(dict(capture_output = True, text = True, encoding = "utf-8") | kwargs))
