package perfait;
import perfait.*;

class Procperf {
  static private void on_process(){
    for (int i = 0; i < 100000000; ++i){}
  }

  static public void main(String[] args){
    System.out.printf("%.6f\n", Perfait.measure(Procperf::on_process));
  }
}
