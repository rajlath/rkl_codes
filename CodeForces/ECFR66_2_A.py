
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 09:08:52
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
    n, divs = RMI()
    ans = 0
    while n > 0:
        n, rest = divmod(n, divs)
        ans += (rest + (n > 0))
    print(ans)

