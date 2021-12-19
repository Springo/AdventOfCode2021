from copy import deepcopy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


all_rots = [
    "",
    "x",
    "y",
    "xx",
    "xy",
    "yx",
    "yy",
    "xxx",
    "xxy",
    "xyx",
    "xyy",
    "yxx",
    "yyx",
    "yyy",
    "xxxy",
    "xxyx",
    "xxyy",
    "xyxx",
    "xyyy",
    "yxxx",
    "yyyx",
    "xxxyx",
    "xyxxx",
    "xyyyx"
]


def recenter(points, old_c, new_c):
    old_cx, old_cy, old_cz = old_c
    new_cx, new_cy, new_cz = new_c
    dx = old_cx - new_cx
    dy = old_cy - new_cy
    dz = old_cz - new_cz

    new_points = set()
    for p in points:
        px, py, pz = p
        new_p = (px - dx, py - dy, pz - dz)
        new_points.add(new_p)

    return new_points, (dx, dy, dz)


def orient(point, rots):
    new_point = list(point)[:]
    for r in rots:
        new_new_point = None
        if r == 'x':
            new_new_point = new_point[:]
            new_new_point[1] = -new_point[2]
            new_new_point[2] = new_point[1]
        elif r == 'y':
            new_new_point = new_point[:]
            new_new_point[0] = new_point[2]
            new_new_point[2] = -new_point[0]
        new_point = new_new_point
    return tuple(new_point)


def orient_all(points, rots):
    new_points = set()
    for p in points:
        new_points.add(orient(p, rots))
    return new_points


def match(p1, p2):
    count = 0
    for p in p1:
        if p in p2:
            count += 1
    return count


def find_match(all_beacons, s):
    for r in all_rots:
        s_rot = orient_all(s, r)
        for p1 in all_beacons:
            for p2 in s_rot:
                s_trans, scan_coords = recenter(s_rot, p2, p1)
                count = match(all_beacons, s_trans)
                if count > 11:
                    return s_trans, scan_coords
    return None, None


def man_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2])


scanners = []
coords = set()
lines = readFile("d19input.txt")
for line in lines:
    if len(line) == 0:
        scanners.append(coords)
        coords = set()
    elif line[0] == '-' and line[1] == '-':
        continue
    else:
        ls = line.split(',')
        coords.add((int(ls[0]), int(ls[1]), int(ls[2])))


start = scanners[0]
scan_locs = [(0, 0, 0)]
all_beacons = set()
all_beacons = all_beacons.union(start)
remaining_scanners = list(range(1, len(scanners)))
done = False
last_all_beacons = deepcopy(all_beacons)
while not done:
    found_i = set()
    for i in remaining_scanners:
        s = scanners[i]
        new_beacons, scan_coords = find_match(all_beacons, s)
        if new_beacons is not None:
            all_beacons = all_beacons.union(new_beacons)
            scan_locs.append(scan_coords)
            found_i.add(i)

    for idx in found_i:
        remaining_scanners.remove(idx)
    if all_beacons == last_all_beacons:
        done = True
    last_all_beacons = deepcopy(all_beacons)


print(len(all_beacons))

largest = 0
for s1 in scan_locs:
    for s2 in scan_locs:
        dist = man_dist(s1, s2)
        if dist > largest:
            largest = dist
print(largest)
