
# -*- coding: utf-8 -*-
# @Date    : 2019-06-28 12:36:16
# @Author  : raj lath (oorja.halt@(gmail.com)
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
s = input()

ans = 0

si = {s}
k -= 1

for d in range(1, n + 1):
    si = {t[:i] + t[i+1:] for i in range(n - d + 1) for t in si}
    ni = len(si)
    if ni < k:
        ans += ni * d
        k -= ni
    else:
        ans += k * d
        k = 0
        break
print(-1 if k > 0 else ans)
