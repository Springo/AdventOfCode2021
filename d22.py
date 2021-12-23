def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def get_intersection(c1, c2):
    def get_diff(x1, x2):
        a1, a2 = x1
        b1, b2 = x2
        if a2 < b1 or b2 < a1:
            return None, None

        if a1 <= b1 and a2 >= b2:
            return (b1, b2)
        if b1 <= a1 and b2 >= a2:
            return (a1, a2)
        if a1 <= b1 and a2 <= b2:
            return (b1, a2)
        if b1 <= a1 and b2 <= a2:
            return (a1, b2)

    x1, y1, z1 = c1
    x2, y2, z2 = c2

    new_x1, new_x2 = get_diff(x1, x2)
    new_y1, new_y2 = get_diff(y1, y2)
    new_z1, new_z2 = get_diff(z1, z2)

    if new_x1 is None or new_y1 is None or new_z1 is None:
        return None, None, None

    return (new_x1, new_x2), (new_y1, new_y2), (new_z1, new_z2)


def cube_subtract(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = get_intersection(c1, c2)
    if x2 is None:
        return [c1]

    x1 = list(x1)
    y1 = list(y1)
    z1 = list(z1)

    new_cubes = []

    if x2[0] > x1[0]:
        new_cubes.append(((x1[0], x2[0] - 1), (y1[0], y1[1]), (z1[0], z1[1])))
        x1[0] = x2[0]

    if x2[1] < x1[1]:
        new_cubes.append(((x2[1] + 1, x1[1]), (y1[0], y1[1]), (z1[0], z1[1])))
        x1[1] = x2[1]

    if y2[0] > y1[0]:
        new_cubes.append(((x1[0], x1[1]), (y1[0], y2[0] - 1), (z1[0], z1[1])))
        y1[0] = y2[0]

    if y2[1] < y1[1]:
        new_cubes.append(((x1[0], x1[1]), (y2[1] + 1, y1[1]), (z1[0], z1[1])))
        y1[1] = y2[1]

    if z2[0] > z1[0]:
        new_cubes.append(((x1[0], x1[1]), (y1[0], y1[1]), (z1[0], z2[0] - 1)))
        z1[0] = z2[0]

    if z2[1] < z1[1]:
        new_cubes.append(((x1[0], x1[1]), (y1[0], y1[1]), (z2[1] + 1, z1[1])))
        z1[1] = z2[1]

    return new_cubes


class CubeMass:
    def __init__(self):
        self.cubes = []

    def subtract_cube(self, c):
        new_cubes = []
        for c1 in self.cubes:
            subs = cube_subtract(c1, c)
            new_cubes.extend(subs)
        self.cubes = new_cubes

    def add_cube(self, c):
        to_add = [c]
        inter_cubes = []
        for c1 in self.cubes:
            result = get_intersection(c, c1)
            if result[0] is not None:
                inter_cubes.append(c1)
        for c1 in inter_cubes:
            new_to_add = []
            for c2 in to_add:
                subs = cube_subtract(c2, c1)
                new_to_add.extend(subs)
            to_add = new_to_add

        self.cubes.extend(to_add)

    def _cube_vol(self, c):
        x, y, z = c
        return ((x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1))

    def get_volume(self):
        total = 0
        for c in self.cubes:
            total += self._cube_vol(c)
        return total


lines = readFile("d22input.txt")
p1_cube = ((-50, 50), (-50, 50), (-50, 50))

on_cubes = []
off_cubes = []
p1_mass = CubeMass()
p2_mass = CubeMass()
for line in lines:
    ls1 = line.split(' ')
    mode = ls1[0]
    ls2 = ls1[1].split(',')
    bx = [int(x) for x in ls2[0].split('=')[1].split('..')]
    by = [int(x) for x in ls2[1].split('=')[1].split('..')]
    bz = [int(x) for x in ls2[2].split('=')[1].split('..')]

    new_cube = (bx, by, bz)
    new_cube_aug = get_intersection(new_cube, p1_cube)

    if mode == "on":
        if new_cube_aug[0] is not None:
            p1_mass.add_cube(new_cube_aug)
        p2_mass.add_cube(new_cube)
    elif mode == "off":
        if new_cube_aug[0] is not None:
            p1_mass.subtract_cube(new_cube_aug)
        p2_mass.subtract_cube(new_cube)

print(p1_mass.get_volume())
print(p2_mass.get_volume())
