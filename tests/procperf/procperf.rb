require "perfait"

puts(sprintf("%.6f", Perfait::Perfait::measure{
  for _ in 1..100000000 do
  end
}))
