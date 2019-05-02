
# -*- coding: utf-8 -*-
# @Date    : 2019-03-16 07:35:50
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


N, K = RMI()
arr  = RMI()
forward = [0 for _ in range(N)]
backwrd = [0 for _ in range(N)]
backwrd[0] = arr[0]
backwrd[1] = arr[0] + arr[1]
for i in range(2, N):
    backwrd[i] = arr[i] + max(backwrd[i - 1], backwrd[i - 2])
for i in range(K, N):
    forward[i] = arr[i] + max(forward[i - 1], forward[i - 2])
ans = min_val
for i in range(K - 1, N):
    ans = max(ans, forward[i] + backwrd[i] - arr[i])
print(ans)