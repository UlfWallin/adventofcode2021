const string path = "input/input.txt";
var bitCount = new int[12];
var lines = 0;
using var reader = new StreamReader(path);
while (reader.Peek() >= 0)
{
    var line = reader.ReadLine();
    var num = Convert.ToInt32(line, 2);
    for(var i = 0; i < bitCount.Length; i++) {
        bitCount[i] += (num >> (bitCount.Length - i - 1)) & 1;
    }
    lines++;
}

var g = 0;
var len = bitCount.Length;
for(var i = 0; i < len; i++) {
    g = bitCount[i] > lines/2 ? 
        g | 1 << len - 1 - i :
        g & ~(1 << len - 1 - i);
}
var e = ~(-1 ^0x0FFF | g);

Console.WriteLine($"Result: {g} * {e} = " + g * e);