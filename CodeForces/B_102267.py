
# -*- coding: utf-8 -*-
# @Date    : 2019-08-25 19:27:45
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


def seive(n):
    primes = []
    seqs = [False, False] + [True]  * n
    l = int(n ** 0.5)
    for i in range(2, n):
        if seqs[i]:
            primes.append(i)
            j = i * i
            while j < n:
                seqs[j] = False
                j += i
    return primes

primes = seive(10 ** 7 + 5)
given = int(input())
answer = [-1]
for i in range(2, given):
    if i in primes and given - i in primes:
        answer = [i, given - i]
        break
print(*answer)
