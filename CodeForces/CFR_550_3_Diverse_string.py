
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 20:14:17
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from string import ascii_lowercase as al
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
    ins = ''.join(sorted(input()))
    #print(ins)
    print(["No", "Yes"][ins in al])


