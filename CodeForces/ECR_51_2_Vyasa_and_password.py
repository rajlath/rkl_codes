
# -*- coding: utf-8 -*-
# @Date    : 2018-09-22 16:53:43
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : http://codeforces.com/contest/1051/problem/A
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

def get_id(a):
    c_id = 2
    if "a" <= a <= "z": c_id = 0
    if "A" <= a <= "Z": c_id = 1
    return c_id


nb_test = read_int()
for _ in range(nb_test):
    replacement = ["a","A","1"]
    password    = [x for x in input()]
    c_counts    = [0] * 3
    for i in password:
        c_counts[get_id(i)] += 1
    for i,v in enumerate(password):
        ids = get_id(v)
        if c_counts[ids] > 1:
            for j in range(3):
                if not c_counts[j]:
                    password[i] = replacement[j]
                    c_counts[ids] -= 1
                    c_counts[j]   += 1
                    break
    print(''.join(password))








