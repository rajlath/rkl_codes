# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 20:11:46 2018

@author: rinfo
"""
sums = 0
line = open("input.txt").readline().strip()
for i, x in enumerate(line):
    if x == "(":
        sums += 1
    else:
        sums -= 1
    if sums == -1:
        print(i+1)
        break
        
print(sums)        

