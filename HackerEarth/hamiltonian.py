
# -*- coding: utf-8 -*-
# @Date    : 2019-01-20 16:37:04
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


nb = read_int()
marks = read_ints()
high = 0
valid = []
for i in range(-1, nb*-1, -1):
    curr = marks[i]
    if curr >= high:
        valid.append(curr)
        high = curr
print(*valid[::-1])