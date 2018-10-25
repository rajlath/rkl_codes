
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

has, need = read_ints()
ans = 0
while has < need:
    has *= 2
    ans += 1
ans += has - need
print(ans)

