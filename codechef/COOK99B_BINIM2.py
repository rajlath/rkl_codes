
# -*- coding: utf-8 -*-
# @Date    : 2018-10-22 07:11:28
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


nb_test = read_int()
for _ in range(nb_test):
    nb_stacks, first = read_strs()
    nb_stacks = int(nb_stacks)
    if first == "Dee":
        second = "Dum"
    else:
        second = "Dee"
    cnt_1, cnt_0 = 0, 0
    for _ in range(nb_stacks):
        curr = read_str()
        if curr[0] == "1":
            cnt_1 += 1
            if curr[-1] == "0":
                cnt_0 += 1
        else:
            cnt_0 += 1
            if curr[-1] == "1":
                cnt_1 += 1
    if   cnt_1 > cnt_0:print("Dee")
    elif cnt_0 > cnt_1:print("Dum")
    else:print(first)


