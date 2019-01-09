
# -*- coding: utf-8 -*-
# @Date    : 2018-10-24 15:54:39
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

nb_sellers, has_now = read_ints()
valids = []
for  i in range(nb_sellers):
    prices = read_ints()[1:]
    if min(prices) < has_now:
        valids.append(i+1)
if len(valids) == 0:
    print(0)
else:
    print(len(valids))
    print(*valids)