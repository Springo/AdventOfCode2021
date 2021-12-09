import grid_util as gdu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d09input.txt")
grid = gdu.convert_to_grid(lines)
basins = []

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        neigh = gdu.get_neighbors(grid, i, j, orth=True)
        if grid[i][j] < min(neigh):
            total += grid[i][j] + 1
            basins.append((i, j))
print(total)

adj_list = dict()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        for d in [0, 2, 4, 6]:
            i2, j2 = gdu.grid_project(grid, i, j, d, step=1)
            if i2 is not None:
                if grid[i][j] != 9 and grid[i2][j2] != 9:
                    if (i, j) not in adj_list:
                        adj_list[(i, j)] = []
                    if (i2, j2) not in adj_list:
                        adj_list[(i2, j2)] = []
                    if grid[i][j] < grid[i2][j2]:
                        adj_list[(i, j)].append((i2, j2))


def dfs(i, j):
    q = [(i, j)]
    count = 1
    seen = {(i, j)}
    while len(q) > 0:
        a, b = q.pop()
        for neigh in adj_list[(a, b)]:
            if neigh not in seen:
                q.append(neigh)
                count += 1
                seen.add(neigh)
    return count


b_sizes = []
for b in basins:
    i, j = b
    b_sizes.append(dfs(i, j))

top_3 = sorted(b_sizes, reverse=True)[:3]
print(top_3[0] * top_3[1] * top_3[2])
