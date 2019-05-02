
# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 20:20:44
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import factorial
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

MOD = 1000000007
facts = [1]
factsum = [1]
for i in range(2, 10**5 + 1):
    facts.append((facts[-1] * i)%MOD)
    factsum.append((factsum[-1] + facts[-1])%MOD)
nb_test = RI()
for _ in range(nb_test):
    print(factsum[RI() - 1])



