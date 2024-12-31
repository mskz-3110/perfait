<?php
include "../../perfait_scripts/perfait/perfait.php";

function on_process(){
  for ($i = 0; $i < 100000000; $i++){}
}

perfait\Perfait::measure("on_process");
?>
