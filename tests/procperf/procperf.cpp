#include <perfait.hpp>

int main(int argc, const char* argv[]){
  Perfait::Stopwatch stopwatch = Perfait::Stopwatch();
  for (int i = 0; i < 100000000; ++i){}
  double elapsedTime = stopwatch.ElapsedTime();
  printf("%.6f\n", elapsedTime);
  return EXIT_SUCCESS;
}
