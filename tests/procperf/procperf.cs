public class Procperf {
  static void Main(string[] argv){
    var stopwatch = new Perfait.Stopwatch();
    for (int i = 0; i < 100000000; ++i){}
    System.Console.WriteLine($"{stopwatch.Stop():F6}");
  }
}
