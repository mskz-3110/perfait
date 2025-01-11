<?php
include "perfait.php";

$stopwatch = new Perfait\Stopwatch();
for ($i = 0; $i < 100000000; $i++){}
printf("%.6f\n", $stopwatch->stop());
?>
