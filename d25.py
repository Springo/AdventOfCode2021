import grid_util as gdu
from copy import deepcopy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d25input.txt")
grid = gdu.convert_to_grid(lines)

step = 0
done = False
while not done:
    last_grid = deepcopy(grid)
    new_grid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '>':
                if j < len(grid[i]) - 1:
                    next_j = j + 1
                else:
                    next_j = 0

                if grid[i][next_j] == '.':
                    new_grid[i][j] = '.'
                    new_grid[i][next_j] = '>'
    grid = new_grid
    new_grid = deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'v':
                if i < len(grid) - 1:
                    next_i = i + 1
                else:
                    next_i = 0

                if grid[next_i][j] == '.':
                    new_grid[i][j] = '.'
                    new_grid[next_i][j] = 'v'

    grid = new_grid
    step += 1

    match = True
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != last_grid[i][j]:
                match = False

    done = match

print(step)
