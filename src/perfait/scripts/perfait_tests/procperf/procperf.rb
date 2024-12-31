require "../../perfait_scripts/perfait/perfait"

Perfait::Perfait::measure{
  for _ in 1..100000000 do
  end
}
