
# -*- coding: utf-8 -*-
# @Date    : 2019-03-10 07:11:32
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import log
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]



def solve():
    n = RI()
    p = [0] + RMI()
    v = [0 for _ in range(n+1)]
    ans = 0
    for i in range(1, n + 1):
        if not v[i]:
            cnt = 0
            while not v[i]:
                v[i] = 1
                i = p[i]
                cnt += 1
            if cnt & (cnt - 1):
                return -1
            ans = max(ans, cnt)
    return int(log(ans, 2))

nb_test = RI()
for _ in range(nb_test):
    print(solve())