import pandas as pd
import collections

patterns = pd.read_csv("input/input.txt", sep='|', names=['in', 'out'])
flat = []
for index, row in patterns.iterrows():
    lengths = ([len(s) for s in row["out"].split()])
    flat += lengths

c = collections.Counter(flat)
print(c[2] + c[4] + c[3] + c[7])