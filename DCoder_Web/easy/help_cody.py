'''
Treasure Hunt
Problem statement
You are on a treasure hunt and your team just managed to unlock the treasure chest.
You brought a bag with a maximum weight capacity of maxW to carry the treasure home.
The treasure chest has two items each with a certain value and a certain weight.
Find out the maximum value of treasure that you can take home in your bag.
You can take both items too if your bag can hold it.

Input
First line of input contains the maximum weight capacity of the bag. The second line of input contains the value and weight of item1. The third line of input contains the value and weight of item2.
Output
Print the maximum value that you can carry

Constraint
1 ≤ maxW, value1, weight1, value2, weight2 ≤ 1000

Sample Input
20
30 8
50 10
Sample Output
80
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

read_int()
arr = read_ints()
arr = sorted(arr, reverse=True)
print(*arr)

