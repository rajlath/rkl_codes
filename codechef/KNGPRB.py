'''
Given a directed graph have V vertex and E edges
find if it is possible to go from source to destination
by converting some of the edges to bidirectional
answer would be nos of edges that need to be converted
and -1 if not possible
sample
Input Test 1
1
7 7
1 2
2 4
1 3
5 3
5 6
6 4
7 5
1 7
output Test 1
2

Input Test 2
1
10 9
 1 2
 2 4
 1 3
 5 3
 5 6
 6 4
 7 5
 9 10
 10 8
 1 10
output Test 2
-1
'''
# ttps://www.codechef.com/ENAU2018/problems/KNGPRB
# oorj oorja.halt#gmail.com
# 2018-08-13 10:16:12
# python 3,6
from collections import defaultdict
maxs = int(-10e16)
def bfs(adj, x, y):
    vis = [maxs] * (len(adj)+ 5)
    q = []
    q.append((x, 0))
    vis[x] = 0
    while q:
        u, w = q.pop(0)
        if u == y:return vis[u]
        for i in adj[u]:
            v, w = i
            if vis[v] > vis[u]+w:
                if vis[v] !=  maxs:
                    q.remove((v, vis[v]))
                vis[v] = vis[u] + w
                q.append((v.vis[v]))
    return -1



for _ in range(int(input())):
    city, road = [int(x) for x in input().split()]
    adj = defaultdict(list)
    for _ in range(road):
        u, v = [int(x) for x in input().split()]
        adj[u].append((v, 0))
        adj[v].append((u, 1))
    x, y = [int(x) for x in input().split()]
    print(adj)
    print(bfs(adj, x, y))

#incomplete 2018-08-13 10:43:34







