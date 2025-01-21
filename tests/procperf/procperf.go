package main

import (
  "perfait"
  "fmt"
)

func main(){
  stopwatch := perfait.StopwatchNew()
  for i := 0; i < 100000000; i++ {}
  elapsedTime := stopwatch.ElapsedTime()
  fmt.Printf("%.6f\n", elapsedTime)
}
