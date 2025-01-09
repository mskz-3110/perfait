#include <perfait.hpp>

static void on_process(){
  for (int i = 0; i < 100000000; ++i){}
}

int main(int argc, const char* argv[]){
  printf("%.6f\n", perfait::Perfait::measure(on_process));
  return EXIT_SUCCESS;
}
