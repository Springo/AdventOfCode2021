def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d02input.txt")
f_pos = 0
d_pos_1 = 0
d_pos_2 = 0
aim = 0
for line in lines:
    args = line.split()
    val = int(args[1])
    if args[0] == "forward":
        f_pos += val
        d_pos_2 += aim * val
    elif args[0] == "up":
        d_pos_1 -= val
        aim -= val
    elif args[0] == "down":
        d_pos_1 += val
        aim += val

print(f_pos * d_pos_1)
print(f_pos * d_pos_2)
