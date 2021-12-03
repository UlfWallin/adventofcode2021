const string path = "input/input.txt";
using var reader = new StreamReader(path);
var prevSample = 0;
var ascents = 0;
while (reader.Peek() >= 0)
{
    var sample = int.Parse(reader.ReadLine());
    ascents += sample > prevSample && prevSample > 0 ? 1 : 0;
    prevSample = sample;
}
Console.WriteLine(ascents);