
# -*- coding: utf-8 -*-
# @Date    : 2019-07-21 13:47:04
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

def generate_prime_factors(n):
    pfacts = [0] * (n + 1)
    for p in range(2, n + 1):
        if pfacts[p] == 0:
            for i in range(p, n + 1, p):
                pfacts[i] += 1
    return pfacts

factors = generate_prime_factors(100000)
for _ in range(int(input())):
    a, b, k = [int(x) for x in input().split()]
    counts = 0
    for i in range(a, b+1):
        counts += factors[i] == k
    print(counts)




