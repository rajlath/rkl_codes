
# -*- coding: utf-8 -*-
# @Date    : 2019-05-18 09:13:19
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

#thanks to Ashishgup

import sys
sys.setrecursionlimit(10**5+1)

inf     =  int(10 ** 20)
max_val =  inf
min_val = -inf

RW  = lambda : sys.stdin.readline().strip()
RI  = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


vowels = "aeiou"
lens = RI()
rows = -1
cols = -1
i = 5
while i * i <= lens:
  if lens % i == 0 and lens // i >= 5:
    rows = i
    cols = lens // i
    break
  i += 1
if rows == -1:
  print("-1")
else:
  ans = ''
  for i in range(rows)  :
    for j in range(cols):
      ans += vowels[(i + j) % 5]
  print(ans)

