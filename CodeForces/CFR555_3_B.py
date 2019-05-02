
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 08:10:47
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


lens = RI()
src  = [int(x) for x in input()]
maps = [0]+RMI()
i = 0
while i < lens and maps[src[i]] <= src[i]:
        i += 1
j = i
while j < lens and maps[src[j]] >= src[j]:
    src[j] = maps[src[j]]
    j += 1
print(''.join(map(str, src)))


