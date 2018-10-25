
# -*- coding: utf-8 -*-
# @Date    : 2018-10-08 08:28:00
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
A    = read_ints()
B    = read_ints()
l, r = min_val, max_val
sums = 0
for i in range(lens):
    sums += max(0, max(A[i]-r, l-B[i]))
    if l < A[i]:
        l = A[i]
    elif B[i] < l:
        l = B[i]
    if r < A[i]:
        r = A[i]
    elif  B[i] < r:
        r = B[i]

print(sums)


