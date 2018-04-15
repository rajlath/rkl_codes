'''
3 2
1 2 4
1 3 5
1
3
'''
from collections import defaultdict
import heapq
n, m = [int(x) for x in input().split()]
distance = [int(10e8)]*n
visited   = [False] * n
edges = defaultdict(list)
for _ in range(m):
    a, b, w = [int(x) for x in input().split()]
    edges[a].append([w, b])
    edges[b].append([w, a])
que = []
print(distance)
for _ in range(int(input())):
    node = int(input())
    print(node)
    distance[node-1] = 0
    heapq.heappush(que, node-1)

while len(que)>0:
    curr = heapq.heappop(que)
    print(curr)
    v = curr[1]
    if not visited[v]:
        visited[v] = 1
        for j in range(len(edges[v])):
            f=edges[v][j][0]
            e=edges[v][j][1]
            if (distance[v] + f) < distance[e]:
                distance[e] = distance[v] + f
                heapq.heappush([distance[e], e])

for i in range(n):
    print(distance[i])


