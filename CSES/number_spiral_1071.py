
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 09:50:21
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
    inss = RMI()
    a, b = max(inss), min(inss)
    ans = (a - 1) ** 2
    if a == b: ans += a
    elif ans % 2:
        if a == inss[0]:ans += a * 2 - inss[1]
        else:ans += inss[0]
    else:
        if inss[1] == a: ans += a * 2 - inss[0]
        else:ans += inss[1]
    print(ans)
