chunk = []
open_c = "([{<"
close_c = ")]}>"
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

instructions = []
illegals = []

with open('input/input.txt') as file:
    for line in file:
        instructions.append(line)

for i, line in enumerate(instructions):    
    illegal = ""
    for ic, c in enumerate(line):
        if c in open_c: 
            chunk.append(c)
        elif c in close_c:
            cc = chunk.pop()
            expected = pairs[cc]
            if expected != c:
                illegal = c
                illegals.append(illegal)
                print(f"SYNTAX ERROR on {i + 1},{ic + 1}. Found {illegal}. Expected {expected}")
                break

print(illegals)
print(sum([points[x] for x in illegals]))