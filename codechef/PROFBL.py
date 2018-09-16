
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 20:11:11
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/ENSE2018/problems/PROFBL
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)
mods   = 10 ** 9 + 7

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]


nots = read_int()
for _ in range(nots):
    hiearchy = read_int()
    ans = ( (pow(7,hiearchy+1, mods)-1) * pow(6,mods-2, mods) ) % mods
    print(ans)





