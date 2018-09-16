
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 19:35:04
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/ENSE2018/problems/ARGTS
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]


nb_sites, needed = read_ints()
for _ in range(nb_sites):
    read_int()
    print("FAILURE" if needed < sum([x  for x in read_ints()]) else "SUCCESS")

