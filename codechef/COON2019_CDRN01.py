
# -*- coding: utf-8 -*-
# @Date    : 2019-04-09 16:32:40
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import ceil, floor
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
    curr = RI()
    ans =  ceil(curr / 10) * 10
    #print(ans)
    if ans % 100 == 0 or ans % 1000 == 0:ans += 10
    print(ans)