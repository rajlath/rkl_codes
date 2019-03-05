def update_health(curr,health, lower, increase):
    if curr == "O":
        health -= lower
    elif curr == "+":
        health += increase
    return health

def spiral_sum(matrix, lens, lower, increase, health):
    # o decrease by lower
    # + increase by increase
    # h = curr health
    row_start = 0
    row_length= lens
    col_start = 0
    col_length = lens
    while row_start <= row_length and col_start <= col_length:
        for i in range(row_start, col_length+1):
            curr = matrix[row_start][i]
            health = update_health(curr,health, lower, increase)
            if health == 0:return 0
        for i in range(row_start+1, row_length+1):
            curr = matrix[i][col_length]
            health = update_health(curr, health, lower, increase)
            if health == 0:return 0
        if row_start + 1 <= row_length:
            for i in range(col_length - 1, col_start+1):
                curr = matrix[row_length][i]
                health = update_health(curr, health, lower, increase)
                if health == 0:return 0
        if col_start + 1 <= col_length:
            for i in range(row_length - 1, row_start, -1):
                curr = matrix[i][col_start]
                health = update_health(curr, health, lower, increase)
                if health == 0:return 0
        row_start += 1
        row_length -= 1
        col_start += 1
        col_start -= 1
    return health

matrix_dim = int(input())
l, i, h   = [int(x) for x in input().split()]
matrix = []
for i in range(matrix_dim):
    matrix.append([x for x in input().split()])
if spiral_sum(matrix,matrix_dim, h, l, i) == 0:
    print("NO")
else:
    print("YES")






