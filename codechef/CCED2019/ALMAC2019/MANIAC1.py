
# -*- coding: utf-8 -*-
# @Date    : 2019-03-04 19:31:08
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from  itertools import accumulate
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

nb_items, nb_friend = RMI()
elems = sorted(RMI())
sums = 0
step = 0
for j in range(nb_items - nb_friend - 1, -1, -1):
    if (nb_items - j - 1) % nb_friend == 0:
        step += 1
    sums += elems[j] * (1 + step)
sums += sum(elems[nb_items - nb_friend:])
print(sums)






