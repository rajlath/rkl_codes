
# -*- coding: utf-8 -*-
# @Date    : 2019-08-31 10:55:22
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


from itertools import permutations
alls = "abc"
permlist = [''.join(perms) for perms in list(permutations(alls))]
answer = []
n,s,t = RI(), RW(),RW()

for i in permlist:
    answer.append(i * n)
    curr = ''
    curr = i[0] * n
    curr += i[1] * n
    curr += i[2] * n
    answer.append(curr)
valid = "NO"
for i in answer:
    if s in i or t in i:continue
    else:
        valid = "YES"
        break
print(valid)
if valid=="YES":print(i)
