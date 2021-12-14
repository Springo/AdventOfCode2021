def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d14input.txt")
start = lines[0]
rules = dict()
for line in lines[2:]:
    ls = line.split(' -> ')
    rules[ls[0]] = ls[1]


def get_polymer(start, rules, steps):
    counts = dict()
    pairs = {r: 0 for r in rules}
    for i in range(1, len(start)):
        pairs[start[i - 1:i + 1]] += 1

    for c in start:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1

    for step in range(steps):
        new_pairs = {r: 0 for r in rules}
        for pair in pairs:
            result = rules[pair]
            p1 = pair[0] + result
            p2 = result + pair[1]
            new_pairs[p1] += pairs[pair]
            new_pairs[p2] += pairs[pair]

            if result not in counts:
                counts[result] = 0
            counts[result] += pairs[pair]
        pairs = new_pairs

    max_key = max(counts, key=counts.get)
    min_key = min(counts, key=counts.get)
    return counts[max_key] - counts[min_key]


print(get_polymer(start, rules, 10))
print(get_polymer(start, rules, 40))
