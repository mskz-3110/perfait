const perfait = require("perfait");

var stopwatch = new perfait.Stopwatch();
for (let i = 0; i < 100000000; ++i){}
var elapsedTime = stopwatch.elapsed_time();
console.log("%f", elapsedTime);
