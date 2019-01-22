
# -*- coding: utf-8 -*-
# @Date    : 2019-01-19 20:55:34
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin
from collections import defaultdict

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]


nb_test = int(input())
for _ in range(nb_test):
    lens = input()
    elem = read_ints()
    eles = defaultdict(list)
    for i in elem:
       eles[bin(i)[2:].count("1")].append(i)

    ordr = sorted(eles.keys())
    for i in ordr:
        curr = eles[i]
        for j in curr:
            print(j, end = " ")