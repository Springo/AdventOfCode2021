def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d01input.txt")
vals = []
for line in lines:
    vals.append(int(line))

count = 0
for i in range(1, len(vals)):
    if vals[i] > vals[i-1]:
        count += 1
print(count)

count = 0
for i in range(3, len(vals)):
    if sum(vals[i-2:i+1]) > sum(vals[i-3:i]):
        count += 1
print(count)
