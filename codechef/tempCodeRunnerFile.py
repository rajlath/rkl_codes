
# -*- coding: utf-8 -*-
# @Date    : 2019-05-12 16:01:40
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

valids = set()

def get_count(s, e, a):
  global valids
  if s % a == 0:
    begin = s
  else:
    begin = s + (s - s % a)
  if e % a == 0:
    end = e
  else:
    end = e - (e % a)

  for i in range(begin, end + 1, a):
    valids.add(i)



a, b = RMI()
s, e = RMI()

get_count(s, e, a)
get_count(s, e, b)
print(valids)








