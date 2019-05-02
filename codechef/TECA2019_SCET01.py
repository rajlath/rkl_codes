
# -*- coding: utf-8 -*-
# @Date    : 2019-03-30 11:47:41
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

nb_test = RI()
for _ in range(nb_test):
    rng, k = RMI()
    lst = list(range(1, rng + 1))
    i = 1
    lens = rng
    while len(lst) > 1:
        if i  % k == 0:
            del lst[i%len(lst) - 1]
            print(lst)
        i += 1
    print(lst)

