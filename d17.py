def fire(xv, yv, tx, ty):
    x = 0
    y = 0
    tx1, tx2 = tx
    ty1, ty2 = ty
    max_y = 0
    while y > ty1 and x < tx2:
        x = x + xv
        y = y + yv
        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1
        yv -= 1
        if y > max_y:
            max_y = y

        if tx1 <= x <= tx2 and ty1 <= y <= ty2:
            return max_y
    return -1


tx = [282, 314]
ty = [-80, -45]

max_y = 0
counts = 0
for xv in range(tx[1] + 1):
    for yv in range(ty[0] - 1, 200):
        new_max = fire(xv, yv, tx, ty)
        if new_max != -1:
            counts += 1
        if new_max > max_y:
            max_y = new_max

print(max_y)
print(counts)

