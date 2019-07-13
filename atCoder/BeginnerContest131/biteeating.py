
# -*- coding: utf-8 -*-
# @Date    : 2019-06-24 21:15:56
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


n, L = RMI()
arr = [ L + i -1  for i in range(1, n + 1)]
count_0 = arr.count(0)
sums    = sum(arr)
if count_0 == 1: del arr[arr.index(0)]
elif count_0 == 0 and sums >= 1: del arr[arr.index(min(arr))]
elif count_0 == 0 and sums <= -1:del arr[arr.index(max(arr))]
else:pass
print(sum(arr))

