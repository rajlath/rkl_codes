
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 20:11:11
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/ENSE2018/problems/MNZEQ
# @Version : 1.0.0
# variation of solution by ethfar https://www.codechef.com/viewsolution/20075852

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)
mods   = 10 ** 9 + 7

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

from math import floor, ceil

nots = read_int()
for _ in range(nots):
    lens = read_int()
    arrs = read_ints()
    sums = sum(arrs)
    favg = floor(sums / lens)
    cavg =  ceil(sums / lens)
    cavg += favg == cavg

    fsum, csum = 0 , 0
    for i in range(lens):
        fsum += (arrs[i] - favg) ** 2
        csum += (arrs[i] - cavg) ** 2
    if fsum < csum:print(favg)
    else:print(cavg)










