from copy import copy
from time import time


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def search_paths(node, target, adj_list, visited, allowed, memo):
    key = (node, frozenset(visited), allowed)
    if key in memo:
        return memo[key]

    if node == "end":
        return 1
    path_count = 0
    for ne in adj_list[node]:
        if ne not in visited:
            new_visited = copy(visited)
            if not ne.isupper():
                new_visited.add(ne)
            c_path_count = search_paths(ne, target, adj_list, new_visited, allowed, memo)
            path_count += c_path_count
        else:
            if ne != "start" and ne != "end" and allowed > 0:
                c_path_count = search_paths(ne, target, adj_list, visited, allowed - 1, memo)
                path_count += c_path_count

    memo[key] = path_count
    return path_count


lines = readFile("d12input.txt")
adj_list = dict()
for line in lines:
    ls = line.split('-')
    if ls[0] not in adj_list:
        adj_list[ls[0]] = []
    if ls[1] not in adj_list:
        adj_list[ls[1]] = []

    adj_list[ls[0]].append(ls[1])
    adj_list[ls[1]].append(ls[0])

t1 = time()
print("Part 1: {}".format(search_paths("start", "end", adj_list, {"start"}, 0, dict())))
t2 = time()
print("Time (s): {}".format(t2 - t1))
print("Part 2: {}".format(search_paths("start", "end", adj_list, {"start"}, 1, dict())))
t3 = time()
print("Time (s): {}".format(t3 - t2))
print("With 2 revisits: {}".format(search_paths("start", "end", adj_list, {"start"}, 2, dict())))
t4 = time()
print("Time (s): {}".format(t4 - t3))
print("With 100 revisits: {}".format(search_paths("start", "end", adj_list, {"start"}, 100, dict())))
t5 = time()
print("Time (s): {}".format(t5 - t4))
