import pandas as pd

#   dddd
#  e    a
#  e    a
#   ffff
#  g    b
#  g    b
#   cccc

#   dddd
#  e    a
#  e    a
#   ffff
#  g    b
#  g    b
#   cccc



# segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
patterns = pd.read_csv("input/sample.txt", sep='|', names=['signal_pattern', 'out'])

chars = {2: '1', 3: '7', 4: '4', 7: '8'}

for index, row in patterns.iterrows():
    pattern = row["signal_pattern"].split()
    out = row["out"].split()
    segments = zip(map(len, pattern), pattern)
    pattern_char = dict()
    
    for l, seg in zip(map(len, pattern), pattern):
        if l == 2:
            pattern_char[seg] = 1
        elif l == 3:
            pattern_char[seg] = 7
        elif l == 4:
            pattern_char[seg] = 4
        elif l == 7:
            pattern_char[seg] = 8

    #lengths = ([len(s) for s in row["out"].split()])
    print(pattern, chars.get(len(out[0]), out[0]), 
        chars.get(len(out[1]), out[1]), 
        chars.get(len(out[2]), out[2]),
        chars.get(len(out[3]), out[3]))

    # 1 = 2 seg
    # 4 = 4 seg
    # 7 = 3 seg
    # 8 = 7 seg

    # 3 = len 5 & all seg in 1
    # 2 = len 5, g & c
    # 5 = len 5, e & f
    # 
    