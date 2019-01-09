
# -*- coding: utf-8 -*-
# @Date    : 2018-10-26 11:44:49
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


nb_pokemon  = read_int()
powers      = read_ints()
fights      = [0] * nb_pokemon
winner      = 0
for i in range(1, nb_pokemon):
    if powers[winner] < powers[i]:
        winner = i
    fights[winner] += 1
print(* fights)


