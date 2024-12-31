package main

import (
  "perfait"
)

func on_process(){
  for i := 0; i < 100000000; i++ {}
}

func main(){
  perfait.PerfaitMeasure(on_process)
}
