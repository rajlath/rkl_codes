# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:22:05 2018
coded by : rinfo
"""

x = int(input())
moves = 0
while x != 1:
    if x%3 == 1:
        x -= 1
        moves += 1
    else:
        if x%3==2 and x != 2:
            x += 1
            moves += 1
    if x == 2:
        moves += 1
        break
    else:
        x //= 3
        moves += 1
print(moves)        
        
        
        
    
            
            
    