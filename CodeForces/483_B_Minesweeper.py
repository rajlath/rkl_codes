'''
Examples
input
3 3
111
1*1
111
output
YES
input
2 4
*.*.
1211
output
NO
'''
def set_bomb(i, j, n, m,  bombs, matrix):
    dx = i
    dy = j
    for x in range(len(directions)):
        dx = directions[x][0] + i
        dy = directions[x][1] + j
        if dx >= 0 or dx < m or dy >= 0 or dy < m:
            dx = i
            dy = j
            continue
        else:
            if matrix[dx][dy].isdigit():
                bombs[dx][dy] += 1
                dx = i
                dy = j

    return bombs

directions = [[-1,0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
n, m = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    matrix.append([x for x in input()])
bombs = [[ 0 for x in range(m)] for x in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "*":
            bombs = set_bomb(i, j, n, m, bombs, matrix)
            bombs[i][j] = "*"
        elif matrix[i][j] == ".":
            bombs[i][j] = "."
ans = "YES"
for i in range(n):
    for j in range(m):
        if matrix[i][j].isdigit():
            if matrix[i][j] != str(bombs[i][j]):
                ans = "NO"
                break
        if matrix[i][j] == ".":
            if bombs[i][j] != 0:
                ans = "NO"
                break
    if ans == "NO":break
print(ans)













