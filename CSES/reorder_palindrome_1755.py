
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 12:18:33
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
ins = RW()
cins = Counter(ins)
odd = 0
oddc = ''
for i in cins:
    if cins[i] % 2 == 1:
        if odd == 0:
            oddc = i
        odd += 1
    if odd > 1: break
if odd > 1:
    print("NO SOLUTION")
else:
    part1 = part2 = ''
    for i in cins:
        if cins[i]%2 == 0:
            cnt = cins[i] // 2
            part1 += i * cnt
            part2 =  i * cnt + part2
    answer = part1 + oddc + part2
    print(answer)



