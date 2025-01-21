public class Procperf {
  static void Main(string[] argv){
    var stopwatch = new Perfait.Stopwatch();
    for (int i = 0; i < 100000000; ++i){}
    var elapsedTime = stopwatch.ElapsedTime();
    System.Console.WriteLine($"{elapsedTime:F6}");
  }
}
