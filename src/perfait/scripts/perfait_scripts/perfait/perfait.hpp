#ifndef __PERFAIT_H__
#define __PERFAIT_H__
#include <cstdlib>
#include <stdio.h>
#include <time.h>

namespace perfait {
  class Stopwatch {
    private:
      static double __get_time(){
        struct timespec ts;
        clock_gettime(CLOCK_REALTIME, &ts);
        return (double)ts.tv_sec + ((double)ts.tv_nsec / 1000000000);
      }

      double __StartTime;

    public:
      Stopwatch(){
        start();
      }

      void start(){
        __StartTime = __get_time();
      }

      double stop(){
        return __get_time() - __StartTime;
      }
  };

  class Perfait {
    public:
      typedef void (*ProcessEvent)();

      static void measure(ProcessEvent onProcess){
        Stopwatch stopwatch = Stopwatch();
        onProcess();
        printf("%.6f\n", stopwatch.stop());
      }
  };
}
#endif
