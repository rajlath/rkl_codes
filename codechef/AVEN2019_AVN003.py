
# -*- coding: utf-8 -*-
# @Date    : 2019-04-29 08:01:02
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

MOD = int(10 ** 9 + 7)
nb_test = RI()
for _ in range(nb_test):
    lens = RI()
    elem = RMI()
    odds = sum([1 for x in elem if x%2])
    anss = (odds * (lens - odds)) % MOD
    print(anss)



