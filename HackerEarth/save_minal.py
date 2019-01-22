
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


noe = int(input())
arr = [0] + [int(x) for x in input().split()] + [0]
noq = int(input())
for i in range(noq)   :
    lr = [int(x) for x in input().split()]
    if len(lr) == 2:
        l, r = lr[0], lr[1]
    else:
        continue
    print(len(set(arr[l:r+1])))

