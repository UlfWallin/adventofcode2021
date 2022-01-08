import numpy as np
import pandas as pd

vectors = []
with open('input/input.txt') as file:
    for line in file:
        row = list(map(int, line.replace(' -> ', ',').split(',')))
        vectors.append(row)

map = np.zeros((1000, 1000), dtype=int)

columns = ["x1", "y1", "x2", "y2"]
df = pd.DataFrame(data=vectors, columns=columns)

for index, row in df.iterrows():
    x1 = min(row["x1"], row["x2"])
    x2 = max(row["x1"], row["x2"])
    y1 = min(row["y1"], row["y2"])
    y2 = max(row["y1"], row["y2"])

    hline = np.arange(x1, x2 + 1, dtype=int)
    if (row["x1"] < row["x2"]):
        hline = np.flip(hline)
    vline = np.arange(y1, y2 + 1, dtype=int)
    if (row["y1"] < row["y2"]):
        vline = np.flip(vline)

    m = np.broadcast(vline, hline)
    for x in m:
        map[x] = map[x] + 1

nums = (map > 1).sum()
print(nums)