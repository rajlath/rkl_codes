# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 15:56:32 2018
coded by : rinfo
"""
import itertools as it

n, l = [int(x) for x in input().split()]
lst = range(1, n+1)
for x in it.combinations(lst, l):
    print(*x)

    
  
    
    
    
