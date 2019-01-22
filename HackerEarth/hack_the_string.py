
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 19:29:00
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
elem = read_ints()
zeros= [i for i, v in enumerate(elem) if v == 0]
ans = 0
for i, v in enumerate(zeros):
    ans = max(ans, elem[v+1] - i)
print(ans, zeros)



