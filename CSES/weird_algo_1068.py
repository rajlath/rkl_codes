
# -*- coding: utf-8 -*-
# @Date    : 2019-07-01 16:52:26
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


n = RI()
a = []
while n != 1:
    a.append(n)
    if n & 1:
        n = 3 * n + 1
    else:
        n //=  2
a+=[1]
print(*a)