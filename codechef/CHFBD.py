
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 20:11:11
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/ENSE2018/problems/CHFBD
# @Version : 1.0.0
# my adoptation of  solution by pulkit100  https://www.codechef.com/viewsolution/20075795

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)
mods   = 10 ** 9 + 7

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_bags, have_amt, min_items = read_ints()
options = []
for _ in range(nb_bags):
    item_in_bag , price = read_ints()
    options.append([item_in_bag, price, item_in_bag / price])
options.sort(reverse=True, key=lambda x: x[2])
selected = 0
index = 0
while have_amt >= options[-1][1]:
    curr = options[index][1]
    curs = have_amt / curr
    if curs >= 1:
        maybe = int(curs)
        selected += maybe * (options[index][0])
        have_amt -= maybe * options[index][1]
    index += 1
print("YES "+str(selected) if selected >= min_items else "NO")











