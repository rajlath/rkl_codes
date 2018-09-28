
# -*- coding: utf-8 -*-
# @Date    : 2018-09-27 20:06:27
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

nb_names = read_int()
names_count = dict()
for _ in range(nb_names):
    name = read_str()
    names_count[name] = names_count.get(name, -1) + 1
    #print(names_count[name])
    if names_count[name] == 0:
        print("OK")
    else:print(name + str(names_count[name]))

