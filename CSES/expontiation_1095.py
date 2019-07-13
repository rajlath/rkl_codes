
# -*- coding: utf-8 -*-
# @Date    : 2019-07-04 11:34:27
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

def power(x, y, MOD):
    r = 1
    e = x
    while y:
        if (y & 1): r = (r * e) % MOD
        e = (e * e    ) % MOD
        y >>= 1
    return r


MOD = int(10e9 + 7)
nb_test = RI()
for _ in range(nb_test):
    a, p = RMI()
    print(power(a, p, MOD ))