import pandas as pd

def decode(output, segments):
    decoded = ""
    for o in output:
        decoded += str(next(k for k, v in segments.items() if v == set(o)))
    return decoded


values = []
patterns = pd.read_csv("input/input.txt", sep='|', names=['signal_pattern', 'out'])
for index, row in patterns.iterrows():
    pattern = row["signal_pattern"].split()
    out = row["out"].split()
    display_segments = dict()
    
    # Fill with unique
    for l, seg in zip(map(len, pattern), pattern):
        segset = set(seg)
        if l == 2:
            display_segments[1] = segset
        elif l == 3:
            display_segments[7] = segset
        elif l == 4:
            display_segments[4] = segset
        elif l == 7:
            display_segments[8] = segset
            
    # New pass, fill in the blanks
    for l, seg in zip(map(len, pattern), pattern):
        segset = set(seg)
        if l == 5:
            if ((display_segments[4] - display_segments[1]).issubset(segset)):
                display_segments[5] = segset
            elif (segset.issuperset(display_segments[1])):
                display_segments[3] = segset
            else:
                display_segments[2] = segset
        elif l == 6:
            if ((display_segments[8] - display_segments[1]).issubset(segset)):
                display_segments[6] = segset
            elif (segset.issuperset(display_segments[4])):
                display_segments[9] = segset
            else:
                display_segments[0] = segset
            
    values.append(int(decode(out, display_segments)))

print(sum(values))