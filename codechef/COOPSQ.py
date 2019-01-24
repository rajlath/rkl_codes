
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 20:20:26
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

z = int(input())
maxz = int(z ** 0.5)
for i in range(maxz, -1, -1):
    if (i + 3) % 3 == 0:
        print(i)
        break

