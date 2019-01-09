
# -*- coding: utf-8 -*-
# @Date    : 2018-10-28 17:09:32
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

def other_got(arr, k):
    return sum([k - x for x in arr])

nb_studs = read_int()
elodreip_got = read_ints()
maxe = max(elodreip_got)
sume = sum(elodreip_got)
if (maxe * nb_studs) - sume > sume :
    print(max(elodreip_got))
else:
    i = maxe
    while sume > other_got(elodreip_got, i):
        i += 1
    print(i)


