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

var aim = 0;
var depth = 0;
var horizontal = 0;
foreach(var command in commands) 
{
    switch(command.Direction)
    {
        case "forward":
            horizontal += command.Amount;
            depth += command.Amount * aim;
            break;
        case "down":
            aim += command.Amount;
            break;
        case "up":
            aim -= command.Amount;
            break;

        default:
            Console.WriteLine($"Ignoring command {command.Direction}");
            break;
    }
}

Console.WriteLine($"Aim: {aim}");
Console.WriteLine($"Depth: {depth}");
Console.WriteLine($"Horizontal: {horizontal}");

Console.WriteLine($"Result: {horizontal * depth}");

readonly record struct Command(string Direction, int Amount);