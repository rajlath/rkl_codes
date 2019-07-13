
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 10:09:45
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


r, g, b = map(int, input().split())
t_r = 0 + 3 * ((r - 1) // 2)
t_g = 1 + 3 * ((g - 1) // 2)
t_b = 2 + 3 * ((b - 1) // 2)
print(30 + max(t_r, t_g, t_b))