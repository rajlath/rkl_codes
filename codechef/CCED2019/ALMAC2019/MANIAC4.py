
# -*- coding: utf-8 -*-
# @Date    : 2019-03-05 08:18:46
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

nb_elems, nb_query = RMI()
lefties = [0 for x in range(nb_elems + 1)]
rightie = [[] for x in  range(nb_elems + 1)]
for _ in range(nb_query):
    l, r = RMI()
    lefties[l - 1] += 1
    rightie[r].append(l - 1)
arrs = [0 for x in range(nb_elems + 1)]
cnt = 0
pres= 0
for i in range(nb_elems):
    cnt += lefties[i]
    pres+= (i * lefties[i])
    for j in rightie[i]:
        pres -= j
        cnt  -= 1
    arrs[i]  = cnt * (i + 1)
    arrs[i] -= pres
    print(arrs[i], end = " ")


