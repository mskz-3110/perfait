const perfait = require("../../perfait_scripts/perfait/perfait");

function on_process(){
  for (let i = 0; i < 100000000; ++i){}
}

perfait.Perfait.measure(on_process);
