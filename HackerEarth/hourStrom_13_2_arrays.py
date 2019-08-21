
# -*- coding: utf-8 -*-
# @Date    : 2019-07-18 08:52:54
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

def solve(ca, sa, cb, sb):
    if (ca > 0) and (cb > 0): return "Infinite"
    if cb > 0:
        sa, sb = sb, sa
        ca, cb = cb, ca
    result = 0
    if ca > 0:
        if sa > sb:
            result = 0
        else:
            diff = sb - sa
            if ca == 1:result = 1
            else:result = diff + 1
    return result




lens = RI()
arra = RMI()
cnta = arra.count(-1)
suma = sum(arra) + cnta
arrb = RMI()
cntb = arrb.count(-1)
sumb = sum(arrb) + cntb

print(solve(cnta, suma, cntb, sumb))
