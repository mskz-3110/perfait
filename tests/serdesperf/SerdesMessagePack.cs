using MessagePack;

namespace Serdesperf {
  [MessagePackObject]
  public class SerdesDoubleMessagePack {
    [Key(0)]
    public List<double> Values {get; set;} = new List<double>();
  }
}
