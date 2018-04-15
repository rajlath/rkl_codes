from bisect import insort


N, M = [int(x) for x in input().split()]
marked = [False] * N
edges = []

for _ in range(N):
    edges.append([])

for _ in range(M):
    x, y, r = [int(x) - 1 for x in input().split()]
    edges[x].append([r+1, y])
    edges[y].append([r+1, x])

S = int(input()) - 1
q = [[0, 0, S]]

s = 0

while q:
    d, _, x = q.pop(0)
    if marked[x]: continue

    marked[x] = True
    s += d

    for w, t in filter(lambda n: not marked[n[1]], edges[x]):
        insort(q, [w, t+x, t])

print(s)