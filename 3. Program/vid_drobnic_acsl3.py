# Vid Drobnič
# Gimnazija Vič, 4.b
# Intermediate 3
# Language: Python 3.6

moves = [(0, 0), (0, -1), (0, -2), (0, 1), (0, 2), (-1, 0), (-2, 0), (1, 0), (2, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

for _ in range(5):
    data = input().split()
    r = int(data[0])
    column_data = [list(map(int, list(i))) for i in data[1:r+1]]
    n = int(data[r+1])
    press_data = [list(map(int, list(i))) for i in data[-n:]]

    board = [[False for i in range(8)] for j in range(8)]

    for column in column_data:
        c = column[0]-1
        for i in column[1:]:
            board[c][i-1] = True

    for press in press_data:
        for move in moves:
            y = press[0] + move[0] - 1
            x = press[1] + move[1] - 1
            if y < 0 or y > 7 or x < 0 or x > 7:
                continue
            board[y][x] = not board[y][x]

    count = 0
    for line in board:
        count += sum(line)
    print(count)
