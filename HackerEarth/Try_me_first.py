
# -*- coding: utf-8 -*-
# @Date    : 2019-01-20 13:06:33
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

n = read_int()
bits = len(bin(n)[2:])
maxs = ((1 << bits) - 1) ^ n
print(n, maxs)


