import perfait

stopwatch = perfait.Stopwatch()
for _ in range(100000000): pass
print("""{:.6f}""".format(stopwatch.stop()))
