
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 20:18:38
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : http://codeforces.com/contest/1036/problem/A
# @Version : 1.0.0

import os
from sys import stdin
from math import floor, ceil

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

classy=set()

for i in range(19):
    for j in range(i):
        for k in range(j):
            for a in range(10):     # a=0 for good measure
                for b in range(10):
                    for c in range(10):
                        what=a*10**i+b*10**j+c*10**k
                        classy.add(what)

li=sorted(classy)

def counting(i):
    # return len([x for x in li if x <= i])+C
    lo=0
    hi=len(li)-1
    while lo<hi:
        mid=(lo+hi+1)//2
        if li[mid]<=i:
            lo=mid
        else:
            hi=mid-1
    return lo

for _ in range(int(input())):
    a,b=read_ints()
    print(counting(b)-counting(a-1))