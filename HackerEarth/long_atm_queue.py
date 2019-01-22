
# -*- coding: utf-8 -*-
# @Date    : 2019-01-20 15:01:43
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


nb = read_int()
ns = read_ints()
cnt = 1
for i in range(1, nb):
    cnt += ns[i]<ns[i-1]
print(cnt)