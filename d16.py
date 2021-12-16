def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d16input.txt")
inp = bin(int("1" + lines[0], 16))[3:]


def parse_packet(inp, i):
    ver = int(inp[i:i + 3], 2)
    p_type = int(inp[i + 3:i + 6], 2)
    if p_type == 4:
        done = False
        j = i + 6
        num = ""
        while not done:
            num = num + inp[j + 1:j + 5]
            if inp[j] == '0':
                done = True
            j += 5
        return int(num, 2), ver, j
    else:
        i_type = inp[i + 6]
        total = ver
        vals = []
        if i_type == '0':
            pack_len = int(inp[i + 7:i + 7 + 15], 2)
            j = i + 7 + 15
            while j < i + 7 + 15 + pack_len:
                new_val, new_ver, new_j = parse_packet(inp, j)
                vals.append(new_val)
                total += new_ver
                j = new_j
        else:
            pack_count = int(inp[i + 7:i + 7 + 11], 2)
            j = i + 7 + 11
            for iter in range(pack_count):
                new_val, new_ver, new_j = parse_packet(inp, j)
                vals.append(new_val)
                total += new_ver
                j = new_j

        final_val = 0
        if p_type == 0:
            final_val = sum(vals)
        elif p_type == 1:
            final_val = 1
            for val in vals:
                final_val *= val
        elif p_type == 2:
            final_val = min(vals)
        elif p_type == 3:
            final_val = max(vals)
        elif p_type == 5:
            if vals[0] > vals[1]:
                final_val = 1
            else:
                final_val = 0
        elif p_type == 6:
            if vals[0] < vals[1]:
                final_val = 1
            else:
                final_val = 0
        elif p_type == 7:
            if vals[0] == vals[1]:
                final_val = 1
            else:
                final_val = 0
        else:
            print("ERROR")
        return final_val, total, j


val, ver, _ = parse_packet(inp, 0)
print(ver)
print(val)
