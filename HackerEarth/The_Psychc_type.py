
# -*- coding: utf-8 -*-
# @Date    : 2019-01-18 20:33:39
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


lens = int(input())
pos  = read_ints()
start, end = read_ints()
ans = "YES"
while True:
    curr = pos[start-1]
    if curr in range(lens-1):
        start = curr
    else:
        ans = "NO"
        break
print(ans)





