
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 15:08:15
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


lens = int(input())
if lens == 0:
    print(0)
else:
    elem = read_ints()
    max_here = max_all = elem[0]
    for i, v in enumerate(elem[1:]):
        max_here = max(max_here+v, v)
        max_all  = max(max_all, max_here)
    print(max_all)