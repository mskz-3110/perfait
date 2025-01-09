const perfait = require("perfait");

function on_process(){
  for (let i = 0; i < 100000000; ++i){}
}

console.log("%f", perfait.Perfait.measure(on_process));
