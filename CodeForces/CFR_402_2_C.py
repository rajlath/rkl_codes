
# -*- coding: utf-8 -*-
# @Date    : 2019-08-25 19:06:58
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


n, k = RMI()
acst = RMI()
sums = sum(acst)
bcst = RMI()
bcst = [bcst[i] - acst[i] for i in range(n)]
bcst = sorted(bcst)[:n - k]
while bcst and bcst[-1] > 0:
    bcst.pop()
print(sums + sum(bcst))