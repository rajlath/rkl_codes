
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 14:37:37
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

nb_test = int(input())
for _ in range(nb_test):
    ins = input()
    f   = [0] * 10
    for i in range(len(ins)):
        f[int(ins[i])] += 1
    maxs = f[0]
    mv   = 0
    for i in range(1, 10):
        if f[i] > maxs:
            maxs = f[i]
            mv = i
    print(mv)

