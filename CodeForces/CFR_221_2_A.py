
# -*- coding: utf-8 -*-
# @Date    : 2019-01-22 18:58:14
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



s = input()
n = s.find("^")
m = sum((i - n) * int(c) for i, c in enumerate(s) if c.isdigit())
print("left" if m < 0 else "right" if m > 0 else "balance")