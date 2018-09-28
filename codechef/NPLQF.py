

# -*- coding: utf-8 -*-
# @Date    : 2018-09-22 21:34:56
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]



'''
Example
Input:
2
arqpadparta
mnxprtpvghap
Output:
7
9
'''
from collections import Counter
nb_test = int(input().strip())
for _ in range(nb_test):
    s = [x for x in read_str()]
    lens = len(s)
    sc = Counter(s)
    mins = max_val
    for i in sc:
        mins = min(mins, lens-sc[i])
    print(mins)


