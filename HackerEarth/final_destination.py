
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 13:15:59
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


offset = {"L":(-1, 0), "R":(1, 0), "U":(0, 1), "D":(0, -1)}
def next_location(a, b):
    return ((a[0]+b[0], a[1]+b[1]))
ins = input()
pos = (0, 0)
for i in ins:
    pos = next_location(pos, offset[i])
print(*pos)