import graph_util as gu
# functions: transpose, bfs, top_sort, scc
import grid_util as gdu
# functions: convert_to_grid, serialize, get_neighbors, count_val, grid_project


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def bin_to_dec(val):
    result = 0
    for c in val:
        result = 2 * result + int(c)
    return result


lines = readFile("d03input.txt")
gamma = ""
epsilon = ""
zeros = [0] * len(lines[0])
ones = [0] * len(lines[0])
for line in lines:
    for i, c in enumerate(line):
        if c == '0':
            zeros[i] += 1
        else:
            ones[i] += 1

for i in range(len(zeros)):
    if zeros[i] > ones[i]:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    else:
        gamma = gamma + "1"
        epsilon = epsilon + "0"

print(bin_to_dec(gamma) * bin_to_dec(epsilon))

valid = lines[:]
count = len(valid)
i = 0
while count > 1:
    new_valid = []
    zero_c = 0
    one_c = 0
    for line in valid:
        if line[i] == '0':
            zero_c += 1
        if line[i] == '1':
            one_c += 1

    for line in valid:
        if zero_c > one_c and line[i] == '0':
            new_valid.append(line)
        elif one_c >= zero_c and line[i] == '1':
            new_valid.append(line)

    valid = new_valid
    count = len(new_valid)
    i += 1

v1 = valid[0]

valid = lines[:]
count = len(valid)
i = 0
while count > 1:
    new_valid = []
    zero_c = 0
    one_c = 0
    for line in valid:
        if line[i] == '0':
            zero_c += 1
        if line[i] == '1':
            one_c += 1
    for line in valid:
        if zero_c > one_c and line[i] == '1':
            new_valid.append(line)
        elif one_c >= zero_c and line[i] == '0':
            new_valid.append(line)

    valid = new_valid
    count = len(new_valid)
    i += 1

v2 = valid[0]

print(bin_to_dec(v1) * bin_to_dec(v2))
