import heapq
from copy import deepcopy


class State:
    def __init__(self, hall, pits):
        self.hall = hall
        self.pits = pits

    def serialize(self):
        rep = []
        rep.extend(self.hall)
        for p in self.pits:
            rep.extend(p)
        return tuple(rep)

    def check_pit(self, i):
        top = len(self.pits[i])
        check = True
        for j, h in enumerate(self.pits[i]):
            if h != 0:
                if top == len(self.pits[i]):
                    top = j
                if h != i + 1:
                    check = False
        return check, top

    def get_reachable(self, i):
        r_bound = len(self.hall)
        l_bound = -1
        for j in range(len(self.hall) - (i + 2)):
            if self.hall[i + 2 + j] != 0:
                r_bound = i + 2 + j
                break

        for j in range(i + 2):
            if self.hall[i + 1 - j] != 0:
                l_bound = i + 1 - j
                break
        return l_bound, r_bound

    def get_neighbor(self):
        neighbors = []
        for i, p in enumerate(self.pits):
            check, top = self.check_pit(i)
            l_bound, r_bound = self.get_reachable(i)

            # move out of pits
            if not check:
                for j in range(l_bound + 1, r_bound):
                    new_hall = deepcopy(self.hall)
                    new_pits = deepcopy(self.pits)
                    new_hall[j] = p[top]
                    new_pits[i][top] = 0
                    ne = State(new_hall, new_pits)
                    if j == 0:
                        dist = top + 2 + 2 * (i + 1 - 1) + 1
                    elif j <= i + 1:
                        dist = top + 2 + 2 * (i + 1 - j)
                    elif j == len(self.hall) - 1:
                        dist = top + 2 + 2 * (len(self.hall) - 2 - (i + 2)) + 1
                    elif j >= i + 2:
                        dist = top + 2 + 2 * (j - (i + 2))
                    else:
                        print("ERROR")
                        dist = -1
                    val = 10 ** (p[top] - 1) * dist
                    neighbors.append((ne, val))
            # move into pits
            else:
                if l_bound >= 0 and self.hall[l_bound] == i + 1:
                    new_hall = deepcopy(self.hall)
                    new_pits = deepcopy(self.pits)
                    new_hall[l_bound] = 0
                    new_pits[i][top - 1] = self.hall[l_bound]
                    ne = State(new_hall, new_pits)
                    if l_bound == 0:
                        val = 10 ** (self.hall[l_bound] - 1) * (top + 1 + 2 * (i + 1 - l_bound) - 1)
                    else:
                        val = 10 ** (self.hall[l_bound] - 1) * (top + 1 + 2 * (i + 1 - l_bound))
                    neighbors.append((ne, val))
                if r_bound < len(self.hall) and self.hall[r_bound] == i + 1:
                    new_hall = deepcopy(self.hall)
                    new_pits = deepcopy(self.pits)
                    new_hall[r_bound] = 0
                    new_pits[i][top - 1] = self.hall[r_bound]
                    ne = State(new_hall, new_pits)
                    if r_bound == len(self.hall) - 1:
                        val = 10 ** (self.hall[r_bound] - 1) * (top + 1 + 2 * (r_bound - (i + 2)) - 1)
                    else:
                        val = 10 ** (self.hall[r_bound] - 1) * (top + 1 + 2 * (r_bound - (i + 2)))
                    neighbors.append((ne, val))

        return neighbors

    def __repr__(self):
        rep = ""
        for h in self.hall:
            if h == 0:
                rep = rep + ". "
            else:
                rep = rep + "{} ".format(h)

        rep = rep + "\n"
        for j in range(len(self.pits[0])):
            rep = rep + "   "
            for i in range(len(self.pits)):
                if self.pits[i][j] == 0:
                    rep = rep + ". "
                else:
                    rep = rep + "{} ".format(self.pits[i][j])
            rep = rep + " \n"

        return rep

    def __hash__(self):
        return hash(self.serialize())

    def __eq__(self, other):
        return self.serialize() == other.serialize()


def shortest_path(s, t):
    q = []
    heapq.heappush(q, (0, 0, 0, s))
    min_v = {s: 0}
    final = {}
    idx = 0
    while len(q) > 0:
        cx = heapq.heappop(q)
        _, val, _2, c = cx

        if c not in final:
            if c == t:
                return val
            final[c] = val

            nes = c.get_neighbor()
            for nex in nes:
                ne, vne = nex
                if ne not in final:
                    heur = heuristic(ne)
                    if ne not in min_v or val + vne + heur < min_v[ne]:
                        min_v[ne] = val + vne + heur
                        heapq.heappush(q, (val + vne + heur, val + vne, idx, ne))
                        idx += 1

    return -1


def heuristic(s):
    p_dist = {
        0: [0, 0, 0, 0, 0, 0, 0],
        1: [3, 2, 2, 4, 6, 8, 9],
        2: [50, 40, 20, 20, 40, 60, 70],
        3: [700, 600, 400, 200, 200, 400, 500],
        4: [9000, 8000, 6000, 4000, 2000, 2000, 3000]
    }
    total = 0
    for i, h in enumerate(s.hall):
        total += p_dist[h][i]

    for i in range(len(s.pits)):
        for j in range(len(s.pits[i])):
            c = s.pits[i][j]
            if c != 0 and c != i + 1:
                left_ind = i + 1
                right_ind = i + 2
                total += min(p_dist[c][left_ind], p_dist[c][right_ind]) + (10 ** (c - 1) * (j + 2))

    return total


s1_halls = [0, 0, 0, 0, 0, 0, 0]
s1_pits = [
    [4, 2],
    [2, 4],
    [1, 1],
    [3, 3]
]
t1_halls = [0, 0, 0, 0, 0, 0, 0]
t1_pits = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4]
]


s2_halls = [0, 0, 0, 0, 0, 0, 0]
s2_pits = [
    [4, 4, 4, 2],
    [2, 3, 2, 4],
    [1, 2, 1, 1],
    [3, 1, 3, 3]
]
t2_halls = [0, 0, 0, 0, 0, 0, 0]
t2_pits = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]
]


start = State(s1_halls, s1_pits)
end = State(t1_halls, t1_pits)
print(shortest_path(start, end))

start = State(s2_halls, s2_pits)
end = State(t2_halls, t2_pits)
print(shortest_path(start, end))
