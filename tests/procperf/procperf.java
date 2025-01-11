package perfait;
import perfait.*;

class Procperf {
  static public void main(String[] args){
    var stopwatch = new perfait.Stopwatch();
    for (int i = 0; i < 100000000; ++i){}
    System.out.printf("%.6f\n", stopwatch.stop());
  }
}
