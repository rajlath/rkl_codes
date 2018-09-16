'''
The Game of Brackets
Problem statement
The problem is based on real life scenario our Team at Dcoder faced during development of this IDE, In a code editor you need to indent the code and color the closing paranthesis of a selected paranthesis, to know the code block and if there are unequal number of paranthesis, there must be something wrong, ie every opening brackets/paranthesis should be having closing brackets/paranthesis. This problem is scaled down version, you are given a string and you need to tell is it valid or not, based on the fact stated above.
Input
Input contains a string
Output
Print "Yes" for a valid string,else "No" , without quotes.
Examples:
{{[]}} : Yes
{[}] : No
[[]) : No
{}([]) : Yes
Constraint
0≤string length≤100
Ps: Parenthesis for this problem includes "{([])}"
Sample Input
[[{{()}}]]
Sample Output
Yes
'''

# -*- coding: utf-8 -*-
# @Date    : 2018-09-12 12:10:35
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

expression = read_str()
opens = ["(","{","["]
close = [")","}","]"]
stacks= []
ans = "Yes"
for i in expression:
    if i in opens:
        stacks.append(i)
    else:
        if len(stacks) > 0:
            shouldbe = stacks.pop()
            if shouldbe != opens[close.index(i)]:
                ans = "No"
                break

if len(stacks)>0:ans = "No"
print(ans)



