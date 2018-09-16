
# -*- coding: utf-8 -*-
# @Date    : 2018-09-05 22:16:26
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline()]
def read_str_list(): return [x for x in stdin.readline().split()]

nol , cost_white, cost_black = read_ints()
cost = [cost_white, cost_black]
series = read_ints()
ans = 0
if nol%2 == 1:
    l, r = nol//2, nol//2
else:
    l, r = nol//2 - 1, nol//2

while l >= 0 and r < nol:

    if series[l] == series[r]:
        if series[l] == 2:
            if l == r:
                ans += min(cost)
            else:
                ans += min(cost) * 2
    else:
        if series[l] != series[r]:
            if series[l] == 2:
                ans += cost[series[r]]
            elif series[r] == 2:
                ans += cost[series[l]]
            else:
                ans = -1
                break
    l -=1
    r += 1
print(ans)














