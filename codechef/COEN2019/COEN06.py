
# -*- coding: utf-8 -*-
# @Date    : 2019-03-05 10:24:35
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import gcd
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
    a, b = RMI()
    _gcd = gcd(a, b)
    ans = -1
    for i in range(2, _gcd + 1):
        if _gcd % i == 0:
            ans = i
            break
    print(ans)

