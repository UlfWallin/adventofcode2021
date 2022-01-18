from statistics import median

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 1, ']': 2, '}': 3, '>': 4}

instructions = []
line_points = []

with open('day10/input/input.txt') as file:
    for line in file:
        instructions.append(line.strip())

for i, line in enumerate(instructions):    
    chunk = []
    illegal = ""
    line_error = False
    for ic, c in enumerate(line):
        if c in pairs: 
            chunk.append(c)
        else: # Assume that instructions only contains valid chars
            cc = chunk.pop()
            expected = pairs[cc]
            if expected != c:
                line_error = True
                break

    if len(chunk) > 0 and line_error == False:
        score = 0
        while len(chunk) > 0:
            last_open = chunk.pop()
            close_last_open = pairs[last_open]
            score = (score * 5) + points[close_last_open]

        line_points.append(score)

print(median(line_points))