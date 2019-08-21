
# -*- coding: utf-8 -*-
# @Date    : 2019-08-01 07:30:35
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


options = {x:[0] * 9 for x in "smp"}
for x in input().split():
    options[x[1]][int(x[0]) - 1] += 1
ans = 2
for c in "smp":
    curr = options[c]
    if max(curr) >= 2:
        ans = min(ans, 3 - max(curr))
    else:
        for i in range(7):
            sums = sum(curr[i:i+3])
            ans  = min(ans, 3 - sums)
print(ans)
