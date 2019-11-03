
# -*- coding: utf-8 -*-
# @Date    : 2019-08-31 10:00:51
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
    n, m = RMI()
    tens = [(i * m) % 10 for i in range(1, 10) ]
    main, rest = divmod(n //m, 10)
    answ = main * sum(tens) + sum(tens[:rest])
    print(answ)




