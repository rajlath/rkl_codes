from heapq import heappop, heappush;N, inf = 10**5 + 10, 10**18;n, m = map(int, input().split())
adj, visited, dist, parent = [[] for _ in range(N)], [False]*N, [inf]*N, [-1]*N
def dijkstra(src):
    pq, dist[src], parent[src] = [], 0, 0;heappush(pq, (0, src))
    while pq:
        curr_dist, u = heappop(pq)
        if visited[u]:continue
        visited[u] = True
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:dist[v] = dist[u] + w;parent[v] = u;heappush(pq, (dist[v], v))
for _ in range(m):
    u, v, w = map(int, input().split());adj[u].append((v, w));adj[v].append((u, w))
dijkstra(1)
if dist[n] >= inf:print(-1);exit()
stk, node = [], n
while node:stk.append(node);node = parent[node]
for node in reversed(stk):print(node, end=" ")
