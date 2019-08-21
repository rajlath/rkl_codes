
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 08:03:35
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

from collections import Counter
nb_students, nb_drink_type = [int(x) for x in input().split()]
favorites = Counter([int(input()) for _ in range(nb_students)])
invalids  = sum([1 for x in favorites.values() if x%2==1]) // 2
print(nb_students - invalids)