
# -*- coding: utf-8 -*-

# @Date    : 2018-11-27 09:39:35
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from functools import reduce

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]


n = read_int()
if n == 1:
    print(1)
else:
    a = reduce(lambda x, y : x * y ,[ x for x in range(n, 2 *(n-1) + 1)])
    b = reduce(lambda x, y : x * y , [ x for x in range(1, n)])
    print(a // b)

