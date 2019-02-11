
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 20:43:43
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
from collections import Counter
nb_test = int(input())
for _ in range(nb_test):
    nb_elems , k = read_ints()
    vals = read_ints()
    can  = [int(Ai/((Ai%k)+2)) for Ai in vals]
    valc = Counter(vals)
    canc = Counter(set(can))
    count = 0
    print(valc, canc)
    for i in canc:
        if i in valc:
            count += valc[i]
       #print(count, i)
    print(nb_elems - count)

