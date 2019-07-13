
# -*- coding: utf-8 -*-
# @Date    : 2019-06-10 16:54:22
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

n, t = RMI()
src  = RWI()
for i in range(t):
    curr = RW()
    valid= [False] * ( len(curr) + 1)
    valid[0] = True
    for i1 in range(len(curr)):
        if valid[i1]:
            for j in range(n):
                if i1 + len(src[j]) - 1 < len(curr) and curr[i1:len(src[j])] == src[j]:
                    valid[i+len(src[j])]=True
    if valid[len(curr)]:
        print("Yes")
    else:
        print("No")
