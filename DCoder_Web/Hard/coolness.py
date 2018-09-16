'''
The Cool Numbers
Problem statement
For a number X, let its "Coolness" be defined as the number of "101"s occurring in its binary representation. For example, the number 21 has Coolness 2, since its binary representation is 10101, and the string "101" occurs twice in this representation.

A number is defined as Very Cool if its Coolness is greater than or equal to K. Please, output the number of Very Cool integers between 1 and R.
Input
The first line contains an integer T, the number of test cases.
The next T lines contains two space-separated integers, R and K.
Output
Output T lines, the answer for each test case.
Constraint
1<=T<=100
1<=R<=105
1<=K<=100
Sample Input
1
5 1
Sample Output
1
'''
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 16:53:30
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

lookup = [None] * (10 ** 5 + 1)
lookup[0] = 0

def coolness(n):
    if lookup[n] is None:
        st = bin(n)[2:]
        stl= len(st)
        count = 0
        for i in range(stl-2):
            count += st[i:i+3] == "101"
        lookup[n] = count
    return lookup[n]

nb_test = read_int()
for _ in range(nb_test):
    r, k = read_ints()
    ans = 0
    for j in range(1, r+1):
        ans += coolness(j) >= k
    print(ans)















