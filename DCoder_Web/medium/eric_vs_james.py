
'''
Problem statement
Eric is very good in finding LCM(Least Common Multiple). But his friend James finds a way to confuse him. He gives Eric 2 numbers a,b (a≤b) and Eric has to find the smallest number that is divisible by all the numbers between a and b (both inclusive). Help Eric.
Input
First line contains 2 space-separated integers a and b.
Output
Print LCM of the given range.
Constraint
0 ≤ a ≤ b ≤ 50
Sample Input
1 10
Sample Output
2520

'''
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 12:54:09
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

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


a, b = read_ints()
arr  = list(range(a, b))
lcm = arr[0]
for i in arr[1:]:
    lcm = lcm * i // gcd(lcm, i)
print(lcm)




