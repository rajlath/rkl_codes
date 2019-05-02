
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 17:25:30
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

def ss(tar, count):
    global comps,mins,ans
    if tar == 0:
        mins = count
        ans  = True
        return
    elif tar < 0:return
    for x in comps:
        if not ans:
            ss(tar - x, count + 1)




nb_test = RI()
for _ in range(nb_test):
    size, *comps = RMI()
    comps = set(comps)
    mins = min_val
    ans  = False
    ss(size, 0)
    print(mins)