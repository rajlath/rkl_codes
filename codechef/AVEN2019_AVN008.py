
# -*- coding: utf-8 -*-
# @Date    : 2019-04-29 09:12:53
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
    lens, k = RMI()
    elems = RMI()
    res = sum(elems[:k])
    curr= res
    for i in range(k, lens):
        curr += elems[i] - elems[i - k]
        res = max(res, curr)
    print(res)