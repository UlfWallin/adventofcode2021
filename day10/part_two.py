open_c = "([{<"
close_c = ")]}>"
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 1, ']': 2, '}': 3, '>': 4}

instructions = []
illegals = []
line_points = []

with open('day10/input/sample.txt') as file:
    for line in file:
        instructions.append(line)

for i, line in enumerate(instructions):    
    chunk = []
    illegal = ""
    line_error = False
    for ic, c in enumerate(line):
        if c in open_c: 
            chunk.append(c)
        elif c in close_c:
            cc = chunk.pop()
            expected = pairs[cc]
            if expected != c:
                illegal = c
                illegals.append(illegal)
                line_error = True
                print(f"SYNTAX ERROR on {i + 1},{ic + 1}. Found {illegal}. Expected {expected}")
                break

    if len(chunk) > 0 and line_error == False:
        missing = []
        while len(chunk) > 0:
            missing.insert(0, chunk.pop())

        print(missing)
        # line_sum = sum([points[x] for x in missing])
        # line_points.append(line_sum)

print(line_points)