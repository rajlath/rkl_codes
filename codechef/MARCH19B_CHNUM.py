
# -*- coding: utf-8 -*-
# @Date    : 2019-03-15 08:45:56
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
    nb_elements = RI()
    elements    = RMI()
    positive, negetives = 0, 0
    for i in elements:
        positive += i > 0
        negetives+= i < 0
    if negetives == 0:
        negetives = positive
    print(positive, negetives)