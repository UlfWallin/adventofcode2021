import numpy as np

population = np.fromfile("input/input.txt", sep=',')

for day in range(80):    
    nums = np.count_nonzero(population==0)
    
    population[population == 0] = 7
    population = population - 1
    
    # Generate new generation
    new_gen = np.repeat(8, nums)
    population = np.concatenate((population, new_gen))

print(population.size)