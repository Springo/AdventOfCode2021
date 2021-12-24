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


def parse_val(reg, val):
    if val.isnumeric():
        try:
            val = int(val)
            return val
        except:
            val = float(val)
            return val
    else:
        return get_val(reg, val)


def get_val(reg, key):
    if key not in reg:
        reg[key] = 0
    return reg[key]


def parse_input(ins_list, inp):
    inp_idx = 0
    reg = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for args in ins_list:
        ins = args[0]
        v1 = args[1]
        if len(args) > 2:
            v2 = args[2]
            if isinstance(v2, str):
                v2 = get_val(reg, v2)

        if ins == "inp":
            print(reg['z'])
            reg[v1] = inp[inp_idx]
            inp_idx += 1
        elif ins == "add":
            reg[v1] = get_val(reg, v1) + v2
        elif ins == "mul":
            reg[v1] = get_val(reg, v1) * v2
        elif ins == "div":
            if v2 != 0:
                reg[v1] = get_val(reg, v1) // v2
        elif ins == "mod":
            reg[v1] = get_val(reg, v1) % v2
        elif ins == "eql":
            if get_val(reg, v1) == v2:
                reg[v1] = 1
            else:
                reg[v1] = 0
        else:
            print("OH NO!")

    return reg['z']


def parse_input_manual(inp, c1, c2, c3):
    z = 0
    for i in range(len(inp)):
        print("{} == {} ({})".format(inp[i], z % 26 + c1[i], z))
        if inp[i] == z % 26 + c1[i]:
            z = z // c2[i]
        else:
            z = 26 * (z // c2[i]) + inp[i] + c3[i]
        #print("{}, {}".format(z, z % 26))
    return z


lines = readFile("d24input.txt")

ins_list = []
for line in lines:
    args = line.split()
    parsed_args = [args[0]]
    for arg in args[1:]:
        sign = 1
        new_arg = arg
        if arg[0] == '-':
            sign = -1
            new_arg = new_arg[1:]
        if new_arg.isnumeric():
            try:
                val = int(new_arg)
                parsed_args.append(val * sign)
            except:
                val = float(new_arg)
                parsed_args.append(val * sign)
        else:
            parsed_args.append(arg)
    ins_list.append(parsed_args)

inp_1 = [int(x) for x in "97919997299495"]
inp_2 = [int(x) for x in "51619131181131"]
c1 = [12, 12, 13, 12, -3, 10, 14, -16, 12, -8, -12, -7, -6, -11]
c2 = [1, 1, 1, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26, 26]
c3 = [7, 8, 2, 11, 6, 12, 14, 13, 15, 10, 6, 10, 8, 5]


print(parse_input(ins_list, inp_2))
print(parse_input_manual(inp_2, c1, c2, c3))

