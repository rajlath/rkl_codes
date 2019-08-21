
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 09:11:36
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
    area = RI()
    side = int(area ** 0.5)
    if side * side == area:
        print(0)
    else:
        x = side
        while x > 0:
            if area % x = 0:
                should_be = area//x
                print(abs(should_be - x))
            



