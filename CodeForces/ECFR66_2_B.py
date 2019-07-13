
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 09:13:44
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

overflow = 2 ** 32
ans = 0
nb_test = RI()
calc = [1]
for _ in range(nb_test):
    mods, *vals = RWI()
    if mods == "add":
        ans += calc[-1]
    elif mods == "for":
        val = int(vals[0])
        calc.append(min((calc[-1] * val),overflow))
        #print(calc)
    else:calc.pop()
ans = "OVERFLOW!!!" if ans >=overflow else ans
print(ans)



