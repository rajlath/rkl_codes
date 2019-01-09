
# -*- coding: utf-8 -*-
# @Date    : 2018-11-16 20:33:44
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


lens = read_int()
arrs = read_strs()
cnt = 0
i = 0
while i < lens - 2:
    if arrs[i] == "1" and arrs[i+1] == "0" and arrs[i+2] == "1":
        cnt += 1
        i += 3
    else:
        i += 1
print(cnt)