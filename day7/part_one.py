import numpy as np

crab_pos = np.fromfile("input/input.txt", sep=',')

m = np.median(crab_pos)
cost = abs(crab_pos - m)

print(m)
print(cost.sum())