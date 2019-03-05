
# -*- coding: utf-8 -*-
# @Date    : 2019-03-04 19:31:08
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from  collections import Counter
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
    lens = int(input())
    arrs = sorted(Counter(RMI()).values())
    if len(arrs) == 1:
        print(lens, lens)
    else:
        maxs = max(arrs)
        arrs = sorted(arrs, reverse = True)
        for i in arrs[1:]:
            if i != maxs:
                break
        mins = maxs - i 
        print(maxs, mins)




