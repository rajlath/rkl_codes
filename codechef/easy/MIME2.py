
# -*- coding: utf-8 -*-
# @Date    : 2019-07-21 20:27:02
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


nb_ext, nb_qry = [int(x) for x in input().split()]
extension = dict(input().strip().split() for _ in range(nb_ext))
for _ in range(nb_qry):
    exts = [x for x in input().strip().split(".")][-1]
    #print(exts)
    if exts in extension:
        print(extension[exts])
    else:
        print("unknown")

