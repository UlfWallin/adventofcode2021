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
df = df[
    (df["x1"] == df["x2"]) | (df["y1"] == df["y2"])
    ].assign(
        width = (df["x1"] - df["x2"]).abs(), 
        height = (df["y1"] - df["y2"]).abs())

for index, row in df.iterrows():
    x1 = min(row["x1"], row["x2"])
    x2 = max(row["x1"], row["x2"])
    y1 = min(row["y1"], row["y2"])
    y2 = max(row["y1"], row["y2"])

    if (row["width"] > 0):
        hline = np.arange(x1, x2 + 1, dtype=int)
        for x in hline:
            map[y1, x] = map[y1, x] + 1

    if (row["height"] > 0):
        vline = np.arange(y1, y2 + 1, dtype=int)
        for y in vline:
            map[y, x1] = map[y, x1] + 1

nums = (map > 1).sum()
print(nums)