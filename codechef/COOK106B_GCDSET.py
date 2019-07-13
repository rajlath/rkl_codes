
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 13:41:52
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


nb_test = RI()
for _ in range(nb_test):
    l, r, g = RMI()
    ans = 0
    if g > r: ans = 0
    else:
        first = l + (g - l % g) % g
        last  = r - r % g
        ans = (last - first ) // g + 1
        if ans == 1 and last != g:
            ans = 0
    print(ans)
