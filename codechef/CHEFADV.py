
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 15:55:20
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : https://www.codechef.com/SEPT18B/problems/CHEFADV
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

nb_tests = read_int()
for _ in range(nb_tests):
    ans = "Pofik"
    k_n, p_n, k_f, p_f=read_ints()
    k_n -= 1
    p_n -= 1
    if k_n % k_f == 0 and p_n % p_f ==0:
        ans = "Chefirnemo"
    if ans == "Pofik":
        k_n -= 1
        p_n -= 1
        if k_n>= 0 and p_n >=0 and k_n % k_f == 0 and p_n % p_f ==0:
            ans = "Chefirnemo"
    print(ans)












