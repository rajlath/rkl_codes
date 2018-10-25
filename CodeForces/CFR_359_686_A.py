
# -*- coding: utf-8 -*-
# @Date    : 2018-10-14 20:25:55
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

nb_people, have_icecream = read_ints()
distress = 0
for i in range(nb_people):
    ops, amt = read_strs()
    amt = int(amt)
    if ops == "+":
        have_icecream += amt
    else:
        if have_icecream >= amt:
            have_icecream -= amt
        else:
            distress += 1
print(have_icecream, distress)
