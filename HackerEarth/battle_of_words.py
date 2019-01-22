
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 19:12:53
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from collections import Counter

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_test = int(input())
for _ in range(nb_test):
    a = input()
    b = input()
    ac =  Counter([x for x in a if x != " "])
    bc =  Counter([x for x in b if x != " "])
    acs = ''
    bcs = ''
    for i in ac:
        if i in bc:
            if ac[i] > bc[i]:
                acs += i*(ac[i] - bc[i])
        else:
            acs += i * ac[i]
    for i in bc:
        if i in ac:
            if bc[i] > ac[i]:
                bcs += i * (bc[i] - ac[i])
        else:
            bcs += i * bc[i]
    lena, lenb = 0, 0
    if acs:
        lena = len(acs)
    if bcs:
        lenb = len(bcs)
    if lena>0 and lenb>0:
        print("You draw some.")
    elif lena == 0:
        print("You lose some")
    else:
        print("You win some.")












