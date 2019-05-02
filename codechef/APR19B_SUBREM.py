
# -*- coding: utf-8 -*-
# @Date    : 2019-04-15 16:33:02
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


nb_test = RI()
for _ in range(nb_test):
    nb_nodes, xfactor = RMI()
    wieghts = RMI()
    visited = [False] * (nb_nodes + 1)
    adj= [list() for _ in range(nb_nodes + 1)]
    for i in range(nb_nodes - 1):
        frm, tos = RMI()
        adj[frm].append(tos)
        adj[tos].append(frm)
    def solve(node):
        visited[node] = True
        value = wieghts[node - 1]
        for n in adj[node]:
            if not visited[n]:
                value = max(value - xfactor, value + solve(n))
        return value

    result = max(-xfactor, solve(1))
    print(result)
