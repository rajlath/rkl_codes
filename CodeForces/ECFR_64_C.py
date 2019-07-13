
# -*- coding: utf-8 -*-
# @Date    : 2019-05-02 15:18:06
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


nb_elem, min_diff = RMI()
elems = sorted(RMI())
mids  = nb_elem // 2
left, rite, ans = 0, mids, 0
while left < mids and rite < nb_elem:
    if elems[left] + min_diff <= elems[rite]:
        left += 1
        ans  += 1
    rite += 1
print(ans)

