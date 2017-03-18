# Vid Drobnič
# Gimnazija Vič, 4.b
# Intermediate 3
# Python 3.6

import copy

table = [[0 for i in range(4)] for j in range(4)]
hint = [[[0, 0] for i in range(4)] for j in range(2)]

# Debug function
def print_table(table):
    for i in table:
        print(' '.join(map(str, i)))

def seen(skyscrapers):
    m = 0
    count = 0
    for sk in skyscrapers:
        if sk > m:
            m = sk
            count += 1
    return count

def find_empty(table):
    for i in range(4):
        if 0 in table[i]:
            return (i, table[i].index(0))
    return None

def is_solved(table):
    for i in range(4):
        row = table[i]
        if seen(row) != hint[0][i][0]:
            return False
        if seen(reversed(row)) != hint[0][i][1]:
            return False

        column = [table[j][i] for j in range(4)]
        if seen(column) != hint[1][i][0]:
            return False
        if seen(reversed(column)) != hint[1][i][1]:
            return False
    return True

def solve(table_):
    table = copy.deepcopy(table_)

    if find_empty(table) is None:
        return (is_solved(table), table)

    i, j = find_empty(table)
    not_allowed = set()
    for a in table[i]:
        not_allowed.add(a)
    for a in range(4):
        not_allowed.add(table[a][j])
    allowed = {1, 2, 3, 4}
    possible = allowed - not_allowed
    for a in possible:
        table[i][j] = a
        success, solved_table = solve(table)
        if success:
            return (True, solved_table)

    return (False, table)


data = input().split()
for i in range(4):
    hint[1][i][0] = int(data[0][i])
    hint[1][i][1] = int(data[5][i])

for i in range(1, 5):
    d = data[i]
    if len(d) == 2:
        hint[0][i-1][0] = int(d[0])
        hint[0][i-1][1] = int(d[1])
    else:
        hint[0][i-1][0] = int(d[0])
        hint[0][i-1][1] = int(d[5])

        for j in range(1, 5):
            table[i-1][j-1] = int(d[j])

success, solved = solve(table)

for _ in range(5):
    i, j = map(int, list(input()))
    print(solved[i-1][j-1])
