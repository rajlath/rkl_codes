
# -*- coding: utf-8 -*-
# @Date    : 2019-01-20 15:33:16
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


nb_elem , nb_qry = read_ints()
elems = [-1] + read_ints() +[-1]
for _ in range(nb_qry):
    ins = read_ints()
    if ins[0] == 1:
        l = ins[1]
        if elems[l] == 1:elems[l] = 0
        else:elems[l] = 1
    if ins[0] == 0:
        l, r = ins[1], ins[2]
        if elems[l] == 1:
            print("ODD")
        else:
            print("EVEN")