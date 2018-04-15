def bellman_ford(graph, n_verices, n_edges, source):
    distances = [int(10e12)]*n_verices
    distances[source] = 0

    for v in range(1, n_verices):
        for e in range(n_edges):
            u, v, w = graph[e][0],graph[e][1],graph[e][2]
            if distances[u]!=int(10e12) and distances[u]+w < distances[v]:
                distances[v] = distances[u]+w
    return distances

g = []
n_verices = 5
n_edges   = 7
for _ in range(n_edges):
    g.append(([int(x) for x in input().split()]))
print(bellman_ford(g,5,7, 0))

