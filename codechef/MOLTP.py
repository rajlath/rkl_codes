
# -*- coding: utf-8 -*-
# @Date    : 2019-06-15 14:06:00
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
import re

LIMIT = 2 * (10 ** 6) + 5
#LIMIT = 30
counts= [0] * LIMIT
for i in range(1, LIMIT):
    counts[i] = counts[i - 1]
    counts[i] += len(re.findall('[abcdef]',hex(i)[2:]))
nb_test = RI()
for _ in range(nb_test):
    left, rite = RMI()
    print(counts[rite] - counts[left -1])








