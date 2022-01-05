import numpy as np

draws = []
boards = []

with open('input/input.txt') as file:
    header = file.readline() # Read draws
    draws.extend(map(int, header.split(',')))
    file.readline() # Skip empty line
    nums = []
    for line in file:
        nums.extend(map(int, line.split()))
        if line == '\n':
            boards.append(nums)
            nums = []
    else:
        boards.append(nums)


bingo = False
bingo_board = 0
bingo_boards = boards
number_of_draws = 5 # Start at first possible win

while len(boards) > 1: 
    for board_index, board in enumerate(list(boards)):
        for i in range(5):
            row = board[i*5:i*5+5]
            col = board[i::5]

            is_row_full = all(elem in draws[:number_of_draws] for elem in row)
            is_col_full = all(elem in draws[:number_of_draws] for elem in col)

            if (is_row_full | is_col_full):
                bingo = True
                bingo_board = board_index
                boards.remove(board)
                print(f'Bingo! Board {board_index + 1}')
                break
    number_of_draws += 1

print(boards[0])
print(draws[:number_of_draws])
unmarked = np.setdiff1d(boards[0], draws[:number_of_draws])
sum_unmarked = sum(unmarked)
last_called = draws[number_of_draws-1]
print(f'Sum unmarked = {sum_unmarked}, Last Called = {last_called}. {sum_unmarked} * {last_called} = {sum_unmarked * last_called}')