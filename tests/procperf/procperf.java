package perfait;
import perfait.*;

class Procperf {
  static public void main(String[] args){
    var stopwatch = new perfait.Stopwatch();
    for (int i = 0; i < 100000000; ++i){}
    var elapsedTime = stopwatch.elapsed_time();
    System.out.printf("%.6f\n", elapsedTime);
  }
}
