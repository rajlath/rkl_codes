
# -*- coding: utf-8 -*-
# @Date    : 2019-08-21 12:55:43
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


bin_string = input()
lens = len(bin_string)
answer = lens + ('1' in bin_string[1:])
print(answer >> 1)


# solution 2
ins = int(input(), 2)
cnt = 0
indx = 1
while indx < ins:
    cnt += 1
    indx *= 4
print(cnt)

# solution  3


