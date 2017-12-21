from collections import defaultdict


def dfs(index, flag=0):
    global cost, clib, cpath, adj, color
    if flag==1:cost += clib
    else:
        cost += cpath
    color[index] = 1
    for i in range(len(adj[index])):
        vertex = adj[index][i]
        if not color[vertex]:dfs(vertex)
    return None

for _ in range(int(input())):
    color = [0] * 100010
    cost = 0
    n, m, clib, cpath = [int(x) for x in input().split()]
    adj = defaultdict(list)
    for i in range(m):
        u, v = [int(x) for x in input().split()]
        adj[u].append(v)
        adj[v].append(u)
    if clib < cpath:
        print(n * clib)
    else:
        for i in range(1, n+1):
            if color[i] == 0:
                dfs(i, 1)
        print(cost)

