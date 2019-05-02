
# -*- coding: utf-8 -*-
# @Date    : 2019-03-18 08:45:05
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

# solution adapted from solution by arsh_16

import sys
import bisect
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]

LIMIT = int(10 ** 11 + 1)
MAXS  = int(pow(10**11, 0.5))+1

is_primes = [False] * 2 + [True] * (MAXS - 2)
primes    = []

for indx, val in enumerate(is_primes):
    if val:
        primes.append(indx)
        for j in range(indx, MAXS, indx):
            is_primes[j] = False
powers = []

for i in range(len(primes)):
    for j in range(len(primes)):
        curr = primes[i]**primes[j]
        if curr <= 10**11:
            powers.append(curr)
        else: break



powers.sort()
#print(powers[100])
nb_test = RI()
for _ in range(nb_test):
    curr = RI()
    if curr < 4: print(-1)
    elif curr < 8:print(4)
    else:
        pos = bisect.bisect_left(powers, curr)
        if pos==len(powers):
            print(powers[pos-1])
        elif powers[pos]==curr:
            print(powers[pos])
        else:
            print(powers[pos-1])









