# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 07:37:45 2018

@author: rinfo
"""
nb_test = int(input())
for _ in range(nb_test):
    has, pick = [int(x) for x in input().split()]
    while True:
        if has < pick:
            ans = "Bob"
            break
        has -= pick
        if has < pick:
            ans = "Alice"
            break
        has -= pick
        pick *= pick
    print(ans)    
    