import grid_util as gdu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def add_border(grid, bx=2):
    new_grid = [['.'] * (len(grid) + (2 * bx)) for _ in range(bx)]
    for i in range(len(grid)):
        new_row = ['.'] * bx
        for j in range(len(grid[i])):
            new_row.append(grid[i][j])
        new_row.extend(['.'] * bx)
        new_grid.append(new_row)
    new_grid.extend([['.'] * (len(grid) + (2 * bx)) for _ in range(bx)])
    return new_grid


def get_bin(ne):
    bs = ""
    for n in ne:
        if n == '.':
            bs = bs + '0'
        else:
            bs = bs + '1'
    return bs


def enhance(grid, code):
    key = grid[0][0]
    if key == '#':
        key = '.'
    else:
        key = '#'

    new_grid = [[key] * len(grid)]
    for i in range(1, len(grid) - 1):
        new_row = [key]
        for j in range(1, len(grid[i]) - 1):
            ne = gdu.get_neighbors(grid, i, j)
            ne = [ne[5], ne[6], ne[7], ne[4], grid[i][j], ne[0], ne[3], ne[2], ne[1]]
            bs = get_bin(ne)
            ind = int(bs, 2)
            new_row.append(code[ind])
        new_row.append(key)
        new_grid.append(new_row)
    new_grid.append([key] * len(grid))
    return new_grid


lines = readFile("d20input.txt")
code = lines[0]
grid = gdu.convert_to_grid(lines[2:])
grid = add_border(grid, bx=51)

for i in range(50):
    if i == 2:
        print(gdu.count_val(grid, '#'))
    grid = enhance(grid, code)

print(gdu.count_val(grid, '#'))
