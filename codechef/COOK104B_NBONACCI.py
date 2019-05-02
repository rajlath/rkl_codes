
# -*- coding: utf-8 -*-
# @Date    : 2019-03-25 12:10:39
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


nb_elem, nb_query = RMI()
elems = [0] + RMI()
for i in range(1, nb_elem + 1):
    elems[i] ^= elems[i - 1]
nb_elem += 1
for _ in range(nb_query)    :
    print(elems[RI() % nb_elem])