import sys
sys.setrecursionlimit(1000000)
dirs = {}
dirs['n'] = [[-1, 0], [0, 1], [0, -1], [1, 0]]
dirs['e'] = [[0, 1], [-1, 0], [1, 0], [0, -1]]
dirs['s'] = [[1, 0], [0, 1], [0, -1], [-1, 0]]
dirs['w'] = [[0, -1], [-1, 0], [1, 0], [0, 1]]

'''
4
n
0 0
'''
matn = int(input())
wind = input()
x1, y1 = [int(x) for x in input().split()]
grid = [[0]*matn for i in range(matn)]
visited = [[0]*matn for i in range(matn)]
t = 1

def dfs(x, y, t):
    visited[x][y] = t
    for i in dirs[wind]:
        dx = x + i[0]
        dy = y + i[1]
        if dx >=0 and dx < matn and dy >=0 and dy < matn and not visited[dx][dy]:
            dfs(dx, dy, t+1)
dfs(x1, y1, t)
for i in visited:
    print(*i)






