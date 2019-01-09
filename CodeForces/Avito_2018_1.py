# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:23:53 2018

@author: rinfo
"""

nb_test = int(input()) 
for _ in range(nb_test):
    lens = int(input())
    arrs = sorted([int(x) for x in input().split()])
    print(arrs)
    i = 0
    ans = 0
    while i < lens-1:
        if arrs[i] < 0 and arrs[i+1] < 0:
            ans += abs(arrs[i] - arrs[i+1])
            i += 2
            print(ans)
        else:
            ans += abs(arrs[i] - arrs[lens - 1])
            
            i += 1
            
    print(ans)    
    
            
        