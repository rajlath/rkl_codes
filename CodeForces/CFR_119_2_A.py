
# -*- coding: utf-8 -*-
# @Date    : 2018-09-27 13:25:36
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


lens, a, b, c = read_ints()
result = [min_val]*5001
result[0] = 0
for i in range(1, lens + 1):
    result[i] = 1 + max(result[i-a], result[i-b], result[i-c])
print(result[lens])





