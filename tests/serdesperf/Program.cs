using System;
using Google.Protobuf;
using MessagePack;
using MemoryPack;
using Serdesperf;

class Program {
  static public void MeasureProtobuf(out double serializedTime, out int serializedSize, out double deserializedTime, int maxCount){
    var stopwatch = new Perfait.Stopwatch();
    var serializeData = new SerdesDoubleProtobuf();
    byte[] serializedBytes;
    SerdesDoubleProtobuf deserializeData;
    var random = new Random();
    for (var i = 0; i < maxCount; ++i){
      serializeData.Values.Add((float)random.NextDouble());
    }
    using (var stream = new MemoryStream()){
      stopwatch.Start();
      serializeData.WriteTo(stream);
      serializedBytes = stream.ToArray();
      serializedTime = stopwatch.Stop();
      serializedSize = serializedBytes.Length;
    }
    using (var stream = new MemoryStream(serializedBytes)){
      stopwatch.Start();
      deserializeData = SerdesDoubleProtobuf.Parser.ParseFrom(stream);
      deserializedTime = stopwatch.Stop();
    }
  }

  static public void MeasureMessagePack(out double serializedTime, out int serializedSize, out double deserializedTime, int maxCount){
    var stopwatch = new Perfait.Stopwatch();
    var serializeData = new SerdesDoubleMessagePack();
    byte[] serializedBytes;
    SerdesDoubleMessagePack deserializeData;
    var random = new Random();
    for (var i = 0; i < maxCount; ++i){
      serializeData.Values.Add((float)random.NextDouble());
    }
    using (var stream = new MemoryStream()){
      stopwatch.Start();
      serializedBytes = MessagePackSerializer.Serialize(serializeData);
      serializedTime = stopwatch.Stop();
      serializedSize = serializedBytes.Length;
    }
    using (var stream = new MemoryStream(serializedBytes)){
      stopwatch.Start();
      deserializeData = MessagePackSerializer.Deserialize<SerdesDoubleMessagePack>(serializedBytes);
      deserializedTime = stopwatch.Stop();
    }
  }

  static public void MeasureMemoryPack(out double serializedTime, out int serializedSize, out double deserializedTime, int maxCount){
    var stopwatch = new Perfait.Stopwatch();
    var serializeData = new SerdesDoubleMemoryPack();
    byte[] serializedBytes;
    SerdesDoubleMemoryPack? deserializeData;
    var random = new Random();
    for (var i = 0; i < maxCount; ++i){
      serializeData.Values.Add((float)random.NextDouble());
    }
    using (var stream = new MemoryStream()){
      stopwatch.Start();
      serializedBytes = MemoryPackSerializer.Serialize(serializeData);
      serializedTime = stopwatch.Stop();
      serializedSize = serializedBytes.Length;
    }
    using (var stream = new MemoryStream(serializedBytes)){
      stopwatch.Start();
      deserializeData = MemoryPackSerializer.Deserialize<SerdesDoubleMemoryPack>(serializedBytes);
      deserializedTime = stopwatch.Stop();
    }
  }

  static public void Main(string[] args){
    int minCount = 1;
    int maxCount = 1000;
    double serializedTime;
    int serializedSize;
    double deserializedTime;
    Console.WriteLine("{");
    Console.WriteLine("  \"Tick\": {\"Dtick\": 1000, \"Format\": \"d\"},");
    Console.WriteLine("  \"LayoutTitleText\": \"<b>[serdesperf]<br>Performance comparison of binary serializers</b>\",");
    Console.WriteLine("  \"XTitleText\": \"\",");
    Console.WriteLine("  \"YTitleText\": \"Binary serializer\",");
    Console.WriteLine("  \"Array\": [");
    Console.WriteLine("    [\"\", \"Ser(μs)\", \"Des(μs)\", \"Size(byte)\"],");
    MeasureProtobuf(out serializedTime, out serializedSize, out deserializedTime, minCount);
    MeasureProtobuf(out serializedTime, out serializedSize, out deserializedTime, minCount);
    Console.WriteLine($"    [\"Protobuf<br>double[{minCount}]\", {(int)(serializedTime * 1000000)}, {(int)(deserializedTime * 1000000)}, {serializedSize}],");
    MeasureProtobuf(out serializedTime, out serializedSize, out deserializedTime, maxCount);
    Console.WriteLine($"    [\"Protobuf<br>double[{maxCount}]\", {(int)(serializedTime * 1000000)}, {(int)(deserializedTime * 1000000)}, {serializedSize}],");
    MeasureMessagePack(out serializedTime, out serializedSize, out deserializedTime, minCount);
    MeasureMessagePack(out serializedTime, out serializedSize, out deserializedTime, minCount);
    Console.WriteLine($"    [\"MessagePack<br>double[{minCount}]\", {(int)(serializedTime * 1000000)}, {(int)(deserializedTime * 1000000)}, {serializedSize}],");
    MeasureMessagePack(out serializedTime, out serializedSize, out deserializedTime, maxCount);
    Console.WriteLine($"    [\"MessagePack<br>double[{maxCount}]\", {(int)(serializedTime * 1000000)}, {(int)(deserializedTime * 1000000)}, {serializedSize}],");
    MeasureMemoryPack(out serializedTime, out serializedSize, out deserializedTime, minCount);
    MeasureMemoryPack(out serializedTime, out serializedSize, out deserializedTime, minCount);
    Console.WriteLine($"    [\"MemoryPack<br>double[{minCount}]\", {(int)(serializedTime * 1000000)}, {(int)(deserializedTime * 1000000)}, {serializedSize}],");
    MeasureMemoryPack(out serializedTime, out serializedSize, out deserializedTime, maxCount);
    Console.WriteLine($"    [\"MemoryPack<br>double[{maxCount}]\", {(int)(serializedTime * 1000000)}, {(int)(deserializedTime * 1000000)}, {serializedSize}]");
    Console.WriteLine("  ]\n}");
  }
}
