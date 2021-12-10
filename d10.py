def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


open_type = {'(', '[', '{', '<'}
opp = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
point = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
p2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
points = 0
scores = []
lines = readFile("d10input.txt")
for line in lines:
    s = []
    done = False
    for c in line:
        if not done:
            if c in open_type:
                s.append(c)
            else:
                if len(s) == 0 or c == opp[s[-1]]:
                    s.pop()
                else:
                    points += point[c]
                    done = True

    if not done:
        score = 0
        while len(s) > 0:
            a = s.pop()
            score = score * 5 + p2[opp[a]]
        scores.append(score)

print(points)
print(sorted(scores)[len(scores) // 2])
