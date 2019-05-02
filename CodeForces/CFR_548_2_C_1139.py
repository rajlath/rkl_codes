
# -*- coding: utf-8 -*-
# @Date    : 2019-03-22 08:08:26
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

vertices, limit = RMI()
graph = [[] for _ in range(vertices)]
for i in range(vertices - 1):
    u, v, x = RMI()
    graph[u - 1].append((v - 1, x))
    graph[v - 1].append((u - 1, x))
done = [0 for _ in range(vertices)]
comps = []
for i in range(vertices):
    if done[i]:continue
    done[i] = 1
    comps.append([i])
    qu = [i]
    while qu:
        curr_u = qu[0]
        qu = qu[1:]
        for u, x in graph[curr_u]:
            if x == 0 and done[u] == 0:
                qu.append(u)
                done[u] = 1
                comps[-1].append(u)
answer = vertices ** limit

for comp in comps:
    answer -= len(comp) ** limit

print( answer % (10 ** 9 + 7))