from math import gcd
from collections import defaultdict

class Graph():
    def __init__(self, n):
        self.count = 0
        self.graph = defaultdict(list)
        for i in range(n):
            self.graph[i] = []

    def addEdge(self, u, v):
        self.graph[u] += [v]

    def DFSUtil(self, v, visited):
        visited[v] = True
        self.count += 1
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False for j in range(len(self.graph))]
        self.DFSUtil(v, visited)

n = int(input())
a = []
for j in range(n):
    a += [int(input())]

g = Graph(n)
for x in range(n):
    for y in range(x+1, n):
        if gcd(a[x], a[y]) != 1:
            g.addEdge(x, y)
            g.addEdge(y, x)

# print(g.graph)

g.DFS(0)

ans = g.count
if ans != n:
    print(0)
else:
    print(1)


