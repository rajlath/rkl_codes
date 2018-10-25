
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

nb_planks, widths = read_ints()
heights = read_ints()
mins = curr = sum(heights[:widths])
pos  = 1
for i in range(widths, nb_planks):
    curr += heights[i] - heights[i-widths]
    if curr < mins:
        pos = i - widths + 2
        mins = curr
print(pos)

