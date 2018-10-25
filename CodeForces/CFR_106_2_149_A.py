
# -*- coding: utf-8 -*-
# @Date    : 2018-09-29 09:04:10
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

need_growth = read_int()
months      = sorted(read_ints(), reverse=True)
if need_growth == 0:
    print("0")
else:
    growth = 0
    month = 0
    ans = -1
    for i in months:
        growth += i
        month += 1
        if growth >= need_growth:
            ans = month
            break
    print(ans)

