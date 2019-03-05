
# -*- coding: utf-8 -*-
# @Date    : 2019-02-24 21:20:31
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
arrs = read_ints()
pos, neg = 0, 0
for i in arrs:
    if  i > 0:
        pos += 1
        ansp = i
    if i < 0:
        neg += 1
        negp = i
if pos >= lens // 2:
    print(ansp)
elif neg >= lens // 2:
    print(negp)
else:
    print(0)