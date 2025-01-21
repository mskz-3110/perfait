import perfait

stopwatch = perfait.Stopwatch()
for _ in range(100000000): pass
elapsedTime = stopwatch.elapsed_time()
print("""{:.6f}""".format(elapsedTime))
