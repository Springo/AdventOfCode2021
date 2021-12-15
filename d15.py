import grid_util as gdu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d15input.txt")
grid = gdu.convert_to_grid(lines)


n1 = len(grid)
n2 = len(grid[0])


def get_grid_val(grid, i, j):
    offset = i // n1 + j // n2
    i2 = i % n1
    j2 = j % n2
    return ((grid[i2][j2] + offset - 1) % 9) + 1


def get_shortest_path(grid, k):
    opt = [[-1] * (len(grid[0]) * k) for _ in range(len(grid) * k)]
    check = {(0, 0): 0}
    while len(check) > 0:
        i, j = min(check, key=check.get)
        dist = check[(i, j)]

        opt[i][j] = dist
        nes = []
        if i > 0:
            nes.append((i - 1, j))
        if j > 0:
            nes.append((i, j - 1))
        if i < (k * n1) - 1:
            nes.append((i + 1, j))
        if j < (k * n2) - 1:
            nes.append((i, j + 1))

        for ne in nes:
            i3, j3 = ne
            if opt[i3][j3] == -1:
                if (i3, j3) not in check:
                    check[(i3, j3)] = opt[i][j] + get_grid_val(grid, i3, j3)
                else:
                    check[(i3, j3)] = min(check[(i3, j3)], opt[i][j] + get_grid_val(grid, i3, j3))

        check.pop((i, j))

    return opt[-1][-1]


print(get_shortest_path(grid, 1))
print(get_shortest_path(grid, 5))
