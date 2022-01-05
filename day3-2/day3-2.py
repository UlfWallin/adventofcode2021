def filterbits(arr, bit=0):
    result0 = list(filter(lambda l: l[bit]=='0', arr))
    result1 = list(filter(lambda l: l[bit]=='1', arr))
    return result0, result1

life_support=[]
with open('input/input.txt') as file:
    life_support = file.readlines()
    life_support = [line.rstrip() for line in life_support]

bit_len = len(life_support[0])
oxygen = 0
co2 = 0
arr = life_support
bit_index = 0
while(len(arr) > 1):
    zeros, ones = filterbits(arr, bit_index)
    if (len(ones) >= len(zeros)):
        arr = ones
    else:
        arr = zeros
    bit_index = bit_index + 1

oxygen = int(arr[0], 2)

arr = life_support
bit_index = 0
while(len(arr) > 1):
    zeros, ones = filterbits(arr, bit_index)
    if (len(ones) >= len(zeros)):
        arr = zeros
    else:
        arr = ones
    bit_index = bit_index + 1

co2 = int(arr[0], 2)

print(f"Oxygen Generator Rating {oxygen}, CO2 Scrubber Rating {co2}. Result = ", oxygen * co2)