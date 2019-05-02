
# -*- coding: utf-8 -*-
# @Date    : 2019-04-20 13:33:55
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import gcd
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
    primer = RI()
    lens   = RI()
    emms   = RMI()
    emml   = []
    for i in range(lens):
        curr = emms[i]
        canbe= False
        while True:
            curr_gcd = gcd(primer, curr)
            curr = curr // curr_gcd
            if curr_gcd == 1 and curr != 1:
                break
            elif curr_gcd == 1 and curr == 1:
                emml.append(emms[i])
                break
    ans = ("-1", "")
    if emml:
        ans = (max(emml), min(emml))
    print(*ans)


