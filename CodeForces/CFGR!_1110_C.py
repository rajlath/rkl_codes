
# -*- coding: utf-8 -*-
# @Date    : 2019-02-08 08:18:25
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
from math import sqrt
nb_test = read_int()
for _ in range(nb_test):
    curr = int(input())
    curr_bin = format(curr, 'b')
    #print(curr_bin)
    if curr_bin.count("0") == 0:
        for i in range(2, int(sqrt(curr))+1):
            if  curr % i == 0:
                print(curr // i)
                break
        else:
            print(1)
    else:
        print(pow(2, len(curr_bin)) - 1)


'''
from math import sqrt
q = int(input())
for _ in range(q):
    a = int(input())
    bi = format(a, 'b')
    if bi.count("0") == 0:
        for i in range(2, int(sqrt(a))+1):
            if a%i == 0:
                print(a//i)
                break
        else:
            print(1)
    else:
        print(pow(2, len(bi)) - 1)
'''