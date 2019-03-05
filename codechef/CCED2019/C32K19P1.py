
# -*- coding: utf-8 -*-
# @Date    : 2019-02-28 09:16:20
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
import heapq
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


nb_vertices, nb_edges = RI(), RI()
connections = [[] for i in range(nb_vertices)]
current, distances, durations, fares = {}, {}, {}, {}
for i in range(nb_edges):
    src, dest, fare, distance, duration = RMI()
    src -= 1
    dest -= 1
    connections[src].append(dest)
    fares[(src, dest)] = fare
    distances[(src, dest)] = distance
    durations[(src, dest)] = duration
src, dest = RMI()
src -= 1
dest -= 1
in_line = [(0, src)]
task = RI()

if   task == 1: current = fares.copy()
elif task == 2: current = distances.copy()
else: current  = durations.copy()

dp = [max_val for i in range(nb_vertices)]
visited = [0 for i in range(nb_vertices)]
while in_line:
    cst, root = in_line[0]
    heapq.heappop(in_line)
    dp[root] = min(dp[root], cst)
    if visited[root] == 0:
        visited[root] = 1
        for i in connections[root]:
            if visited[i] == 0:
                heapq.heappush(in_line, (cst + current[(root, i)], i))
print(dp[dest])

