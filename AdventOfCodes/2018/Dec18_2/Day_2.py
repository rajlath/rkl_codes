# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 07:30:12 2018

@author: rinfo
"""
from collections import Counter
input = open("input.txt")
data = input.readlines()
'''
is_2 = 0
is_3 = 0
for line in data:
    line = Counter(line.strip())
    is_2 += (2 in line.values())
    is_3 += (3 in line.values())
print(is_2 * is_3) 
'''
done = []
for line in data:
    for dones in done:
        curr = "".join([a for a, b in zip(line, dones) if a == b])        
        if len(curr) == len(line)-1:
            print(curr)
            break
    done.append(line)    

   
    


