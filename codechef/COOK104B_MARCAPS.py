
# -*- coding: utf-8 -*-
# @Date    : 2019-03-25 11:36:03
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from collections import Counter
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


nb_Test = RI()
for _ in range(nb_Test):
    nb_elem = RI()
    elem = RMI()
    elems   = [(v, i) for i, v in enumerate(elem)]
    elemc = Counter(elem)
    maxs = max(elemc.values())
    if maxs * 2 > nb_elem:
        print("No")
    else:
        elems = sorted(elems)
        res = [0] * nb_elem
        for i in range(nb_elem):
            res[elems[(i + nb_elem // 2) % nb_elem][1]] = elems[i][0]
        print("Yes")
        print(*res)

