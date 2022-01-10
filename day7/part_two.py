import numpy as np
import math

crab_pos = np.fromfile("input/input.txt", sep=',')

new_pos = math.floor(np.mean(crab_pos))

steps = abs(crab_pos - new_pos)
cost = steps * (steps + 1) / 2

print(f"Move to {new_pos}. Total cost: {cost.sum()}")