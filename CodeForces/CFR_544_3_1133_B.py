
# -*- coding: utf-8 -*-
# @Date    : 2019-03-08 09:41:26
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from collections import Counter
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


nb_boxes, nb_girls = RMI()
candies = Counter([x % nb_girls for x in RMI()])
ways = 0
for i in range(nb_girls):
    curr = (nb_girls - i) % nb_girls
    if  curr == i:
        way = candies[i] // 2
        candies[i] -= way * 2
        ways += way * 2
    else:
        way = min(candies[i], candies[curr])
        candies[i] -= way
        candies[curr] -= way
        ways += way * 2
print(ways)


