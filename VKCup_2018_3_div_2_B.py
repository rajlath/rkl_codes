
# -*- coding: utf-8 -*-
# @Date    : 2019-01-30 20:41:28
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


nb_holes, volume, flow = read_ints()
hole_size = read_ints()
totals = sum(hole_size)
first = hole_size[0]
closed = 0
other = sorted(hole_size[1:], reverse=True)
while first * volume < flow * totals:
    totals -= other.pop()
    closed += 1
print(closed)



