'''
Reverse Everything.
Problem statement
You are given an array, you need to reverse it.
Input
First line of input contains n, no. of elements of array.
Next line contains elements of array separated by space.
Output
Print reverse of array of elements, separated by space.
Constraint
1≤n≤100
0≤ element of array ≤ 1000000
Sample Input
3
1 2 4
Sample Output
4 2 1
'''

# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 13:16:53
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
read_int()
arr = read_ints()
arr = arr[::-1]
print(*arr)

