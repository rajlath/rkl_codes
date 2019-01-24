
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 13:56:09
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


nb_days = int(input())
temps   = read_ints()
avg_days = [(b - a) for a, b in zip(temps, temps[1:])]
if len(set(avg_days)) == 1:
    print(temps[-1] + avg_days[0])
else:
    print(temps[-1])
