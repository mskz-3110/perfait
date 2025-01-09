<?php
include "perfait.php";

function on_process(){
  for ($i = 0; $i < 100000000; $i++){}
}

printf("%.6f\n", perfait\Perfait::measure("on_process"));
?>
