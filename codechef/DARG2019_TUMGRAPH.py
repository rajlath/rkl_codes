
# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 22:12:39
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import gcd
from collections import defaultdict

sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

class Graph():
    def __init__(self, n):
        self.count = 0
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u] += [v]

    def DFSHelper(self, v, visited):
        visited[v] = True
        self.count += 1
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSHelper(i, visited)

    def DFS(self, v):
        visited = [False for j in range(len(self.graph))]
        self.DFSHelper(v, visited)

n = RI()
a = [RI() for _ in range(n)]
g = Graph(n)
for x in range(n):
    for y in range(x + 1, n):
        if gcd(a[x], a[y]) != 1:
            g.add_edge(x, y)
            g.add_edge(y, x)

g.DFS(0)
print(0 if g.count != n else 1)


