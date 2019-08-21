
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 08:24:42
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
    need, have, amount, nb_book=RMI()
    notebook = [RMI() for _ in range(nb_book)]
    notebook = sorted(notebook, key = lambda x:(x[0], x[1]))
    ans = "UnluckyChef"
    for i in notebook:
        if i[0] >= (need - have) and i[1] <= amount:
            ans = "LuckyChef"
            break
    print(ans)
