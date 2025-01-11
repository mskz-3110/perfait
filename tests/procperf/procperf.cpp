#include <perfait.hpp>

int main(int argc, const char* argv[]){
  Perfait::Stopwatch stopwatch = Perfait::Stopwatch();
  for (int i = 0; i < 100000000; ++i){}
  printf("%.6f\n", stopwatch.Stop());
  return EXIT_SUCCESS;
}
