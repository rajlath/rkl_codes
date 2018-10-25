
# -*- coding: utf-8 -*-
# @Date    : 2018-10-22 07:11:28
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


nb_test = read_int()
for _ in range(nb_test):
    nb_steps, limit = read_ints()
    heights = read_ints()
    needed = 0
    heights = [0] + heights
    for i in range(1, nb_steps+1):
        diffs = heights[i] - heights[i-1]
        needed += (diffs // limit)
        needed -= (diffs % limit == 0)
    print(needed)




