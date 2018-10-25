
# -*- coding: utf-8 -*-
# @Date    : 2018-10-19 07:22:47
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


lens = read_int()
arrs = read_ints()
ans  = -1
should_be = -1
for i, v in enumerate(arrs):
    if v > (should_be + 1):
        ans = i + 1
        break
    should_be = max(v, should_be)
print(ans)