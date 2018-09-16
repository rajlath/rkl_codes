'''
Fit Me In
Problem statement
You have 2 paintings of size a x b and c x d. You want to hang the paintings inside a rectangular board on the wall. The board has dimensions n x m. You are allowed to rotate the paintings but at least one edge of each of the paintings must be parallel to an edge of the board. The paintings can touch each other and the edges of the board but cannot overlap or go beyond the edge of the board. Is it possible to place the paintings on the board?
Input
The input contains 3 lines in the form -
n m
a b
c d
First line contains space separated integers n and m. Second line contains space separated integers a and b. Third line contains space separated integers c and d.
Output
Print "Yes" if the paintings can be placed inside the board, otherwise "No", without quotes.
Constraint
All integers are in the range 1 to 1000.
Sample Input
4 2
2 2
2 1
Sample Output
Yes
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

n, m = read_ints()
a, b = read_ints()
c, d = read_ints()

def valid(x, y):
    return n >= x and m >= y or n >= y and m >= x

k = valid(a+c, max(b,d)) or valid(a+d, max(c , b)) or valid(b+d, max(a,c)) or valid(c+b, max(a,d))

if k:
    print("Yes")
else:
    print("No")












