
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 09:52:24
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
arr = [0] * (n + 1)
current = 1
for i in range(2, n+1):
    if arr[i] == 0:
        for j in range(i, n+1, i):
            arr[j] = current
        current += 1
print(*arr[2:])