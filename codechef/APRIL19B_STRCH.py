
# -*- coding: utf-8 -*-
# @Date    : 2019-04-06 09:56:32
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

nb_test = int(input())
for _ in range(nb_test):
    lens = RI()
    src, need = RWI()
    pos = [-1] + [i for i, v in enumerate(src) if v == need]
    answer = 0
    for i in range(1, len(pos)):
        answer += (pos[i] - pos[i - 1]) * (lens - pos[i])
    print(answer)






