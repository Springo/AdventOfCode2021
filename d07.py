def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d07input.txt")
pos = [int(x) for x in lines[0].split(',')]
start = min(pos)
end = max(pos)

best = -1
for i in range(start, end + 1):
    total = 0
    for x in pos:
        total += abs(x - i)
    if best == -1 or total < best:
        best = total
print(best)

best = -1
for i in range(start, end + 1):
    total = 0
    for x in pos:
        dist = abs(x - i)
        total += (dist * (dist + 1)) // 2
    if best == -1 or total < best:
        best = total
print(best)
