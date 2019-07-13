
# -*- coding: utf-8 -*-
# @Date    : 2019-07-05 18:52:59
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
    lens = RI()
    coin = RMI()
    sums = sum(coin)
    aver, balance = divmod(sums, lens)
    if balance != 0:
        print("Impossible")
    elif aver in coin:
        check, bal = divmod(sums - aver, lens - 1)
        if bal == 0 and check == aver:
            print(coin.index(aver) + 1)
        else:
            print("Impossible")
