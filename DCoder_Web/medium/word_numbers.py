
'''
Problem statement
Wade is unable to convert a number in its word form. Help Wade to convert a number to its word form. For example, the word form of 198 would 'one nine eight'.
Input
A single integer N
Output
Print the word form of N
Constraint
0 ≤ N ≤ 10000
Sample Input
200
Sample Output
two zero zero
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

def digit_2_word(digit):
    num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',0:'zero'}
    ans = []
    return num2words1[digit]

number = read_str()
ans = [digit_2_word(int(x)) for x in number ]
print(*ans)




