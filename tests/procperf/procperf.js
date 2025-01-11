const perfait = require("perfait");

var stopwatch = new perfait.Stopwatch();
for (let i = 0; i < 100000000; ++i){}
console.log("%f", stopwatch.stop());
