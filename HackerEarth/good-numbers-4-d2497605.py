
# -*- coding: utf-8 -*-
# @Date    : 2019-05-16 20:33:04
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


good_numbers = [ 1 if x%2==0 and x%4!=0 else 0 for x in range(1, 10 ** 5 + 1)]
nb_test = RI()
for _ in range(nb_test):
  print(sum(good_numbers[:RI()]))