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
            lowpoints.append(heightmap[(row, col)])

print(sum(lp + 1 for lp in lowpoints))
