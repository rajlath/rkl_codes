
# -*- coding: utf-8 -*-
# @Date    : 2019-06-15 20:02:29
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
from collections import defaultdict

nb_points = RI()
points    = [RMI() for _ in range(nb_points)]
if nb_points == 1:
    print(1)
else:
    pq = defaultdict(int)
    for i in range(nb_points):
        for j in range(nb_points):
            if i == j : continue
            p1 = points[i][0] - points[j][0]
            q1 = points[i][1] - points[j][1]
            pq[(p1, q1)]  = pq.get((p1, q1), 0) + 1
    print(nb_points - max(pq.values()))
