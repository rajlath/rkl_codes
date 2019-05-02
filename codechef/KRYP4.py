
# -*- coding: utf-8 -*-
# @Date    : 2019-03-08 09:25:52
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

from collections import Counter
nb = RI()
ins= Counter(RMI())
print(sum([ i * (i - 1) // 2 for i in ins.values() if i >=2]))
