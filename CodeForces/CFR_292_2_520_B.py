
# -*- coding: utf-8 -*-
# @Date    : 2018-09-29 20:30:50
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

has , need = read_ints()
ops = 0
while has != need:
    ops += 1
    if need < has or need%2==1:
        need += 1
    else: need //= 2
print( ops )



