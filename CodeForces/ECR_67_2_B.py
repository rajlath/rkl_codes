
# -*- coding: utf-8 -*-
# @Date    : 2019-07-01 07:44:43
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

from collections import defaultdict
has = defaultdict(list)
lens = RI()
given = input()
for i, v in enumerate(given):
    has[v].append(i + 1)
nb_word = RI()
for i in range(nb_word):
    answer = 0
    current = input()
    dicts = defaultdict(int)
    for i,v in enumerate(current):
        dicts[v] += 1
        answer = (max(answer, has[v][dicts[v] - 1] ))
    print(answer)

