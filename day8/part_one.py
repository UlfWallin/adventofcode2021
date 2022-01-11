import pandas as pd
import collections

segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

patterns = pd.read_csv("input/input.txt", sep='|', names=['in', 'out'])

flat = []
for index, row in patterns.iterrows():
    x = ([len(s) for s in row["out"].split()])
    flat += x

# 0 = 6
# 1 = 2 
# 2 = 5
# 3 = 5
# 4 = 4
# 5 = 5
# 6 = 6
# 7 = 3
# 8 = 7
# 9 = 6

# 1, 4, 7, or 8 

c = collections.Counter(flat)
print(c[2] + c[4] + c[3] + c[7])