
# -*- coding: utf-8 -*-
# @Date    : 2019-08-23 19:02:36
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


import math
for _ in range(RI()):
    a, b = RMI()
    g = math.gcd(a, b)
    ans = -1
    for i in range(2, g + 1):
        if g % i == 0:
            ans = i
            break
    print(ans)
