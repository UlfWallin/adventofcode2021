const string path = "input/input.txt";
var diagnostics = new List<int>();
var countBit = new int[12];
var lines = 0;
using var reader = new StreamReader(path);
while (reader.Peek() >= 0)
{
    var line = reader.ReadLine();
    var num = Convert.ToInt32(line, 2);
    for(var i = 0; i < countBit.Length; i++) {
        countBit[i] += (num >> (countBit.Length - i - 1)) & 1;
    }
    diagnostics.Add(num);
    lines++;
}
Console.WriteLine($"Lines: {lines}");
var gamma = "";
var epsilon = "";
for(var i = 0; i < countBit.Length; i++) {
    gamma += countBit[i] < lines/2 ? "0" : "1"; 
    epsilon += countBit[i] < lines/2 ? "1" : "0"; 
}
Console.WriteLine($"Gamma: {gamma}, Epsilon: {epsilon}");
var gammaVal = Convert.ToInt32(gamma, 2);
var epsilonVal = Convert.ToInt32(epsilon, 2);
Console.WriteLine("Result: " + gammaVal * epsilonVal);
