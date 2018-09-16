'''
Great Power comes with great responsibility
Problem statement
x^y mod z, is remainder when x is raise to power y , divided by z.mod or modulus in programming is equivalent to remainder.You have to find x^y mod z for given x y and z.
Input
First line of the input contains number of test cases T,followed by T lines each contains x y and z separated by a space.
Output
For each test cases print x^y mod z in a newline.
Constraint
1≤T≤100
1≤x,y,z≤10000000
Note: The problem is tricky and require quite big calculations,your output can overflow easily the range of datatypes you are using, keep this in mind while making your code.You may have to use modulo's property.
Modulo operations might be implemented such that a division with a remainder is calculated each iteration.
Sample Input
2
3 3 5
32 54 13
Sample Output
2
12
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

nb_test = read_int()
for _ in range(nb_test):
    a, b, m = read_ints()
    print(pow(a, b, m))







