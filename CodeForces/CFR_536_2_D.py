from heapq import heappop, heappush

n, m = [int(x) for x in input().split()]
a = []
as_ = set()
g = [set() for _ in range(n + 2)]
for _ in range(m):
    u, v = [int(x) for x in input().split()]
    g[u].add(v)
    g[v].add(u)

h = [1]
while h:
    u = heappop(h)
    if u not in as_:
        a.append(u)
        as_.add(u)

        for v in g[u]:
            heappush(h, v)
print(*a)

