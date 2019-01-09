
# -*- coding: utf-8 -*-
# @Date    : 2018-11-13 09:21:05
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


n = read_int()
i = 2
while i * i < n and n % i :
    i += 1
if i * i <= n:
    print((n - i) // 2 + 1)
else  :
    print(1)
