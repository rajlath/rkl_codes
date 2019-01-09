
# -*- coding: utf-8 -*-
# @Date    : 2018-12-06 18:24:42
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


hs, ms = read_ints()
he, me = read_ints()
travel = read_int()
delay  = read_int()

started_at = hs * 60 + ms
actual_start = started_at + delay
after_travel = actual_start + travel
should_be    = he * 60 + me
if after_travel <= should_be:
    print("YES")
else:
    print("NO")