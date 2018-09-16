#-------------------------------------------------------------------------------
# Name:        LOCJUL18_COLCHEF
# Purpose:
#
# Author:      oorja_rinfo_raj
#
# Created:     30/07/2018
# Copyright:   (c) rinfo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from collections import defaultdict
class Graph():
    def __init__(self,vertices):
        self.V     = vertices
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected(self, s, d):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            n = queue.pop(0)
            if n == d:return True
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
            return False

graph = Graph(int(input()))
for _ in range(int(input())):
    c, u, v = [int(x) for x in input().split()]
    if c is 0: graph.add_edge(u, v)
    if c is 1: print(["NO", "YES"][graph.is_connected(u, v) or graph.is_connected(v, c)])





def main():
    pass

if __name__ == '__main__':
    main()
