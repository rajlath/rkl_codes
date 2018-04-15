c = 1000000007

n, m = [int(x) for x in input().split()]
grids = [[0 for x in range(m)] for y in range(n)]
for _ in range(int(input())):
    x, y, v = [int(x) for x in input().split()]
    grids[x][y] = v
ways = [[0 for x in range(m)] for y in range(n)]
ways[0][0] = 1
for i in range(n):
    for j in range(m):
        curr = grids[i][j]
        if curr == -1:
            continue
        if (i + 1) < n and grids[i+1][j] != -1:
            ways[i+1][j] = (ways[i+1][j] + ways[i][j])%c
        if (j + 1) < m and grids[i][j+1] != -1:
            ways[i][j+1] = (ways[i][j+1] + ways[i][j])%c
        if curr != 0:
            if i+v < n and grids[i+v][j] != -1:
                ways[i+v][j] = (ways[i+v][j] + ways[i][j])
            if j+v < m and grids[i][j+v] != -1 :
                ways[i][j+v] = (ways[i][j+v] + ways[i][j])
print(ways[n-1][m-1])

'''
5 5
4
0 2 -1
1 2 3
2 0 4
4 3 2
70
58
'''


