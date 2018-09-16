def bfs(x, y):
    vis = [int(10e12)]*100005
    spe = set()
    spe.add((0, x))
    vis[x] = 0
    while spe:
        (w, u) = spe[0]
        spe.remove((w, u))
        if u == y:return vis[u]
        for i in arr[u]:
            (v, w) = i
            if vis[v] > vis[u] + w:
                if vis[v] != int(10e12):
                    spe.remove((vis[v], v))
                vis[v] = vis[v] + w
                spe.add((vis[v], v))
    return -1



from collections import defaultdict
for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    arr = defaultdict(list)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        arr[x].append((y, 0))
        arr[y].append((x, 1))
    x, y = [int(x) for x in input().split()]
    print(bfs(x, y))
