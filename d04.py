import grid_util as gdu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def check_bingo(board, row, col):
    val = 0
    for i in range(5):
        val += board[row][i]
    if val == 5:
        return 1
    val = 0
    for i in range(5):
        val += board[i][col]
    if val == 5:
        return 2
    return 0

lines = readFile("d04input.txt")
nums = [int(x) for x in lines[0].split(',')]

new_lines = []
for line in lines[2:]:
    if len(line) > 1:
        ls = line.split()
        new_lines.append(ls)
lines = new_lines

boards = []
board_check = []
i = 0
while i < len(lines):
    boards.append(gdu.convert_to_grid(lines[i:i+5]))
    new_board = [[0] * 5 for _ in range(5)]
    board_check.append(new_board)
    i += 5

last_winner = -1
win_num = -1
win_num_id = -1
won = set()
for idx, x in enumerate(nums):
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == x:
                    board_check[i][j][k] = 1
                    result = check_bingo(board_check[i], j, k)
                    if result != 0:
                        if last_winner == -1:
                            unmark = 0
                            for i2 in range(len(boards[i])):
                                for j2 in range(len(boards[i][i2])):
                                    if board_check[i][i2][j2] == 0:
                                        unmark += boards[i][i2][j2]
                            print(unmark * x)
                        if i not in won:
                            won.add(i)
                            last_winner = i
                            win_num = x
                            win_num_id = idx

for i in range(len(board_check)):
    board_check[i] = [[0] * 5 for _ in range(5)]

for idx in range(win_num_id + 1):
    x = nums[idx]
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == x:
                    board_check[i][j][k] = 1


unmark = 0
for i2 in range(len(boards[last_winner])):
    for j2 in range(len(boards[last_winner][i2])):
        if board_check[last_winner][i2][j2] == 0:
            unmark += boards[last_winner][i2][j2]
print(unmark * win_num)
