
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 22:04:30
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
    curr = RI()
    ans = 0
    while curr > 1:
        last = int(curr ** 0.5)
        curr -= (last * last)
        ans += 1
    ans +=  (curr == 1)
    print(ans)
