# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:22:05 2018
coded by : rinfo
"""

nb_points = int(input())
maxx = 0
maxy = 0
points = []
for _ in range(nb_points):
    points.append([int(x) for x in input().split()])
    maxx = max(maxx, points[-1][0])
    maxy = max(maxy, points[-1][1])
ans = -1
for i, v in enumerate(points):
    if v == [maxx, maxy]:
        ans = i
        break
print(ans)        
    
    
   
    
    
        
        
    
            
            
    