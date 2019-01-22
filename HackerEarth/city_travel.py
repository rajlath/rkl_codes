
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 19:12:53
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

distance, normal, extended = read_ints()
days = 0
different = [[0, 0] for _ in range(extended)]
for i in range(extended):
    a, b = read_ints()
    extended[i][0] = a
    extended[i][1] = b
for i in range(extended):
    mins = i
    for j in range(i+1, extended):
        if extended[mins][0] > extended[j][0]:
            mins = j
        extended[i][0], extended[mins][0] = extended[mins][0], extended[j][0]
        extended[i][1], extended[mins][1] = extended[mins][1], extended[j][1]
    







