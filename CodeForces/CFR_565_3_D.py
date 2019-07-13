
# -*- coding: utf-8 -*-
# @Date    : 2019-06-07 20:26:19
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


def digsum(n):
        return sum([int(x) for x in str(n)])


nb_test = RI()
for _ in range(nb_test):
    n = RI()
    ans = (n * 10) + (10 - digsum(n) % 10)
    if digsum(ans) % 10 != 0:
            ans -= 10
    print(ans)'
