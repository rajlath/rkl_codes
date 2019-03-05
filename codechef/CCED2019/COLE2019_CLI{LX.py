
# -*- coding: utf-8 -*-
# @Date    : 2019-02-28 12:24:40
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

nb_Test = RI()
for _ in range(nb_Test):
    n, k = RMI()
    if n <= k:
        ans = 0
    elif n <= (2 * k):
        if n  % k:
            ans = n % k
        else:
            ans = n // 2
    print(ans)

