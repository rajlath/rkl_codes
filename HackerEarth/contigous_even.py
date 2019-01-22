
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 13:28:49
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
from itertools import groupby
nb_test = read_int()
for _ in range(nb_test):
    nb_elem = read_int()
    elems   = read_ints()
    elems   = [1 if x%2==0 else 0 for x in elems]
    maxs = -nb_elem
    found= False
    for key, group in groupby(elems):
        if key == 1:
            found = True
            maxs = max(maxs, len(list(group)))
    if found: print(maxs)
    else:print(-1)
