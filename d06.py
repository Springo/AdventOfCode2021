def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def lanternfish(intervals, steps):
    counter = [0] * 9

    for val in intervals:
        counter[val] += 1

    for t in range(steps):
        add = counter[0]
        for i in range(1, 9):
            counter[i - 1] = counter[i]
        counter[6] += add
        counter[8] = add

    return sum(counter)


lines = readFile("d06input.txt")
intervals = [int(x) for x in lines[0].split(',')]

print(lanternfish(intervals, 80))
print(lanternfish(intervals, 256))
