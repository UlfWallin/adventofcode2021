import numpy as np

octopuses = np.array(
   [[2,3,4,4,6,7,1,2,1,2],
    [6,6,1,1,7,4,2,6,8,1],
    [5,5,7,5,5,7,5,5,7,3],
    [3,1,6,7,8,4,8,5,3,6],
    [1,3,5,3,8,2,7,3,1,1],
    [4,4,1,6,4,6,3,2,6,6],
    [2,6,2,4,7,6,1,6,1,5],
    [1,7,8,6,5,6,1,2,6,3],
    [3,6,2,2,6,4,3,2,1,5],
    [4,1,4,3,2,8,4,6,5,3]]
)

sample = np.array(
   [[5,4,8,3,1,4,3,2,2,3],
    [2,7,4,5,8,5,4,7,1,1],
    [5,2,6,4,5,5,6,1,7,3],
    [6,1,4,1,3,3,6,1,4,6],
    [6,3,5,7,3,8,5,4,7,8],
    [4,1,6,7,5,2,4,6,4,5],
    [2,1,7,6,8,4,1,7,2,1],
    [6,8,8,2,8,8,1,1,3,4],
    [4,8,4,6,8,4,8,5,5,4],
    [5,2,8,3,7,5,1,5,2,6]]
)
flashers = []
flashed = []
counter = 0

def inc_octo(pos):
    if pos[0] >= 0 and pos[0] < octopuses.shape[0] and pos[1] >= 0 and pos[1] < octopuses.shape[1]:
        octopuses[pos] += 1
        if octopuses[pos] > 9 and pos not in flashers:
            flashers.append(pos)

def flash(pos):
    if pos in flashed:
        return
    flashed.append(pos)
    inc_octo((pos[0]-1, pos[1]-1))
    inc_octo((pos[0]-1, pos[1]))
    inc_octo((pos[0]-1, pos[1]+1))
    inc_octo((pos[0],   pos[1]-1))
    inc_octo((pos[0],   pos[1]+1))
    inc_octo((pos[0]+1, pos[1]-1))
    inc_octo((pos[0]+1, pos[1]))
    inc_octo((pos[0]+1, pos[1]+1))


for s in range(100):
    octopuses += 1
    flashers.clear()
    flashed.clear()

    fo = np.nonzero(octopuses > 9)
    fo_index = list(zip(fo[0], fo[1]))
    for o in fo_index:
        flashers.append(o)
        
    while len(flashers) > 0:
        octopus = flashers.pop()
        flash(octopus)
        
    counter += len(flashed)
    octopuses[octopuses > 9] = 0

print(counter)