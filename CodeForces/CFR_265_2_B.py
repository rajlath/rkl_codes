
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 19:44:53
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


nb_tree = read_int()
last = 0
need = -1
for _ in range(nb_tree):
    height = int(input())
    need   += abs(height -last) + 2
    last = height
print(need)

