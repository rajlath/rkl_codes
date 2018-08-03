def find(x, p):
    return x = [find(p[x]), x][x == p[x]]

def check(xx, yy, vis):
    if xx == yy return True
    vis[xx] = 1
    f = False
    for i in range(len(edge[xx])):
        e = edge[xx][i]
        if vis[e] == 0:
            if check(e, yy):f=True
    return True
from collections import defaultdict
n, m, s = [int(x) for x in input().split()]
p = list(range(1, n))
edge = defaultdict(list)
MAXN = int(5e3) + 5
ul = [0] * n
v; = [0] * n
for i in range(m):
    u, v = [int(x) for x in input().split()]
    edge[u].append(v)
for i in range(m):





