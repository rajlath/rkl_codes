# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:15:48 2018

@author: rinfo
"""
from itertools import combinations
from collections import Counter
containers = []
with open("input.txt") as f:
    for line in f:
        containers.append(int(line))
counter = Counter(len(c) for i in range(len(containers)) for c in combinations(containers, i) if sum(c) == 150)
print(sorted(counter.items(), key=lambda x: x[0])[0][1])


       