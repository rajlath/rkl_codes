# numpy and scipy are available for use
'''
5 7 2
1 2
2 1
2 2
3 2
2 5
5 3
4 5

1 0 2 -1 1
'''

def bfs(v):
    global dist,adj
    dist[v] = 0
    queue  = [v]
    visited[v] = 1
    while queue:
        curr = queue.pop()
        for neigh in adj[curr]:
            if not visited[neigh]:
                visited[neigh] = 1
                dist[neigh] = dist[curr] + 1
                queue = [neigh] + queue
n, m, sn = [int(x) for x in input().split()]
adj = [[] for y in range(n)]
for _ in range(m):
    u, v = [int(x)-1 for x in input().split()]
    adj[u].append(v)
dist = [-1] * (n)
visited = [0] * (n)
bfs(sn-1)
print(*dist)
