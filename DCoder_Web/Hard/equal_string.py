'''
Problem statement
Jimmy and Ryan have two strings S1 and S2 respectively of equal length. Jimmy will win the game if any of the permutations of his string become equal to Ryan's string. Print whether Jimmy is winning or not.
Input
First Line of the input contains an integer T denoting the number of test cases. The first line of each test case contains Jimmy's and Ryan's string respectively.
Output
For each test case print "YES" if Jimmy wins else print "NO".
Constraint
1<=T<=100.
1<=Length of the String<=100000.
String is made up of lower case letters only.
Sample Input
2
dcoder codder
abc abd
Sample Output
YES
NO
'''

# -*- coding: utf-8 -*-
# @Date    : 2018-09-12 11:57:27
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

nb_tests = read_int()
for _ in range(nb_tests):
    strA, strB = read_strs()
    print("YES" if sorted(strA) == sorted(strB) else "NO")

