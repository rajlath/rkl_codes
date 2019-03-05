
# -*- coding: utf-8 -*-
# @Date    : 2019-02-28 11:16:19
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


nb_cows = RI()
milks = [RI() for _ in range(nb_cows) ]
milk_sums = sum(milks)
limit = 1 << nb_cows
ways  = 0
adjacent = [[] for _ in range(limit)]
for i in range(1, limit):
    sums = sum([milks[j] for j in range(nb_cows) if i & 1 << j])
    for j in range(len(adjacent[sums])):
        ways += (i & adjacent[sums][j] == 0)
    adjacent[sums].append(i)
print(ways)

