require "perfait"

stopwatch = Perfait::Stopwatch.new
i = 0
while i < 100000000 do
  i = i + 1
end
puts(sprintf("%.6f", stopwatch.stop()))
