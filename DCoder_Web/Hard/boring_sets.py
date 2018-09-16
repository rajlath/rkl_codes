'''
The boring Sets
Problem statement
Cody hates Maths.He recently finished Set Theory in school. He was solving a problem based on set, and found himself lost. The problem is like you are given a Set, find its Power Set and compute sum of all elements of all the subsets in power set.Now you need to help Cody in his assignment.
Input
First line has T, the total number of test cases.
The next T lines contains a number N in each line.
Output
T lines giving answer as defined in the question for each N.
For given Sample Input for N=3
S={1,2,3}
P(S) = {{1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
answer = (1)+(2)+(3)+(1+2)+(1+3)+(2+3)+(1+2+3) = 24
Constraint
1<=T<=40
1<=N<=40
Power set of a set S is defined as set of all possible subsets of S.
Set S consist of all the number from 1 to N.
Sample Input
1
3
Sample Output
24

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

nb_tests = read_int()
for _ in range(nb_tests):
    upto     = read_int()
    ans = 1
    for i in range(1, upto):
        ans = ans << 1
    ans *= (upto * (upto + 1) //2)
    print(ans)












