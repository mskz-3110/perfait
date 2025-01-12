using System;
using Google.Protobuf;
using MessagePack;
using MemoryPack;
using Serdesperf;

class Program {
  private delegate byte[] SerializeEvent(object serializeData);

  private delegate void DeserializeEvent(byte[] serializedBytes);

  static private void Measure(out double serializedTime, out int serializedSize, out double deserializedTime, object serializeData, SerializeEvent onSerialize, DeserializeEvent onDeserialize){
    try{
      var stopwatch = new Perfait.Stopwatch();
      var serializedBytes = onSerialize(serializeData);
      serializedTime = stopwatch.Stop();
      serializedSize = serializedBytes.Length;
      stopwatch.Start();
      onDeserialize(serializedBytes);
      deserializedTime = stopwatch.Stop();
    }catch(Exception e){
      Console.WriteLine(e.ToString());
      serializedTime = deserializedTime = 0;
      serializedSize = -1;
    }
  }

  static private byte[] SerializeProtobuf(object serializeData){
    using (var stream = new MemoryStream()){
      ((SerdesDoubleProtobuf)serializeData).WriteTo(stream);
      return stream.ToArray();
    }
  }

  static private void DeserializeProtobuf(byte[] serializedBytes){
    using (var stream = new MemoryStream(serializedBytes)){
      SerdesDoubleProtobuf.Parser.ParseFrom(stream);
    }
  }

  static private void MeasureProtobuf(out double serializedTime, out int serializedSize, out double deserializedTime, int maxCount){
    var random = new Random();
    var serializeData = new SerdesDoubleProtobuf();
    for (var i = 0; i < maxCount; ++i){
      serializeData.Values.Add((float)random.NextDouble());
    }
    Measure(out serializedTime, out serializedSize, out deserializedTime, serializeData, SerializeProtobuf, DeserializeProtobuf);
  }

  static private void MeasureMessagePack(out double serializedTime, out int serializedSize, out double deserializedTime, int maxCount){
    var random = new Random();
    var serializeData = new SerdesDoubleMessagePack();
    for (var i = 0; i < maxCount; ++i){
      serializeData.Values.Add((float)random.NextDouble());
    }
    Measure(out serializedTime, out serializedSize, out deserializedTime, serializeData, (serializeData) => MessagePackSerializer.Serialize((SerdesDoubleMessagePack)serializeData), (serializedBytes) => MessagePackSerializer.Deserialize<SerdesDoubleMessagePack>(serializedBytes));
  }

  static private void MeasureMemoryPack(out double serializedTime, out int serializedSize, out double deserializedTime, int maxCount){
    var random = new Random();
    var serializeData = new SerdesDoubleMemoryPack();
    for (var i = 0; i < maxCount; ++i){
      serializeData.Values.Add((float)random.NextDouble());
    }
    Measure(out serializedTime, out serializedSize, out deserializedTime, serializeData, (serializeData) => MemoryPackSerializer.Serialize((SerdesDoubleMemoryPack)serializeData), (serializedBytes) => MemoryPackSerializer.Deserialize<SerdesDoubleMemoryPack>(serializedBytes));
  }

  static private int ToMicroTime(double elapsedTime){
    return (int)(elapsedTime * 1000000);
  }

  static public void Main(string[] args){
    int minCount = 1;
    int maxCount = 1000;
    double serializedTime;
    int serializedSize;
    double deserializedTime;

    Console.WriteLine("{");
    Console.WriteLine("  \"Tick\": {\"Dtick\": 2000, \"Format\": \"d\"},");
    Console.WriteLine("  \"LayoutTitleText\": \"<b>[serdesperf]<br>Performance comparison of binary serializers</b>\",");
    Console.WriteLine("  \"XTitleText\": \"\",");
    Console.WriteLine("  \"YTitleText\": \"Binary serializer\",");
    Console.WriteLine("  \"Array\": [");
    Console.WriteLine("    [\"\", \"Ser(μs)\", \"Des(μs)\", \"Size(byte)\"],");

    MeasureProtobuf(out serializedTime, out serializedSize, out deserializedTime, minCount);
    Console.WriteLine($"    [\"Protobuf<br>double[{minCount}] first\", {ToMicroTime(serializedTime)}, {ToMicroTime(deserializedTime)}, {serializedSize}],");
    MeasureProtobuf(out serializedTime, out serializedSize, out deserializedTime, minCount);
    Console.WriteLine($"    [\"Protobuf<br>double[{minCount}]\", {ToMicroTime(serializedTime)}, {ToMicroTime(deserializedTime)}, {serializedSize}],");
    MeasureProtobuf(out serializedTime, out serializedSize, out deserializedTime, maxCount);
    Console.WriteLine($"    [\"Protobuf<br>double[{maxCount}]\", {ToMicroTime(serializedTime)}, {ToMicroTime(deserializedTime)}, {serializedSize}],");

    MeasureMessagePack(out serializedTime, out serializedSize, out deserializedTime, minCount);
    Console.WriteLine($"    [\"MessagePack<br>double[{minCount}] first\", {ToMicroTime(serializedTime)}, {ToMicroTime(deserializedTime)}, {serializedSize}],");
    MeasureMessagePack(out serializedTime, out serializedSize, out deserializedTime, minCount);
    Console.WriteLine($"    [\"MessagePack<br>double[{minCount}]\", {ToMicroTime(serializedTime)}, {ToMicroTime(deserializedTime)}, {serializedSize}],");
    MeasureMessagePack(out serializedTime, out serializedSize, out deserializedTime, maxCount);
    Console.WriteLine($"    [\"MessagePack<br>double[{maxCount}]\", {ToMicroTime(serializedTime)}, {ToMicroTime(deserializedTime)}, {serializedSize}],");

    MeasureMemoryPack(out serializedTime, out serializedSize, out deserializedTime, minCount);
    Console.WriteLine($"    [\"MemoryPack<br>double[{minCount}] first\", {ToMicroTime(serializedTime)}, {ToMicroTime(deserializedTime)}, {serializedSize}],");
    MeasureMemoryPack(out serializedTime, out serializedSize, out deserializedTime, minCount);
    Console.WriteLine($"    [\"MemoryPack<br>double[{minCount}]\", {ToMicroTime(serializedTime)}, {ToMicroTime(deserializedTime)}, {serializedSize}],");
    MeasureMemoryPack(out serializedTime, out serializedSize, out deserializedTime, maxCount);
    Console.WriteLine($"    [\"MemoryPack<br>double[{maxCount}]\", {ToMicroTime(serializedTime)}, {ToMicroTime(deserializedTime)}, {serializedSize}]");

    Console.WriteLine("  ]\n}");
  }
}
