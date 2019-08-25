
# -*- coding: utf-8 -*-
# @Date    : 2019-08-23 19:10:06
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


lens = int(input())
arrs = [int(x) for x in input().split()]
for _ in range(int(input())):
    left, rite, ops = [int(x) for x in input().split()]
    if rite - left == ops:
        print(sum(arrs[left - 1:rite]))
    elif rite - left > ops:
        print("Suneo is sad")
    else:
        curr = arrs[left - 1:rite]
        answer = sum(curr)
        maxi = max(curr)
        if maxi > 0:
            end = ops - rite + left
            answer += end * maxi
        print(answer)

