var commands = new List<Command>();

const string path = "input/input.txt";
using var reader = new StreamReader(path);
while (reader.Peek() >= 0)
{
    var line = reader.ReadLine();
    var direction = line.Split(' ')[0];
    var amount = int.Parse(line.Split(' ')[1]);
    commands.Add(new Command(direction, amount));
}

var sumForward = commands.Where(c => c.Direction == "forward").Sum(c => c.Amount);
var sumUp = commands.Where(c => c.Direction == "up").Sum(c => c.Amount);
var sumDown = commands.Where(c => c.Direction == "down").Sum(c => c.Amount);
Console.WriteLine($"Forward: {sumForward}");
Console.WriteLine($"Up: {sumUp}");
Console.WriteLine($"Down: {sumDown}");
Console.WriteLine($"Depth = " + (sumDown - sumUp)); 

var answer = sumForward * (sumDown - sumUp);
Console.WriteLine($"Answer: {answer}");

readonly record struct Command(string Direction, int Amount);