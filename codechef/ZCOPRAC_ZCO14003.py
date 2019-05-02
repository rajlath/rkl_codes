
# -*- coding: utf-8 -*-
# @Date    : 2019-03-17 15:32:44
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


nb_person = RI()
print(max([((nb_person - i) * amt) for i, amt in enumerate(sorted([RI() for _ in range(nb_person)]))]))
