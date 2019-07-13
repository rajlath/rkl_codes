
# -*- coding: utf-8 -*-
# @Date    : 2019-05-13 19:27:34
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

def get_max_total(arr):
  rets = 0
  for _ in range(2):
    rets += arr.pop(arr.index(max(arr)))
  return rets




nb_test = RI()
for _ in range(nb_test):
  lens = RI()
  Ayushi = get_max_total(RMI())
  Daksh  = get_max_total(RMI())
  print(["AAYUSHI", "DAKSH"][Daksh >= Ayushi])
