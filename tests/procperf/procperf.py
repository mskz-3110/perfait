import perfait

def on_process():
  for _ in range(100000000): pass

print("""{:.6f}""".format(perfait.Perfait.measure(on_process)))
