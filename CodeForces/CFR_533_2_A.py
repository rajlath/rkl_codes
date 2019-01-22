
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 13:04:33
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


nb_sticks = read_int()
sticks = read_ints()
mins = min(sticks)
maxs = max(sticks)
x = int(10e12)
num = 0
for j in range(mins , maxs+1):
    curr = 0
    for i in sticks:
        if abs(i-j) > 1:
            curr += (abs(i-j)-1)
    if x > curr:
        x = curr
        num = j

print(num, x)

