import grid_util as gdu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


grid = [[0] * 2000 for _ in range(2000)]
lines = readFile("d13input.txt")
fold_check = False
folds = []
for line in lines:
    if not fold_check:
        if len(line) == 0:
            fold_check = True
        else:
            coords = line.split(',')
            grid[int(coords[1])][int(coords[0])] = 1
    else:
        ls = line.split('=')
        f = (ls[0][-1], int(ls[1]))
        folds.append(f)


def fold_grid(grid, dir, val):
    dim_1 = len(grid)
    dim_2 = len(grid[0])
    if dir == 'x':
        new_grid = [[0] * (val) for _ in range(dim_1)]
        for i in range(len(new_grid)):
            for j in range(len(new_grid[i])):
                new_grid[i][j] = grid[i][j]
        for i in range(1, len(grid[0]) - val):
            r_i = val + i
            f_i = val - i
            if f_i >= 0:
                for j in range(len(grid)):
                    new_grid[j][f_i] = max(new_grid[j][f_i], grid[j][r_i])

        return new_grid

    elif dir == 'y':
        new_grid = [[0] * dim_2 for _ in range(val)]
        for i in range(len(new_grid)):
            for j in range(len(new_grid[i])):
                new_grid[i][j] = grid[i][j]
        for i in range(1, len(grid) - val):
            r_i = val + i
            f_i = val - i
            if f_i >= 0:
                for j in range(len(grid[0])):
                    new_grid[f_i][j] = max(new_grid[f_i][j], grid[r_i][j])

        return new_grid


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                print('.', end=" ")
            else:
                print('#', end=" ")
        print()


for iter, fold in enumerate(folds):
    d, v = fold
    grid = fold_grid(grid, d, v)
    if iter == 0:
        print(gdu.count_val(grid, 1))

print_grid(grid)

