using MemoryPack;

namespace Serdesperf {
  [MemoryPackable]
  public partial class SerdesDoubleMemoryPack {
    public List<double> Values {get; set;} = new List<double>();
  }
}
