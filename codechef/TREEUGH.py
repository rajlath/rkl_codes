from collections import deque

n, q = [int(x) for x in input().split()]
ans  = [0] * (n+1)
ans[1:] = [int(x) for x in input().split()]
graph   = {i:[] for i in range(1, n+1)}
for i in range(n-1):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)
d = {}
for i in range(q):
    u, val = [int(x) for x in input().split()]
    try:
        d[u] += val
    except:
        d[u] = val
parents = [0 for i in range(n+1)]
visited = [0 for i in range(n+1)]
dq = deque([1])
visited[1] = 1
while dq:
    v = dq.popleft()
    #print(v, graph[v])
    for child in graph[v]:
        if not visited[child]:
            visited[child] = 1
            dq.append(child)
            parents[child] = v
for i in range(1, n+1):
    if i in d:
        ans[i] += d[i]
    x = parents[i]
    while x:
        if x in d:
            ans[i] += d[x]
        x = parents[x]
out = [str(ans[i]) for i in range(1, n+1)]
print(' '.join(out))
