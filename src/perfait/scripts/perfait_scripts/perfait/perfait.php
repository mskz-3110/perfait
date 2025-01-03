<?php
namespace perfait;

class Stopwatch {
  static private function __get_time(){
    $nowTime = hrtime();
    return (double)$nowTime[0] + ((double)$nowTime[1] / 1000000000);
  }

  private $__StartTime;

  function __construct(){
    $this->start();
  }

  public function start(){
    $this->__StartTime = Stopwatch::__get_time();
  }

  public function stop(){
    return Stopwatch::__get_time() - $this->__StartTime;
  }
}

class Perfait {
  static public function measure($onProcess){
    $stopwatch = new Stopwatch();
    $onProcess();
    printf("%.6f\n", $stopwatch->stop());
  }
}
?>
