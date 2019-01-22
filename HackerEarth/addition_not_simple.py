
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 19:29:00
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
    ins = [ord(i) for i in input()]
    lens = len(ins)
    sums = 0
    ans  = ["a"] * len(ins)
    for i in range(lens):
        sums = ins[i] + ins[lens - 1 - i] - 192
        if sums > 26:
            ans[i] = chr(sums - 26 + 96)
        else:
            ans[i] = chr(sums + 96)
    print("".join(ans))


