
# -*- coding: utf-8 -*-
# @Date    : 2018-10-08 22:43:08
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
def lucas_seq(n):
    rets = [2, 1]
    for _ in range(n):
        rets.append(rets[-1] + rets[-2])
    return rets

lucas = lucas_seq(10 ** 5 + 1)
#print(lucas[:10])
lucas[0], lucas[1] = lucas[1], lucas[0]
#print(lucas[:10])
nb_test =read_int()
for _ in range(nb_test):
    ins = read_str()
    if len(ins) < 2:
        print("UNFIT")
    elif len(ins) ==2 and len(set(ins))==1:
        print("FIT")
    else:
        counts = sorted(Counter(ins).values())
        #print(counts)
        if all(a==b for a, b in zip(counts, lucas)):
            print("FIT")
        else:
            print("UNFIT")
