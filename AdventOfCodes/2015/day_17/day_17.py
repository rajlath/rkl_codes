# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:15:48 2018

@author: rinfo
"""
from itertools import combinations
containers = []
with open("input.txt") as f:
    for line in f:
        containers.append(int(line))
print(sum(1 for i in range(len(containers)) for c in combinations(containers, i ) if sum(c) == 150))     
       