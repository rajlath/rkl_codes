
# -*- coding: utf-8 -*-
# @Date    : 2019-08-19 08:23:10
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


for _ in range(RI()):
    lens, nb_query = RMI()
    given = input()
    a = [0] * lens
    b = [0] * lens
    for i in range(2, lens):
        if given[i] == given[i - 1] or given[i] == given[i - 2] or given[i - 1] == given[i - 2]:
            a[i] = 1
            if i == 2:
                b[2] = a[2]
            if i > 2:
                b[i] = b[i - 1] + a[i]
    b[0] = b[1] = 0
    for i in range(nb_query):
        left, rite = RMI()
        if rite - left < 2:
            print("NO")
        elif b[rite - 1] - b[left] > 0:
            print("YES")
        else:
            print("NO")
