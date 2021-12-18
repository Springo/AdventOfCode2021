import ast


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d18input.txt")
raw_pairs = []
for line in lines:
    raw_pairs.append(ast.literal_eval(line))


class Tree:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        return "[{},{}]".format(self.left, self.right)


def convert_to_tree(nums):
    root = Tree()
    if isinstance(nums, list):
        root.left = convert_to_tree(nums[0])
        root.right = convert_to_tree(nums[1])
    else:
        root.val = nums
    return root


def add_trees(t1, t2):
    root = Tree()
    root.left = t1
    root.right = t2
    return root


def explode_tree(t, depth=0):
    if t.val is not None:
        return None, None
    else:
        if depth >= 4:
            return t, None
        else:
            ex, pa = explode_tree(t.left, depth=depth+1)
            if ex is not None:
                if pa is None:
                    pa = t
                return ex, pa
            else:
                ex, pa = explode_tree(t.right, depth=depth+1)
                if ex is not None and pa is None:
                    pa = t
                return ex, pa


def split_tree(t):
    if t.val is not None:
        if t.val >= 10:
            return True, False
        return False, False

    spl, proc = split_tree(t.left)
    if spl:
        if not proc:
            s_val = t.left.val // 2
            s_rem = t.left.val % 2
            t.left.val = None
            t.left.left = Tree(s_val)
            t.left.right = Tree(s_val + s_rem)
            return spl, True
        return spl, proc

    spl, proc = split_tree(t.right)
    if spl:
        if not proc:
            s_val = t.right.val // 2
            s_rem = t.right.val % 2
            t.right.val = None
            t.right.left = Tree(s_val)
            t.right.right = Tree(s_val + s_rem)
            return spl, True
        return spl, proc

    return False, False


def get_leftmost(t):
    if t.val is not None:
        return t
    return get_leftmost(t.left)


def get_rightmost(t):
    if t.val is not None:
        return t
    return get_rightmost(t.right)


def get_borders(t, s_t):
    if t.val is not None:
        return False, None, None

    if t is s_t:
        return True, None, None

    true_l = None
    true_r = None
    result, l, r = get_borders(t.left, s_t)
    if result:
        if l is not None:
            true_l = l
        if r is not None:
            true_r = r
        else:
            true_r = get_leftmost(t.right)

        return True, true_l, true_r

    result, l, r = get_borders(t.right, s_t)
    if result:
        if l is not None:
            true_l = l
        else:
            true_l = get_rightmost(t.left)
        if r is not None:
            true_r = r

        return True, true_l, true_r

    return False, None, None


def magnitude(t):
    if t.val is not None:
        return t.val
    return 3 * magnitude(t.left) + 2 * magnitude(t.right)


def reduce(t):
    done = False
    while not done:
        passed = True
        ex, ex_pa = explode_tree(t, depth=0)
        if ex is not None:
            passed = False
            _, l, r = get_borders(t, ex)
            if l is not None:
                l.val += ex.left.val
            if r is not None:
                r.val += ex.right.val

            if ex is ex_pa.left:
                ex_pa.left = Tree()
                ex_pa.left.val = 0
            elif ex is ex_pa.right:
                ex_pa.right = Tree()
                ex_pa.right.val = 0
            else:
                print("ERROR")

        if passed:
            spl, _ = split_tree(t)
            if spl:
                passed = False

        done = passed


result = convert_to_tree(raw_pairs[0])
for pair in raw_pairs[1:]:
    result = add_trees(result, convert_to_tree(pair))
    reduce(result)

print(magnitude(result))

best = 0
for p1 in raw_pairs:
    for p2 in raw_pairs:
        t1 = convert_to_tree(p1)
        t2 = convert_to_tree(p2)
        result = add_trees(t1, t2)
        reduce(result)
        mag = magnitude(result)
        if mag > best:
            best = mag
print(best)
