
# -*- coding: utf-8 -*-
# @Date    : 2019-03-15 21:33:34
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/INOIPRAC/problems/INOI1402
# @Version : Free Ticket 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

ans = min_val
nb_cities, nb_flights = RMI()
graph = [[max_val for _ in range(nb_cities)] for _ in range(nb_cities)]
for i in range(nb_cities):
    graph[i][i] = 0
for _ in range(nb_flights)    :
    src,tgt, cost = RMI()
    graph[src - 1][tgt - 1] = cost
    graph[tgt - 1][src - 1] = cost

for k in range(nb_cities):
    for i in range(nb_cities):
        for j in range(nb_cities):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(nb_cities):
    for j in range(nb_cities):
        ans = max(graph[i][j], ans)

print(ans)




