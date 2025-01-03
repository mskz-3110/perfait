module Perfait
  class Stopwatch
    def self.__get_time
      return Time.now().to_f
    end

    def initialize
      start()
    end

    def start
      @__StartTime = Stopwatch.__get_time()
    end

    def stop
      Stopwatch.__get_time() - @__StartTime
    end
  end

  class Perfait
    def self.measure(&onProcess)
      stopwatch = Stopwatch.new
      onProcess.call()
      puts(sprintf("%.6f", stopwatch.stop()))
    end
  end
end
