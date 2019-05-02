
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 20:41:06
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


nb_elements = RI()
elements = sorted(RMI())
if any(elements[i] == elements[i+2] for i in range(nb_elements - 2)):
    print("NO")
else:
    print("YES")
    a = [x for x in elements[::2]]
    print(len(a))
    print(*a)
    a = [x for x in elements[1::2][::-1]]
    print(len(a))
    print(*a)


