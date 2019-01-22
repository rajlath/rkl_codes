
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 15:57:22
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

n = int(input())
i, j, p = read_ints()
for m in range(n):
    for k in range(n):
        u = abs(m - i)
        y = abs(k - j)
        maxs = max(u, y)
        if p - maxs > 0:
            print(p-maxs, end= " ")
        else:
            print(0, end=" ")
    print()



