# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:23:53 2018

@author: rinfo
"""

nb_test = int(input())
for _ in range(nb_test):
    curr = input()
    aa = curr.find_all("AA")
    bb = curr.find_all("BB")
    if any(x%2==0 for x in aa) or any(x%2==0 for x in bb):
        print("no")
        
        