package perfait;

class Stopwatch {
  static public double __get_time(){
    var nanoTime = (double)System.nanoTime();
    return nanoTime / 1000000000 + ((nanoTime % 1000000000) / 1000000000);
  }

  private double __StartTime;

  public Stopwatch(){
    this.start();
  }

  public void start(){
    this.__StartTime = Stopwatch.__get_time();
  }

  public double stop(){
    return Stopwatch.__get_time() - this.__StartTime;
  }
}

class Perfait {
  public interface ICallback {
    void OnProcess();
  }

  static public void measure(ICallback callback){
    var stopwatch = new Stopwatch();
    callback.OnProcess();
    System.out.printf("%.6f\n", stopwatch.stop());
  }
}
