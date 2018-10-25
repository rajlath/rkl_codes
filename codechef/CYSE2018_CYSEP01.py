
# -*- coding: utf-8 -*-
# @Date    : 2018-09-29 22:11:10
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline().strip())
def read_ints()    : return [int(x) for x in stdin.readline().strip().split()]
def read_str()     : return input().strip()
def read_strs()    : return [x for x in stdin.readline().strip().split()]
'''
4
uwgs
sbdhd
hsvw
bhls
'''

from string import ascii_lowercase as lc
nb_test = read_int()
for _ in range(nb_test):
    ins = read_str()
    out = ''
    for i in list(ins):
        #print(i)
        index = lc.index(i)
        iord  = ord(i)
        out += lc[(iord - (26 - index))%26]
    print(out)
