
# -*- coding: utf-8 -*-
# @Date    : 2019-01-27 11:54:22
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
    lens = int(input())
    has = [int(x) for x in input()]
    need = 0
    if lens == 1:
        print([1, 0][has[0]==1])
    else:
        if has[0] == 0 and has[1] == 0:
            has[0] = 1
            need += 1
        if has[-1] == 0 and has[-2] == 0:
            has[-1] = 1
            need += 1
        for i in range(1, lens-1):
            if has[i] == 0 and has[i-1]==0 and has[i+1]== 0:
                has[i] = 1
                need += 1
        print(need)

