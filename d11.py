import grid_util as gdu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d11input.txt")
grid = gdu.convert_to_grid(lines, convert_numeric=True)


flashes = 0
unison = False
step = 0
while not unison:
    step += 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] += 1

    done = False
    flashed_grid = [[0] * len(grid) for _ in range(len(grid[0]))]
    while not done:
        done = True
        sum_grid = [[0] * len(grid) for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] >= 10 and flashed_grid[i][j] == 0:
                    done = False
                    neighbors = gdu.get_neighbors(grid, i, j, indices=True)
                    for ne in neighbors:
                        i2, j2 = ne
                        sum_grid[i2][j2] += 1
                    flashed_grid[i][j] = 1
                    if step <= 100:
                        flashes += 1

        for i in range(len(grid)):
            for j in range(len(grid)):
                if flashed_grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] += sum_grid[i][j]

    unison = True
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                unison = False


print(flashes)
print(step)
