
# -*- coding: utf-8 -*-
# @Date    : 2019-03-17 21:17:58
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


nb_chars = RI()
chars    = RW()
has = []
cnt = 0
ans = "No"
for i in chars:
    if i in "aeiou":
        if i not in has:
            has.append(i)
            cnt += 1
            if cnt == 4:
                ans = "Yes"
                break

print(ans)

