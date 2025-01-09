public class Procperf {
  static void OnProcess(){
    for (int i = 0; i < 100000000; ++i){}
  }

  static void Main(string[] argv){
      System.Console.WriteLine($"{perfait.Perfait.Measure(OnProcess):F6}");
  }
}
