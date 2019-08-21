
# -*- coding: utf-8 -*-
# @Date    : 2019-07-21 12:32:10
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


for _ in range(int(input())):
    current = list(input())
    i = 0
    lens = len(current)
    while i < lens:
        done = False
        if i + 4 <= lens:
            curr = current[i:i+4]
            if curr[0] in "C?" and curr[1] in "H?" and curr[2] in "E?" and curr[3] in "F?":
                current[i]   = "C"
                current[i+1] = "H"
                current[i+2] = "E"
                current[i+3] = "F"
                i += 4
                done = True
        if not done:
            if current[i] == "?": current[i] = "A"
            i += 1
    print(''.join(current))



