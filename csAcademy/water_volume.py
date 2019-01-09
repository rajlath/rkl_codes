# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:22:05 2018
coded by : rinfo
"""

nb_ops = int(input())
curr = 0
maxs = 0
maxi = 0
mins = int(1e9)
for i in range(nb_ops):
    mode, qty = [int(x) for x in input().split()]
    if mode == 0:
        curr += qty
        maxs = max(maxs, curr)
    else:
        curr -= qty
        mins = min(mins, curr)       
print(maxs - mins)        
    
    
        
        
    
            
            
    