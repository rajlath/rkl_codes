
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 14:52:44
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


nb_test = RI()
for _ in range(nb_test):
    one, two = input().split()
    lo = len(one)
    tw = len(two)
    if lo > tw: mins, maxs = two, one
    else:mins,maxs = one, two
    #print(mins, maxs)
    indx = 0
    ans = "NO"
    for j in range(len(maxs))        :
        if maxs[j] == mins[indx]:indx += 1
        if indx == len(mins):
           ans = "YES"
           break
    print(ans)




