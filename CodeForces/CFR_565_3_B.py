
# -*- coding: utf-8 -*-
# @Date    : 2019-06-10 14:05:24
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

from collections import defaultdict
nb_test = RI()
for _ in range(nb_test):
    _ = RI()
    maps = defaultdict(int)
    arrs = RMI()
    for i in arrs:
        maps[i%3] += 1
    ans = 0

    for i in range(maps[1] + 1):
        rem1 = maps[1] - i
        rem2 = maps[2] - i
        if rem2 < 0:break
        cur = maps[0] + i + rem1 // 3 + rem2 // 3
        ans = max(ans, cur)
    print(ans)

