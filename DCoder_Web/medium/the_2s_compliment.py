'''
The 2's Complement
Problem statement
You are given a binary number as a String as input, find its 2's complement and print the output in decimal.
Input
Input contains a binary number as a String b
Output
Print 2's Complement of b in decimal.
Constraint
1≤b lenght≤50
Sample Input
1001
Sample Output
7
'''

# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 17:04:10
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

s = read_str()
ones = ''
for i in s:
    if i is "0":
        ones += "1"
    else:
        ones += "0"
twos = list(ones)
for i in range(len(ones)-1, -1 , -1):
    if ones[i] is "1": twos[i] =  "0"
    else:
        twos[i]= "1"
        break

if i is -1:
    twos = "1" + twos
twos = ''.join(twos)
print(int(twos, 2))




























