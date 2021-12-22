input_p1 = 8
input_p2 = 9

p1_pos = input_p1
p2_pos = input_p2
done = False
dc = 0
rolls = 0
p1_score = 0
p2_score = 0
while not done:
    move = 3 * dc + 6
    dc = (dc + 3) % 100
    rolls += 3
    p1_pos = (p1_pos + move - 1) % 10 + 1
    p1_score += p1_pos
    if p1_score >= 1000:
        done = True
        print(p2_score * rolls)
        break

    move = 3 * dc + 6
    dc = (dc + 3) % 100
    rolls += 3
    p2_pos = (p2_pos + move - 1) % 10 + 1
    p2_score += p2_pos
    if p2_score >= 1000:
        done = True
        print(p1_score * rolls)
        break


rolls = [1, 2, 3]


def outcomes(p1_pos, p2_pos, p1_score, p2_score, turn, win_thresh, memo):
    key = (p1_pos, p2_pos, p1_score, p2_score, turn)
    if key in memo:
        return memo[key]
    t1 = 0
    t2 = 0
    for r1 in rolls:
        for r2 in rolls:
            for r3 in rolls:
                tr = r1 + r2 + r3
                if turn == 1:
                    new_p1_pos = (p1_pos + tr - 1) % 10 + 1
                    new_p1_score = p1_score + new_p1_pos
                    if new_p1_score >= win_thresh:
                        t1 += 1
                    else:
                        n1, n2 = outcomes(new_p1_pos, p2_pos, new_p1_score, p2_score, 2, win_thresh, memo)
                        t1 += n1
                        t2 += n2
                elif turn == 2:
                    new_p2_pos = (p2_pos + tr - 1) % 10 + 1
                    new_p2_score = p2_score + new_p2_pos
                    if new_p2_score >= win_thresh:
                        t2 += 1
                    else:
                        n1, n2 = outcomes(p1_pos, new_p2_pos, p1_score, new_p2_score, 1, win_thresh, memo)
                        t1 += n1
                        t2 += n2

    memo[key] = (t1, t2)
    return t1, t2


print(max(outcomes(input_p1, input_p2, 0, 0, 1, 21, dict())))
