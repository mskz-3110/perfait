using System;
using System.Diagnostics;

namespace perfait {
  public class Perfait {
    public delegate void ProcessEvent();

    static public double Measure(ProcessEvent onProcess){
      var stopwatch = new Stopwatch();
      stopwatch.Start();
      onProcess();
      stopwatch.Stop();
      return stopwatch.Elapsed.TotalSeconds;
    }
  }
}
