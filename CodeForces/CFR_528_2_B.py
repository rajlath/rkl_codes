# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 07:04:13 2018

@author: rinfo
"""

n, k = [int(x) for x in input().split()]
for i in range(k-1, 0, -1):
    if n % i == 0:
        ans = (n // i) * k  + i
        print(ans)
        break
        
            