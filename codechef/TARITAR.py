
from collections import defaultdict
def dfs(source, target):
    global a, d, adj, t
    t += 1
    a[source] = t
    for i in range(len(adj[source])):
        if adj[u][i] != target:
            dfs(adj[u][i], u)
    d[u] = t



nots = int(input())
for _ in range(nots):
    num_node, num_query, tarini_node = [int(x) for x in input().split()]
    tarini_node -= 1
    adj = defaultdict(list)
    a = [0] * num_node
    d = [0] * num_node
    for i in range( num_node-1):
        u, v = [int(x)-1 for x in input().split()]
        adj[u].append(v)
        adj[v].append(u)
    print(adj)
    t = 0
    dfs(tarini_node, -1)

    for i in range(num_query):
        u, v = [int(x)-1 for x in input().split()]
        if a[v] >= a[u] and a[v] <= d[u]:
            print("Taran")
        else:
            print("Sakub-Jafin")





