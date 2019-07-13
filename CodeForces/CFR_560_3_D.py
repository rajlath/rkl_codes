
# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 09:44:10
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

from math import sqrt
def factors(n):
  results = set()
  for i in range(1, int(sqrt(n)) + 1):
      if n % i == 0:
          results.add(i)
          results.add(n//i)
  return results

nb_test = RI()
for _ in range(nb_test):
  lens = RI()
  elem = RMI()
  could_be = min(elem) * max(elem)
  could_be_factors = factors(could_be)
  #print(could_be_factors)
  if sorted(set(could_be_factors)) == sorted(set(elem + [1, could_be])):
    print(could_be)
  else:
    print(-1)





