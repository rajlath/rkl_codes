
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
    knowledge = 1
    power = 1
    snap  = 0
    if knowledge + 1 == k_n and power + 1 == p_n:
        ans = "Chefirnemo"
    elif knowledge == k_n and power == p_n:
        ans = "Chefirnemo"
    else:
        #check for knowledge
        while knowledge < k_n:
            knowledge += k_f
            if knowledge == k_n:
                break
        while power < p_n:
            power += p_f
            if power == p_n:
                break
        


        elif knowledge > k_n or power > p_n:
            break
        else:
            while knowledge < k_n:
                knowledge += k_f
                if knowledge == k_n or knowledge + 1 == k_n:
                    if knowledge + 1 == k_n:snap = 1
                    break
            while power < p_n:
                power += p_f
                if snap == 1:
                    if power + 1 == p_n:
                        ans = "Chefirnemo"
                        break
                    elif power > p_n:
                        break
                else:
                    if power == p_n:
                       ans = "Chefirnemo"
                       break
                    elif power > p_n:
                        break
    print(ans)












