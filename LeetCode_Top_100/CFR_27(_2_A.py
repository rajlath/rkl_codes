
# -*- coding: utf-8 -*-
# @Date    : 2018-09-28 09:18:53
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

teams = [[], [], []]
nb_students  = read_int()
expertise    = read_ints()
for i, v in enumerate(expertise):
    teams[v-1].append(i+1)
answer = list(zip(teams[0], teams[1], teams[2]))
print(len(answer))
for i in answer:print(*i)




