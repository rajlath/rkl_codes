from collections import defaultdict as df
import heapq

def bfs(root, n, edges):
    q = []
    v = [0] * (n+1)
    dist = [0] * (n + 1)
    q=[root]
    v[root]=1
    while len(q)>0:
        node=q[0]
        for i in edges[node]:
            if v[i]==0:
                v[i]=1
                dist[i]=dist[node]+1
                q.append(i)
        q.pop(0)
    return dist


n, m = [int(x) for x in input().split()]
edges = df(list)
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    edges[a].append(b)
    edges[b].append(a)
print(edges)
u, v = [int(x) for x in input().split()]
udist = bfs(u, n, edges)
vdist = bfs(v, n, edges)
print(udist, vdist)
for _ in range(int(input())):
    city = int(input())
    if udist[city] + vdist[city] ==  udist[v]:
        print("YES")
    else:
        print("NO")

#[1, 0, 1, 2] [3, 2, 1, 0, 0]#

