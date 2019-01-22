
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 13:28:49
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

n = int(input())
num = [x for x in input().split()]
num = [-1 if x == "0" else x for x in num ]
best = 0
sums = 0
for i in range(n):
    sums = max(num[i], sums + int(num[i]))
    best = max(best, sums)
maxs = -1
for i in range(n):
    curr = num[i]
    for j in range(i+1, n):
        if curr == best:
            maxs = max(maxs, j-i)
        if curr > best or j == n:
            break
        curr += num[j]
print(maxs)