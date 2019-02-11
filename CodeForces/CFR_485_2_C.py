
# -*- coding: utf-8 -*-
# @Date    : 2019-01-28 18:16:35
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
a = read_ints()
b = read_ints()
l = int(10e18)
for i in range(n-1):
    second =  third = int(10e18)
    for j in range(i):
        if a[j] < a[i]:
            second = min(second, b[j])
    for j in range(i+1, n):
        if a[j] > a[i]    :
            third = min(third, b[j])
    l = min(l, b[i]+second+third)
print([-1, l][l != int(10e18)])