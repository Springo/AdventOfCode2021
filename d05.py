def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d05input.txt")
segments = []
for line in lines:
    ls = line.split(' -> ')
    ls1 = [int(x) for x in ls[0].split(',')]
    ls2 = [int(x) for x in ls[1].split(',')]
    segments.append([ls1, ls2])

grid_1 = [[0] * 1000 for _ in range(1000)]
grid_2 = [[0] * 1000 for _ in range(1000)]
for seg in segments:
    s1x, s1y = seg[0]
    s2x, s2y = seg[1]
    if s1x == s2x:
        max_y = max(s1y, s2y)
        min_y = min(s1y, s2y)
        for i in range(min_y, max_y + 1):
            grid_1[s1x][i] += 1
            grid_2[s1x][i] += 1
    elif s1y == s2y:
        max_x = max(s1x, s2x)
        min_x = min(s1x, s2x)
        for i in range(min_x, max_x + 1):
            grid_1[i][s1y] += 1
            grid_2[i][s1y] += 1
    else:
        dist = abs(s2x - s1x)
        if s2x > s1x:
            x_dir = 1
        else:
            x_dir = -1
        if s2y > s1y:
            y_dir = 1
        else:
            y_dir = -1
        for i in range(dist + 1):
            grid_2[s1x + x_dir * i][s1y + y_dir * i] += 1

count_1 = 0
count_2 = 0
for i in range(len(grid_1)):
    for j in range(len(grid_1[i])):
        if grid_1[i][j] >= 2:
            count_1 += 1
        if grid_2[i][j] >= 2:
            count_2 += 1
print(count_1)
print(count_2)
