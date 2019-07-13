
# -*- coding: utf-8 -*-
# @Date    : 2019-05-12 15:12:59
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from collections import defaultdict
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


def prime_seive(n):
  primes = [False, False] + [True] * (n+ 1)
  for i in range(2, n+ 1):
    if primes[i]:
      j = i * i
      for j in range(i* i, n + 1, i):
        primes[j] = False
  return primes

def get_twin_count(primes, n):
  twins = defaultdict(int)
  last_prime = 3
  primes = prime_seive(n)
  for i in range(3, n):
    if primes[i] == True:
      if abs(i - last_prime) == 2:
        twins[i] += 1
        twins[last_prime] += 1
      last_prime = i
  return twins

twins = get_twin_count(prime_seive(100001), 100001)

nb_test = RI()
for _ in range(nb_test):
  current = RI()
  ans = 0
  if current in twins:
    ans = twins[current]
  print(ans)


