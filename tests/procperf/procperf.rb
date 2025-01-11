require "perfait"

stopwatch = Perfait::Stopwatch.new
for _ in 1..100000000 do
end
puts(sprintf("%.6f", stopwatch.stop()))
