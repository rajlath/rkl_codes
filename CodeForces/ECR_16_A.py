
# -*- coding: utf-8 -*-
# @Date    : 2019-08-30 14:56:18
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

a, b = [x for x in input()]
toIndex = lambda x: "abcdefgh".index(x)+1
a, b = toIndex(a), int(b)
cnts = 0
for x, y in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]):
    x1, y1 = a + x, b + y
    #print(x1, y1)
    cnts += x1 in range(1,9) and y1 in range(1, 9)
print(cnts)


c,d=input()
print((3,5,8)[('a'<c<'h')+('1'<d<'8')])


