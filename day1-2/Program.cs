const int windowsSize = 3;
const string path = "input/input.txt";
using var reader = new StreamReader(path);

var depths = new List<int>(2000);
while (reader.Peek() >= 0)
{
    var sample = 0;
    if (int.TryParse(reader.ReadLine(), out sample)) {
        depths.Add(sample);
    }
}

var previous = int.MaxValue;
var ascents = 0;

// 
for(int i=0; i < depths.Count - windowsSize + 1; i++) {
    var sum = depths[i] + depths[i + 1] + depths[i + 2];
    ascents += sum > previous ? 1 : 0;
    previous = sum;
    Console.WriteLine($"{i} = {previous}: Ascents: {ascents}");
}

