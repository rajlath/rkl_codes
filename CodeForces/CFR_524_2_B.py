
# -*- coding: utf-8 -*-
# @Date    : 2018-11-24 08:40:37
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
ans = []
for i in range(1, 100):
    ans.append(i * (-1) ** i)
print(sum(ans[2:5]))






