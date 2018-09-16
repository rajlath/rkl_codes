'''
Problem statement
Eric wants to identify whether a given sequence of character is a string, number or a variable. A sequence of character containing both string and number is known as variable.
Input
First line of input consists of T: No of Test cases.
T lines containing N:Length of the Character Sequence and String S:Character Sequence.
Output
For each Test case identify whether the char sequence is "Number","Variable" or "String".
Constraint
1<=T<=100.
1<=N<=100.
S:Combinations of character and number.
Sample Input
2
5 abcde
3 ab4
Sample Output
String
Variable
'''

# -*- coding: utf-8 -*-
# @Date    : 2018-09-09 20:14:41
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

nots = read_int()
for _ in range(nots):
    lens, st = read_strs()
    alpha = 0
    digit = 0
    for i in st:
        if i.isdigit():digit += 1
        else:alpha += 1
    print(alpha, digit)

    if alpha == int(lens):print("String")
    elif digit == int(lens):print("Number")
    else: print("Variable")

