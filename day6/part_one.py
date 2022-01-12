import numpy as np

# This method works for short periods (up to 128 days). 
# See part_two.py for a more efficient solution 

population = np.fromfile("input/input.txt", sep=',', dtype=np.uint8)

for day in range(80):    
    nums = np.count_nonzero(population==0)
    
    population[population == 0] = 7
    population -= 1
    
    # Generate new generation
    new_gen = np.repeat(8, nums)
    population = np.concatenate((population, new_gen))

print(population.size)