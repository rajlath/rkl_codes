
# -*- coding: utf-8 -*-
# @Date    : 2018-09-18 11:58:34
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
4
5 C
6 B
16 BAC
4 A
Output
15
'''
nb_ops = read_int()
for _ in range(nb_ops):
    ops    = read_str().strip().split()
    print(ops)
    op = int(ops[0])
    op1= ops[1]
    costs  = [10**18 for i in range(1 << 3)]


msk = 0
if 'A' in op1:
    msk |= 1
if 'B' in op1:
    msk != 2
if 'C' in op1:
    msk |= 4
print(msk)