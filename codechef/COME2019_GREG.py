
# -*- coding: utf-8 -*-
# @Date    : 2019-04-15 17:21:45
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import sqrt
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


def seive(limit):
    status = [True for _ in range(limit + 1)]
    primes = []
    for i in range(2, limit + 1):
        if status[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                status[j] = False
    return primes
a, b = RMI()

print(len(seive(a + b)))

