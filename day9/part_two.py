import numpy as np

temp = []
with open('input/input.txt') as file:
    for line in file:
        temp.append(list(map(int, list(line.rstrip()))))

heightmap = np.pad(temp, (1, 1), 'constant', constant_values=(9, 9))
lowpoints = []
gridsize = heightmap.shape
for row in range(1, gridsize[0] - 1):
    for col in range(1, gridsize[1] - 1):
        adjacent = [
            heightmap[(row - 1, col)],
            heightmap[(row, col + 1)],
            heightmap[(row + 1, col)],
            heightmap[(row, col - 1)]]
        if heightmap[(row, col)] < min(adjacent):
            lowpoint = (row, col, heightmap[(row, col)])
            lowpoints.append(lowpoint)

# Flood fill from lowpoints
# https://en.wikipedia.org/wiki/Flood_fill
# lowpoint: tuple(row, col, height)
basins = []
for point in lowpoints:
    basin = []
    visited = [point]
    while len(visited) > 0:
        pos = visited.pop()
        if pos in basin:
            continue
        height = pos[2]
        # W E N S
        if height < 9:
            row = pos[0]
            col = pos[1]
            basin.append((row, col, height))

            visited.append((row, col - 1, heightmap[(row, col - 1)]))
            visited.append((row, col + 1, heightmap[(row, col + 1)]))
            visited.append((row - 1, col, heightmap[(row - 1, col)]))
            visited.append((row + 1, col, heightmap[(row + 1, col)]))
    basins.append(basin)        
    
largest = sorted([len(b) for b in basins], reverse=True)[:3]
answer = np.prod(largest)
print(answer)