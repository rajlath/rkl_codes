
# -*- coding: utf-8 -*-
# @Date    : 2019-03-23 09:28:20
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


nb_songs, choose = RMI()
songval = []
for _ in range(nb_songs):
    songval.append(RMI())

songval.sort(key = lambda x: -x[1])

maxs = min_val
lsum = 0
choice = []
for i in range(nb_songs):
    ti, bi = songval[i]
    if len(choice) < choose:
        heapq.heappush(choice, ti)
        lsum += ti
    else:
        l = heapq.heappushpop(choice, ti)
        lsum += ti - l
    maxs = max(maxs, lsum * bi)
print(maxs)
