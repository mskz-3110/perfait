package main

import (
  "perfait"
  "fmt"
)

func on_process(){
  for i := 0; i < 100000000; i++ {}
}

func main(){
  fmt.Printf("%.6f\n", perfait.PerfaitMeasure(on_process))
}
