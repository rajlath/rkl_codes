
# -*- coding: utf-8 -*-
# @Date    : 2019-03-05 15:59:08
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

import sys
sys.setrecursionlimit(100000)

n, m = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for j in range(m)]

INF = 10 ** 9
mi = [INF] * (n+1)
cnt = [0] * (n+1)

for a, b in A:
    cnt[a] += 1
    mi[a] = min(mi[a], (b - a) % n)

ANS = []
for i in range(1, n+1):
    ans = 0
    for j in range(1, n+1):
        if cnt[j] == 0:
            continue
        ans = max(ans, (j - i) % n + (cnt[j] - 1) * n + mi[j])
    ANS.append(ans)

print(*ANS)