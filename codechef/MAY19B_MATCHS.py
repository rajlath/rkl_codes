
# -*- coding: utf-8 -*-
# @Date    : 2019-05-18 12:37:12
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
  n, m = RMI()
  if n % m == 0 or m % n == 0:print("Ari")
  else:
    min_pile, max_pile = min(n, m), max(n, m)
    moves = 0
    while True:
      div, extra = divmod(max_pile, min_pile)
      moves += 1
      if div > 1:break
      else:
        max_pile, min_pile = min_pile, extra
        if max_pile < min_pile:
          max_pile, min_pile = min_pile, max_pile
    print(["Ari", "Rich"][moves % 2 == 0])