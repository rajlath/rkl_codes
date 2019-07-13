
# -*- coding: utf-8 -*-
# @Date    : 2019-07-06 09:29:46
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

lens = RI()
candies = RMI()

# using prefix and computation
prefixes = [0] * (lens + 1)
for i in range(1, lens + 1):prefixes[i] = prefixes[i - 1] + candies[i - 1]
query = RI()
for _ in range(query)    :
    l, r = RMI()
    print( (prefixes[r] - prefixes[l - 1]) // 10 )

# using DP






