
# -*- coding: utf-8 -*-
# @Date    : 2018-10-02 08:00:37
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

sequence = read_str() +" "
lens = len(sequence)
cnts = [0] * lens
lens -= 1
for i in range(lens):
    cnts[i+1] = cnts[i] + (sequence[i] == sequence[i+1])
nb_query = read_int()
for _ in range(nb_query):
    x, y = read_ints()
    print(cnts[y-1] - cnts[x-1])





