from pyemon import *
import graspgraph as gg

def test_procperf():
  Command(["docker", "compose", "run", "--rm", "debian", "python3", "/home/perfait/tests/procperf.py"]).run()
  pivotTableArray = Command.json_load("./images/procperf.json")
  pivotgraph = gg.Pivotgraph(gg.PivotgraphAxis(gg.PivotTable.from_array(pivotTableArray), gg.FigureTick(200)))
  figure = pivotgraph.to_figure()
  figure.LayoutTitleText = "<b>[procperf]<br>Processing measurement that increments 100 million times</b>"
  figure.XTitleText = "Elapsed time(ms)"
  figure.YTitleText = "Programming language"
  figure.Write("./images/procperf.png")
