
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 21:25:59
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
from math import sqrt
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


k = RI()
if k < 25:
  print(-1)
else:
  ans = ''
  rows = int(sqrt(k))
  if rows * rows == k or rows * (rows + 1) == k:
    ans = "aeiou" + "x" * ( k//rows  - 5)
    print(ans)
    for i in range(1, rows):
      new = ans[i:rows +  1]
      new += ans[:rows - len(new)+1]
      ans += new

      print(ans)
    print(len(ans))
  else:
    print(-1)
