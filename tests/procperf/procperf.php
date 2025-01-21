<?php
include "perfait.php";

$stopwatch = new Perfait\Stopwatch();
for ($i = 0; $i < 100000000; $i++){}
$elapsedTime = $stopwatch->elapsed_time();
printf("%.6f\n", $elapsedTime);
?>
