'''
Matrix Exploration
Time limit: 1000 ms
Memory limit: 128 MB

You are given a matrix of size N \times MN×M, where an empty cell is represented by a . ,
and a forbidden cell is represented by a #. You also know that KK of the empty cells are special.

For each empty cell you should compute the shortest distance to any special cell.
You should consider that two cells are adjacent if they share a common side. For the special cells the
computed value should be 00.

Standard input
First line contains three integers NN, MM and KK.
Each of the next NN lines contains MM characters, either . or #, representing the matrix.
Each of the next KK lines contains a pair of two integers XX and YY, representing the line and the
column of a special cell.

Standard output
Output a single number representing the sum of the computed distances for each empty cell.

Restrictions and notes
1 \leq N \leq 1 0001≤N≤1000
1 \leq M \leq 1 0001≤M≤1000
1 \leq K \leq 5001≤K≤500
1 \leq X \leq N1≤X≤N
1 \leq Y \leq M1≤Y≤M
It is guaranteed that there is a path from every empty cell to at least one special cell.
Input
6 6 2
.....#
.###.#
...#.#
.#####
.....#
######
3 5
5 3
Output
50
'''

n, m, k = [int(x) for x in input().split()]
mat = []
for i in range(n):
    mat.append([x for x in input()])

queue = []
dirX = [0, 0, -1, 1]
dirY = [-1, 1, 0, 0]
DP   = [[0 for x in range(m)] for y in range(n)]
for _ in range(k):
    x, y = [int(A) for A in input().split()]
    queue.append((x, y))
    DP[x][y] = 1


while queue:
    pos = queue.pop(0)
    for i in range(4):
        xx = pos[0] + dirX[i]
        yy = pos[1] + dirY[i]

        if xx < 0 or xx >= n or yy < 0 or yy >= m:continue
        if mat[xx][yy] != ".":continue
        if DP[xx][yy] != 0:continue
        DP[xx][yy] = DP[pos[0]][pos[1]] + 1
        queue.append((xx, yy))

ans = 0
for i in range(1,n)        :
    for j in range(1,m):
        if DP[i][j] > 0:
            ans += DP[i][j]-1
print(ans)








