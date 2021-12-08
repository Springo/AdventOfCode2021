def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d08input.txt")

codes = []
outs = []

count = 0
for line in lines:
    ls = line.split()
    outputs = ls[11:]
    for o in outputs:
        if len(o) == 2 or len(o) == 4 or len(o) == 7 or len(o) == 3:
            count += 1

    codes.append(ls[0:10])
    outs.append(ls[11:])

print(count)


def find_index(val, poss_vals):
    for idx, p_list in enumerate(poss_vals):
        if len(p_list) == 1 and p_list[0] == val:
            return idx

solution = 0
for i in range(len(codes)):
    code = codes[i]
    out = outs[i]
    poss_digs = [[] for _ in range(10)]

    for j in range(len(code)):
        cd = code[j]
        cd_len = len(cd)
        if cd_len == 2:
            poss_digs[j] = [1]
        elif cd_len == 3:
            poss_digs[j] = [7]
        elif cd_len == 4:
            poss_digs[j] = [4]
        elif cd_len == 5:
            poss_digs[j] = [2, 3, 5]
        elif cd_len == 6:
            poss_digs[j] = [0, 6, 9]
        elif cd_len == 7:
            poss_digs[j] = [8]

    id1 = find_index(1, poss_digs)
    id4 = find_index(4, poss_digs)

    for j in range(len(code)):
        cd = code[j]
        cd_len = len(cd)
        if len(poss_digs[j]) > 1:
            if cd_len == 5:
                if set(code[id1]).issubset(set(cd)):
                    poss_digs[j] = [3]
                else:
                    match = 0
                    for c in code[id4]:
                        if c in cd:
                            match += 1
                    if match == 2:
                        poss_digs[j] = [2]
                    elif match == 3:
                        poss_digs[j] = [5]
            elif cd_len == 6:
                if not set(code[id1]).issubset(set(cd)):
                    poss_digs[j] = [6]
                else:
                    match = 0
                    for c in code[id4]:
                        if c in cd:
                            match += 1
                    if match == 3:
                        poss_digs[j] = [0]
                    elif match == 4:
                        poss_digs[j] = [9]

    true_vals = dict()
    for j in range(len(code)):
        true_vals[tuple(sorted(code[j]))] = poss_digs[j][0]

    out_val = 0
    for j in range(len(out)):
        out_val = 10 * out_val + true_vals[tuple(sorted(out[j]))]

    solution += out_val

print(solution)
