
# -*- coding: utf-8 -*-
# @Date    : 2019-04-20 14:17:20
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
    nb_vert, a, b = RMI()
    near, far = min([a, b]), max([a, b])
    if abs(near - far) == 1:
        if near != 1:
            print(*[near - 1, 3])
        else:
            print(*[far + 1, 3])
    else:
        print(*[near + 1, far - near])