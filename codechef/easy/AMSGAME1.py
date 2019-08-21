
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 14:47:04
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

from math import gcd


nb_test = RI()
for _ in range(nb_test):
    lens = RI()
    elem = RMI()
    answ = gcd(elem[0], elem[1])
    for i in range(2, lens):
        answ = gcd(answ, elem[i])
    print(answ)
