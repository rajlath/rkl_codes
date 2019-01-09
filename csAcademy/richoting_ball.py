# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:22:05 2018
coded by : rinfo
"""

nb_balls = int(input())
heights  = sorted([int(x) for x in input().split()])
median   = heights[(nb_balls + 1) // 2]
ans = 0
for i in range(nb_balls):
    ans += abs(heights[i] - median)
print(ans)    
    
        
        
    
            
            
    