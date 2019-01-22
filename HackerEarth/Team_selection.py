
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

lens = int(input())
A    = read_ints()
B    = sorted(read_ints())
C    = [0] * lens
for i in range(lens-1, -1, -1):
    for j in range(i-1, -1, -1):
        C[i] += A[i] > A[j]
count = 0
for i in range(lens):
    for j in range(lens):
        if A[i] < B[j]:
            if C[i] > 0:
                count += C[i] * (lens - j)
                break
print(count)