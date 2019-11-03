
# -*- coding: utf-8 -*-
# @Date    : 2019-08-26 13:34:11
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

r = n = RI()
a = RMI()
s = set()
i = 0
while i < n and a[i] not in s:
    s |= {a[i]}
    i += 1
while i > 0:
    while n > i and a[n - i] not in s:
        s |= {a[n - 1]}
        n -= 1
    r = min(r, n - i)
    i-= 1
    s -= {a[i]}
print(r)
