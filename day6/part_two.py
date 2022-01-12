import collections, numpy as np

days = 256
population = np.fromfile("input/input.txt", sep=',', dtype=np.uint8)

counts = [0] * 9
for k,v in collections.Counter(population.tolist()).items():
    counts[k] = v

for day in range(days):   
    zeros = counts[0] 
    for i in range(0, 8):
        counts[i] = counts[i+1]
    counts[8] = zeros
    counts[6] += zeros

print(sum(counts))
