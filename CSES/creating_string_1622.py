
# -*- coding: utf-8 -*-
# @Date    : 2019-07-02 12:44:22
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
def listTOString(lst):
    return ''.join(lst)

def permute(a, l, r)    :
    global answer
    if l == r:
        answer.add(listTOString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

ins = list(RW())
answer = set()
permute = sorted(set(list(permutations(ins))))
print(len(permute))
for i in permute:
    #print("".join(i))
    pass

