'''
Problem statement
You are organising a tournament, you have invited N teams and decided that each team play M games with each other. Example If there are 3 teams A, B and C and M is 3. Then A will play 3 matches with B and 3 matches with C. B will play 3 matches with C. That is each team play 6 matches .Calculate the total number of matches the tournament will have.
Input
T:No of test case.
T lines Containing N and M.
Output
For each Test case print total Number of matches the tournament will have.
Constraint
1<=T<=100.
1<=N<=100.
1<=M<=50.
Sample Input
1
3 3
Sample Output
9
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

nots = read_int()
for _ in range(nots):
    nb_team, nb_times = read_ints()
    print( ((nb_team * (nb_team - 1)) // 2) * nb_times )



