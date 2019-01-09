# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:22:05 2018
coded by : rinfo
"""

from math import gcd

nb_values, nb_ops = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]
_gcd = values[0]
for i in values:
    _gcd = gcd(_gcd, i)
for _ in range(nb_ops):
    indx, val = [int(x) for x in input().split()]
    values[indx-1] //= val
    _gcd = gcd(_gcd, values[indx-1])
    print(_gcd)
    
    
        
        
    
            
            
    