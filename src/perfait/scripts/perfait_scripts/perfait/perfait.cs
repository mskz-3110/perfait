using System;
using System.Diagnostics;

namespace perfait {
  public class Perfait {
    public delegate void ProcessEvent();

    static public void Measure(ProcessEvent onProcess){
      var stopwatch = new Stopwatch();
      stopwatch.Start();
      onProcess();
      stopwatch.Stop();
      Console.WriteLine($"{stopwatch.Elapsed.TotalSeconds:F6}");
    }
  }
}
